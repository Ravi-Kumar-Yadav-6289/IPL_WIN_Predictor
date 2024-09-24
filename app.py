import pickle
import pandas as pd
import streamlit as st

teams = ['Royal Challengers Bengaluru', 'Punjab Kings', 'Delhi Capitals',
       'Kolkata Knight Riders', 'Rajasthan Royals', 'Mumbai Indians',
       'Chennai Super Kings', 'Deccan Chargers',
       'Rising Pune Supergiants', 'Kochi Tuskers Kerala',
       'Sunrisers Hyderabad', 'Gujarat Titans', 'Lucknow Super Giants']

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Kochi', 'Indore', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi',
       'Abu Dhabi', 'Rajkot', 'Kanpur', 'Bengaluru', 'Sharjah', 'Dubai',
       'Navi Mumbai', 'Lucknow', 'Guwahati', 'Mohali']

st.title("IPL Win Predictor")
pipe = pickle.load(open("pipe.pkl",'rb'))

col1, col2= st.columns(2)

with col1:
       batting_team = st. selectbox("Select a batting team", sorted(teams))

with col2:
       bowling_team = st. selectbox("Select a bowling team", sorted([team for team in teams if team!=batting_team]))

selected_city = st.selectbox("Select a City", sorted(cities))

target = st.number_input("Target")

col3,col4,col5 = st.columns(3)

with col3:
       score = st.number_input('Score')

with col4:
       overs = st.number_input('Overs Completed')

with col5:
       wickets = st.number_input('Wickets')

if st.button('Predict Probability'):
       runs_left = target-score
       balls_left = 120-(overs*6)
       wickets_left = 10-wickets
       crr = score/overs
       rrr = (runs_left*6)/balls_left
       input = pd.DataFrame({'city':[selected_city],'batting_team':[batting_team],'bowling_team':[bowling_team],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets_left],'target_runs':[target],'crr':[crr],'rrr':[rrr]})
       st.table(input)
       result = pipe.predict_proba(input)
       #st.text(result)
       loss = result[0][0]
       win = result[0][1]
       st.text(batting_team + " :-> " + str(round(win*100))+"% ")
       st.text(bowling_team + " :-> " + str(round(loss*100)) + "% ")

