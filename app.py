import streamlit as st
import json


st.set_page_config(page_title="Initiatives Voting App", page_icon=":ballot_box:")


# Disabling Streamlit's default animation and transition effects [Fade effect]
st.markdown(
    """
    <style>
    body {
        animation: none !important;
        transition: none !important;
    }
    .main {
        transition: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Initiatives Voting App")
st.write("Welcome to the Initiatives Voting App!")


# Sidebar content
st.sidebar.title("How This Benefits You")

# Custom Sidebar Styling (Toned Down for Semi-Formal Feel)
st.markdown(
    """
    <style>
        /* Sidebar Background - Subtle Gradient */
        .sidebar .sidebar-content {
            background: linear-gradient(135deg, #6c757d, #495057);  /* Gradient from Dark Gray to Slightly Lighter Gray */
            color: #f8f9fa;  /* Light text for contrast */
            padding: 20px;
            border-radius: 10px;
        }

        /* Sidebar Title */
        .sidebar .sidebar-content .sidebar-title {
            color: #f8f9fa;
            font-size: 20px;
            font-weight: bold;
            text-transform: uppercase;
        }

        /* Sidebar Text */
        .sidebar .sidebar-content .markdown-text-container p {
            font-size: 14px;
            color: #e0e0e0;
            line-height: 1.6;
        }

        /* Hover effect for links */
        .sidebar .sidebar-content .markdown-text-container a:hover {
            color: #ffffff;
            background-color: #343a40;  /* Darker color for hover effect */
            text-decoration: underline;
        }

        /* Adding a soft shadow to the sidebar */
        .sidebar .sidebar-content {
            box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.2);
        }

        /* Adding rounded corners to sidebar */
        .sidebar .sidebar-content {
            border-radius: 12px;
        }

        /* Customize buttons in the sidebar */
        .sidebar .sidebar-content button {
            background-color: #495057;  /* Dark Gray */
            color: #f8f9fa;  /* Light text */
            border-radius: 6px;
            padding: 10px 15px;
            border: none;
            font-size: 16px;
        }

        /* Hover effect for buttons */
        .sidebar .sidebar-content button:hover {
            background-color: #6c757d;  /* Slightly lighter gray on hover */
            cursor: pointer;
        }
    </style>
    """, unsafe_allow_html=True)
    
# Sidebar Description
st.sidebar.write("""
    As a part of this voting system, you will help choose initiatives that align with your personal goals and growth.
    The initiatives you select will not only help you grow but will also contribute to the collective growth of the team.

    **Why Your Vote Matters:**
    - Your vote determines the initiatives that will be prioritized.
    - Selecting initiatives that resonate with your goals can lead to personal development.
    - The team grows as a whole when everyone contributes their voice in this democratic selection process.

    **Voting Rules:**
    - Each user can only vote once.
    - Be honest and vote for the initiative that truly resonates with you.
    - The initiative with the most votes will be selected for team development.
    - Please avoid misusing the input fields, as this may lead to unnecessary data and affect the accuracy of the results.            

    Together, we are building a stronger, more effective team, where individual growth contributes to a unified objective.
""")

# File paths
INITIATIVES_FILE = 'initiatives.json'
VOTES_FILE = 'votes.json'
ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]

# Initialize session state
if 'role' not in st.session_state:
    st.session_state.role = None

# Load initiatives
try:
    with open(INITIATIVES_FILE, 'r') as f:
        initiatives = json.load(f)
except FileNotFoundError:
    initiatives = []

# Load votes
try:
    with open(VOTES_FILE, 'r') as f:
        votes = json.load(f)
except FileNotFoundError:
    votes = {}

# Choose role
if st.session_state.role is None:
    role = st.radio("Choose your role:", ['Admin', 'Voter'])
    if role == 'Admin':
        password = st.text_input("Enter Admin Password:", type="password")
        if password == ADMIN_PASSWORD:
            st.session_state.role = 'Admin'
            st.success("Welcome, Admin!")
            st.rerun()
        else:
            st.error("Incorrect password. Please try again.")
    else:
        st.session_state.role = 'Voter'
        st.rerun()

# Admin Section
if st.session_state.role == 'Admin':
    if not initiatives:
        options = st.text_area("Enter the initiatives you want to vote on (one per line):")
        if st.button("Submit Initiatives"):
            initiatives = [option.strip() for option in options.splitlines() if option.strip()]
            with open(INITIATIVES_FILE, 'w') as f:
                json.dump(initiatives, f)
            st.success("Initiatives submitted successfully!")
            st.rerun()
    else:
        st.write("Initiatives are already set:")
        st.write(initiatives)

    if st.button("Vote as Admin"):
        st.session_state.role = 'Voter'
        st.rerun()
    # Add Reset Button for Admin
    if st.button("Reset Voting (Admin Only)"):
        with open(INITIATIVES_FILE, 'w') as f:
            json.dump([], f)  # Clear initiatives file
        with open(VOTES_FILE, 'w') as f:
            json.dump({}, f)  # Clear votes file
        st.success("Voting data has been reset!")
        st.rerun()

# Voter Section
if st.session_state.role == 'Voter':
    if not initiatives:
        st.error("No initiatives available. Please wait for the admin to set them.")
    else:
        user_id = st.text_input("Enter your unique ID (e.g., name or email):")
        if user_id in votes:
            st.warning("You have already voted.")
        else:
            choice = st.radio("Select an initiative to vote for:", initiatives)
            if st.button("Submit Vote"):
                votes[user_id] = choice
                with open(VOTES_FILE, 'w') as f:
                    json.dump(votes, f)
                st.success("Thank you for voting!")



# Display Results (for transparency)
st.write("Total Votes:", votes)

#Display Tally of votes to the voters and admins
tally = {}
with open('votes.json','r') as f:
    votes = json.load(f)
    
    for task in votes.values():
            # print(task)
            if task not in tally:
                tally[task] = 1
            else:
                tally[task] += 1    
print("Tally:",tally)
sorted_tally = sorted(tally.items(), key =lambda x:x[1], reverse=True)
if sorted_tally:
    highest_score = sorted_tally[0][1]
    duplicate_initiatives = [name for name,score in sorted_tally if score == highest_score]
    if len(duplicate_initiatives)>1:
        st.warning(f"⚠️ It's a draw between: {', '.join(duplicate_initiatives)} with {highest_score} votes each!")
    else:
        st.success("🏆 The Winner is : {} with {} votes".format(sorted_tally[0][0], sorted_tally[0][1]))
else:
    st.warning("No votes have been cast yet.")


# Footer Section
footer = """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
        }
        .footer a {
            color: #0f4b5a;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
    <div class="footer">
        Made with ❤️ by <a href="https://github.com/Sandeep26Bhaskar" target="_blank">Sandeep Bhaskar</a>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)

