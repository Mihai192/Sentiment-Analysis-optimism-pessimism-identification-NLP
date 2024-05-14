from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import os

def analyze_sentiment(text):
    
	script_dir = os.path.dirname(os.path.abspath(__file__))

	
	file_path = os.path.join(script_dir, 'data.csv')
	dataset = pd.read_csv(file_path)

	def train_model():
        
		X = dataset['text']
		y = dataset['sentiment']

        # Convert text data into TF-IDF representation
		vectorizer = TfidfVectorizer()
		X_tfidf = vectorizer.fit_transform(X)

        # Split data into training and testing sets
		X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

        # Train the model
		model = SVC(kernel='linear')
		model.fit(X_train, y_train)

        # Test the model
		y_pred = model.predict(X_test)
		accuracy = accuracy_score(y_test, y_pred)
		print("Accuracy:", accuracy)

		return vectorizer, model

    # Train the model and get vectorizer and model
	vectorizer, model = train_model()

    # Convert text into TF-IDF representation
	text_tfidf = vectorizer.transform([text])

    # Predict sentiment using the trained model
	sentiment = model.predict(text_tfidf)[0]

	if sentiment == 'positive':
		return "Optimistic"
	elif sentiment == 'negative':
		return "Pessimistic"
	else:
		return "Neutral"

