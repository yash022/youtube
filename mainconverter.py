import streamlit as st 
from pytube import YouTube
import pyshorteners

st.set_page_config("Youtube Converter" , page_icon="https://img.icons8.com/color/48/000000/youtube-play.png")

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">YT converter</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-item nav-link active" href="#">Home <span class="sr-only">(current)</span></a>
      <a class="nav-item" href="https://yash022.github.io/youtube/">Unlisted Videos</a>
    </div>
  </div>
</nav>
""", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

shorten = pyshorteners.Shortener()


st.title("Youtube Converter")
textbox = st.text_input('Enter the video link', 'Video link')

option = st.selectbox(
    'To what format would you like to convert the video',
    ('MP4', 'MP3'))

if st.button('Convert'):
    if option == 'MP4':
        video_parse = YouTube(textbox)
        video_with_audio_hd  = str(video_parse.vid_info).split("'itag': 22,")[1].split(", 'mimeType':")[0].removeprefix(" 'url': '").removesuffix("'")
        st.write("Your video is ready to be downloaded \n visit this link to download the video 👇")
        st.write(shorten.tinyurl.short(video_with_audio_hd))
    if option == 'MP3':
        video_parse = YouTube(textbox)
        video_audio = video_parse.streams.filter(only_audio=True).first().url
        st.write("Your audio is ready to be downloaded \n visit this link to download the video 👇")
        st.write(shorten.tinyurl.short(video_audio))



