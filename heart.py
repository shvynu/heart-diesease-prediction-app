import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Heart Disease Prediction App",
                   layout="wide",
                   page_icon="🥼🩺")

# Function to load the model
def load_model(model_path):
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error(f"Model file not found at {model_path}")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        return None

# Getting the working directory of the script
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(working_dir, 'saved_models', 'heart_disease_model.sav')

# Loading the saved model
heart_disease_model = load_model(model_path)

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['heart'],
                           default_index=0)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy')

    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    # Code for prediction
    heart_diagnosis = ''

    # Creating a button for prediction
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

            # Convert inputs to float
            user_input = [float(x) for x in user_input]

            if heart_disease_model is not None:
                heart_prediction = heart_disease_model.predict([user_input])

                if heart_prediction[0] == 1:
                    heart_diagnosis = 'The person is prone to heart disease'
                else:
                    heart_diagnosis = 'The person does not prone to have any heart disease'

                st.success(heart_diagnosis)
            else:
                st.error("Model could not be loaded. Prediction cannot be performed.")
        except ValueError as ve:
            st.error(f"Input error: {ve}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

