import streamlit as st

def contact_page():
    st.markdown("## Contact Me")
    
    st.markdown("""
    Feel free to reach out to me through any of the following channels:
    
    ### Direct Contact
    - **Email**: [huiying.mai@outlook.com](mailto:huiying.mai@outlook.com)
    - **Phone**: +86 18022089159, +852 59577418
    """)
    
    st.markdown("### Send Me a Message")
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
            
        with col2:
            subject = st.text_input("Subject")
            
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success("Thanks for your message! I'll get back to you soon.")
            # In a real application, you would process the form data here
            # For example, send an email or store in a database
    
    st.markdown("---")
    
 
