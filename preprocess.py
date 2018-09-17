import nltk.classify
#nltk.download('stopwords') -> used once to download all the stopwords
from nltk.corpus import movie_reviews
from nltk.corpus import opinion_lexicon
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download('punkt')

stop_words = stopwords.words("english")

def word_features_positive(words):
	useful_words = [word for word in words if word not in stop_words] #useful words are those words that are in the list words and are not stop words -> list of words, without stop-word
	my_list = [({word: True}, 'positive') for word in useful_words] #filters all the positive words form the word list
	return my_list

def word_features_negative(words):
	useful_words = [word for word in words if word not in stop_words] #useful words are those words that are in the list words and are not stop words -> list of words, without stop-word
	my_list = [({word: True}, 'negative') for word in useful_words] #filters all the positive words form the word list
	return my_list

def word_features(words):
	useful_words = [word for word in words if word not in stopwords.words("english")] #list of all the words that not english stop words
	pos_file = "positive.txt"
	pos_text = get_tokenized_file(pos_file) #tokenizing is getting the words individually withoutspaces. this function is from wordtokenize library
	#postext = open("positve-words.txt").read()
	#pos_text_token = nltk.word_tokenize(postext)

	#negtext = open("negative-words.txt").read()
	#neg_text_token = nltk.word_tokenize(negtext)
	neg_file = "negative.txt"
	neg_text = get_tokenized_file(neg_file)

	my_dict = dict([(word, True) for word in pos_text if word in useful_words])
	my_dict1 = dict([(word, False) for word in neg_text if word in useful_words])

	my_dict.update(my_dict1) #adds keywords frim dict1 to dict

	return my_dict

def get_tokenized_file(file):
	return word_tokenize(open(file, 'r').read()) #open the tokenized file in a read only version

def get_data(): #returns a list of pos and neg words form the words that are in the txt
	print("Collecting Positive Words..")
	#pos_text = get_tokenized_file('positve.txt')
	pos_file = "positive.txt"
	pos_text = get_tokenized_file(pos_file)
	#postext = open("positve-words.txt").read()
	#pos_text_token = nltk.word_tokenize(postext)
	pos_features = word_features_positive(pos_text)

	print("Collecting Negative Words..")
	#neg_text = get_tokenized_file('negative.txt')
	neg_file = "negative.txt"
	neg_text = get_tokenized_file(neg_file)
	#negtext = open("negative-words.txt").read()
	#neg_text_token = nltk.word_tokenize(negtext)
	neg_features = word_features_negative(neg_text)

	return pos_features + neg_features

def process(data):
	return [word.lower() for word in word_tokenize(data)]