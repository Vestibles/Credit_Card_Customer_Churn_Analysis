import streamlit as st
import pandas as pd
import joblib
import seaborn as sns

import matplotlib.pyplot as plt

# ------------------------
# Load model & data
# ------------------------


@st.cache_resource
def load_model():
    return joblib.load("best_churn_model.pkl")


@st.cache_data
def load_data():
    try:
        return pd.read_csv(r"Data/cleaned_bank_churn.csv")
    except FileNotFoundError:
        st.error("Data file not found. Please ensure 'Data/cleaned_bank_churn.csv' exists.")
        return pd.DataFrame()


model = load_model()
df = load_data()

# ------------------------
# Page setup
# ------------------------
st.set_page_config(page_title="Bank Churn Dashboard", layout="wide")
st.title("💳 Bank Customer Churn Dashboard")

# ------------------------
# Tabs for navigation
# ------------------------
tab1, tab2 = st.tabs(["📊 Dashboard", "🔮 Prediction"])

# ========================
# Dashboard Tab
# ========================
with tab1:
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)

    total_customers = len(df)
    churn_rate = df["Attrition_Flag_Attrited Customer"].mean() * 100
    avg_transactions = df["Total_Trans_Amt"].mean()

    col1.metric("Total Customers", f"{total_customers:,}")
    col2.metric("Churn Rate", f"{churn_rate:.1f}%")
    col3.metric("Avg. Transactions", f"${avg_transactions:,.0f}")

    st.markdown("---")

    # Churn Distribution
    fig, ax = plt.subplots()
    sns.countplot(x="Attrition_Flag_Attrited Customer", data=df, ax=ax)
    ax.set_xticklabels(["Stayed", "Churned"])
    ax.set_title("Churn Distribution")
    st.pyplot(fig)

    # Feature importance (if available)
    if hasattr(model, "feature_importances_"):
        feature_cols = df.drop(
            columns=["Attrition_Flag_Attrited Customer"]
        ).columns
        importances = pd.Series(
            model.feature_importances_,
            index=feature_cols
        )
        importances = importances.sort_values(ascending=False)

        fig2, ax2 = plt.subplots()
        sns.barplot(x=importances, y=importances.index, ax=ax2)
        ax2.set_title("Feature Importance")
        st.pyplot(fig2)

# ========================
# Prediction Tab
# ========================
with tab2:
    st.subheader("Single Customer Prediction")

    input_data = {}
    for col in df.drop(columns=["Attrition_Flag_Attrited Customer"]).columns:
        if df[col].dtype in [int, float]:
            input_data[col] = st.number_input(
                col,
                value=float(df[col].median())
            )
        else:
            options = df[col].unique().tolist()
            default_idx = options.index(df[col].mode()[0])
            input_data[col] = st.selectbox(
                col, options, index=default_idx
            )

    if st.button("Predict Churn"):
        X_new = pd.DataFrame([input_data])
        prediction = model.predict(X_new)[0]
        probability = model.predict_proba(X_new)[0][1]

        if prediction == 1:
            st.error(f"⚠️ Likely to churn. Probability: {probability:.2%}")
        else:
            st.success(
                f"✅ Likely to stay. "
                f"Churn probability: {probability:.2%}"
            )

    st.markdown("---")
    st.subheader("📂 Batch Prediction from CSV")
    uploaded_file = st.file_uploader(
        "Upload batch prediction CSV file", type=["csv"]
    )
    if uploaded_file is not None:
        batch_df = pd.read_csv(uploaded_file)
        feature_cols = df.drop(
            columns=["Attrition_Flag_Attrited Customer"]
        ).columns
        # Ensure batch_df has the same columns as the training data
        missing_cols = set(feature_cols) - set(batch_df.columns)
        extra_cols = set(batch_df.columns) - set(feature_cols)
        if missing_cols:
            st.error(f"Missing columns in uploaded file: {missing_cols}")
        else:
            batch_df = batch_df[list(feature_cols)]
            preds = model.predict(batch_df)
            probs = model.predict_proba(batch_df)[:, 1]
            batch_df["Churn_Prediction"] = preds
            batch_df["Churn_Probability"] = probs
            st.write(batch_df)
            csv = batch_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download Predictions",
                data=csv,
                file_name="batch_predictions.csv",
                mime="text/csv"
            )
            