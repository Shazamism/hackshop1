import streamlit as st
import random
def game():
    if "low" not in st.session_state:
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        st.session_state.attempts = 1
    st.title("Computer Guesses Your Number!")
    st.write("Think of a number between 1 and 100, and I'll try to guess it!")
    st.write(f"My guess is: **{st.session_state.guess}**")
    high=st.button("Too High")
    crt=st.button("Correct!")
    if st.button("Too Low"):
        st.session_state.low = st.session_state.guess + 1
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        st.session_state.attempts += 1
    elif high:
        st.session_state.high = st.session_state.guess - 1
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        st.session_state.attempts += 1
    elif crt:
        st.write(f"Yay! I guessed your number in {st.session_state.attempts} attempts.")
        if st.button("Play Again"):
            st.session_state.low = 1
            st.session_state.high = 100
            st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
            st.session_state.attempts = 1
st.title("Welcome to my Streamlit application!!!")

st.subheader("from the creator<3")
port=st.button("PORTFOLIO")
if port:
    st.html("<h3 >PORTFOLIO</h3>")
    st.html("<p ><b>NAME:</b>Praneash shiva S.R<br><b>DEPT:</b>BE.CSE(CYS)<br><b>G-mail:</b>srpshiva2006@gmail.com<br><b>Github:</b>https://github.com/Shazamism</p>")
    st.html("<h3>TECHNICAL SKILLS</h3>")
    st.html("<p ><b>Programming Languages:</b> C++, Python, HTML, CSS<br><b>Hardware & IoT:</b> Arduino, Raspberry Pi<br><b>Cybersecurity Concepts:</b> Blockchain, Networking</p>")
    st.html("<h3>PROJECTS</h3>")
    st.html("<p ><b>1.IoT warehouse robots</b><br><b>Description:</b>Warehouse robots powered by Arduino and Raspberry Pi are an increasingly popular choice for automating small to medium-scale operations due to their affordability, versatility, and ease of programming. These platforms can be used to create mobile robots, robotic arms, or automated systems to improve warehouse efficiency.<br><b>Types of robots:</b><br>Line follower robot, obstacle avoiding robot, pit avoider robot, light follower robots.</p>")


st.title("Welcome to Guessing game!!!")
if 'number_guess' not in st.session_state:
    st.session_state.number_guess = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
st.subheader("------------------------User Guessing Game-------------------------")
st.write("Guess a number between 1 and 100")
guess = st.number_input("Enter your guess:")
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess == st.session_state.number_guess:
        st.success(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
        if st.button("Play Again"):
            st.session_state.number_guess = random.randint(1, 100)
            st.session_state.attempts = 0
    elif guess < st.session_state.number_guess:
        st.write("Try a higher number!")
    else:
        st.write("Try a lower number!")
st.subheader("------------------------------------------------------------------------------")
st.subheader("------------------------Machaine Guessing Game-------------------------")
game()
st.subheader("------------------------------------------------------------------------------")