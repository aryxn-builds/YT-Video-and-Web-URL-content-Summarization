import os
import validators
import streamlit as st
from dotenv import load_dotenv

try:
    from langchain_core.prompts import PromptTemplate
except ImportError:
    from langchain.prompts import PromptTemplate

from langchain_groq import ChatGroq
from langchain_community.document_loaders.youtube import YoutubeLoader
from langchain_community.document_loaders.url import UnstructuredURLLoader

load_dotenv()

## Streamlit APP
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

groq_api_key = os.getenv("GROQ_API") or os.getenv("GROQ_API_KEY")

generic_url = st.text_input("URL", label_visibility="collapsed")

prompt_template = """
Provide a summary of the following content in 300 words:
Content:{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

if st.button("Summarize the Content from YT or Website"):
    ## Validate all the inputs
    if not groq_api_key:
        st.error("Please configure the GROQ_API key in your .env file.")
    elif not generic_url.strip():
        st.error("Please provide a URL to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid Url. It can be a YT video url or website url")
    else:
        try:
            with st.spinner("Waiting..."):
                ## loading the website or yt video data
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=False)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
                    )
                docs = loader.load()

                if not docs or not docs[0].page_content.strip():
                    st.error("Could not extract any readable content from the provided URL.")
                    st.stop()

                ## Chain For Summarization
                llm = ChatGroq(model="openai/gpt-oss-20b", groq_api_key=groq_api_key)
                chain = prompt | llm
                text_content = "\n\n".join([doc.page_content for doc in docs])
                output_summary = chain.invoke({"text": text_content}).content

                st.success(output_summary)
        except Exception as e:
            st.exception(e)