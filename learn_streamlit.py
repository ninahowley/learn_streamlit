import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import time
from datetime import datetime
import csv 
import time as tm

st.set_page_config(layout="wide")

#-----------------------------------------
#Writing
#-----------------------------------------
st.title("✏️ 1. st.write()")
st.write("Hello world! :sunglasses:")
st.write("You can make text *italics* or **bold**... or ***both***")
st.write(f"You can show the result of a calculation: 1 + 3 = **{1+3}**")

df = pd.DataFrame(
    np.random.randn(100,3),
    columns=["a","b","c"]
    )
c = alt.Chart(df).mark_circle().encode(
    x="a", y="b", size="c", color="c",
).properties(title="Graph of Stuff")

st.write("You can also show a dataframe and a chart!!")
st.write("**Stuff**", df.head(10), c)

#-----------------------------------------
#Buttons
#-----------------------------------------
st.title("🔘 2. st.button()")

clicked = st.button("Click me!")

st.write(f"Button clicked: {clicked}")

if clicked:
    st.write("Why hello you 😘")
else:
    st.write("Goodbye")

#-----------------------------------------
#Sliders
#-----------------------------------------
st.title("🗓️ 3. st.slider()")

age = st.slider("How old are you?", 0, 130, 25)
st.write(f"I am **{age}** years old... 😎")

st.subheader("Schedule an appointment...")
dte = st.slider("What date?", value=datetime(2025,3,31))
tme = st.slider("What time?", value=(time(12,30),time(14,0)))
dte = str(dte)[:10]
st.write(f"Appointment scheduled for **{tme[0]}** to **{tme[1]}** on **{dte}**")

#-----------------------------------------
#Charts
#-----------------------------------------
st.title("📈 4. st.line_chart()")

st.write("Using the dataframe from earlier (1)")
st.line_chart(df)

#-----------------------------------------
#Select Box
#-----------------------------------------
st.title("🗳️ 5. st.selectbox()")

color = st.selectbox("What is your favorite color?", ['red','orange','yellow','green','blue','purple','pink'])
st.write(color)

column = st.selectbox("Which column do you want to display?", df.columns)
st.line_chart(df, x=None, y=column)

#-----------------------------------------
#Multiselect
#-----------------------------------------
st.title("🗃️ 6. st.multiselect()")

colors = st.multiselect("What are your favorite colors?", ['red','orange','yellow','green','blue','purple','pink'])
for color in colors:
    st.write(color)

#-----------------------------------------
#Checkbox
#-----------------------------------------
st.title("✅ 7. st.checkbox()")

st.write("What will you order?")
ic = st.checkbox("Ice cream")
co = st.toggle("Cookie")
if ic:
    st.write("🍦")
if co:
    st.write("🍪")

st.write("Choose if you want to see the dataframe")
show = st.toggle("Show preview")
if show:
    st.write(df.head(5))

#-----------------------------------------
#Secrets
#-----------------------------------------
st.title("🔐 8. st.secrets")

st.write("I dont know.. its a secret")

#-----------------------------------------
#Layout
#-----------------------------------------
st.title("🖼️ 10. Let's layout")

st.write("Check the sidebar...")
num = st.sidebar.slider("Choose a number", 0, 100)
st.write(f"Your number is **{num}**!!!")

with st.sidebar:
    st.header("Wassup")

#-----------------------------------------
#Progress
#-----------------------------------------
st.title("🚦 11. st.progress()")

with st.expander("About this app"):
    st.success("success")
    st.warning("warning")
    st.error("error")

st.write("Progression bar!")
prog = st.progress(0)

start = st.button("Click me to start progressing 😊")

if start: 
    for percent_complete in range(0,101,25):
        tm.sleep(0.5)
        prog.progress(percent_complete)
        st.write(f"{percent_complete}%")
        if percent_complete == 100:
            st.balloons()
            st.toast("Your task is complete! 😵‍💫")
            break

#-----------------------------------------
#Form
#-----------------------------------------
st.title("📋 12. st.form()")

with st.form("form"):
    st.header("Order your ice cream **☕**")
    
    flavor = st.selectbox("Flavor", ["vanilla", "chocolate", "strawberry", "oreo"])
    toppings = st.multiselect("Toppings",["sprinkes","m&ms","syrup","oreos"])
    cone = st.checkbox("Cone")

    st.form_submit_button("Submit")

st.write("**My Order**")
st.write("Flavor:")
st.write(f"--- {flavor}")
st.write(f"Toppings:")
for topping in toppings:
    st.write(f"--- {topping}")
st.write(f"Cone?: {cone}")

#-----------------------------------------
#Query Parameters
#-----------------------------------------
st.title("🤔 13. st.experimental_get_query_params()")
st.write("ask me later.... 😴💤")

#-----------------------------------------
#End
#-----------------------------------------
st.title("🪼🐊 Thats the end!!")
st.subheader("Goodbye... 🙋‍♀️")
st.write("Thank you to this youtube guy:")
st.write("https://www.youtube.com/watch?v=ydWjwxQ8fVE")

#-----------------------------------------
#File uploader
#-----------------------------------------
st.title("📂 9. st.file_uploader()")

st.write("Put at the end so it doesn't interrupt")

file = st.file_uploader("Choose a CSV file")

if file is None:
    st.warning("Please upload a CSV file")
    st.stop()

df2 = pd.read_csv(file)
columns = st.multiselect("Choose columns to preview", df2.columns)
preview = st.toggle("Data preview")
if preview:
    st.write(df2[columns])

num = st.slider("Biggest number to show from your file?", -2.5, 2.5, step=0.25)
with st.expander("Selected data preview"):
    st.write("My CSV file")
    st.write(df2[df2 < num])