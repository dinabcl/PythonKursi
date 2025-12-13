import streamlit as st

def main():
    st.title("Hello, World!")

    if st.button("Click me"):
        st.write("Button was clicked")

    st.checkbox("Check me")

    if st.checkbox("Check me to show some text"):
        st.write("You're seeing this text because you checked the checkbox")

    user_input = st.text_input("Enter text", "Sample text")
    st.write("You entered:", user_input)

    age = st.number_input("Enter your age", min_value=0, max_value=100)
    st.write(f"Your age is: {age}")

    message = st.text_area("Enter your message")
    st.write(f"Your message:{message}")

    choice = st.radio("Pick one", ["Choice 1","Choice 2"])
    st.write(f"you chose: {choice}")

    if st.button("Success"):
        st.success("Operation was sucesful")

    try:
        1/0
    except Exception as e:
        st.exception(e)

if __name__ == "__main__":
    main()


