import streamlit as st
import random 
import string

#Common weak Passwords 
weak_password = {"12345678" , "gerrys12", "qwerty123",  "password123", "admin", "123123", "letmein", "1234", "sunshine"}







st.markdown(
    """
    <style>
        /* Style the form box */
        div[data-testid="stForm"] {
            background-color: #FBFBFB;  /* Light gray background */
            padding: 15px;
            border-radius: 8px;
            border: 3px solid #00303F;
           box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);

        }

        /* Style the password input field */
        input[type="password"] {
            border: 2px solid #789DBC;  /* Green border */
            padding: 8px;
            border-radius: 5px;
            font-size: 16px;
        }

         /* Change Streamlit button color */
        div.stButton > button {
            border: 2px solid #00303F !important; /* Dark Blue */
            color: Black !important;
            font-weight:  bold !important;
            padding: 10px !important;
            border-radius: 8px !important;
            font-size: 16px !important;
            box-shadow: 0px 0px 10px rgba(0, 48, 63, 0.5) !important; /* Blur effect */
            transition: 0.3s;
        }

        /* Change button color on hover */
        div.stButton > button:hover {
            background-color: #004F6E !important; /* Lighter Blue */
            color: white !important;
            border: none !important;
        }

        div[data-testid="stForm"] button {
             border: 1px solid #00303F !important; /* Dark Blue */
            color: Black !important;
            font-weight:  bold !important;
            padding: 10px !important;
            border-radius: 8px !important;
            font-size: 16px !important;
            box-shadow: 0px 0px 10px rgba(0, 48, 63, 0.5) !important; /* Blur effect */
            transition: 0.3s;
            transition: 0.3s;
        }

        div[data-testid="stForm"] button:hover {
             background-color: #004F6E !important; /* Lighter Blue */
            color: white !important;
            border: none !important;
        }

      .footer {text-align: center; 
      font-size: 16px; 
      margin-top: 20px; 
      color: #303841;}

    </style>
    """,
    unsafe_allow_html=True
)

#Function to generate a strong  password
def generate_password(length=12):
    Characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "" .join(random.choice(Characters) for _ in range(length))

#Function to check if password is strength

def password_strength(password):
    score = 0
    feedback = []

    if password in weak_password:
        return 1, "Password is too weak"

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Password must contain at least one uppercase letter")


    if any(c.islower() for c in password):
        score += 1
    else:
            feedback.append("Password must contain at least one lowercase letter")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Password must contain at least one digit")

    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        feedback.append("Password must contain at least one special character")

    return score, "\n".join(feedback) if score < 5 else "Strong password!✅"


# stream lit ui 

st.markdown("<h1 style='text-align: center; color: #004F6E;'>🔐 Password Strength Meter 🔑</h1>", unsafe_allow_html=True)

st.write("")
st.markdown("""     _This app checks the strength of your password and suggests a strong password for you_  """)
st.write("")
st.write("")
st.write("")

with st.form("password_form"):
    password = st.text_input("Enter your password", type="password", help="Enter your password here")
    st.form_submit_button("Check Strength")  



    if password:
        score, feedback = password_strength(password)
    

        st.progress(score/5)
        if score >= 5 :
            st.success(f"Password Strength: Strong!✅ ({score}/5)")
        elif score >= 3:
            st.warning(f"Password Strength: Moderate!⚠️ ({score}/5)")
        else:
            st.error(f"Password Strength: Weak!❌ ({score}/5)")


# Password Generator Section
if st.button("Generate Strong Password"):
    st.success(f"Suggested Password: {generate_password()}")
    st.write("")
    st.write("")


# Footer
st.markdown("<div class='footer'>Developed by <b> Simra Jabbar </b> 💜 | Powered by Streamlit</div>", unsafe_allow_html=True)
