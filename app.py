import streamlit as st



def trivia_app():
  
    st.markdown(
        """
        <style>
        .title {
            color: #FF6347;
            text-align: center;
        }
    
        body {
            background-image: url('https://example.com/your-image.jpg');
            background-size: cover; /* Adjust to fit your preference */
        }
       
        </style>
        """,
        unsafe_allow_html=True
    )
    questions = [
        {
        "question": "Which of the following is a correct way to declare a variable in JavaScript?",
        "options": ["var x = 10;", "variable x = 10;", "x = 10;", "int x = 10;"],
        "correct_idx": 0
    },
    {
        "question": "What does the 'DOM' stand for in JavaScript?",
        "options": ["Document Object Model", "Data Object Model", "Dynamic Object Management", "Document Objective Method"],
        "correct_idx": 0
    },
    {
        "question": "What will be the output of the following code snippet: console.log(1 + '2' + '2');",
        "options": ["122", "5", "14", "322"],
        "correct_idx": 3
    },
    {
        "question": "Which function is used to add an element to the end of an array in JavaScript?",
        "options": ["append()", "push()", "addToEnd()", "insertLast()"],
        "correct_idx": 1
    },
    {
        "question": "What is the result of the expression: '3' + 2 + 1 in JavaScript?",
        "options": ["6", "321", "32", "5"],
        "correct_idx": 1
    }
    ]
   

    st.title('Lunar Legion')
    subtopic = {
        "Programming Languages":["JavaScript", "Python", "C++", "Java"],
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

    types = st.sidebar.selectbox(
        "Choose questions type",
        ("Multiple Choice", "Truth/False", "Coding")
    )
    quizes = st.sidebar.button("Create Quiz")

    

    
    
    correct_answers = 0

    

    submit_button = st.button("Submit")
    for idx, question_data in enumerate(questions, start=1):
        st.header(f"Question {idx}: {question_data['question']}")
        selected_option = st.radio("Choose an answer", question_data['options'])

        if question_data['options'].index(selected_option)== question_data['correct_idx'] and submit_button:
            st.write('Correct!')
            correct_answers += 1
        elif question_data['options'].index(selected_option) != question_data["correct_idx"] and submit_button:
            st.write(f"Sorry, the correct answer is: {question_data['options'][question_data['correct_idx']]}")
        else:
            st.write('Not submit yet')
    
    
    percentage_correct = (correct_answers/len(questions))*100
    progress_value= percentage_correct/100
    progress_placeholder = st.empty()
    progress_placeholder.progress(progress_value)

    st.write(f"You got {correct_answers} out of {len(questions)}, {progress_value*100}% correct!")
        
        
    

if __name__ == '__main__':
    trivia_app()