# Fake_News_Classification
In this digital world the fake new spread so rapidly without any authenticity of it. To solve this problem, I worked over this project. The dataset is provided consist of news article along with its authenticity. The task is to train a model that can predict the reliability of news based on the given attributes. Basically, it’s a classification problem.
Adding some random details 
**Tools / Skills Used1:**
1.	Python Programming
2.	Jupyter Notebook
3.	Pandas
4.	NumPy
5.	Matplotlibx
6.	Seaborn
7.	Exploratory Data Analysis
8.	Data Visualization
9.	Machine Learning
10.	Natural Language Processing
11.	Vectorization
12.	Streamlit

**Implementation and Workflow:**

![image](https://user-images.githubusercontent.com/58176446/158067537-98402552-4920-480e-ac7d-4cc4b19ab444.png)

**Modelling:**
1.	**Logistic Regression:** The logistic model is used to model the probability of a certain class or event existing such as pass/fail, win/lose, alive/dead or healthy/sick. This can be extended to model several classes of events such as determining whether an image contains a cat, dog, lion, etc.

2.	**Random Forest:** Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operate by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes or mean prediction of the individual trees.

3.	**Naive Bayes Classifier:** Naive Bayes Classifier is one of the simple and most effective Classification algorithms which helps in building the fast machine learning models that can make quick predictions. It is a probabilistic classifier, which means it predicts on the basis of the probability of an object





**Vectorizer:**

1.	**Count Vectorizer**: CountVectorizer is a great tool provided by the scikit-learn library in Python. It is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text. Count Vectorization involves counting the number of occurrences each word appears in a document (i.e., distinct text such as an article, book, even a paragraph!). 

2.	**TFIDF Vectorizer:** TfidfVectorizer is the base building block of many NLP pipelines. It is a simple technique to vectorize text documents — i.e., transform sentences into arrays of numbers — and use them in subsequent tasks.

**Model Result:**
**Train- 80%, Test- 20%**
1)	TFIDF (max feature = 400) + Random Forest Classifier = 90.76
2)	TFIDF (max feature = 400) + logistic regression = 91.17
3)	CountVectorizer (max feature = 400) + Random Forest Classifier = 90.64
4)	CountVectorizer (max feature = 400) + Random Forest Classifier = 90.37    

5)	TFIDF (max feature = 300) + Random Forest Classifier = 90.597
6)	TFIDF (max feature = 300) + logistic regression = 91.177
7)	CountVectorizer (max feature = 300) + Random Forest Classifier = 89.67
8)	CountVectorizer (max feature = 300) + Random Forest Classifier = 89.58

**Train- 70%, Test- 30%**
1)	TFIDF (max feature = 400) + Random Forest Classifier = 90.97
2)	TFIDF (max feature = 400) + logistic regression = 91.34
3)	CountVectorizer (max feature = 400) + Random Forest Classifier = 90.70
4)	CountVectorizer (max feature = 400) + Random Forest Classifier = 90.55

5)	TFIDF (max feature = 300) + Random Forest Classifier = 89.05
6)	TFIDF (max feature = 300) + logistic regression = 88.99
7)	CountVectorizer (max feature = 300) + Random Forest Classifier = 89.20
8)	CountVectorizer (max feature = 300) + Random Forest Classifier = 88. 

## TFIDF with Logistic regression gives us the best result, so we move ahead with the logitic regressiom model
