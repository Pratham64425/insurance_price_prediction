import streamlit as st
import pickle
import pandas as pd

# Load your models
eda = pickle.load(open(r"C:\\Users\\Pratham Sonigara\\Desktop\\itvedant\\Machine Learning\\Projects\\Insurance_Price_Prediction\\Models\\eda_output.pkl", "rb"))
model = pickle.load(open(r"C:\\Users\\Pratham Sonigara\\Desktop\\itvedant\\Machine Learning\\Projects\\Insurance_Price_Prediction\\Models\\model_analysis.pkl", "rb"))
pipeline = pickle.load(open(r"C:\\Users\\Pratham Sonigara\\Desktop\\itvedant\\Machine Learning\\Projects\\Insurance_Price_Prediction\\Models\\pipeline.pkl", "rb"))

# Page Config (sidebar removed)
st.set_page_config(page_title="Premium Insurance Predictor", page_icon="💎", layout="wide", initial_sidebar_state="collapsed")

# CSS styling updated
st.markdown("""
    <style>
    body {
        background: #eef2f7;
        font-family: 'Poppins', sans-serif;
    }

    .main-title {
        font-size: 46px;
        font-weight: 900;
        color: #111;
        text-align: center;
        margin-bottom: -5px;
    }

    .subtitle {
        font-size: 17px;
        color: #333;
        text-align: center;
        margin-bottom: 22px;
    }

    .glass-card {
        background: #ffffff;
        border-radius: 18px;
        padding: 35px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.10);
        border: 1px solid #ccc;
    }

    .input-label {
        font-size: 15px;
        font-weight: 600;
        color: #111;
        margin-bottom: 4px;
    }

    .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #f7f9fc !important;
        border: 2px solid #444 !important;
        border-radius: 8px !important;
        color: #000 !important;
    }

    .stButton button {
        background: #007bff !important;
        color: white !important;
        font-size: 20px !important;
        padding: 12px !important;
        border-radius: 25px !important;
        width: 100% !important;
        transition: 0.3s;
        border: none;
    }

    .stButton button:hover {
        background: #0056b3 !important;
        transform: scale(1.04);
    }

    .result {
        background: #d9fce4;
        border-left: 8px solid #34c759;
        padding: 18px;
        border-radius: 12px;
        font-size: 22px;
        font-weight: 800;
        text-align: center;
        color: #155d27;
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    .footer {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
        color: #444;
    }

    /* Hide full sidebar */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title + Subheader
st.markdown("<div class='main-title'>📊 Insurance Cost Estimator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Fast and simple estimation for your insurance price</div>", unsafe_allow_html=True)

# Form Layout
col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.markdown("## Personal Details")
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("<div class='input-label'>Age</div>", unsafe_allow_html=True)
        age = st.number_input("", 18, 100, 30, key="age")

    with col_b:
        st.markdown("<div class='input-label'>BMI</div>", unsafe_allow_html=True)
        bmi = st.number_input("", 10.0, 60.0, 22.5, key="bmi")

    st.markdown("<div class='input-label'>Children</div>", unsafe_allow_html=True)
    children = st.number_input("", 0, 5, 1, key="children")

    st.markdown("## Lifestyle")
    col_c, col_d = st.columns(2)

    with col_c:
        st.markdown("<div class='input-label'>Sex</div>", unsafe_allow_html=True)
        sex = st.selectbox("", ["male", "female"], key="sex")

    with col_d:
        st.markdown("<div class='input-label'>Smoker</div>", unsafe_allow_html=True)
        smoker = st.selectbox("", ["yes", "no"], key="smoker")

    st.markdown("<div class='input-label'>Region</div>", unsafe_allow_html=True)
    region = st.selectbox("", ["southwest", "southeast", "northwest", "northeast"], key="region")

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💰 Predict Price"):
        data = pd.DataFrame([[age, bmi, children, sex, smoker, region]],
                            columns=["age", "bmi", "children", "sex", "smoker", "region"])
        
        result = pipeline.predict(data)[0]

        st.markdown(f"<div class='result'>Estimated Price: ₹ {result:,.2f}</div>", unsafe_allow_html=True)

    st.markdown("<div class='footer'>Made By Pratham Jain</div>", unsafe_allow_html=True)
