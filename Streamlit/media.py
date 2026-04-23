import streamlit as st

st.title("Media", anchor=False)

# file upload
image = st.file_uploader("Upload your image:", type=['jpg', 'webp', 'png'], accept_multiple_files=True)

if image:
    col = st.columns(len(image))

    for i, img in enumerate(image):
        with col[i]:
            st.image(img)