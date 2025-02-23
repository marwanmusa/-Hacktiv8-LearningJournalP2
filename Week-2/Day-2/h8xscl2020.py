# -*- coding: utf-8 -*-
"""H8xSCL2020.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ardhiraka/H8_SCL2020/blob/master/H8xSCL2020.ipynb

<img src = "https://hacktiv8.com/assets/img/logos/hacktiv8-text-black.svg" width = 400>
<h1 align=center><font size = 5>Hacktiv8 for Shopee Code League 2020 // The Science of Emotions: Introduction to Sentiment Analysis</font></h1>

Title: Hacktiv8 for Shopee Code League 2020 - The Science of Emotions: Introduction to Sentiment Analysis <br/>
Last Updated: July 10, 2020 <br/>
Author: Raka Ardhi

**Hi! Welcome to Hacktiv8 x Shopee Code League 2020 materials landing page.**

<!-- <div style="text-align: justify"> -->
    
**Labs Description**

Computers have feelings, too! How, you ask? Sentiment Analysis! Sentiment analysis is a vital topic in the field of Natural Language Processing and has easily become one of the hottest topics in the field because of its relevance and the number of business problems it is solving and has been able to answer. In this session we will teach computer to be able to understand emotions and feelings based on what sentence you gave them, covering not-so-simple topic in a simple way. Start from math behind; finish with build a simple sentiment analysis model in the end, so your computers could, care.

**Labs Overview**

Hacktiv8 x SCL2020 Labs has everything you need to learn NLP especially Sentiment Analysis. This labs is perfect for those who want to learn text processing fundamentals, including stemming and lemmatization. Explore machine learning methods in sentiment analysis. Use several algorithm, including Naive Bayes, Maximum Entropy, Support Vector Machines and compare their performance.

**Educational Objectives**

As a participant of Hacktiv8 x SCL2020 Labs, you are expected to meet certain targets which are:
- Able to understand the main techniques used in natural language processing (Sentiment Analysis)
- Familiarized with the terminology and the topics in sentiment analysis
- Able to understand text analysis techniques such as tokenization, stemming, lemmatization, and feature extraction
- Able to understand basic concept of Naive Bayes, Maximum Entropy and Support Vector Machines
- Use Naive Bayes, MaxEnt, SVM to build sentiment analysis model

**Prerequisite**

To enroll this Labs, you should have experience Python programming knowledge, including: At least 40 hours of programming experience, Familiarity with data structures like dictionaries and lists, Experience with libraries like NumPy and pandas. You also should have at least Intermediate statistics background. You are familiar with probability.

Device requirements: Having Anaconda and/or any code editor installed in your system.

**Dataset used in this labs can be found in [here](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt) and/or [here](https://www.kaggle.com/farhan999/tokopedia-product-reviews).**

**Table of Contents**

This section covers what you'll learn in this labs.

1. [NLP and Sentiment Analysis](#Natural-Language-Processing-and-Sentiment-Analysis-Introduction)
1. [Text Preprocessing](#Text-Preprocessing)
1. [Naive Bayes for Sentiment Analysis](#Naive-Bayes-for-Sentiment-Analysis)
1. [Comparing to Other Model](#Comparing-to-Other-Model)
1. [Next Step](#What's-Next%3F)
1. [References](#References)

# Natural Language Processing and Sentiment Analysis Introduction

## Brief Introduction to NLP

Computers are great at working with structured data like spreadsheets and database tables. But us humans usually communicate in words, not in tables. That’s unfortunate for computers 😢

<center><img src='https://s3.us-east-2.amazonaws.com/ardhiraka.com/img/shakes.png' width="20%" /></center>

<!-- <div style="text-align: justify"> -->
According to industry estimates, only 21% of the available data is present in structured form. Data is being generated as we speak, as we tweet, as we send messages on Whatsapp and in various other activities. Majority of this data exists in the textual form, which is highly unstructured in nature.
Few notorious examples include – tweets / posts on social media, user to user chat conversations, news, blogs and articles, product or services reviews and patient records in the healthcare sector. A few more recent ones includes chatbots and other voice driven bots.
Despite having high dimension data, the information present in it is not directly accessible unless it is processed (read and understood) manually or analyzed by an automated system.

Based on information given above, lot of information in the world is unstructured — raw text in English (or bahasa) or another human language. How can we get a computer to understand unstructured text and extract data from it? **Can Computers Understand Language?**

> Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data. - Wikipedia

So, in short; Natural Language Processing, or NLP, is the sub-field of AI that is **focused on enabling computers to understand and process human languages**.
With the help of a Bunch of Algorithms and rules the computer able to understand and communicate with humans in vast human languages and scales other language-related tasks. With NLP, it is possible to perform certain tasks like Automated Speech and Automated Text Writing in less time. Due to the evolving of large data (text), why not to use the computers which have high computing power, capable of working all day and ability to run several algorithms to perform tasks in no time.

NLP can be divided into 3 categories (Rule-based systems, Classical Machine Learning models and Deep Learning models).
1. Rule-based systems rely heavily on crafting domain-specific rules (e.g: regular expressions), can be used to solve simple problems such as extracting structured data (e.g: emails) from unstructured data (e.g: web-pages), but due to the complexity of human natural languages, rule-based systems fail to build models that can really reason about language.
2. Classical Machine Learning approaches can be used to solve harder problems which rule-based systems can’t solve very well (e.g: Spam Detection), it rely on a more general approach to understanding language, using hand-crafted features (e.g: sentence length, part of speech tags, occurrence of specific words) then providing those features to a statistical machine learning model (e.g: Naive Bayes), which learns different patterns in the training set and then be able to reason about unseen data (inference).
3. Deep Learning models are the hottest part of NLP research and applications now, they generalize even better than the classical machine learning approaches as they don’t need hand-crafted features because they work as feature extractors in an automatic way, which helped a lot in building end-to-end models (little human-interaction). Aside from the feature engineering part, deep learning algorithms learning capabilities are more powerful than the shallow/classical ML ones, which paved its way to achieving the highest scores on different hard NLP tasks (e.g: Machine Translation).
    
## Extracting Meaning from Text is Hard
    
The process of reading and understanding English (or bahasa) is very complex — and that’s not even considering that English (or bahasa) doesn’t follow logical and consistent rules. For example, what does this news headline mean?
    
> "Environmental regulators grill business owner over illegal coal fires."
    
Are the regulators questioning a business owner about burning coal illegally? Or are the regulators literally cooking the business owner? As you can see, parsing English with a computer is going to be complicated. Another challenge are listed below:
    
1. Ambiguity / Crash Blossom <br />
    It is the challenge when a Single word has different meanings or a sentence that has different meanings in the context and even a sentence refers to sarcasm.
    - Lexical Ambiguity is the presence of two or more possible meanings within a single word. (ie. I saw her _duck_)
    - Syntactic Ambiguity is the presence of two or more possible meanings within a single sentence or sequence of words. (ie. The chicken is _ready to eat_)
2. Syntax <br />
    Think of how a sentence is valid, it based on two things called syntax and semantics where syntax refers to the grammatical rules, on the other hand, semantics is the meaning of the vocabulary symbols within that structure. People change the ordering of sentences it is valid in some cases but not all.
3. Co-reference / Anaphora Resolution <br />
    The problem of resolving what a pronoun, or a noun phrase refers to. (ie. Hacktiv8's employee took two trips around France. _They_ were both wonderful.)
4. Slang
5. Sarcasm <br />
    Same words different meaning refers to the Ambiguity topic. Suppose when someone does something wrong you reply as very good or well done. it’s also a challenge for a computer to understand the sarcasm because it’s a way more different than a normal conversation.

## Aplications of NLP

- Machine Translation
- Information Extraction
- **Sentiment Analysis**
- Information Retrieval
- Question Answering
- Summarization
"""

