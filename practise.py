import streamlit as st

def show():
    st.title('Question Page')
    # Add content for the contact page here
    questions = [
        {
        "question": "Which of the following is a correct way to declare a variable in JavaScript?",
        "options": ["var x = 10;", "variable x = 10;", "x = 10;", "int x = 10;"],
        "correct_idx": 0
    }
    ]
   
    
    subtopic = {
        "Programming Languages":["JavaScript", "Python", "C++", "Java"],
        "Frontend Development":["HTML", "CSS", "React.js", "Angular","Vue.js","Next.js"],
        "Backend Development": ["Express.js", "Django","Ruby on Rails", "PHP", "Spring boot"],
        "Databases": ["SQL", "MySQL", "PostgreSQL","MongoDB", "Redis"],
        "Cloud Computing": ["AWS", "Azure"]
    }

    topic_selectbox= st.sidebar.selectbox(
        "What types of question would you like?", 
        list(subtopic.keys())
    )
    if topic_selectbox: 
        subtopic_selectbox = st.sidebar.selectbox(
            f"Select a {topic_selectbox} subtopic",
            subtopic[topic_selectbox]
        )

        if subtopic_selectbox:
            st.subheader(f"Selected Topic: {topic_selectbox} -> {subtopic_selectbox}")



    difficulties = st.sidebar.selectbox(
        "Choose difficulty level",
        ("Easy", "Medium", "Hard")
    )

    types = st.sidebar.selectbox(
        "Choose questions type",
        ("Multiple Choice", "Truth/False", "Coding")
    )
    quizes = st.sidebar.button("Create Question")

    



    
    for idx, question_data in enumerate(questions, start=1):
        st.header(f"{question_data['question']}")
        selected_option = st.radio("Choose an answer", question_data['options'])
        submit_button = st.button("Submit")
        if question_data['options'].index(selected_option)== question_data['correct_idx'] and submit_button:
            st.write('Correct!')
            
        elif question_data['options'].index(selected_option) != question_data["correct_idx"] and submit_button:
            st.write(f"Sorry, the correct answer is: {question_data['options'][question_data['correct_idx']]}")
        else:
            st.write('Not submit yet')
    

