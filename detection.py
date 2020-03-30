

import praw
import prawcore


def cleaning(df):


    try:
        df=str(df)
        df = df.lower()

        df = ' '.join(word for word in df.split() if word not in SYMBOLS)
        df = ' '.join(word for word in df.split() if word not in DIGITS)
        df = ' '.join(word for word in df.split() if word not in STOPWORDS)
        return df
    except:
        return "null"



def ml(url):
    reddit = praw.Reddit(client_id='tad4C91o6_CRxQ',
                         client_secret='vdOd7CS9ibUjqGND-Z2iTUQMHGg',
                         password='panda2000',
                         user_agent='Flair Script For Reddit by /u/nandini18056',
                         username='nandini18056')

    USER_AGENT = 'Flair Script For Reddit by /u/nandini18056'
    from sklearn.externals import joblib
    mj=joblib.load('ml_proc/model_joblib')

    DIGITS=[0,1,2,3,4,5,6,7,8,9]
    SYMBOLS=['*','/','-','(',')',';','#','/','{','}','|','+','.','?','&','$',"@","%",'^','=']
    STOPWORDS = {'his', 'more', 'd', 'an', 'myself', 'during', 'but', 'between', 'were', 'your', 'against', 'ourselves', 'few', 'isn', 'he', 'mustn', "wouldn't", 'same', 'other', 'above', "needn't", 'having', 'them', 'can', 'her', "hadn't", 'a', 'doesn', 'didn', 'most', 'yourself', "you'll", 'once', 'y', 'am', 'because', 'and', 'theirs', "you're", 's', 'aren', 'to', "shan't", 'haven', 'just', "wasn't", 'below', 'until', 'shouldn', "didn't", 'so', 'does', 'did', 'she', 'hers', 'that', "doesn't", 're', 'here', "weren't", 'are', 'ain', "you'd", 'you', "aren't", 'wouldn', 'needn', "couldn't", "mightn't", 'after', 'had', 'themselves', 'further', 'not', 'what', 'through', 'm', 'off', 'now', 'from', 'both', 'my', 'such', 'won', 'wasn', 'those', 'it', 'him', "that'll", 'be', 'under', 'when', 'where', 'each', 'have', 'couldn', 'has', 'being', 'of', 've', "don't", "shouldn't", 'been', 'is', 'its', 'weren', 'then', 'nor', 'herself', 'these', 'do', "mustn't", 'their', 'into', 'himself', 'the', 'should', 'ma', 'we', 'which', 't', "you've", 'in', 'any', 'i', 'before', 'out', 'itself', 'will', "isn't", 'ours', 'on', 'at', 'doing', 'mightn', 'no', 'who', 'down', 'o', 'me', 'only', 'than', 'll', "won't", 'how', "she's", 'again', 'yours', 'over', 'this', 'or', 'there', 'by', 'our', "it's", 'hasn', 'up', 'about', "should've", 'don', 'for', 'whom', 'all', 'very', 'while', 'hadn', "hasn't", 'yourselves', 'shan', 'why', 'some', 'they', 'own', "haven't", 'as', 'with', 'too', 'if', 'was'}
    D = reddit.submission(url=url)

    s = ''
    for top_level_comment in D.comments:
    	s = s + ' ' + top_level_comment.body

    title=cleaning(D.title)
    comment=cleaning(s)
    path=cleaning(D.url)
    ans=title+comment+path
    
    result= mj.predict([ans])
    return str(result[0])


# def input(request):
#     if request.method == 'GET':
#         return render(request, 'dataInput.html')
#     else:
#         link_ = request.POST['input_link']
#         output = ml_code(link_)
#         return render(request, 'dataOutput.html', {'link' : link_ , 'output_content' : output})

