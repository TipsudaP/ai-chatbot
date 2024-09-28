import streamlit as st
import google.generativeai as genai

st.title("🍜 Ichiban chatbot app")
st.subheader("Conversation")

# user_input = st.text_input("You:", placeholder="Type your message here...")
# st.write("User Input:", user_input)

# # Initialize session state for storing chat history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = [] # Initialize with an empty list

# # Display the user input
# if user_input := st.text_input("You:", placeholder="Type your message here..."):
#     st.session_state.chat_history.append(user_input)

# # Display all messages using st.write
# for message in st.session_state.chat_history:
#     st.write(message)

# # Initialize session state for storing chat history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = [] # Initialize with an empty list

# # Display all chat messages
# for message in st.session_state.chat_history:
#     with st.chat_message("user"):
#         st.markdown(message)

# # Capture user input and append to chat history
# if prompt := st.chat_input("Type your message here ..."):
#     st.session_state.chat_history.append(prompt)
#     st.chat_message("user").markdown(prompt)

# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type API key...", type="password")

# Initialize the Gemini Model
if gemini_api_key:
    try:
        # Configure Gemini with the provided API Key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        st.success("Gemini API Key successfully configured.")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")

# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [] # Initialize with an empty list

# Display previous chat history using st.chat_message (if available)
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)
    
# Capture user input and generate bot response
if user_input := st.chat_input("Type your message here..."):
    # Store and display user message
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").markdown(user_input)

    # Use Gemini AI to generate a bot response
    if model:
        try:
            personality = "your name is ichimen. You are a Ramen expert that can suggest famous and delicious remen restaurant for anyone who ask. You are a liitle bit sarcastic but cute"
            prompt = f"personality = '{personality}', user input: '{user_input}'"
            response = model.generate_content(prompt)
            bot_response = response.text
        
    # Store and display the bot response
            st.session_state.chat_history.append(("assistant", bot_response))
            st.chat_message("assistant").markdown(bot_response)
        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")