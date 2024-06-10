from main import ChatBot
import streamlit as st

bot = ChatBot()
    
st.set_page_config(page_title="Klose", page_icon=":sparkles:", layout="wide")
with st.sidebar:
    st.markdown('<span style="font-size:40px;"> Klose.</span>', unsafe_allow_html=True)
    st.header('Your personal chatbot to manage time.')

# Function for generating LLM response
def generate_response(input):
    result = bot.rag_chain.invoke(input)
    return result

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome, I'm Klose. How can I help you with time management and productivity?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Getting your answer .."):
            response = generate_response(input)
            index = response.find("Answer:")
            answer = response[(index + 7):]
            answer = answer.strip()
            st.write(answer) 
    message = {"role": "assistant", "content": answer}
    st.session_state.messages.append(message)