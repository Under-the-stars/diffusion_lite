import streamlit as st
from PIL import Image, ImageEnhance
import requests
from io import BytesIO
import base64


def main_method():
    try:

        st.sidebar.markdown(" Sample prompts")
        st.sidebar.markdown(" ")
        st.sidebar.markdown("Diamond ring")
        st.sidebar.markdown(" Yellow Diamond ring")
        st.sidebar.markdown(" Small Diamond ring")
        st.sidebar.markdown('''

                <style>

                [data-testid="stMarkdownContainer"] ul{

                    padding-left:40px;

                }

                </style>

                ''', unsafe_allow_html=True)
        apptitle="Stable Diffusion model for jewellery design"
        # st.set_page_config(page_title=apptitle, page_icon="z:eyeglasses:")
        st.title("Stable Diffusion Demo")
        url = st.text_input("Enter the url")
        if len(url)>0:
            url=url+"/run"
        prompt = st.text_input("Enter textual prompt")

        if st.button("Generate Image"):
            with st.spinner(text="Analysing query"):
                data = {"prompt": prompt}
                headers={"Bypass-Tunnel-Reminder":"ABCD"}
                r = requests.post(url,headers=headers, json=data, timeout=500)
                # print(r.text)
                # st.markdown(type(r.text))
                if r.text=="404" :
                    st.markdown("Endpoint expired! restart server ")
                else:
                    im = Image.open(BytesIO(base64.b64decode(r.text)))
                    st.image(im)

    except Exception as error:
        print(error)
        st.markdown("Some error occured")


if __name__ == "__main__":
    main_method()


