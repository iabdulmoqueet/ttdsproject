import streamlit as st

st.set_page_config("Abdul Moqueet",layout= "wide")

st.sidebar.title("Abdul Moqueet Portfolio")

tab = st.tabs(["Home", "Projects", "Skills", "About Me", "Contact"])

with tab[0]:
    
    col1,temp,col2,temp2 = st.columns([3,0.2,5,0.8])
    
    with col1:
        st.image("profile.jpeg",width= 450)

    with col2:
        st.header("Abdul Moqueet")
        st.markdown("""##### Data Scientist | Data Analyst""")
        st.markdown(
            """
            I am a dedicated and ambitious 5th-semester Data Science student with a solid foundation in data analysis, programming, and quality assurance. My passion lies in ensuring the reliability and efficiency of software systems through rigorous QA processes and testing methodologies. Alongside my academic journey, I have gained practical experience in marketing, social media management, and event promotion, showcasing my ability to manage projects and engage diverse audiences. Eager to contribute and grow, I seek opportunities to apply my skills in data-driven solutions, software testing, and quality assurance while gaining hands-on industry experience.
            """
        )

# Projects Tab
with tab[1]:
    st.header("Projects")
    with st.expander(label="Data Analysis and Visualization Dashboard"):
        st.subheader("1. Data Analysis and Visualization Dashboard")
        st.markdown("""
                    **Description:** Developed an interactive dashboard to analyze sales data and visualize trends, allowing users to filter data by categories and time frames for actionable insights.

                    **Technologies Used:** Python, Pandas, Matplotlib, Streamlit.
                    """)
    
    with st.expander(label= "Student Management System"):
        st.subheader("2. Student Management System")
        st.markdown("""
                    **Description:** Designed and implemented a system to manage student records, including enrollment, grades, and attendance, providing an efficient and user-friendly interface for administrators.

                    **Technologies Used:** MySQL, Python, Tkinter
                    """)
        
    with st.expander(label= "Social Media Engagement Tracker"):
        st.subheader("3. Social Media Engagement Tracker")
        st.markdown("""
                    **Description:** Built a tool to monitor and analyze engagement metrics across multiple social media platforms, helping improve content strategies and audience interaction.

                    **Technologies Used:** Python, Beautiful Soup, MongoDB
                    """)



#Skills
with tab[2]:
    st.header("Skills")
    cola1,colmid, cola2 = st.columns([2,1,2])
    with cola1:
        st.subheader("My Skills:")
        st.markdown("""
                    * Python, C++, C

                    * Data Analysis & Visualization (Pandas, NumPy, Matplotlib)

                    * Databases (MySQL, MongoDB)

                    * QA Processes & Testing Methodologies

                    * Microsoft Office Suite

                    * Streamlit, KNIME

                    """)
        
    with cola2:
        st.subheader("Courses:")
        st.markdown("""
                    * CS50 (In Progress)

                    * QA for Beginners (Completed)

                    * Data Analytics Python (freecodecamp)
                    """)
        


#About Me
with tab[3]:
    st.header("About Me")


    st.subheader("Professional Summary")
    st.write(
        """
        I am a dedicated and ambitious 5th-semester Data Science student with a solid foundation in data analysis,
        programming, and quality assurance. My passion lies in ensuring the reliability and efficiency of software
        systems through rigorous QA processes and testing methodologies. Alongside my academic journey, I have gained
        practical experience in marketing, social media management, and event promotion, showcasing my ability to manage
        projects and engage diverse audiences. Eager to contribute and grow, I seek opportunities to apply my skills in
        data-driven solutions, software testing, and quality assurance while gaining hands-on industry experience.
        #####
        """
    )

    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Education")
        st.markdown(
            """
            ####  University of Central Punjab, Lahore

            _BS Hons. in Data Science | 2022 - 2026_ 

                
            ####  Punjab College Okara

            _F.Sc Pre Engineering | 2019 - 2021_ 


            ####  MC High School Okara


            _Matric | 2017 - 2019_ 

                    
            """
        )

    with col2:
        st.subheader("Languages")
        st.markdown(
            """
            * English

            * Urdu
                
            * Punjabi

            """
        )

with tab[4]:

    form = st.form("Contact Me")
    with form:

            name = st.text_input("Your Name")

            email = st.text_input("Your Email")

            message = st.text_area("Your Message" ,height= 300)

            submit_button = st.form_submit_button("Send Message")

    col1,col2 = st.columns([0.222,5])

    with col1:
        st.image("insta.png", width=50)

    with col2:
        st.markdown(
            """
            <div style="display: flex; align-items: center; height: 50px;">
                <a href="https://www.instagram.com/iabdulmoqueet" target="_blank" 
                   style="text-decoration: none; color: #1DA1F2; font-size: 14px;">
                   Visit my Instagram</a>
            </div>
            """,
            unsafe_allow_html=True,
        )


