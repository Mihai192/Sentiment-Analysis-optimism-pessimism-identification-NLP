from lexer import Lexer

def analyze_sentiment(text):
    # Split the text into tokens (words)
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
    
    # Initialize sentiment counter
	sentiment_score = 0
    
    # Iterate through the tokens and count positive and negative words
	for token in tokens:
		if token in positive_words:
			sentiment_score += 1
		elif token in negative_words:
			sentiment_score -= 1
    
    # Determine overall sentiment
	if sentiment_score > 0:
		return 'Optimistic'
	elif sentiment_score < 0:
		return 'Pessimistic'
	else:
		return 'Neutral'