import streamlit as st
import pandas as pd
import time as tym

@st.dialog("Details Form")
def details_form():
    username = st.text_input("username:")
    email = st.text_input("username:")
    if st.button("Sumit Details"):
        st.write(f"Details on {username} have been submitted successfully")


st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("This is a writer statement")
st.caption("This is a caption")

st.code("""
import streamlit as st

st.title("This is a title")
st.header("This is a header")
st.write("This is a writer statement")
st.caption("This is a caption")
""")

with st.echo():
    st.write("This statement will be executed")

st.divider()
#st.write("-------------")

df = pd.read_csv("data.csv")

st.dataframe(df.head())

edited_df = st.data_editor(df)

st.dataframe(edited_df.head())
st.metric("Temperature", 26,2)
st.metric("Rainfall", 1800, -150)

submit_button = st.button("Submit")
if submit_button:
    st.write("The button has been clicked")

feedback = st.feedback()
if feedback == 0:
    st.write("The user dislikes the content")
elif feedback == 1:
    st.write("The user likes the content")

stars = st.feedback("stars")
if stars or stars == 0:
    if stars == 0 or stars == 1:
        st.write("Low Rating")
    elif stars == 2:
        st.write("Medium Rating")
    elif stars > 2:
        st.write("High Rating")

terms = st.checkbox("I agree to the terms and conditions")

if terms:
    st.write("The user has agreed to the terms and conditions")

st.toggle("Activate")

gender = st.radio("Select your gender", ["Male","Female"])

if gender == "Male":
    st.write("The mens conference will begin shortly")
elif gender == "Female":
    st.write("The girls hang out will be at the spa")

team = st.checkbox("Select your fav team", ["Liverpool", "Arsenal", "Chelsea", "Manchester United"] )
if team == "Liverpool":
    st.write("you will never walk alone")
elif team == "Arsenal":
    st.write("")
elif team == "Chelsea":
    st.write("London is Blue")
elif team == "Manchester United":
    st.write("Glory glory ManU")
st.select_slider("Enter your size here",["XS","S","M","L","XL","2XL"])
age = st.number_input("Enter your age here:", min_value=5, max_value=50, value=25)
st.slider("Enter a number here:", min_value=1, max_value=50)

time = st.time_input("Enter the time for the appointment here")

name = st.text_input("Enter your name here")
las_name = st.text_input("Enter your last name here")
email = st.text_input("Enter your email here")
if st.button("Submit info"):
    st.write(f"Details on {name} have been submitted successfully")

essay = st.text_area("Write an essay here", height=150)
st.write(len(essay))
st.write(len(essay.split()))

uploaded_file = st.file_uploader("Upload your file here")
st.write(uploaded_file)
passport_photo = st.camera_input("Take a passport sized photo here")
st.image("download.jpg", width=100)

col1,col2,col3 = st.columns(3)
with col1:
    st.image("download.jpg", width=100)
with col2:
    st.image("download.jpg", width=100)
with col3:
    st.image("download.jpg", width=100)

col1, col2, col3 = st.columns(3)
with col1:
    f_name = st.text_input("First Name:")
with col2:
    s_name = st.text_input("Second Name:")
with col3:
    t_name = st.text_input("Third Name:")

st.write(f"{f_name} {s_name} {t_name}")

trigger = st.selectbox("Do you want to display the dialog box",["no", "yes"])
if trigger == "yes":
    details_form()

with st.expander("Click to see more details o the sale"):
    st.write("Sale id: 29892293")
    st.write("Sale Date: 23rd April 2024")
    st.write("Sale amount: 5500")
    st.write("customer id: CU8232")
    st.image("download.jpg", width=100)

# with st.sidebar:
#     st.write("This is part of the sidebar")
#     st.write("This is also part of the sidebar")
#     st.write("This is another part of the sidebar")
#     st.write("This is the last part of the sidebar")
#     st.button("Sidebar")

with st.spinner("Operation in progress.Please wait"):
        tym.sleep(5)
        st.write("Operation completed")

st.toast("You have successfully logged in")
st.write("This is a crown:crown: ")
#st.balloons

st.success("You have successfully logged in")
st.info("Upload a .csv or a .tsv file")
st.warning("You are close to exceeding the maximum character content")

st.write("This is so frustrating")
