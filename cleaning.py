import praw
import prawcore
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from urllib.parse import urlparse
import pandas as pd
import urllib.request
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.linear_model import SGDClassifier
import warnings
warnings.filterwarnings("ignore")


flairs=['[R]eddiquette', 'Non-Political', 'AskIndia' ,'Sports', 'Policy/Economy','Photography' ,'Politics' ,'Science/Technology' ,'Business/Finance','Scheduled' ,'Demonetization' ,'Food' ]
#Reading the collected data
posts= pd.read_csv('data_cont.csv')


posts.tag = posts.tag.replace({None: "null"})
posts.netloc = posts.netloc.replace({None: "null"})
posts.path = posts.path.replace({None: "null"})
posts.comments = posts.comments.replace({None: "null"})
posts['title']=posts['title'].str.lower()
posts['comments']=posts['comments'].str.lower()
posts['netloc']=posts['netloc'].str.lower()
posts['path']=posts['path'].str.lower()

#Cleaning the data
def cleaning(df,posts,no):
	count=0
	

	for i in df:
		tokens = [t for t in i.split()]
		clean_tokens = tokens[:]
		sr = stopwords.words('english')
		for token in tokens:
			if token in stopwords.words('english'):
				clean_tokens.remove(token)

		posts.iloc[count,no]=" ".join(clean_tokens)
		count+=1
	return posts

def String(value):
    return str(value)

posts['title']=cleaning(posts['title'],posts,1)['title']
posts['comments']=cleaning(posts['comments'],posts,6)['comments']
posts['netloc']=cleaning(posts['netloc'],posts,3)['netloc']
posts['path']=cleaning(posts['path'],posts,4)['path']

posts['title'] = posts['title'].apply(String)
posts['netloc'] =posts['netloc'].apply(String)
posts['path'] = posts['path'].apply(String)
posts['comments'] = posts['comments'].apply(String)

extras=posts["title"]+ posts['comments'] + posts["netloc"] + posts["path"]
posts['extras'] =extras
df=posts.to_csv('Cleaned_data/data_cont.csv')

posts=pd.read_csv('Cleaned_data/data_cont.csv')

#SVM_MODEL function code from https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568
def SVM_MODEL(X_train, X_test, y_train, y_test):

	from sklearn.linear_model import SGDClassifier

	sgd = Pipeline([('vect', CountVectorizer()),
	('tfidf', TfidfTransformer()),
	('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
	])
	sgd.fit(X_train, y_train)

	from sklearn.externals import joblib
	joblib.dump(sgd,'model_joblib')
	mj=joblib.load('model_joblib')
	y_pred = mj.predict(X_test)

	
	
	print('accuracy %s' % accuracy_score(y_pred, y_test))
	print(classification_report(y_test, y_pred,target_names=flairs))

	
#Splitting the data into trained and test data
def SPLIT_DATA(X,y):

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)
	SVM_MODEL(X_train, X_test, y_train, y_test)

SPLIT_DATA(extras,posts.tag)




