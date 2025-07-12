# Admin-Level Machine Learning and NLP Utility Module
# --- Imports ---
import gspread
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
from transformers import pipeline
# --- Code Generation Function ---
def generate_code(description: str, language: str, model: str) -> str:
    """
    Generates boilerplate code for a specified description and language.
    """
    if model.lower() == "codegen":
        return "Under Construction: Codegen model support not implemented yet."
    function_name = description.replace(" ", "_")
    code = f"""def {function_name}():
    \"\"\"Auto-generated function in {language}.\"\"\"
    pass
"""
    return code
# --- Zero-Shot Classification ---
def zero_shot_classification(text: str, possible_labels: list, model_name: str = "facebook/bart-large-mnli") -> dict:
    """
    Performs zero-shot classification using Hugging Face transformers.
    """
    if not isinstance(possible_labels, list) or not possible_labels:
        raise ValueError("possible_labels must be a non-empty list of strings.")
    classifier = pipeline(
        "zero-shot-classification",
        model=model_name,
        device=0  # Use GPU if available
    )
    results = classifier(text, possible_labels, multi_label=True)
    return results
# --- Chain-of-Thought Placeholder ---
def chain_of_thought(prompt: str, hint: str, model: str):
    """
    Placeholder for chain-of-thought reasoning functionality.
    """
    print("Chain-of-thought reasoning is under construction.")
# --- Spreadsheet Loading ---
def load_spreadsheet(gc_client, sheet_name: str):
    """
    Loads all values from a Google Sheet into a pandas DataFrame.
    """
    try:
        worksheet = gc_client.open(sheet_name).sheet1
        rows = worksheet.get_all_values()
        # Assuming the first row is the header
        if not rows:
            print(f"Spreadsheet '{sheet_name}' is empty.")
            return pd.DataFrame()
        df = pd.DataFrame(rows[1:], columns=rows[0])
        # Attempt to convert columns to numeric where possible
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        return df
    except Exception as e:
        print(f"Error loading spreadsheet '{sheet_name}': {e}")
        return pd.DataFrame()
# --- Data Cleaning ---
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handles missing values using median imputation.
    """
    if df.empty:
        print("DataFrame is empty, skipping cleaning.")
        return df
    imputer = SimpleImputer(strategy='median')
    # Only impute numerical columns
    numerical_cols = df.select_dtypes(include=np.number).columns
    if not numerical_cols.empty:
        df[numerical_cols] = imputer.fit_transform(df[numerical_cols])
    return df
# --- Feature Engineering Placeholder ---
def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Placeholder for feature engineering steps.
    """
    print("Feature engineering is under construction.")
    return df
# --- Model Training ---
def train_model(X_train: pd.DataFrame, y_train: pd.Series, model_type: str = 'logistic_regression'):
    """
    Trains a specified machine learning model.
    """
    if model_type.lower() == 'logistic_regression':
        model = LogisticRegression(max_iter=1000)
    elif model_type.lower() == 'random_forest':
        model = RandomForestClassifier(random_state=42)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")
    model.fit(X_train, y_train)
    return model
# --- Model Evaluation ---
def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series) -> float:
    """
    Evaluates the model's accuracy on the test set.
    """
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy
# --- Model Optimization ---
def optimize_model(model_instance, X_train: pd.DataFrame, y_train: pd.Series, param_space: dict):
    """
    Optimizes model hyperparameters using BayesSearchCV.
    """
    if not param_space:
        print("No parameter space provided for optimization.")
        return None, None
    bayes_search = BayesSearchCV(
        model_instance,
        param_space,
        n_iter=50,  # Number of optimization iterations
        random_state=42,
        cv=3, # Cross-validation folds
        n_jobs=-1 # Use all available cores
    )
    bayes_search.fit(X_train, y_train)
    print("Best parameters found: ", bayes_search.best_params_)
    print("Best accuracy found: ", bayes_search.best_score_)
    return bayes_search.best_estimator_, bayes_search.best_params_
# --- Visualization ---
def plot_distribution(df: pd.DataFrame, column: str):
    """
    Plots the distribution of a specified column.
    """
    if column not in df.columns:
        print(f"Column '{column}' not found in DataFrame.")
        return
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column].dropna(), kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
def plot_correlation_matrix(df: pd.DataFrame):
    """
    Plots the correlation matrix for numerical columns.
    """
    numerical_df = df.select_dtypes(include=np.number)
    if numerical_df.empty:
        print("No numerical columns to plot correlation matrix.")
        return
    plt.figure(figsize=(12, 10))
    sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()
