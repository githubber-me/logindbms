import streamlit as st

# Hardcoded user credentials
USERS = {
    "akash": "password",
    "sahana": "password",
    "admin": "adminpassword"
}

# Function to authenticate user against hardcoded credentials
def authenticate(username, password):
    return USERS.get(username) == password

def life():
    st.title("Login Page")
    
    # Display an image below the title
    st.image("6.png", use_column_width=True)

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.sidebar.success("Logged in as {}".format(username))
            st.markdown("---")
            st.markdown("### Redirecting to Hackathon DBMS...")
            
            # Redirect to the external website
            st.markdown(
                """
                <meta http-equiv="refresh" content="0; url=https://localhost:8501" />
                """,
                unsafe_allow_html=True
            )
        else:
            st.sidebar.error("Incorrect username or password")

if __name__ == "__main__":
    life()
