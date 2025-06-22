from mappings import previous_qualification, course_options, boolean_options
import streamlit as st
import numpy as np
import joblib

# Load package
package = joblib.load("model_package.joblib")
model = package["model"]
scaler = package["scaler"]
feature_order = package["features"]

# Kelompokkan fitur
academic_features = [
    'Previous_qualification',
    'Previous_qualification_grade',
    'Admission_grade',
    'Age_at_enrollment',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations',
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade'
]

administrative_features = [
    'Course',
    'Displaced',
    'Educational_special_needs',
    'Debtor',
    'Tuition_fees_up_to_date',
    'Scholarship_holder'
]

# Streamlit UI
st.set_page_config(page_title="Jaya Jaya Institut Prediksi Dropout Mahasiswa", layout="wide")
st.title("Academic Dropout Predictor")

st.markdown("Please fill in the following data based on the feature category.")

inputs = {}

with st.form("dropout_form"):

    with st.expander("🎓 Student Academic Information"):
        cols = st.columns(3)
        with cols[0]:
            selected_qualification = st.selectbox("Previous Qualification", list(previous_qualification.keys()))
            inputs["Previous_qualification"] = previous_qualification[selected_qualification]

        # Fitur akademik numerik lainnya
        for i, feature in enumerate(academic_features):
            if feature != "Previous_qualification":
                col = cols[i % 3]
                inputs[feature] = col.number_input(feature.replace("_", " ").title(), step=0.01, format="%.2f")


    with st.expander("🧾 Student Administrative Data"):
        cols = st.columns(3)
        with cols[0]:
            selected_course = st.selectbox("Course", list(course_options.keys()))
            inputs["Course"] = course_options[selected_course]

        # Fitur boolean administratif
        boolean_fields = administrative_features[1:] 
        for i, feature in enumerate(boolean_fields):
            col = cols[(i + 1) % 3]
            label = feature.replace("_", " ").title()
            selected = col.selectbox(label, list(boolean_options.keys()))
            inputs[feature] = boolean_options[selected]
    submitted = st.form_submit_button("Dropout Prediction")

# Prediksi
if submitted:
    input_array = np.array([inputs[f] for f in feature_order]).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]

    label = "Dropout" if prediction == 1 else "No Dropout"

    if label == "No Dropout":
        st.success(f"✅ Predicted Results: **{label}** - Students tend to persist.")

    else:
        st.error(f"⚠️ Predicted Results: **{label}** - Dropout risk detected.")