# --- Authentication (for Colab/Jupyter) ---
def authenticate_google():
    """
    Authenticates the user for Google services (Colab/Jupyter).
    Returns the gspread client.
    """
    from google.colab import auth
    import gspread
    from google.auth import default
    try:
        auth.authenticate_user()
        creds, _ = default()
        gc = gspread.authorize(creds)
        print("Google authentication successful.")
        return gc
    except Exception as e:
        print(f"Google authentication failed: {e}")
        return None
# --- Main Execution Example ---
if __name__ == '__main__':
    # Example Usage:
    # 1. Authenticate
    gc_client = authenticate_google()
    if gc_client:
        # 2. Load data from a Google Sheet
        sheet_name = 'Your Google Sheet Name' # Replace with your sheet name
        df = load_spreadsheet(gc_client, sheet_name)
        if not df.empty:
            print("Original DataFrame head:")
            print(df.head())
            print("\nDataFrame Info:")
            df.info()
            # 3. Clean data
            df_cleaned = clean_data(df)
            print("\nCleaned DataFrame head:")
            print(df_cleaned.head())
            # 4. Feature Engineering (placeholder)
            df_engineered = feature_engineering(df_cleaned)
            # 5. Prepare data for modeling
            # Assuming 'target_column' is your target variable and other numerical columns are features
            target_column = 'Your Target Column Name' # Replace with your target column name
            if target_column in df_engineered.columns and df_engineered[target_column].dtype in [np.number, 'object']:
                # Convert target to numeric if it's not already, coercing errors
                df_engineered[target_column] = pd.to_numeric(df_engineered[target_column], errors='coerce')
                # Drop rows where the target is NaN after conversion
                df_engineered.dropna(subset=[target_column], inplace=True)
                if not df_engineered.empty:
                    features = df_engineered.select_dtypes(include=np.number).drop(columns=[target_column], errors='ignore')
                    target = df_engineered[target_column]
                    if not features.empty:
                        # Split data
                        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
                        print(f"\nTraining data shape: {X_train.shape}")
                        print(f"Testing data shape: {X_test.shape}")
                        # 6. Train a model
                        # Choose 'logistic_regression' or 'random_forest'
                        model_type = 'random_forest'
                        model = train_model(X_train, y_train, model_type=model_type)
                        print(f"\n{model_type} model trained.")
                        # 7. Evaluate the model
                        accuracy = evaluate_model(model, X_test, y_test)
                        print(f"\nModel accuracy on test set: {accuracy:.4f}")
                        # 8. Optimize the model (Example for Random Forest)
                        if model_type == 'random_forest':
                            rf_param_space = {
                                'n_estimators': Integer(50, 200),
                                'max_depth': Integer(3, 10),
                                'min_samples_split': Integer(2, 10),
                                'min_samples_leaf': Integer(1, 5),
                                'criterion': Categorical(['gini', 'entropy'])
                            }
                            optimized_model, best_params = optimize_model(RandomForestClassifier(random_state=42), X_train, y_train, rf_param_space)
                            if optimized_model:
                                optimized_accuracy = evaluate_model(optimized_model, X_test, y_test)
                                print(f"\nOptimized {model_type} model accuracy on test set: {optimized_accuracy:.4f}")
                        # 9. Visualize data
                        # Example: Plot distribution of a feature column (replace 'Your Feature Column Name' with an actual column)
                        feature_to_plot = features.columns[0] if not features.empty else None
                        if feature_to_plot:
                            plot_distribution(df_engineered, feature_to_plot)
                        # Plot correlation matrix
                        plot_correlation_matrix(df_engineered)
                    else:
                        print("No numerical features found for modeling.")
                else:
                    print(f"No data remaining after dropping rows with missing target values in '{target_column}'.")
            else:
                print(f"Target column '{target_column}' not found or is not suitable for classification/regression.")
        else:
            print("Failed to load spreadsheet data.")
    else:
        print("Google authentication failed. Cannot proceed with spreadsheet operations.")
    # Example Zero-Shot Classification
    text_to_classify = "This movie was fantastic and I loved the acting."
    possible_labels = ["positive", "negative", "neutral"]
    try:
        classification_results = zero_shot_classification(text_to_classify, possible_labels)
        print("\nZero-Shot Classification Results:")
        print(classification_results)
    except Exception as e:
        print(f"\nZero-Shot Classification failed: {e}")
    # Example Code Generation (Placeholder)
    generated_code = generate_code("create a data visualization", "python", "placeholder")
    print("\nGenerated Code Example:")
    print(generated_code)
    # Example Chain-of-Thought (Placeholder)
    chain_of_thought("Explain the concept of overfitting.", "Hint: Mention bias-variance trade-off.", "placeholder")
