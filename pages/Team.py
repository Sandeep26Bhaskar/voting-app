import streamlit as st
import json
import time

# Team member list
# team_members = [
#     {"name": "Alice Johnson", "title": "Software Engineer", "photo": "https://randomuser.me/api/portraits/women/1.jpg"},
#     {"name": "Bob Smith", "title": "Data Scientist", "photo": "https://randomuser.me/api/portraits/men/2.jpg"},
#     {"name": "Charlie Brown", "title": "Product Manager", "photo": "https://randomuser.me/api/portraits/men/3.jpg"},
#     {"name": "Diana Prince", "title": "UI/UX Designer", "photo": "https://randomuser.me/api/portraits/women/4.jpg"},
#     {"name": "Ethan Hunt", "title": "Security Analyst", "photo": "https://randomuser.me/api/portraits/men/5.jpg"},
#     {"name": "Fiona Gallagher", "title": "Marketing Specialist", "photo": "https://randomuser.me/api/portraits/women/6.jpg"},
#     {"name": "George Miller", "title": "DevOps Engineer", "photo": "https://randomuser.me/api/portraits/men/7.jpg"},
#     {"name": "Hannah Lee", "title": "Business Analyst", "photo": "https://randomuser.me/api/portraits/women/8.jpg"},
#     {"name": "Ian Wright", "title": "Cloud Architect", "photo": "https://randomuser.me/api/portraits/men/9.jpg"},
#     {"name": "Julia Roberts", "title": "Content Strategist", "photo": "https://randomuser.me/api/portraits/women/10.jpg"},
#     {"name": "Kevin Durant", "title": "AI Researcher", "photo": "https://randomuser.me/api/portraits/men/11.jpg"},
#     {"name": "Laura Palmer", "title": "Graphic Designer", "photo": "https://randomuser.me/api/portraits/women/12.jpg"},
#     {"name": "Michael Scott", "title": "Team Lead", "photo": "https://randomuser.me/api/portraits/men/13.jpg"},
#     {"name": "Nina Simone", "title": "HR Manager", "photo": "https://randomuser.me/api/portraits/women/14.jpg"},
#     {"name": "Oscar Wilde", "title": "Technical Writer", "photo": "https://randomuser.me/api/portraits/men/15.jpg"},
#     {"name": "Paula Abdul", "title": "Quality Assurance", "photo": "https://randomuser.me/api/portraits/women/16.jpg"},
# ]

# Introduction with a typing effect
st.set_page_config(page_title="Team Members", page_icon=":guardsman:", layout="wide") #with wide layout

def greetings(greets,delay=0.05):
    for char in greets:
        yield char
        time.sleep(delay)
st.write_stream(greetings("# anovIP's Patent Monetization"))
st.write_stream(greetings("#### Team Members:"))
# st.title("anovIP's Patent Monetization")
# st.subheader("Team Members:")

# CSS styling
st.markdown("""
    <style>
    .team-card {
        text-align: center;
        padding: 10px;
    }
    .team-photo {
        width: 100px;
        height: 100px;
        object-fit: cover;
        border-radius: 10%;
        border: 1px solid #ddd;
    }
    .team-card:hover {
        transform: scale(1.1);
        cursor: pointer;
        transition: transform 0.5s;
    }
    </style>
""", unsafe_allow_html=True)


with open('profiles.json', 'r') as f:
    team_members = json.load(f)

# Display team members in rows of 6
for i in range(0, len(team_members), 5):
    cols = st.columns(5)
    for j, member in enumerate(team_members[i:i+5]):
        with cols[j]:
            st.markdown(f"""
                <div class="team-card">
                    <img src="{member['photo']}" class="team-photo" />
                    <div><strong>{member['name']}</strong><br>{member['title']}</div>
                </div>
            """, unsafe_allow_html=True)
