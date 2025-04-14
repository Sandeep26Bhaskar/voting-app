import streamlit as st
from files.Team import team_members
from files.profiler_ import profiler
from files.voting import voting_app

st.set_page_config(page_title="My App", page_icon="🚀", layout="wide")

# Navigation sidebar
st.sidebar.title("Sitemap")
if st.sidebar.button("Home", key="home_button"):
    st.session_state.page = "voting"

if st.sidebar.button("Profiler", key="profiler_button"):
    st.session_state.page = "profiler"

if st.sidebar.button("Team", key="team_button"):
    st.session_state.page = "team"

# Default to app.py
if 'page' not in st.session_state:
    st.session_state.page = "voting"


# Redirect to the selected page
if st.session_state.page == "voting":
    voting_app()
elif st.session_state.page == "profiler":
    profiler()

elif st.session_state.page == "team":
    team_members()

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




