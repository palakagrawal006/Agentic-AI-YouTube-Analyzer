import streamlit as st
from youtubeAnalizer import build_youtube_agent


# configuration of page
st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered" ,
)

st.title("🎥 AI Youtube Video Analyzer")

# function - hrr bar scratch se agent create na  ho 
# cache krne - fast access, temp storage= most freq accessed -- ex - ml = model 
@st.cache_resource  #decorator
def get_agent():
    return build_youtube_agent() 

agent = get_agent() 


# input box
video_url = st.text_input("Enter Youtube Video Link") #str
button = st.button("Analyze Video") #true/false 

# analyze when - video url - valid and button-  true
if video_url and button : 
    with st.spinner("Analyzing video..."): #while analyzing - wait
        response  = agent.run(
            f"Analyze this video: {video_url}"
        )
    
    # print(response)
    st.markdown("Analysis Report of Video")
    st.markdown(response.content)

 
