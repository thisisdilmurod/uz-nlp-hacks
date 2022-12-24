# Importing all the necessary libraries
import streamlit as st
import replicate
import time
from googletrans import Translator

# Create text-to-image generation API model
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")
translator = Translator()


# Visualize the design of the web application
def main():
    st.title("Cube")
    st.header("Sarlavha")
    with st.sidebar:
        page_image = """
        <style>
        [data-testid="stImage"]{
        width: 200px;
        height: 200px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        }
        </style>
        """
        st.markdown(page_image, unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/2641/2641264.png")
        st.header("Abdusamadov Dilmurod | 18")
        with st.expander("Biografiya"):
            st.write("""
            My name is Dilmurod, from Tashkent, Uzbekistan. I've been working in interior designing field for a 
            decade already with an experience of western and eastern. My clients are always grateful for
            choosing me. Of this Cube model, I can now make my work easier 
            and your desires nearer than I could've done ever before.""")
    menu = ["Sarlavha", "Takliflar", "Dizaynlar"]
    choice = st.sidebar.selectbox("Menyu", menu)
    if choice == "Sarlavha":
        st.write("Explore all-new personalization features, privacy and security enhancements, and more ways to "
                 "communicate seamlessly. Turn an eligible device into credit towards a new one, or recycle it for "
                 "free. Apple Trade In is good for you and the planet.")

        st.write("How does stable diffusion work?")
        st.write("Diffusion models are a new class of state-of-the-art generative models that generate diverse "
                 "high-resolution images. They have attracted a lot of attention after OpenAI, Nvidia and "
                 "Google managed to train models. Example architectures that are based on diffusion models "
                 "are GLIDE, DALLE-2, Imagen, and the full open-source stable diffusion.")
        st.latex(r'''q(x_{t}|x_{t-1})=N(x_{t};\mu_{t}=\sqrt{1-\beta_{t}}x_{t-1},\sum_{t}^{}=\beta_{t}I)''')
        st.write("If we take a step back, we can notice that the combination of qq and pp is very similar to a "
                 "variational autoencoder (VAE). Thus, we can train it by optimizing the negative log-likelihood of "
                 "the training data.")
        st.write("Diffusion models are a new class of state-of-the-art generative models that generate diverse "
                 "high-resolution images. They have attracted a lot of attention after OpenAI, Nvidia and "
                 "Google managed to train models. Example architectures that are based on diffusion models "
                 "are GLIDE, DALLE-2, Imagen, and the full open-source stable diffusion.")

    # Add image generating feature
    if choice == "Takliflar":
        st.header("Takliflar")
        user_suggestion = st.text_input("Takliflaringizni yozing", key="suggestions")
        translated_suggestion = translator.translate(user_suggestion, dest='en')
        time.sleep(10)
        st.button("Download")
        output = version.predict(prompt=translated_suggestion.text)
        st.image(output)

    if choice == "Dizaynlar":
        st.header("Dizaynlar")
        st.write("Below are some awesome templates, and community apps curated from our forums or Twitter. Try them "
                 "out, browse their source code, share with the world, and get inspired for your own projects!")
        st.write("")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("https://replicate.delivery/pbxt/ZgRvaC9Ol3a3AJwkP8fUKvqHaYRSrqXKEli3WfK9DR9n6INQA/out-0.png")
            st.image("https://replicate.delivery/pbxt/0KnK657qsGqBO5YxnjDlub6dAGOye3EDfGSc8IayeLyDIAagA/out-0.png")
        with col2:
            st.image("https://replicate.delivery/pbxt/BRFhAsoz97Z6ANR9Q3s072iRaM3u8MPUc65u8QGgfOJI1hGIA/out-0.png")
            st.image("https://replicate.delivery/pbxt/ZgRvaC9Ol3a3AJwkP8fUKvqHaYRSrqXKEli3WfK9DR9n6INQA/out-0.png")

        with col3:
            st.image("https://replicate.delivery/pbxt/UbTGWrjuc9bfTy67UBlz0v4dvVPV90t3ZF8J8mfggJ6dDANQA/out-0.png")
            st.image("https://replicate.delivery/pbxt/G956h9Wup2KZAtMSBgyzdI5fpeK1QxgJ6a4cp6AbBeWelfnBC/out-0.png")
if __name__ == '__main__':
    main()
