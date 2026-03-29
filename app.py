ooooo
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
data = pd.read_csv("faq.csv")

questions = data['Question']
answers = data['Answer']

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def chatbot(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()
    return answers[index]

# Run chatbot
print("College Helpdesk Chatbot (type 'exit' to stop)")
while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    print("Bot:", chatbot(user))