import subprocess as sp
import sys,os
from os.path import join

# mount Google Drive
from os.path import expanduser
gd_path=join(expanduser("~"),'gd')

if not os.path.isdir(gd_path):
    try:
        # load Google Drive
        from google.colab import drive,files
        drive.mount('/drive')
        sp.call('ln -s /drive/My\ Drive '+gd_path, shell=True)
    except:
        print('unable to find Google Drive Folder')
os.chdir(gd_path+'/Colab Notebooks/Datasets')
os.listdir('.')

"""# Data Preparation"""

import pandas as pd
import numpy as np
import re
import string

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure

sns.set_style("whitegrid")
import warnings
warnings.filterwarnings('ignore')

dfAmazon = pd.read_csv('datasets/amazon_reviews_us_Electronics_v1_00.tsv.gz', sep='\t', compression='gzip', error_bad_lines=False)

dfAmazon.head()

dfAmazon.shape

dfAmazon.isnull().sum()

dfAmazon.dropna(subset=['star_rating', 'review_body'], inplace=True)

dfAmazon.isnull().sum()

amazonReviews = dfAmazon[['star_rating', 'review_body']].copy()

amazonReviews.head()

amazonReviews.tail()

sample_text = amazonReviews.loc[3091020]['review_body']

print(sample_text)

