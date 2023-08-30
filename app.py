from pathlib import Path

import streamlit as st
from PIL import Image

#-----Path Settings-----

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "SukhrajCheema_CV.pdf"
profile_pic = current_dir / "assets" / "profile_picture.png"



#-----General Settings-----

PAGE_TITLE = "Digital CV | Sukhraj Cheema"
PAGE_ICON = ":wave:"
NAME = "Sukhraj Cheema"
DESCRIPTION = """
Technical Account Executive, experience in performance marketing and automation.
"""
EMAIL = "sukh.100@hotmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com/SukhrajCheema",
}
PROJECTS = {
    "🏆 Machine Learning - Developed supervised machine learning algorithms to predict the median house price in any California district, using the Scikit-Learn API.": "https://github.com/SukhrajCheema/MachineLearning",
    "🏆 Google Ads API - Implemented a safety net for accounts in Google Ads, which would have their target automatically updated based on performance.": "",
    "🏆 2D Alien Invasion Game - Developed a fully interactive 2D Alien Invasion game using the Pygame module. The design pattern of the program consisted of a game loop which: handled user input, rendered assets and updated the game state.": "https://github.com/SukhrajCheema/AlienInvasion",
    "🏆 Binance API - Implemented a web socket client to stream candlestick data for a chosen cryptocurrency every minute. ": "https://github.com/SukhrajCheema/Binance_Trading_Bot",
}

st.set_page_config(PAGE_TITLE, PAGE_ICON)
st.title("Welcome, to my digital CV!")


#-----Load CSS, PDF & profile pic-----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFByte = pdf_file.read()

profile_pic = Image.open(profile_pic)


#-----Hero Section-----

col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "Download CV",
        data = PDFByte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )

st.write("email:", EMAIL)


#-----Social Links-----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#-----Experience & Qualifications

st.write("#")
st.subheader('Experience & Qualifications')
st.write(
    """
- ✔️ Taking a data first approach to campaign optimisation, through constant interation rather than perfection.
- ✔️ Strong hands on experience and knowledge in Python, Javascript and SQL.
- ✔️ Exceptional understanding of applied statistics, particulalry Bayesian and Frequentist statistics garnered through Mathematics degree (first-class honours).
- ✔️ Excellent team-player with almost 7 years experience working in customer/client facing roles. 
    """
)

#-----Skills-----

st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, JavaScript, R, API's, Scripting
- 📊 Data Visulization: Looker, MS Excel, GSheets, Plotly
- 📚 Statistics & Modelling: Multiple linear regression, ANOVA, Model Selection, Experimental Design, Hypothesis Testing
- 🗄️ Databases: Big Query, SQL
"""
)

#-----Work History-----
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Technical Account Executive | Kinase**")
st.write("02/2022 - Present")
st.write(
    """
- ► Optimise search and shopping campaigns through data-driven decisions combined with a deep understanding of the automated bidding systems, attribution models and key metrics. 
- ► Develop new scripts using the Google Ads API to streamline workflows for varying clients; consisting of generating analytical reports, building specific ad assets, and real-time tracking of performance.
- ► Conduct end-to-end AB tests to continually refine our campaigns based on statistically significant data. Previous tests include comparing attribution models using profit margin as a performance measure, as well as testing multiple versions of promotional copy to improve conversion rates. 
- ► Provide proactive troubleshooting support to resolve subtle and complex issues with active scripts, acting as the automation lead for multiple client teams. 
- ► Provide ad-hoc analysis of campaign performance to clients during weekly calls, interpreting recent performance trends and drawing insightful conclusions from data to inform business decisions.
- ► Build custom dashboards for clients and internal stakeholders, using SQL to extract, transform, and analyse data from multiple sources, providing a comprehensive and relevant view of performance.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Technology Consultant | Deloitte**")
st.write("10/2020 - 11/2020")
st.write(
    """
- ► Designed an implementation plan regarding an innovative online banking platform. The main considerations consisted of technology, business and cost estimates. 
- ► Generated a detailed overview of cloud computing for the purpose of advising a client on benefits, risks, and considerations for which applications would be suitable for cloud transition. 
- ► Drafted a project strategy plan for a new financial accounting system. Guided client through the market scan, evaluation and selection process. 
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
