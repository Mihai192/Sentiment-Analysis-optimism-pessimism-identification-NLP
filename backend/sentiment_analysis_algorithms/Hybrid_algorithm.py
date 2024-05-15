from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import os
from lexer import Lexer

def analyze_sentiment(text):
	
	def lexicon_approuch(text):
		positive_words = {
			'good', 'great', 'excellent', 'positive', 'awesome', 'fantastic', 'amazing', 'wonderful', 'brilliant', 'terrific',
			'superb', 'outstanding', 'remarkable', 'phenomenal', 'splendid', 'magnificent', 'stellar', 'exceptional', 'praiseworthy',
			'joyful', 'delightful', 'glorious', 'sensational', 'uplifting', 'thrilling', 'encouraging', 'inspiring', 'breathtaking',
			'beautiful', 'lovely', 'charming', 'attractive', 'captivating', 'appealing', 'enchanting', 'exhilarating', 'heartwarming',
			'positive', 'optimistic', 'fortunate', 'cheerful', 'blissful', 'ecstatic', 'radiant', 'vibrant', 'exuberant', 'euphoric',
			'content', 'grateful', 'thankful', 'satisfied', 'blessed', 'joyous', 'gleeful', 'elated', 'jubilant', 'festive',
			'excited', 'enthusiastic', 'passionate', 'ardent', 'fervent', 'zealous', 'dynamic', 'energetic', 'vital', 'buoyant',
			'lively', 'spirited', 'entertaining', 'upbeat', 'optimistic', 'hopeful', 'confident', 'reassuring', 'comforting',
			'affirmative', 'constructive', 'productive', 'progressive', 'beneficial', 'valuable', 'favorable', 'advantageous', 'profitable',
			'excellent', 'superior', 'first-rate', 'top-notch', 'premium', 'quality', 'classy', 'sophisticated', 'elegant', 'refined',
			'graceful', 'polished', 'cultivated', 'stylish', 'trendy', 'chic', 'modern', 'cutting-edge', 'innovative', 'dynamic'
		}
		negative_words = {
			'bad', 'terrible', 'poor', 'negative', 'awful', 'horrible', 'dreadful', 'atrocious', 'abysmal', 'disastrous',
			'appalling', 'lousy', 'miserable', 'grim', 'bleak', 'gloomy', 'dreary', 'depressing', 'sorrowful', 'melancholy',
			'unfortunate', 'tragic', 'woeful', 'wretched', 'pitiful', 'dismal', 'forlorn', 'desperate', 'deplorable', 'disheartening',
			'disappointing', 'unpleasant', 'distressing', 'unfavorable', 'disgusting', 'repulsive', 'revolting', 'vile', 'obnoxious',
			'repugnant', 'noxious', 'offensive', 'abominable', 'disgustful', 'hideous', 'unsightly', 'gross', 'repellent', 'filthy',
			'dirty', 'vulgar', 'foul', 'nauseating', 'displeasing', 'irritating', 'annoying', 'bothersome', 'frustrating', 'infuriating',
			'exasperating', 'maddening', 'aggravating', 'irksome', 'disturbing', 'troubling', 'worrying', 'concerning', 'anxious',
			'nervous', 'distressed', 'alarmed', 'panicked', 'frightened', 'scared', 'terrified', 'petrified', 'horrified', 'apprehensive',
			'tense', 'uneasy', 'worried', 'bothered', 'stressed', 'agitated', 'restless', 'tense', 'edgy', 'jittery', 'unsettled',
			'fearful', 'pessimistic', 'dejected', 'disheartened', 'discouraged', 'hopeless', 'despairing', 'melancholic', 'gloomy',
			'dismal', 'dismayed', 'dispirited', 'crestfallen', 'downhearted', 'sad', 'miserable', 'woeful', 'grief-stricken',
			'heartbroken', 'broken-hearted', 'tearful', 'weepy', 'depressed', 'unhappy', 'sorrowful', 'despondent', 'desolate',
			'lonely', 'wretched', 'forlorn', 'downcast', 'blue', 'down', 'glum', 'sullen', 'morose', 'moody', 'sulky', 'gloomy',
			'dour', 'dreary', 'cheerless', 'sombre', 'grim', 'sullen', 'somber', 'disconsolate', 'melancholy', 'lugubrious',
			'lamentable', 'pessimistic', 'bleak', 'desperate', 'gloomy', 'hopeless', 'futile', 'powerless', 'dismal', 'dejected',
			'depressed', 'despondent', 'forlorn', 'miserable', 'woeful', 'tragic', 'pitiful', 'sorry', 'unfortunate', 'disheartening',
			'dismaying', 'unpromising', 'discouraging', 'dour', 'pessimistic', 'gloomy', 'morose', 'despairing', 'heartbreaking'
    	}


		tokens = Lexer.tokenize(text)
    
		sentiment_score = 0
    
		for token in tokens:
			if token in positive_words:
				sentiment_score += 1
			elif token in negative_words:
				sentiment_score -= 1

		return sentiment_score
		
	def supervised_approuch(text):
		script_dir = os.path.dirname(os.path.abspath(__file__))

		
		file_path = os.path.join(script_dir, 'data.csv')
		dataset = pd.read_csv(file_path)

		def train_model():
			X = dataset['text']
			y = dataset['sentiment']

			
			vectorizer = TfidfVectorizer()
			X_tfidf = vectorizer.fit_transform(X)

			X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

			
			model = SVC(kernel='linear')
			model.fit(X_train, y_train)
			
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

		return sentiment
		
	lexicon_weight = 0.1
	supervised_weight = 0.9

	lexicon_score = lexicon_approuch(text)
	supervised_response = supervised_approuch(text)
    # Combine lexicon-based and supervised sentiments using weighted average
	weighted_sentiment_score = (lexicon_weight * lexicon_score) + (supervised_weight * (1 if supervised_response == 'positive' else (-1 if supervised_response == 'negative' else 0)))

    # Determine overall sentiment based on the weighted score
	if weighted_sentiment_score > 0:
		return 'Optimistic'
	elif weighted_sentiment_score < 0:
		return 'Pessimistic'
	else:
		return 'Neutral'
	
