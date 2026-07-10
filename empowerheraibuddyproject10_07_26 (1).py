
import streamlit as st
import google.generativeai as genai
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEYS")

api_key = os.environ.get("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
model =genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI Learning Buddy", page_icon="🎓🎓")
st.title("🎓🎓 AI Learning Buddy")
topic = st.text_input("Please enter a topic") 
option = st.selectbox(
"Choose Activity",
    ["Explain Concept",
     "Real-Life Example",
        "Generate Quiz",
       "Ask Anything"])

if option == "Explain Concept":
    level = st.selectbox(
         "Choose Difficulty",
         ["Beginner",
         "Intermediate",
         "Advanced"
        ]
    )
if st.button("Generate"):
   st.write("Button clicked")

   if topic == "":
      st.warning("⚠ Please enter a topic.")
   else:
        if option == "Explain Concept":
           prompt = f"Explain {topic} with answers grounded if you donot know then tell I don't know the answer, if you know the answer then answer according to knowledge level of user on the topic"
           if level == "Beginner":
              system_instruction= (f"Explain as a expert teacher on {topic} using simple English." "Avoid technical jargon." "Keep the response within 300 words.")
           elif level == "Intermediate":
                system_instruction = (f"Explain {topic} with moderate technical depth  act as a expert technical mentor." "Use simple examples where necessary." "generate 3 to 5 flash cards on the highlighting the topic that should cover within 3 lines covering important points on the topic""Keep the response within 600 words.")
           elif level =="Advanced":
                system_instruction = (f"Explain {topic} in detail using technical terminology act as a AI Professional.\n"
                                     "Provide an in-depth explanation.""Keep the response within 1000 words.")

 
         elif option == "Real-Life Example":
              system_instruction =f"you are an expert concepts explanation bot, your task is to explain concepts using real time examples with simple clear and grounded responses wrapping the sentences within 2 to 3 lines"
              prompt = f"Give one simple real-life application on {topic}."
 
         elif option == "Ask Anything":
              system_instruction =f"explain user provided topics clearly with grounded answers, if you don't know the answer say you don't know but always give real answers to user "
              prompt = f"Ready to answer on given {topic} with grounded answers."
         elif option == "Generate Quiz":
              system_instruction =f"""Create a quiz with 5 MCQ along witht he answers at the bottom of the each question.
                                      Rules:
                                     - Each question should have 4 options (A, B, C, D) followed by its correct answer.
                                     - provide relevant learning links up on the topic
                                     - provide questions within 2 lines.
                                     - divide the score (100) into 5 parts (20,20,20,20,20) based on the score give feedback.
                                     - This quiz is user self assessment quiz."""
              prompt =f"Create 5 MCQs on {topic}. Do NOT provide the answers."
 
         response = model.generate_content(system_instruction + "\n\n" + prompt)
         st.write(response.text)

