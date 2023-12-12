import streamlit as st



def trivia_app():
    questions = [
        {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Rome"],
        "correct_idx": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Venus", "Mercury"],
        "correct_idx": 0
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Michelangelo", "Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"],
        "correct_idx": 1
    }
    ]

    st.title('Lunar Legion')
    subtopic = {
        "Languages":["JavaScript", "Python", "C++", "Java"],
        "Frontend Development":["HTML", "CSS", "React.js", "Angular","Vue.js","Next.js"],
        "Backend Development": ["Express.js", "Django","Ruby on Rails", "PHP", "Spring boot"],
        "Databases": ["SQL", "MySQL", "PostgreSQL","MongoDB", "Redis"],
        "Cloud Computing": ["AWS", "Azure"]
    }
    topic_selectbox= st.sidebar.selectbox(
        "What types of questions would you like?", 
        list(subtopic.keys())
    )
    if topic_selectbox: 
        subtopic_selectbox = st.sidebar.selectbox(
            f"Select a {topic_selectbox} subtopic",
            subtopic[topic_selectbox]
        )

        if subtopic_selectbox:
            st.subheader(f"Selected Topic: {topic_selectbox} -> {subtopic_selectbox}")
    
    questions_number= st.sidebar.number_input(
        f"How many questions you want to generate",
        min_value=5, max_value=25, value = 5
    )


    difficulties = st.sidebar.selectbox(
        "Choose difficulty level",
        ("Easy", "Medium", "Hard")
    )

    
    with st.sidebar:
        add_radio = st.radio(
            "Timer", 
            ("Yes", "No")
        )
    
    
    correct_answers = 0

    for idx, question_data in enumerate(questions, start=1):
        st.header(f"Question {idx}: {question_data['question']}")
        selected_option = st.radio("Choose an answer", question_data['options'])
        
        if question_data['options'].index(selected_option) == question_data['correct_idx']:
            st.write("Correct!")
            correct_answers += 1
        else:
            st.write(f"Sorry, the correct answer is: {question_data['options'][question_data['correct_idx']]}")
    percentage_correct = (correct_answers/len(questions))*100
    progress_value= percentage_correct/100
    progress_placeholder = st.empty()
    progress_placeholder.progress(progress_value)

    st.write(f"You got {correct_answers} out of {len(questions)}, {progress_value*100}% correct!")

if __name__ == '__main__':
    trivia_app()