# # Initialize session state if not present
# if "input_text" not in st.session_state:
#     st.session_state.input_text = ""

# if "formatted_options" not in st.session_state:
#     st.session_state.formatted_options = []

# if "submitted" not in st.session_state:
#     st.session_state.submitted = False

# #Add a button to clear all the initiatives 
# if st.button("Clear Input"):
#     st.session_state.formatted_options = ""  # Ensure options reflect the cleared state
#     st.success("Input cleared successfully!")


# if not st.session_state.formatted_options:
#     options = st.text_area("Enter the initiatives you want to vote on (one per line):")


# #Add a button to submit the initiatives 
#     if st.button("submit"):
#         options = options.splitlines()
#         formatted_options = [option.strip() for option in options]
#         st.session_state.formatted_options = formatted_options  # Store the formatted options in session state
#         st.session_state.submitted = True
#         st.success("Initiatives submitted successfully!")
# if st.session_state.submitted:
#     st.info("Initiatives have been submitted. Voting is now open!")
#     voting = st.radio("Select an initiative to vote for:", options=st.session_state.formatted_options, index=None)

#     if voting:
#         st.write("You voted for:", voting)
#         st.write("### Thank you for voting!")

# # Display Submitted Initiatives
# # if "formatted_options" in st.session_state:
# #     st.write("### Initiatives Entered:")
# #     st.write(st.session_state.formatted_options)




