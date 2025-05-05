import streamlit as st
import numpy as np
import pickle
import plotly.graph_objects as go

# Load trained model
model = pickle.load(open('home_price_model.pkl', 'rb'))

# Function to generate improvement suggestions
def generate_suggestions(features):
    suggestions = []
    crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat = features

    if crim > 1.0:
        suggestions.append("📉 Lower crime rate (CRIM < 0.5) areas tend to increase home value.")
    if nox > 0.6:
        suggestions.append("🌿 Choose less polluted areas (NOX < 0.5) for better pricing.")
    if rm < 6.0:
        suggestions.append("🛏️ More rooms (RM > 6.5) usually boost house value.")
    if lstat > 15:
        suggestions.append("📊 Lower % low-income population (LSTAT < 12) areas may have higher prices.")
    if ptratio > 18.0:
        suggestions.append("🏫 Lower pupil-teacher ratio (PTRATIO < 18) can positively affect prices.")
    if tax > 500:
        suggestions.append("💸 Lower property tax (TAX < 400) zones are generally more valuable.")
    
    if not suggestions:
        suggestions.append("✅ This house has balanced features. Looks good!")

    return suggestions

# Centered form layout
st.title("🏠 AI-Powered Home Price Predictor")
st.markdown("### Fill out the details below and click 'Predict' to get the home price estimation.")

# Creating form inside the main body (not sidebar)
with st.form("input_form"):
    # Collect input features for the prediction
    crim = st.number_input("Crime Rate (CRIM)", min_value=0.0, max_value=100.0, step=0.01, value=0.2, help="Per capita crime rate by town")
    zn = st.number_input("Residential Land % (ZN)", min_value=0.0, max_value=100.0, step=0.1, value=12.5, help="Proportion of residential land zoned")
    indus = st.number_input("Industrial Area (INDUS)", min_value=0.0, max_value=30.0, step=0.1, value=10.5, help="Proportion of non-retail business acres")
    chas = st.selectbox("Near Charles River (CHAS)", options=[0, 1], help="1 if tract bounds river; else 0")
    nox = st.number_input("Nitric Oxides (NOX)", min_value=0.3, max_value=1.0, step=0.01, value=0.45, help="Pollution levels (NOX)")
    rm = st.number_input("Avg Rooms per House (RM)", min_value=3.0, max_value=9.0, step=0.1, value=6.2, help="Average number of rooms per dwelling")
    age = st.number_input("Old Homes % (AGE)", min_value=0, max_value=100, step=1, value=60, help="Proportion of homes built before 1940")
    dis = st.number_input("Distance to Employment Centers (DIS)", min_value=1.0, max_value=15.0, step=0.1, value=4.5, help="Distance to employment centers")
    rad = st.number_input("Access to Highways (RAD)", min_value=1, max_value=24, step=1, value=4, help="Index of highway accessibility")
    tax = st.number_input("Tax Rate ($/10,000)", min_value=100, max_value=800, step=1, value=300, help="Full value property-tax rate")
    ptratio = st.number_input("Pupil-Teacher Ratio (PTRATIO)", min_value=10.0, max_value=25.0, step=0.1, value=15.3, help="Pupil-teacher ratio")
    b = st.number_input("Black Population Index (B)", min_value=0, max_value=400, step=1, value=350, help="B = 1000(Bk - 0.63)^2")
    lstat = st.number_input("% Low-Income Population (LSTAT)", min_value=0.0, max_value=40.0, step=0.1, value=12.5, help="% lower status of the population")

    submit = st.form_submit_button("🔍 Predict")

# On Submit
if submit:
    features = [crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]

    with st.spinner("🔎 Analyzing..."):
        prediction = model.predict([features])
        predicted_price = round(prediction[0], 2)

        # Tabs for structured output
        tab1, tab2, tab3 = st.tabs(["📈 Prediction", "💡 Suggestions", "📊 Feature Comparison"])

        with tab1:
            st.subheader("🏠 Predicted Home Price")
            if predicted_price > 400:
                st.success(f"🏡 High-value Property! Estimated Price: **${predicted_price}k**")
                st.balloons()
            elif predicted_price > 250:
                st.info(f"📊 Moderate Value: **${predicted_price}k**")
            else:
                st.warning(f"🔍 Low Value: **${predicted_price}k** — See improvement tips below.")
            
            st.metric(label="Estimated Price", value=f"${predicted_price}k")

        with tab2:
            st.subheader("💡 Suggestions to Improve Home Value:")
            suggestions = generate_suggestions(features)
            for suggestion in suggestions:
                st.write(f"- {suggestion}")

        with tab3:
            st.subheader("📊 Feature Comparison: Your Input vs Ideal")
            ideal = [0.5, 20.0, 5.0, 0, 0.4, 6.5, 30, 5.0, 4, 300, 15.0, 350, 12.0]
            labels = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"]

            fig = go.Figure()
            fig.add_trace(go.Bar(x=labels, y=features, name='Your Input'))
            fig.add_trace(go.Bar(x=labels, y=ideal, name='Ideal'))

            fig.update_layout(barmode='group', title="Feature Comparison (Your Inputs vs Ideal)")
            st.plotly_chart(fig)

    # Optional reset
    if st.button("🔁 Reset All"):
        st.experimental_rerun()
