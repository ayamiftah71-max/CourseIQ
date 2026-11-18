
import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="CourseIQ",
    page_icon="🎓",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return joblib.load("modele_svm.pkl")

model = load_model()

# ---------------- CSS DESIGN ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #070B2B, #101044, #160D35);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #11163D, #171044);
    border-right: 1px solid #343B80;
}

h1, h2, h3, p, label {
    color: white !important;
}

.hero {
    padding: 35px;
    border-radius: 22px;
    background: linear-gradient(120deg, #171B55, #302078, #111B55);
    border: 1px solid #4549A0;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
}

.hero span {
    color: #7B8CFF;
}

.subtitle {
    color: #B8C3F5 !important;
    font-size: 17px;
}

.metric-card {
    background: linear-gradient(135deg, #20275B, #17183F);
    border: 1px solid #414B91;
    border-radius: 18px;
    padding: 22px;
    text-align: center;
}

.metric-title {
    color: #AAB8EF;
    font-size: 15px;
}

.metric-value {
    font-size: 30px;
    font-weight: bold;
    color: #FFFFFF;
}

.panel {
    background: linear-gradient(145deg, #1B2050, #101638);
    border: 1px solid #454B96;
    border-radius: 20px;
    padding: 25px;
}

.result-popular {
    background: linear-gradient(135deg, #064D58, #102C59);
    border: 1px solid #00E5C0;
    border-radius: 20px;
    padding: 35px;
    text-align: center;
}

.result-not-popular {
    background: linear-gradient(135deg, #51234B, #242052);
    border: 1px solid #B45CDB;
    border-radius: 20px;
    padding: 35px;
    text-align: center;
}

div.stButton > button {
    background: linear-gradient(90deg, #493BFF, #C52EFF, #F044B7);
    color: white;
    border: none;
    border-radius: 30px;
    padding: 12px 25px;
    font-weight: bold;
    width: 100%;
}

div.stButton > button:hover {
    border: 1px solid white;
    color: white;
}

[data-testid="stMetric"] {
    background: #1B2050;
    border: 1px solid #414B91;
    padding: 15px;
    border-radius: 15px;
}

[data-testid="stMetricValue"] {
    color: white;
}

.stTextInput input, .stNumberInput input {
    background-color: #202653;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("<h1 style='text-align:center;color:#65DDF5'>🎓 CourseIQ</h1>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#AAB8EF'>Smart Analytics</p>",
                unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "Navigation",
        ["🏠 Dashboard", "🤖 Prediction", "📊 Insights", "ℹ️ About"]
    )

    st.divider()

    st.markdown("### 🟢 Model Status")
    st.success("Model Online")

    st.markdown("**Algorithm:** SVM (RBF)")
    st.markdown("**Test Accuracy:** 61.45%")
    st.markdown("**Features:** 11")

    st.divider()
    st.caption("CourseIQ © 2026")

# ---------------- DASHBOARD ----------------
if page == "🏠 Dashboard":

    st.markdown("""
    <div class="hero">
        <h1>Predict the <span>Popularity</span><br>of Your Course 🎓</h1>
        <p class="subtitle">
        Discover the potential of your online courses
        using Machine Learning.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Test Accuracy</div>
            <div class="metric-value">61.45%</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Selected Model</div>
            <div class="metric-value">SVM - RBF</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Input Features</div>
            <div class="metric-value">11</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown("### ✨ Ready to analyze your course?")
    st.write("Go to the Prediction section to test a course.")

    if st.button("🚀 Start Prediction"):
        st.session_state["go_prediction"] = True
        st.rerun()

    if st.session_state.get("go_prediction"):
        st.info("Select Prediction from the navigation menu.")

# ---------------- PREDICTION ----------------
elif page == "🤖 Prediction":

    st.markdown("""
    <div class="hero">
        <h1>Course <span>Prediction</span></h1>
        <p class="subtitle">
        Enter your course information to discover its popularity.
        </p>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1, 1])

    with left:
        st.markdown("### 🎓 Course Information")

        with st.form("course_form"):

            note = st.slider(
                "⭐ Course Rating",
                min_value=1.0,
                max_value=5.0,
                value=4.5,
                step=0.1
            )

            niveau = st.selectbox(
                "📊 Difficulty Level",
                ["Beginner", "Intermediate", "Advanced", "Mixed"]
            )

            certificat = st.selectbox(
                "🏅 Certificate Type",
                ["COURSE", "SPECIALIZATION",
                 "PROFESSIONAL CERTIFICATE"]
            )

            taille_org = st.number_input(
                "🏢 Number of courses by organization",
                min_value=1,
                value=10
            )

            titre = st.text_input(
                "✏️ Course Title",
                placeholder="e.g. Introduction to Python"
            )

            submitted = st.form_submit_button(
                "✨ Predict Popularity"
            )

    with right:
        st.markdown("### 🔮 Prediction Result")

        if submitted:

            if not titre.strip():
                st.warning("Please enter a course title.")

            else:
                # Feature Engineering
                longueur_titre = len(titre.split())

                niveau_inter = int(niveau == "Intermediate")
                niveau_adv = int(niveau == "Advanced")
                niveau_mixed = int(niveau == "Mixed")

                specialisation = int(
                    certificat == "SPECIALIZATION"
                )

                certif_pro = int(
                    certificat == "PROFESSIONAL CERTIFICATE"
                )

                mot_data = int("data" in titre.lower())
                mot_python = int("python" in titre.lower())
                mot_intro = int("introduction" in titre.lower())

                # DataFrame with the exact training columns
                donnees = pd.DataFrame([{
                    "note": note,
                    "niveau_Intermediate": niveau_inter,
                    "niveau_Advanced": niveau_adv,
                    "niveau_Mixed": niveau_mixed,
                    "specialisation": specialisation,
                    "certif_pro": certif_pro,
                    "longueur_titre": longueur_titre,
                    "taille_org": taille_org,
                    "mot_Data": mot_data,
                    "mot_Python": mot_python,
                    "mot_Introduction": mot_intro
                }])

                # Prediction
                prediction = model.predict(donnees)[0]

                if prediction == 1:
                    st.markdown("""
                    <div class="result-popular">
                        <h1>🏆</h1>
                        <h2>Popular Course!</h2>
                        <p>This course is predicted to be popular.</p>
                    </div>
                    """, unsafe_allow_html=True)

                else:
                    st.markdown("""
                    <div class="result-not-popular">
                        <h1>📘</h1>
                        <h2>Non-Popular Course</h2>
                        <p>This course is predicted to be less popular.</p>
                    </div>
                    """, unsafe_allow_html=True)

                st.write("")
                st.markdown("### 📋 Course Summary")

                a, b, c = st.columns(3)

                a.metric("Rating", f"{note}/5")
                b.metric("Difficulty", niveau)
                c.metric("Title Length", f"{longueur_titre} words")

        else:
            st.info("👈 Complete the form and click Predict Popularity.")

# ---------------- INSIGHTS ----------------
elif page == "📊 Insights":

    st.markdown("""
    <div class="hero">
        <h1>Model <span>Insights</span></h1>
        <p class="subtitle">Understanding our Machine Learning model.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Model Performance")

    col1, col2, col3 = st.columns(3)
    col1.metric("Accuracy", "61.45%")
    col2.metric("Precision", "69.64%")
    col3.metric("Recall", "42.86%")

    st.markdown("### Model Information")
    st.write("""
    - Algorithm: Support Vector Machine (SVM)
    - Kernel: RBF
    - Best C: 1
    - Best Gamma: 0.01
    - Cross-validation score: 58.43%
    """)

    st.info(
        "The model has a moderate predictive performance. "
        "Its predictions should be interpreted as estimates."
    )

# ---------------- ABOUT ----------------
elif page == "ℹ️ About":

    st.markdown("""
    <div class="hero">
        <h1>About <span>CourseIQ</span></h1>
        <p class="subtitle">
        A Machine Learning project for predicting online course popularity.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Project Objective")

    st.write("""
    CourseIQ uses Machine Learning to predict whether an online course
    is popular or non-popular based on its characteristics.

    The project uses a Support Vector Machine with an RBF kernel.
    """)

    st.markdown("### 🧠 Technologies")
    st.write("Python · Pandas · Scikit-learn · Streamlit")
