import pandas as pd 
import pickle 
import streamlit as st 

# Load your model
movies_dict = pickle.load(open('LinearRegressionModel_dict.pkl', 'rb'))
moviess = pd.DataFrame(movies_dict)
model = pickle.load(open('LinearRegressionModel)(2).pkl','rb'))

# Custom CSS
st.markdown(
    """
    <style>
    /* Your CSS styles here */
    .title {
        font-size: 40px;
        color: #FF5733;
        text-align: center;
    }
    .stButton > button {
        background-color: #007BFF; /* Bright blue for the button */
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 10px;
         transition: background-color 0.3s ease, transform 0.3s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3); /* Add shadow for depth */
    }
    .stButton > button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        transform: translateY(-2px); /* Slight lift on hover */
    }
    .stButton > button:active {
        background-color: #004494; /* Even darker blue on click */
        transform: translateY(0px); /* Button stays flat on click */
    }
    
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <h1 style='text-align: center; font-size: 40px; color: #DAA520;'>
        🎬 Movies Ticket Price Prediction<br>
        
    </h1>
""", unsafe_allow_html=True)

# App title
#st.title('🎬 Movie Ticket Price Prediction & Recommendation System ')
st.header('Predict Movie Ticket Prices')

# User inputs with columns
col1, col2, col3 = st.columns(3)

with col1:
    selected_movie = st.selectbox('Select A Movie:', moviess['title'].values, key='movie_select')

with col2:
    selected_day = st.selectbox('Select A Day:', ('Weekday', 'Weekend'), key='day_select')

with col3:
    selected_theater = st.selectbox('Select A Theater Type:', ('multiplex', 'single screen'), key='theater_select')


# Button to make prediction
if st.button('Predict Price'):
    input_data = {
        'title': selected_movie,
        'Day of the Week': selected_day,
        'Theater Type': selected_theater
    }
    input_df = pd.DataFrame([input_data])
    predicted_price = model.predict(input_df)

    st.success(f'The predicted ticket price is: **{predicted_price[0]:.2f}**')

    