# Basic Text Preprocessing

# Case Folding
sample_text = sample_text.lower()
sample_text = re.sub(r'\d+', '', sample_text)
sample_text = sample_text.translate(str.maketrans("","", string.punctuation))
sample_text = sample_text.strip()

print(sample_text)

# Sentence Tokenization
from nltk.tokenize import sent_tokenize
sent_token = sent_tokenize(sample_text)

print(sent_token)

# Word Tokenization
from nltk.tokenize import word_tokenize
word_token = word_tokenize(sample_text)

print(word_token)

# Frequency Distribution
from nltk.probability import FreqDist

fdist = FreqDist(word_token)

fdist.most_common(2)

fdist.plot(30, cumulative=False)
plt.show()

# stopwords
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
print(stop_words)

sent_filtered = []

for w in word_token:
    if w not in stop_words:
        sent_filtered.append(w)
        
print("Tokenized Sentence:", word_token)
print("Filterd Sentence:", sent_filtered)

fdist = FreqDist(sent_filtered)

fdist.plot(30, cumulative=False)
plt.show()

# Lexicon Normalization

# Stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

stemmed_words = []
for w in sent_filtered:
    stemmed_words.append(ps.stem(w))

print("Filtered Sentence:", sent_filtered)
print("Stemmed Sentence:", stemmed_words)

# Performing stemming and Lemmatization

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()

print("Lemmatized Word:",lem.lemmatize('lying', "v"))
print("Stemmed Word:",stem.stem('lying'))

lemmatized_words = []

for w in sent_filtered:
    lemmatized_words.append(lem.lemmatize(w))
    
print("Filtered Sentence:", sent_filtered)
print("Lemmatized Sentence:", lemmatized_words)

amazonReviews.reset_index(inplace=True)

"""## Amazon Dataset Preprocessing"""

