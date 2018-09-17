import random
import preprocess
import nltk

def get_classifier():

	data = preprocess.get_data()
	random.shuffle(data)

	split = int(0.8*len(data))

	"""this is cross-validation method where you split the examples in training and testing sets"""
	train_set = data[:split] #contains a known output, model learns on this data -> 80% of examples
	test_set = data[split:] #data set to test our model -> 20% of examples

	classifier = nltk.NaiveBayesClassifier.train(train_set) #this ia a classifier based on Bayes Theorm. to find prob of a label/word it uses Bayes theorm then it makes naive assumthat all features are indepndent

	accuracy = nltk.classify.util.accuracy(classifier, test_set) #chackes the accuracy of the trained model on the test set

	print("Generated Classifier")
	print('-'*70)
	print("Accuracy: ", accuracy)
	return classifier

