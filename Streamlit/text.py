import streamlit as st

# h1 Tag
st.title("My First Streamlit App", anchor=False)

# h3 Tag
st.header("This is a header", divider=True)

# h4 Tag
st.subheader("This is a subheader", divider=True)

# p tag
st.write("Hello World")
st.text("This is a text element")

# markdown
st.markdown("**Bold** word")
st.markdown("*Italic* word")

st.markdown(":red[Red Alert]")

# background
st.markdown(":blue-background[this is background]")
st.markdown(":smiling_face_with_three_hearts:")