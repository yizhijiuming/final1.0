import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Huiying_Mai_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Huiying Mai")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** huiying.mai@outlook.com
    - **Phone:** +86 18022089159, +852 59577418
    """)

    st.header("Internship Experience")
    st.markdown("""
    **Intern of External Communication, Pfizer China**
    - *April 2024 – July 2024*
    - Establish a good relationship with external communication channels and maintain multi-channel relationship with media, exhibitions and experts by organizing various workshops.
    - Improve and deploy the company's self media matrix, becoming the only company in the industry with comprehensive self media deployment. Independently complete video editing work, including the People's Daily Cancer Theme Conference video, to improve content quality and audience appeal. Achieved a video content fan conversion rate of more than 50%, significantly increasing brand influence.
    - Support the planning and design of Pfizer's promotional videos, graphics, booths, and accessories for the CIIE, independently innovate proposals and preliminarily design the Pfizer brand “guandan” poker.

    **Marketing Intern of Nescafe, Nestle China**
    - *June 2023 – December 2023*
    - Participate in new product selection and winter new product promotional photography, assist in the key visual design and formulate the product launch programme and promotional strategy.
    - Participate in the preparation of the "Nescafe Freshly Ground Coffee" brand brochure structure, and be responsible for contacting agencies for the design and content, also arranging the long articles on the social media based on the extension of the content. Lead the design and extension application of brand accessories, complete the communication and production work of brand accessories. Assist sales department to develop online and offline promotion activities.
    - Responsible for key account image building and relationship maintenance, completing the selection of customers in each district, customising different marketing plans for different key account with different image support and promotion activity support, and producing and distributing specific material support into shops.
    - Develop new business models for channel customers. Analyze competitor independently, and assist the company to develop more competitive sales strategy and pricing strategy.
   
    **Marketing Intern of long-form audio, Tencent Music Entertainment Group**
    - *May 2022 – June 2022*
    - Participated in the new A-level audio drama product launch. Managed communication materials including copywriting and key visual of audio drama and post them on social media, creating a popular case that generates 4 times the usual user interaction.
    - Operated official accounts on various media platforms, and handled negative public opinion related to IP in crisis public relation. Maintained the relationship between users and partners, and activated interaction of users.
    """)

    st.header("Education")
    st.markdown("""
    **Bachelor of Management in Marketing (Big Data Marketing)**
    - Central University of Finance and Economics (CUFE)
    - *Graduated: June 2024*
    - GPA: 87.5/100

    **Master of Science in Marketing**
    - The Chinese University of Hong Kong (CUHK)
    - *Graduated: Octomber 2025*
    - GPA: 3.58/4.0
    """)

    st.header("Publicatioins")
    st.markdown("""
    Virtual Marketing of the Entertainment Industry in the Information Age: Building and Promotion of IPs—A Case Study of Luo Tianyi, ICAMM 2023 Paper ID: ICAMM-2583
    """)

    st.header("Research and Projects")
    st.markdown("""
    - 3rd Prize Winner of the 17th "Challenge Cup" National College Student Entrepreneurship Competition, Beijing Division (For Independent Retail Stations in Vietnam Cross-border E-commerce)
    - 3rd Prize Winner of the 12th "Zhengda Cup" National College Student Market Survey and Analysis Competition, Beijing Division (For Consumer Characteristics and Preferences Analysis of VR Offline Experience Stores in Beijing)
    """)

    st.header("Languages")
    st.markdown("""
    - **Cantonese:** Native
    - **Chinese:** Native
    - **English:** Fluent (IELTS 7.0)
    """)


    st.markdown("---") 