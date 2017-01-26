import os # allows us to use CLI
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from KaggleWord2VecUtility import KaggleWord2VecUtility
import panda as pd
import numppy as np

#Figure out imports --obj--

if __name__ == '__main__':
	train.pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'labeledTrainData.tsv'), header=0, delimiter="\t", quoting=3)
	test = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'testData.tsv'), header=0, delimiter="\t", quoting=3)
	print 'the First Review is:' # To print the first review
	print train["review"][0]
	raw_input("Press Enter to Continue") # ask for step 
	clean_train_review = [] #inint empty lsit to hold reviews
	print 'time to clean and parse this shit'
	for i in xrange(0, len(train["review"])):
		clean_train_review.append("".join(KaggleWord2VecUtility.review_to_wordlist(train["review"][i], True)))

		#Create a bag of words from the training set
		vectorizer = CountVectorizer(analyzer = "word", tokenizer=None, preprocessor= None, stop_words = None, max_features = 5000)
		train_data_features = vectorizer.fit_transform(clean_train_review)

		train_data_features= train_data_features.toarray()

		print "Training the Rando Forest thingy still dont know what it is ffs"
		forest = forest.fit(train_data_features, train["sentiment"])
		clean_test_review = [] # empty list to store clean review append shit
		for i in xrange(0,len(test["review"])):
			clean_test_review.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(test["review"][i], True)))

			test_data_features = vector.transform(clean_test_review)
			test_data_features = test_data_features.toarray()

			print "Here comes the predictions"
			result = forest.predict(test_data_features)
			output = pd.DataFrame(data={"id":test["id"], "sentiment":result})
			#usidng panda to write output to file
			output.to_csv(os.path.join(os.path.dirname(__file__), 'data', 'Bag_of_Words_model.csv'), index=False, quoting=3)
			print "done hai scene scv file check karo"