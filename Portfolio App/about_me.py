import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.write('''
# Abhas Jaiswal
##### *Aspiring Data Scientist* 
''')

image = Image.open('Abhas_DP.jpeg')
st.image(image, width=300)

def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
    
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/abhasjaiswal" target="_blank">Abhas Jaiswal</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#positions-of-responsibility">Positions of Responsibility</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
st.markdown('''
## Education
''')
txt('**B.tech Computer Science & Engineering** (Data Science), *School of Computer Science, UPES*, Dehradun,Uttarakhand',
'2023-27')

st.markdown('''
''')
txt('**Pre University(10+2)**, *Sri Chatianya PU College*, Bengaluru,Karnataka',
'2020-22')

######################


st.markdown('''
## Skills
''')
txt3('Programming', '`C`, `Python`')
txt3('Data Analysis and Visualization', '`Pandas`, `NumPy`, `Seaborn`, `Matplotlib`,`Data Modelling`')
txt3('Version Control', '`Git & GitHub`')
txt3('Operating System', '`Linux`',)
txt3('Web Scraping', '`Beautiful Soup & Requests`')

#####################
st.markdown('''
## Work Experience
''')

txt('**Accenture North America Data Analytics and Visualization Job Simulation on Forage**', 'Feb’24')
st.markdown('''
- Completed a simulation focused on advising a hypothetical social media client as a Data Analyst at Accenture.
- Cleaned, modeled, and analyzed 7 datasets to uncover insights into content trends to inform strategic decisions.
- Prepared a PowerPoint deck and video presentation to communicate key insights for the client and internal stakeholders.
''')

#####################

st.markdown('''
## Positions of Responsibility
''')

txt('**Computer Society of India-UPES | Technical Core Committee Member**', 'Oct’23-Present')
st.markdown('''
- Actively contributing to technical initiatives, collaborating with peers on projects, and organizing events to promote technological awareness within the campus community.
''')

txt('**UPES (University of Petroleum and Energy Studies) | Change Maker**', 'Dec’23 – Present')
st.markdown('''
- Selected as Change Maker by UPES Career Service Dept.
- Led a team to improve communication between the department and students.
- Coordinated student engagement and managed operational tasks such as data analysis and record-keeping.
- Developed strategies to enhance student experience.
- Assisted in pre, during, and post-internship activities.
- Gained leadership, management skills, and hands-on experience in placement processes.
- Mentored by officials.
''')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/abhasjaiswal')
txt2('GitHub', 'https://github.com/Abhasjaiswal')