# Stopwords
amazonReviews['stopwords'] = amazonReviews['review_body'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
amazonReviews[['review_body','stopwords']].head()

# Punctuation
def count_punct(text):
    count = sum([1 for char in text if char in string.punctuation])
    return count

amazonReviews['punctuation'] = amazonReviews['review_body'].apply(lambda x: count_punct(x))
amazonReviews[['review_body','punctuation']].head()

# Hastag
amazonReviews['hastags'] = amazonReviews['review_body'].apply(lambda x: len([x for x in x.split() if x.startswith('#')]))
amazonReviews[['review_body','hastags']].head()

# Numbers / Digits
amazonReviews['numerics'] = amazonReviews['review_body'].apply(lambda x: len([x for x in x.split() if x.isdigit()]))
amazonReviews[['review_body','numerics']].head()

# Uppercase
amazonReviews['upper'] = amazonReviews['review_body'].apply(lambda x: len([x for x in x.split() if x.isupper()]))
amazonReviews[['review_body','upper']].head()

# Make all Text LowerCase
amazonReviews['review_body'] = amazonReviews['review_body'].apply(lambda x: " ".join(x.lower() for x in x.split()))
amazonReviews['review_body'].head()

# Remove Punctuation
amazonReviews['review_body'] = amazonReviews['review_body'].str.replace('[^\w\s]','')
amazonReviews['review_body'].head()

# Remove Stopwords
from nltk.corpus import stopwords
stop = stopwords.words('english')

amazonReviews['review_body'] = amazonReviews['review_body'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
amazonReviews['review_body'].sample(10)

def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

round1 = lambda x: clean_text_round1(x)

amazonReviews['review_body'] = amazonReviews['review_body'].apply(round1)
amazonReviews['review_body']

def clean_text_round2(text):
    '''Get rid of some additional punctuation and non-sensical text that was missed the first time around.'''
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    return text

round2 = lambda x: clean_text_round2(x)

amazonReviews['review_body'] = amazonReviews['review_body'].apply(round2)
amazonReviews['review_body']

# Number of Words
amazonReviews['word_count'] = amazonReviews['review_body'].apply(lambda x: len(str(x).split(" ")))
amazonReviews[['review_body','word_count']].head()

# Number of Character
amazonReviews['char_count'] = amazonReviews['review_body'].str.len()
amazonReviews[['review_body','char_count']].head()

# Average Words
def avg_word(sentence):
  words = sentence.split()
  return (sum(len(word) for word in words)/(len(words)+0.000001))

amazonReviews['avg_word'] = amazonReviews['review_body'].apply(lambda x: avg_word(x)).round(1)
amazonReviews[['review_body','avg_word']].head()

amazonReviews.sample(2)

# Write to CSV
amazonReviews.to_csv('Amazon_reviews_processed.csv', index=False)

"""# Data Visualization"""

amazonReview = pd.read_csv('Amazon_reviews_processed.csv')
amazonReview.head(5)

amazonReview.describe().round(0)

# Distribution of stopwords values
figure(dpi = 120)
sns.distplot(amazonReview.stopwords, rug=True, hist=False, color = 'green')

amazonReview.loc[amazonReview.stopwords >= 900].review_body

# Distribution of 'punctuation'
figure(dpi = 130)
sns.kdeplot(amazonReview.punctuation,shade=True, color = 'red')

amazonReview.loc[amazonReview.word_count <=3].review_body

amazonReview.shape

# Remove duplicate review
amazonReview = amazonReview.drop_duplicates(subset = ['review_body'])

amazonReview.shape

# Distribution of word_count values
figure(dpi = 120)
sns.kdeplot(amazonReview.word_count,shade=True, color = 'green')

amazonReview.loc[amazonReview.word_count >=800].review_body

# Distribution of char_count values
figure(dpi = 120)
sns.kdeplot(amazonReview.char_count,shade=True, color = 'purple')

# Distribution of avg_word values
figure(dpi = 120)
sns.kdeplot(amazonReview.avg_word,shade=True, color = 'red')

amazonReview.info()

# Distribution of star rating values
amazonReview.star_rating.value_counts(ascending = False).plot(kind= 'bar', figsize= (6,6))

plt.xlabel("Scores")
plt.ylabel('Number of Rating')
plt.title('Distribution of Scores')

# Number of Characters in Reviews
fig, axs = plt.subplots(3,2, figsize=(10, 15))

#Score 1
review_len = amazonReview.loc[amazonReview['star_rating']==1]['review_body'].str.len()
axs[0,0].hist(review_len, color='blue', range=(0,1500))
axs[0,0].set_title('Score is 1')

#Score 2
review_len = amazonReview.loc[amazonReview['star_rating']==2]['review_body'].str.len()
axs[0,1].hist(review_len, color='red',range=(0,1500))
axs[0,1].set_title('Score is 2')

#Score 3
review_len = amazonReview.loc[amazonReview['star_rating']==3]['review_body'].str.len()
axs[1,0].hist(review_len, color='green', range=(0,1500))
axs[1,0].set_title('Score is 3')

#Score 4
review_len = amazonReview.loc[amazonReview['star_rating']==4]['review_body'].str.len()
axs[1,1].hist(review_len, color='orange', range=(0,1500))
axs[1,1].set_title('Score is 4')


#Score 5
review_len = amazonReview.loc[amazonReview['star_rating']==5]['review_body'].str.len()
axs[2,0].hist(review_len, color='purple', range=(0,1500))
axs[2,0].set_title('Score is 5')

#All Scores
review_len = amazonReview['review_body'].str.len()
axs[2,1].hist(review_len, color='black', range=(0,1500))
axs[2,1].set_title('Length of All Reviews')


fig.suptitle('Number of characters in Reviews')

plt.show()

# Convert 5 Stars to Binary Value
amazonReview['Good_reviews'] = amazonReview.star_rating
amazonReview.Good_reviews[amazonReview.star_rating <= 3] = 0
amazonReview.Good_reviews[amazonReview.star_rating >= 4] = 1

a = amazonReview.groupby(['Good_reviews'])['index'].count()
a = a.reset_index()
a = a.rename(columns={'index': 'Number of Reviews'})
fig, ax = plt.subplots(figsize=(6, 6))

sns.barplot(x='Good_reviews', y='Number of Reviews', data=a)
plt.xlabel("Good Reviews")
plt.ylabel('Number of Reviews')
plt.title('Distribution of Good Reviews')

amazonReview.to_csv('Amazon_reviews_cleaned_finalform.csv', index=False)

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Start with one review:
abc = amazonReview.review_body[5]

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(abc)

# Display the generated image:
figure(figsize= (10,10), dpi= 90)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

amazonReview['review_body'] = amazonReview['review_body'].astype(str)

text_for_cloud = " ".join(x for x in amazonReview['review_body'].head(100000))
print ("There are {} words in the combination of all reviews.".format(len(text_for_cloud)))

stopwords = set(STOPWORDS)

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text_for_cloud)

# Display the generated image:
# the matplotlib way:
figure(figsize= (8,8), dpi= 100)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

"""# Modeling"""

import itertools
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
from sklearn.dummy import DummyClassifier

amazonReview = pd.read_csv('Amazon_reviews_cleaned_finalform.csv')
amazonReview.head(5)

# from textblob import TextBlob

# amazonReview['review_body'] = amazonReview['review_body'].astype(str)

# pol = lambda x: TextBlob(x).sentiment.polarity
# sub = lambda x: TextBlob(x).sentiment.subjectivity


# amazonReview['polarity'] = amazonReview['review_body'].apply(pol)
# amazonReview['subjectivity'] = amazonReview['review_body'].apply(sub)
# amazonReview.head()

# amazonReview['polarity'] = amazonReview['polarity'].round(2)
# amazonReview['subjectivity'] = amazonReview['subjectivity'].round(2)
# amazonReview.sample(5)

amazonReview.isnull().sum()

amazonReview.dropna(subset=['review_body'], inplace=True)

data_used = amazonReview.sample(n = 10000)
# data_used = amazonReview
X = data_used.review_body
y = data_used.Good_reviews
print(X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
print ('Train Set Shape\t\t:{}\nTest Set Shape\t\t:{}'.format(X_train.shape, X_test.shape))

# Confusion Matrix Plot
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title = 'Confusion matrix',
                          cmap = plt.cm.ocean):
    """
    Create a confusion matrix plot for 'good' and 'bad' rating values 
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis = 1)[:, np.newaxis]
    plt.imshow(cm, interpolation = 'nearest', cmap = cmap)
    plt.title(title, fontsize = 20)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, fontsize = 20)
    plt.yticks(tick_marks, classes, fontsize = 20)
    
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.

    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), horizontalalignment = "center", 
                 color = "white" if cm[i, j] < thresh else "black", fontsize = 40)
    
    plt.tight_layout()
    plt.ylabel('True Label', fontsize = 30)
    plt.xlabel('Predicted Label', fontsize = 30)

    return plt

def disp_confusion_matrix(y_pred, model_name, vector = 'CounterVectorizing'):
    """
    Display confusion matrix for selected model with countVectorizer
    """
    cm = confusion_matrix(y_test, y_pred)
    fig = plt.figure(figsize=(10, 10))
    plot = plot_confusion_matrix(cm, classes=['Bad','Good'], normalize=False, 
                                 title = model_name + " " + 'with' + " " + vector + " "+ '\nConfusion Matrix')
    plt.show()

"""## CountVectorizer Bag of Word"""

# Create the word vector with CountVectorizer

count_vect = CountVectorizer(ngram_range=(1,1))
count_vect_train = count_vect.fit_transform(X_train)
count_vect_train = count_vect_train.toarray()
count_vect_test = count_vect.transform(X_test)
count_vect_test = count_vect_test.toarray()

# Print vocabulary length
print('Vocabulary length :', len(count_vect.get_feature_names()))

# Assign feature names of vector into a variable
vocab = count_vect.get_feature_names()

# Dataframe for train countvectorizer dataset
pd.DataFrame(count_vect_train, columns = vocab).head()

# Creating a function for applying different algorithms
def modeling(Model, Xtrain = count_vect_train, Xtest = count_vect_test):
    """
    This function apply countVectorizer with machine learning algorithms. 
    """
    
    # Instantiate the classifier: model
    model = Model
    
    # Fitting classifier to the Training set (all features)
    model.fit(Xtrain, y_train)
    
    global y_pred
    # Predicting the Test set results
    y_pred = model.predict(Xtest)
    
    # Assign f1 score to a variable
    score = f1_score(y_test, y_pred, average = 'weighted')
    
    # Printing evaluation metric (f1-score) 
    print("f1 score: {}".format(score))

# Dummy Classifier
clf = DummyClassifier(strategy = 'stratified', random_state =42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score = f1_score(y_test, y_pred, average = 'weighted')
    
# Printing evaluation metric (f1-score) 
print("f1 score: {}".format(score))

# Compute and print the classification report
print(classification_report(y_test, y_pred))

"""# Naive Bayes for Sentiment Analysis"""

# Call the modeling function for naive bayes with countvectorizer and print f1 score
modeling(MultinomialNB())

# Assign y_pred to a variable for further process
y_pred_cv_nb = y_pred

# Compute and print the classification report
print(classification_report(y_test, y_pred_cv_nb))

# Print confusion matrix for naive bayes with countVectorizer
disp_confusion_matrix(y_pred_cv_nb, "Naive Bayes")

"""# Comparing to Other Model

## Logistic Regression
"""

# Call the modeling function for Logistic Regression with countvectorizer and print f1 score
# modeling(LogisticRegression(multi_class = 'multinomial', solver = 'newton-cg', class_weight = 'balanced', C = 0.1, n_jobs = -1, random_state = 42))
modeling(LogisticRegression())

# Assign y_pred to a variable for further process
y_pred_cv_logreg = y_pred

# Print confusion matrix for naive bayes with countVectorizer
disp_confusion_matrix(y_pred_cv_logreg, "LogReg")

"""## Support Vector Machine"""

# Call the modeling function for SVM with countvectorizer and print f1 score
modeling(SVC(gamma='auto'))

# Assign y_pred to a variable for further process
y_pred_cv_svm = y_pred

# Print confusion matrix for naive bayes with countVectorizer
disp_confusion_matrix(y_pred_cv_svm, "SVM")

"""## Comparison Table"""

# Function for converting the "classification report" results to a dataframe
def pandas_classification_report(y_true, y_pred):
    metrics_summary = precision_recall_fscore_support(
            y_true=y_true, 
            y_pred=y_pred)

    avg = list(precision_recall_fscore_support(
            y_true=y_true, 
            y_pred=y_pred,
            average='weighted'))

    metrics_sum_index = ['precision', 'recall', 'f1-score', 'support']
    class_report_df = pd.DataFrame(
        list(metrics_summary),
        index=metrics_sum_index)

    support = class_report_df.loc['support']
    total = support.sum() 
    avg[-1] = total

    class_report_df['weighted avg'] = avg

    return class_report_df.T

# Function for adding explanatory columns and organizing all dataframe
def comparison_matrix(y_test, y_pred, label, vector):
    df = pandas_classification_report(y_test, y_pred)
    df['class']=['bad', 'good', 'average']
    df['accuracy']= metrics.accuracy_score(y_test, y_pred)
    df['model'] = label
    df['vectorizer'] = vector
    df = df[['vectorizer', 'model', 'accuracy', 'class', 'precision', 'recall', 'f1-score', 'support']]
    return df

# For loop for using "comparison functions" 

def comparison_table(y_preds, labels):
    
    # empty list for collecting dataframes
    frames_tv = [] 
    
    # list for y_preds
    y_preds_tv = y_preds
    
    # list for labels
    labels_tv = labels  
    
    vector_tv = 'CountVect'
    
    for y_pred, label in zip(y_preds_tv, labels_tv):
        df = comparison_matrix(y_test, y_pred, label, vector_tv)
        frames_tv.append(df)

    # concatenating all dataframes
    global df_tv
    df_tv = pd.concat(frames_tv)
    
    global df_tv2
    df_tv2 = df_tv.set_index(['vectorizer', 'model', 'accuracy', 'class'])

def f1_score_bar_plot(df, category, title):
    df = df[df['class']==category]
    x = list(df['model'])
    y = list(df['f1-score'])
    y_round = list(round(df['f1-score'],2))
    a = (list(df['f1-score'])).index(max(list(df['f1-score'])))
    z = (list(df['f1-score'])).index(min(list(df['f1-score'])))
    y_mean = round(df['f1-score'].mean(),2)
    
    plt.rcParams['figure.figsize']=[15,5]
    b_plot = plt.bar(x=x,height=y)
    b_plot[a].set_color('g')
    b_plot[z].set_color('r')
    
    for i,v in enumerate(y_round):
        plt.text(i-.15,0.018,str(v), color='black', fontsize=15, fontweight='bold')
    
    plt.axhline(y_mean,ls='--',color='k',label=y_mean)
    plt.title(title)
    plt.legend()
    
    return plt.show()

comparison_table(y_preds = [y_pred_cv_logreg, y_pred_cv_nb, y_pred_cv_svm], labels = ['LogReg', 'Naive Bayes', 'SVM'])

df_tv2

# Plotting f1 score with "f1_score_bar_plot" function
f1_score_bar_plot(df=df_tv, category='average', title= "Average f1 Score")

"""# TF-IDF"""

# Create the word vector with TF-IDF Vectorizer
tfidf_vect = TfidfVectorizer(ngram_range=(1, 1))
tfidf_vect_train = tfidf_vect.fit_transform(X_train)
tfidf_vect_train = tfidf_vect_train.toarray()
tfidf_vect_test = tfidf_vect.transform(X_test)
tfidf_vect_test = tfidf_vect_test.toarray()

# Call the modeling function for logistic regression with TF-IDF and print f1 score
# modeling(LogisticRegression(multi_class = 'multinomial', solver = 'newton-cg', class_weight = 'balanced', C = 0.1, n_jobs = -1, random_state = 42), tfidf_vect_train, tfidf_vect_test)
modeling(LogisticRegression(), tfidf_vect_train, tfidf_vect_test)

# Assign y_pred to a variable for further process
y_pred_tfidf_logreg = y_pred

# Compute and print the classification report
print(classification_report(y_test, y_pred_tfidf_logreg))

# Call the modeling function for naive bayes with TF-IDF and print f1 score
modeling(MultinomialNB(), tfidf_vect_train, tfidf_vect_test)

# Assign y_pred to a variable for further process
y_pred_tfidf_nb = y_pred

# Compute and print the classification report
print(classification_report(y_test, y_pred_tfidf_nb))

# Call the modeling function for naive bayes with TF-IDF and print f1 score
modeling(SVC(), tfidf_vect_train, tfidf_vect_test)

# Assign y_pred to a variable for further process
y_pred_tfidf_svm = y_pred

# Compute and print the classification report
print(classification_report(y_test, y_pred_tfidf_svm))

comparison_table(y_preds = [y_pred_tfidf_logreg, y_pred_tfidf_nb, y_pred_tfidf_svm], 
                labels = ['LogReg', 'Naive Bayes', 'SVM'])

# Print the comparision matrix

print('\nComparison Matrix of Models with TF-IDF Vectorizer\n')
df_tv2

# Plotting f1 score with "f1_score_bar_plot" function
f1_score_bar_plot(df=df_tv, category='average', title= "Average F1 Score")

"""# What's Next?"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))

sentiment_analyzer_scores("The phone is super cool.")

sentiment_analyzer_scores("The phone is super cool!")

print(sentiment_analyzer_scores("The phone is super cool!!"))
print(sentiment_analyzer_scores("The phone is super cool!!!"))

print(sentiment_analyzer_scores("The phone is SUPER COOL!!!"))

print(sentiment_analyzer_scores("The phone is cool"))

print(sentiment_analyzer_scores("The phone is extremely cool"))
print(sentiment_analyzer_scores("The phone is marginally cool"))

print(sentiment_analyzer_scores("The phone is cool, but the price is horrible"))

print(sentiment_analyzer_scores("The phone is 🔥"))

print(sentiment_analyzer_scores("The phone is LIT"))

print(sentiment_analyzer_scores("The phone is :D"))

"""# Thanks for completing this labs!

Notebook created by: <a href="https://ardhiraka.com/"> Raka Ardhi</a>.

This notebook is part of training on **Shopee Coding League 2020**. If you accessed this notebook outside the course, you can take Python remote course by clicking [here](https://hacktiv8.com/parttime/).

\
### References

1. Amazon Customer Reviews Dataset in [AWS Open Data](https://registry.opendata.aws/amazon-reviews/)
1. [Natural Language Toolkit](https://www.nltk.org/)
1. [PySastrawi](https://github.com/har07/PySastrawi)
1. [Scikit-Learn](https://scikit-learn.org/)
1. Tokopedia Product Reviews by Farhan in [Kaggle](https://www.kaggle.com/farhan999/tokopedia-product-reviews)
1. Devlin, Jacob & Chang, Ming-Wei & Lee, Kenton & Toutanova, Kristina. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.
1. Foundations of Statistical Natural Language Processing, MIT Press. Cambridge, MA: May 1999.
1. Go, Alec & Bhayani, Richa & Huang, Lei. (2009). Twitter sentiment classification using distant supervision. Processing. 150.
1. Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
1. Nigam, Kamal & Laertyy, John & McCallumzy, Andrew. (1999). Using Maximum Entropy for Text Classication.
1. Rathor, Abhilasha & Agarwal, Amit & Dimri, Preeti. (2018). Comparative Study of Machine Learning Approaches for Amazon Reviews. Procedia Computer Science. 132. 1552-1561. 10.1016/j.procs.2018.05.119.

<hr />

Copyright &copy; 2020 [PT Hacktivate Teknologi Indonesia](https://hacktiv8.com).
"""