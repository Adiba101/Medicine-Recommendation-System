# Medical Recommendation System & Healthcare Analytics

An AI-powered healthcare analytics platform that predicts diseases from patient symptoms and recommends medicines, alternative therapies, precautions, dietary plans, and recovery advice. 

The application utilizes a Machine Learning pipeline trained on the **Medical Conditions 50000 Dataset** to support digital triage and visual clinical explanations through **10 Interactive Dashboards** built with Streamlit.

---

## 🚀 Key Features

* **Three ML Models Compared**: Random Forest, XGBoost, and Gradient Boosting Classifiers.
* **Explainable AI (XAI)**: Global feature importance and dynamic, instance-level **SHAP Waterfall explanations** explaining which symptom words drove the prediction.
* **Advanced Medical Knowledge Mapping**: Leverages a structured clinical lookup database mapping predicted conditions to first-line medicines, alternative medicines, warning details, dosage guidelines, precautions, and recovery timelines.
* ** HIPAA-ready & Private**: Operates entirely client-side without storing user or patient details.

---

## 📂 Project Architecture

```
Medicine_recommendation_system/
│
├── models/                       # Serialized models, vectorizer, & precomputed metrics
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│   ├── gradient_boosting.pkl
│   ├── vectorizer.pkl
│   ├── label_encoder.pkl
│   └── metrics.pkl
│
├── app.py                        # Streamlit web app (Contains the 10 Dashboards)
├── train_models.py               # Prepares data, trains models, evaluates, & saves metrics
├── helper_data.py                # Structured medical lookup mapping table (20 classes)
├── test_models.py                # Pipeline verification unit tests
├── requirements.txt              # Project package dependencies
└── README.md                     # Platform documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone or Open the Project
Ensure the project is located within the workspace:
`c:\Users\dell\OneDrive\Desktop\Medicine_recommendation_system`

Ensure the dataset `medical_question_answer_dataset_50000.csv` is present in the `data/` directory inside the project root:
`c:\Users\dell\OneDrive\Desktop\Medicine_recommendation_system\data\`

### 2. Install Dependencies
Install all required libraries using pip:
```bash
pip install -r requirements.txt
```

### 3. Train the Models
Run the training pipeline to fit the TF-IDF vectorizer, train the classifiers, compile validation metrics, and save serialized outputs to `models/`:
```bash
python train_models.py
```

### 4. Verify Model Integrity
Execute the automated tests to verify model behavior and ensure latency is far below the **2 seconds** limit:
```bash
python test_models.py
```

### 5. Launch the Streamlit App
Launch the interactive web portal locally:
```bash
streamlit run app.py
```

---

## 📊 The 10 Dashboards

1. **Home**: Overview of the project goals, KPIs (Accuracies, Dataset size, Response times), and the ML pipeline diagram.
2. **Dataset Overview**: Detailed statistics of the 50,000-row dataset, null value audits, and an interactive data browser.
3. **Disease Analytics**: Frequency and prevalence graphs of diagnosed conditions in the database.
4. **Symptom Analytics**: Distribution of main symptom blocks and NLP-driven term frequency bar charts of symptom descriptions.
5. **Disease Prediction**: Live diagnostics form allowing patient details entry and symptom description inputs (predefined or free-text query), showing predictions across Random Forest, XGBoost, and Gradient Boosting.
6. **Medicine Recommendations**: Access to first-line recommended medications, clinical alternative drugs, and thorough usage instructions.
7. **Advice & Precautions**: Essential precautions to avoid complications, long-term lifestyle suggestions, and a structured recovery timeline.
8. **Explainable AI (SHAP)**: Global feature importance comparisons across all 3 models and instance-level SHAP Waterfall graphs detailing word contributions to the prediction.
9. **Model Performance**: Bar charts comparing accuracy vs. training latency, 20x20 Confusion Matrix heatmaps, and One-vs-Rest ROC curve dashboards for every disease.
10. **Project Insights**: Analysis of model tradeoffs, business value inside clinic triage workflows, and digital healthcare delivery impacts.
