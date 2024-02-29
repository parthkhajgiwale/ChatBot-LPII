from flask import Flask, render_template, request

app = Flask(__name__)

qa_pairs = {
    "how can i reduce stress?": "You can try relaxation techniques such as deep breathing, meditation, or engaging in physical activity.",
    "what are some tips for improving sleep?": "Maintain a consistent sleep schedule, avoid caffeine and screens before bed, and create a relaxing bedtime routine.",
    "i feel anxious all the time. what should i do?": "Practice mindfulness and deep breathing exercises. Consider seeking support from a therapist or counselor.",
    "how do i cope with feelings of loneliness?": "Reach out to friends and family, join social groups or clubs, and consider volunteering or adopting a pet for companionship.",
    "what should i do if i'm feeling depressed?": "Talk to someone you trust about your feelings, prioritize self-care activities, and consider seeking professional help.",
    "how can i improve my self-esteem?": "Focus on your strengths and accomplishments, practice self-compassion, and surround yourself with supportive people.",
    "what are some coping strategies for dealing with anger?": "Practice deep breathing, count to 10 before reacting, and express your feelings calmly and assertively.",
    "how can i establish boundaries in relationships?": "Communicate your needs clearly and assertively, prioritize self-care, and be willing to say 'no' when necessary.",
    "what are some ways to manage overwhelming emotions?": "Try grounding techniques such as focusing on your senses, journaling, or talking to a trusted friend or therapist.",
    "how can i improve my concentration and focus?": "Break tasks into smaller, manageable steps, eliminate distractions, and practice mindfulness and meditation.",
    "what are some signs that i should seek professional help for my mental health?": "If you experience persistent feelings of sadness, hopelessness, or anxiety that interfere with daily functioning, it's important to seek help.",
    "how can i support a friend or loved one who is struggling with mental health issues?": "Listen without judgment, offer your support and encouragement, and help them connect with professional help if needed.",
    "what are some relaxation techniques i can try?": "Deep breathing exercises, progressive muscle relaxation, guided imagery, and aromatherapy can help promote relaxation.",
    "what role does exercise play in mental health?": "Regular exercise can help reduce symptoms of depression and anxiety, improve mood, and boost self-esteem.",
    "how does nutrition impact mental health?": "Eating a balanced diet rich in fruits, vegetables, whole grains, and lean proteins can support overall mental well-being.",
    "what are some common myths about mental health?": "Some common myths include that mental illness is a sign of weakness, that it can't be treated, or that people with mental health issues are dangerous.",
    "how can i practice self-care on a daily basis?": "Make time for activities you enjoy, prioritize sleep and relaxation, set boundaries, and practice self-compassion.",
    "what are the benefits of seeking therapy or counseling?": "Therapy can provide a safe space to explore your thoughts and feelings, learn coping skills, and gain insight into yourself and your relationships.",
    "what are some strategies for managing stress at work or school?": "Prioritize tasks, set realistic goals, practice time management, and take regular breaks to recharge.",
    "how can i build resilience in the face of adversity?": "Focus on developing problem-solving skills, cultivate a positive outlook, seek social support, and practice self-care."
}

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle chatbot interactions
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.form['user_message'].lower().strip()
    chatbot_response = qa_pairs.get(user_message, "I'm sorry, I don't have an answer to that question.")
    return {'response': chatbot_response}

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
