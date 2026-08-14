import os
import pickle
import time
import numpy as np

def test_pipeline():
    print("=== Testing Saved Models and Vectorizer ===")
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    
    # 1. Load Vectorizer
    vectorizer_path = os.path.join(models_dir, "vectorizer.pkl")
    assert os.path.exists(vectorizer_path), "Vectorizer file missing!"
    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)
    print("[OK] Vectorizer loaded successfully.")
    
    # 2. Load Label Encoder
    le_path = os.path.join(models_dir, "label_encoder.pkl")
    assert os.path.exists(le_path), "Label Encoder file missing!"
    with open(le_path, "rb") as f:
        label_encoder = pickle.load(f)
    print("[OK] Label Encoder loaded successfully.")
    classes = label_encoder.classes_
    print(f"Number of classes: {len(classes)}")
    
    # 3. Load Models
    model_names = ["random_forest", "xgboost", "gradient_boosting"]
    models = {}
    for name in model_names:
        path = os.path.join(models_dir, f"{name}.pkl")
        assert os.path.exists(path), f"Model {name} file missing!"
        with open(path, "rb") as f:
            models[name] = pickle.load(f)
        print(f"[OK] Model '{name}' loaded successfully.")
        
    # 4. Test Predictions
    test_inputs = [
        ("muscle cramps and weakness", "Electrolyte Imbalance"),
        ("cold hands and feet", "Raynaud's Disease"),
        ("headache and nausea", "Migraine"),
        ("I feel difficulty sleeping and can't rest", "Insomnia"),  # Slightly noisy input
    ]
    
    for symptom_text, expected_disease in test_inputs:
        print(f"\nTesting input: '{symptom_text}'")
        
        # Transform input
        start_vec = time.time()
        vec = vectorizer.transform([symptom_text])
        vec_time = time.time() - start_vec
        print(f"  Vectorization time: {vec_time*1000:.3f} ms")
        
        for name, model in models.items():
            start_pred = time.time()
            # Predict probability and class
            probs = model.predict_proba(vec)[0]
            pred_idx = np.argmax(probs)
            pred_class = label_encoder.inverse_transform([pred_idx])[0]
            confidence = probs[pred_idx]
            pred_time = time.time() - start_pred
            
            print(f"  [{name}] Predicted: '{pred_class}' | Confidence: {confidence:.4f} | Time: {pred_time*1000:.3f} ms")
            
            # Check shape
            assert len(probs) == len(classes), f"Probabilities size {len(probs)} does not match classes size {len(classes)}"
            
            # Check classification if exact match expected
            if expected_disease in classes and symptom_text in ["muscle cramps and weakness", "cold hands and feet", "headache and nausea"]:
                assert pred_class == expected_disease, f"[{name}] Expected {expected_disease}, got {pred_class}"
                
    print("\n[OK] All automated checks passed successfully!")

if __name__ == "__main__":
    test_pipeline()
