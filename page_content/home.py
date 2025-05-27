import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Huiying Mai</h4>
        <p>Recent Master's Graduate in Marketing<br>
        The Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="huiying.mai@outlook.com">huiying.mai@outlook.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "mai.JPG")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I have explored various industries such as entertainment, FMCG, Medicine, and the Internet. I have interned at Tencent Music Entertainment, Nestlé, and Pfizer. 
        I have extensive experience in both planning and execution. Moreover, I have a keen sense of current trendy trends. I have conducted academic research in the fields of virtual idols and female-oriented games a long time ago and published papers.
        """
    )

    st.markdown(
        """
        ### Skills
        - Languages: English (IELTS 7.0), Chinese (Native), Cantonese(Native)
        - Programming Languages: Python, R
        - Communication: Proficient in Microsoft Office, PS, PR, Adobe Lightroom (LR), Adobe After Effects (AE)
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 