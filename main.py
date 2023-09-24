import numpy as np
import pandas as pd
import streamlit as st
from scraper import main
from app import sentiment_score
import re

st.title("Youtube Video Comments Sentiment Analysis")

st.subheader('Insert Youtube video URL')
input_url = st.text_area("enter url")

def extract_video_id(input_url):
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, input_url)
    if match:
        return match.group(1)
    return None

input_id = extract_video_id(input_url)

if st.button('Analysis'):
    comments = main(input_id)
    df = pd.DataFrame(np.array(comments), columns=['Comments'])
    df['sentiment'] = df['Comments'].apply(lambda x: sentiment_score(x[:512]))
    st.table(df)
