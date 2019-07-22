# FlairDetection

## View the working project on 
[https://nandini-precog.herokuapp.com/](https://nandini-precog.herokuapp.com/)

## Directory Structure 
The folder ML_Proc consists of all the django files.
The folder NewPanda consists of all the cleaning, detection and collected data(MongoDB) files.
The folder Static consists of the CSS files.
The folder Template consists of the HTML files.
The Pip file is for dependencies to be installed.
The file manage.py is used to start Django server.


## Codebase
Coded in Python programming language, SVM module is used for training and testing data, Natural Language Processing to perform data cleaning. The application has been developed using Django web framework and hosted on Heroku web server.

## Approach
⋅⋅* Collected 100 India Subreddit Data for each flair using praw module.
⋅⋅* The collected data is stored using MongoDB, and it includes Title, Comments, Upvotes, ID and URL.
⋅⋅* The data was cleaned using NLP, all the stopwords are removed, and data is split randomly into 80% train and 20% test data.
⋅⋅* The ML algorithm is applied on the data set.
⋅⋅* Then the model is saved using joblib, and is used for prediction of the flair. 

## Accuracy
61%

## Project Execution
Open the Terminal.
Clone the repository by entering git clone https://github.com/radonys/Reddit-Flair-Detector.git.
Ensure that Python3 and pip is installed on the system.
