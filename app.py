import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Dry Bean Classification",
    page_icon="🌱",
    layout="wide"
)


# =========================================================
# LOAD MODEL AND SCALER
# =========================================================

model = joblib.load("models/dry_bean_model.pkl")
scaler = joblib.load("models/scaler.pkl")


# =========================================================
# HEADER
# =========================================================

st.title("🌱 Dry Bean Classification System")

st.markdown(
    """
    ### Machine Learning Based Dry Bean Variety Recognition

    This application predicts the variety of a dry bean using
    **16 geometric measurements** and a trained **Support Vector
    Machine (SVM)** classifier.
    """
)

st.divider()


# =========================================================
# MODEL INFORMATION
# =========================================================

st.subheader("🤖 Model Information")

info1, info2, info3, info4 = st.columns(4)

with info1:
    st.metric(
        "Algorithm",
        "SVM"
    )

with info2:
    st.metric(
        "Features",
        "16"
    )

with info3:
    st.metric(
        "Accuracy",
        "92.73%"
    )

with info4:
    st.metric(
        "Bean Classes",
        "7"
    )

st.divider()


# =========================================================
# INPUT SECTION
# =========================================================

st.subheader("📏 Enter Bean Measurements")

st.write(
    "Enter the geometric measurements of the bean below."
)


# =========================================================
# TWO COLUMNS
# =========================================================

col1, col2 = st.columns(2)


# =========================================================
# COLUMN 1
# =========================================================

with col1:

    area = st.number_input(
        "Area",
        min_value=0.0,
        value=50000.0
    )

    perimeter = st.number_input(
        "Perimeter",
        min_value=0.0,
        value=800.0
    )

    major_axis = st.number_input(
        "Major Axis Length",
        min_value=0.0,
        value=300.0
    )

    minor_axis = st.number_input(
        "Minor Axis Length",
        min_value=0.0,
        value=200.0
    )

    aspect_ratio = st.number_input(
        "Aspect Ratio",
        min_value=0.0,
        value=1.5
    )

    eccentricity = st.number_input(
        "Eccentricity",
        min_value=0.0,
        value=0.7
    )

    convex_area = st.number_input(
        "Convex Area",
        min_value=0.0,
        value=51000.0
    )

    equiv_diameter = st.number_input(
        "Equivalent Diameter",
        min_value=0.0,
        value=250.0
    )


# =========================================================
# COLUMN 2
# =========================================================

with col2:

    extent = st.number_input(
        "Extent",
        min_value=0.0,
        value=0.75
    )

    solidity = st.number_input(
        "Solidity",
        min_value=0.0,
        value=0.99
    )

    roundness = st.number_input(
        "Roundness",
        min_value=0.0,
        value=0.8
    )

    compactness = st.number_input(
        "Compactness",
        min_value=0.0,
        value=0.8
    )

    shape_factor1 = st.number_input(
        "Shape Factor 1",
        min_value=0.0,
        value=0.006
    )

    shape_factor2 = st.number_input(
        "Shape Factor 2",
        min_value=0.0,
        value=0.001
    )

    shape_factor3 = st.number_input(
        "Shape Factor 3",
        min_value=0.0,
        value=0.7
    )

    shape_factor4 = st.number_input(
        "Shape Factor 4",
        min_value=0.0,
        value=0.99
    )


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.divider()

predict_button = st.button(
    "🔍 Predict Bean Variety",
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    # -----------------------------------------------------
    # Create input dataframe
    # -----------------------------------------------------

    input_data = pd.DataFrame(
        [[
            area,
            perimeter,
            major_axis,
            minor_axis,
            aspect_ratio,
            eccentricity,
            convex_area,
            equiv_diameter,
            extent,
            solidity,
            roundness,
            compactness,
            shape_factor1,
            shape_factor2,
            shape_factor3,
            shape_factor4
        ]],
        columns=[
            "Area",
            "Perimeter",
            "MajorAxisLength",
            "MinorAxisLength",
            "AspectRation",
            "Eccentricity",
            "ConvexArea",
            "EquivDiameter",
            "Extent",
            "Solidity",
            "roundness",
            "Compactness",
            "ShapeFactor1",
            "ShapeFactor2",
            "ShapeFactor3",
            "ShapeFactor4"
        ]
    )


    # -----------------------------------------------------
    # Scale input
    # -----------------------------------------------------

    input_scaled = scaler.transform(
        input_data
    )


    # -----------------------------------------------------
    # Prediction
    # -----------------------------------------------------

    prediction = model.predict(
        input_scaled
    )


    predicted_class = prediction[0]


    # -----------------------------------------------------
    # Display result
    # -----------------------------------------------------

    st.success(
        f"🌱 Predicted Bean Variety: **{predicted_class}**"
    )


    # -----------------------------------------------------
    # Additional information
    # -----------------------------------------------------

    st.subheader("📊 Prediction Details")

    result_col1, result_col2 = st.columns(2)

    with result_col1:

        st.metric(
            "Predicted Variety",
            predicted_class
        )

    with result_col2:

        st.metric(
            "Model Accuracy",
            "92.73%"
        )


# =========================================================
# ABOUT THE PROJECT
# =========================================================

st.divider()

with st.expander("ℹ️ About This Project"):

    st.write(
        """
        This project uses machine learning to classify dry bean
        varieties based on geometric measurements extracted from
        bean images.

        Seven bean varieties are classified:

        • BARBUNYA
        • BOMBAY
        • CALI
        • DERMASON
        • HOROZ
        • SEKER
        • SIRA

        The final SVM classifier uses 16 geometric features and
        achieved an overall classification accuracy of 92.73%.
        """
    )


# =========================================================
# FEATURE INFORMATION
# =========================================================

with st.expander("📐 Features Used by the Model"):

    feature_list = [
        "Area",
        "Perimeter",
        "Major Axis Length",
        "Minor Axis Length",
        "Aspect Ratio",
        "Eccentricity",
        "Convex Area",
        "Equivalent Diameter",
        "Extent",
        "Solidity",
        "Roundness",
        "Compactness",
        "Shape Factor 1",
        "Shape Factor 2",
        "Shape Factor 3",
        "Shape Factor 4"
    ]

    for feature in feature_list:

        st.write(
            f"• {feature}"
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Dry Bean Classification System | Machine Learning Project"
)