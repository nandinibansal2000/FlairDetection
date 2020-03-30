import praw
import prawcore
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from urllib.parse import urlparse
import pandas as pd

reddit = praw.Reddit(client_id='#',
                     client_secret='#',
                     password='#',
                     user_agent='#',
                     username='#')

USER_AGENT = 'Flair Script For Reddit by /u/nandini18056'
subreddit = reddit.subreddit('india')
le = preprocessing.LabelEncoder()
f= open("data_cont.json","a+")

#Storing the data in MongoDB
f.write("[")
posts = []
dict_id={}
flairs=['[R]eddiquette', 'Non-Political', 'AskIndia' ,'Sports', 'Policy/Economy','Photography' ,'Politics' ,'Science/Technology' ,'Business/Finance','Scheduled' ,'Demonetization' ,'Food' ,'Casual AMA 9¾/10']
ml_subreddit = reddit.subreddit('india')

#Collecting the data of particular flairs
for y in flairs:
	x=ml_subreddit.search(y,limit=200)
	for post in x:
		parse_object = urlparse(post.url)
		try:

			if(dict_id.get(post.id,0)==0 ):
				if(post.link_flair_text  in flairs):
					dict_id[post.id]=1
					s=""

					#Colecting only top comments
					for top_level_comment in post.comments:
						s=s+" "+str(top_level_comment.body)
					
					f.write('{"title": '+post.title+', \n  "flair": '+post.link_flair_text+',  \n  "netloc": '+parse_object.netloc+',  \n  "path": '+parse_object.path+',  \n  "upvote ratio": '+str(post.upvote_ratio)+',  \n  "comments": '+s+' "}')
					
					posts.append([post.title,post.link_flair_text , parse_object.netloc,parse_object.path,post.upvote_ratio,s])

		except:
			continue  
f.write("]")

posts = pd.DataFrame(posts,columns=['title', 'tag',  'netloc','path','upvote','comments'])
df=posts.to_csv('data_cont.csv')
