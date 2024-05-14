from flask import Flask, request
from flask_cors import CORS, cross_origin

from sentiment_analysis_algorithms import Lexicon_algorithm
from sentiment_analysis_algorithms import Supervised_algorithm
from sentiment_analysis_algorithms import Hybrid_algorithm

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/analyze', methods=['POST'])
@cross_origin(supports_credentials=True)
def analyze():
	text = request.form['text']
	if text == None or text == '':
		return 'Text is empty'
	
	if request.form['algorithm-type'] == '0':
		return Lexicon_algorithm.analyze_sentiment(text)
	elif request.form['algorithm-type'] == '1':
		return Supervised_algorithm.analyze_sentiment(text)
	else:
		return Hybrid_algorithm.analyze_sentiment(text)
	
	

if __name__ == '__main__':
    app.run(debug=True)