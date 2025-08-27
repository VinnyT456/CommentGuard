import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Youtube Spam Detection App",
    page_icon="👋",
    layout="centered",  # Center content on the page
    initial_sidebar_state="expanded",
)

st.title("Welcome to our **Youtube Spam Detection App!** 👋")

st.markdown(
    """
    This app was designed as part of our CS 250 final project to tackle the problem of **YouTube Spam Detection**.  
    Navigate through the app using the sidebar to explore the features we have built!
    """
)

st.markdown("---")

st.subheader("📚 Want to learn more?")
st.markdown(
    """
    - 🔗 **[Source code on Github](https://github.com/VinnyT456/Youtube-Spam-Detection-Software)**  
    - 📊 **[Dataset used](https://www.kaggle.com/datasets/ahsenwaheed/youtube-comments-spam-dataset/data)**
    """
)

st.markdown("---")

image = Image.open("Images/youtube_logo.png")
st.image(
    image,
    caption="Your AI-powered YouTube Spam Detection App",
    use_column_width=True,
)

st.markdown(
    """
    🛠️ Built with **[Streamlit](https://streamlit.io/)**  
    💡 Enhance your YouTube experience by identifying and managing spam!
    """,
    unsafe_allow_html=True,
)