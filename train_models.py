import os
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
import xgboost as xgb
import time

def main():
    print("=== Medical Recommendation System ML Pipeline ===")
    
    # Paths
    csv_path = os.path.join(os.path.dirname(__file__), "data", "medical_question_answer_dataset_50000.csv")
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(models_dir, exist_ok=True)
    
    # 1. Load Dataset
    print(f"Loading dataset from {csv_path}...")
    df = pd.read_csv(csv_path)
    
    X_raw = df['Symptoms/Question'].values
    y_raw = df['Disease Prediction'].values
    
    # 2. Encode Labels
    print("Encoding labels...")
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y_raw)
    classes = label_encoder.classes_
    print(f"Total unique classes (diseases): {len(classes)}")
    
    # 3. Train-Test Split
    print("Splitting data (80% train, 20% test)...")
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        X_raw, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )
    
    # 4. Feature Engineering: TF-IDF Vectorization
    print("Fitting TF-IDF Vectorizer...")
    vectorizer = TfidfVectorizer(lowercase=True, ngram_range=(1, 2))
    X_train = vectorizer.fit_transform(X_train_raw)
    X_test = vectorizer.transform(X_test_raw)
    
    feature_names = vectorizer.get_feature_names_out()
    print(f"Number of extracted TF-IDF features: {len(feature_names)}")
    
    # 5. Train Models
    models = {}
    metrics = {}
    
    # Model A: Random Forest
    print("\nTraining Random Forest Classifier...")
    start_time = time.time()
    rf_model = RandomForestClassifier(n_estimators=50, max_depth=12, random_state=42, n_jobs=-1)
    rf_model.fit(X_train, y_train)
    rf_time = time.time() - start_time
    print(f"Random Forest trained in {rf_time:.2f} seconds.")
    models['random_forest'] = rf_model
    
    # Model B: XGBoost
    print("Training XGBoost Classifier...")
    start_time = time.time()
    # XGBoost needs classes from 0 to N-1 which is satisfied by LabelEncoder
    xgb_model = xgb.XGBClassifier(
        n_estimators=50,
        max_depth=6,
        learning_rate=0.1,
        random_state=42,
        n_jobs=-1,
        eval_metric='mlogloss'
    )
    xgb_model.fit(X_train, y_train)
    xgb_time = time.time() - start_time
    print(f"XGBoost trained in {xgb_time:.2f} seconds.")
    models['xgboost'] = xgb_model
    
    # Model C: Gradient Boosting
    print("Training Gradient Boosting Classifier...")
    start_time = time.time()
    gb_model = GradientBoostingClassifier(n_estimators=30, max_depth=4, random_state=42)
    gb_model.fit(X_train, y_train)
    gb_time = time.time() - start_time
    print(f"Gradient Boosting trained in {gb_time:.2f} seconds.")
    models['gradient_boosting'] = gb_model
    
    # 6. Evaluation & Metrics Calculation
    print("\nEvaluating models...")
    
    for name, model in models.items():
        print(f"\n--- Metrics for {name} ---")
        
        # Predictions
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)
        
        # Accuracy
        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {acc:.4f}")
        
        # Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        
        # Classification Report (dictionary format for saving)
        report = classification_report(y_test, y_pred, target_names=classes, output_dict=True)
        
        # Feature Importance
        importances = model.feature_importances_
        # Sort features by importance
        indices = np.argsort(importances)[::-1]
        feature_importance_list = [
            {"feature": feature_names[i], "importance": float(importances[i])}
            for i in indices[:30] # Keep top 30 features
        ]
        
        # Compute ROC curve and ROC area for each class
        roc_data = {}
        # Binarize labels for multi-class ROC
        y_test_bin = pd.get_dummies(y_test).values
        for i, class_name in enumerate(classes):
            fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_prob[:, i])
            roc_auc = auc(fpr, tpr)
            # Downsample ROC points slightly to save space (e.g., take 100 points)
            step = max(1, len(fpr) // 100)
            roc_data[class_name] = {
                "fpr": fpr[::step].tolist(),
                "tpr": tpr[::step].tolist(),
                "auc": float(roc_auc)
            }
            
        metrics[name] = {
            "accuracy": float(acc),
            "report": report,
            "confusion_matrix": cm.tolist(),
            "feature_importance": feature_importance_list,
            "roc_data": roc_data
        }
        
    # Add training times and dataset metadata to metrics
    metrics["metadata"] = {
        "num_train": len(y_train),
        "num_test": len(y_test),
        "total_records": len(df),
        "unique_diseases": list(classes),
        "training_times": {
            "random_forest": rf_time,
            "xgboost": xgb_time,
            "gradient_boosting": gb_time
        }
    }
    
    # 7. Save Everything
    print("\nSaving models and vectorizers...")
    
    # Save Vectorizer
    with open(os.path.join(models_dir, "vectorizer.pkl"), "wb") as f:
        pickle.dump(vectorizer, f)
        
    # Save Label Encoder
    with open(os.path.join(models_dir, "label_encoder.pkl"), "wb") as f:
        pickle.dump(label_encoder, f)
        
    # Save Models
    for name, model in models.items():
        with open(os.path.join(models_dir, f"{name}.pkl"), "wb") as f:
            pickle.dump(model, f)
            
    # Save Metrics
    with open(os.path.join(models_dir, "metrics.pkl"), "wb") as f:
        pickle.dump(metrics, f)
        
    print(f"All ML artifacts saved to {models_dir} successfully!")

if __name__ == "__main__":
    main()
