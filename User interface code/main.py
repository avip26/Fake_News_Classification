def fake_news(text):
    import pandas as pd
    import pickle
    import re
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    abc_series = pd.Series(text)
    df = pd.DataFrame(abc_series, columns=['text'])

    def clean_text(text):
        # Remove punctuations
        text = re.sub(r'[?!.;:,#-@-]', '', text)
        text = re.sub('[\\\’]', '', text)
        text = re.sub('[^\w\s]', '', text)

        # Remove Stop word and Normalization()
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        filtered_sentence = []
        for word in word_tokens:
            word = lemmatizer.lemmatize(word)
            if word not in stop_words and len(word) > 2:
                filtered_sentence.append(word)
        text = " ".join(filtered_sentence)

        # Convert to lowercase to maintain consistency
        text = text.lower().replace('\n', '').replace('\r', '').strip()
        text = re.sub(' +', ' ', text)

        return text

    df['text'] = df['text'].apply(clean_text)

    fake_news_vectorize = pickle.load(open('fake_news_vectorizer.sav', 'rb'))
    model_text  = fake_news_vectorize.transform(df['text'])

    fake_news_model = pickle.load(open('fake_news_model.sav', 'rb'))
    result = fake_news_model.predict(model_text)
    print(result)
    if result == 0:
        return 'Reliable'
    if result == 1:
        return 'Unreliable'


if __name__ == '__main__':
    import streamlit as st
    st.title("Fake news detector")
    news = st.text_area("News Article", "Type here",height = 275)
    result = ""
    if st.button("predict"):
        result = fake_news(news)
        st.success("The given news is {}" .format(result))
    #print(fake_news("US President Joe Biden said on Friday that the relationship between India and the US, the world's two largest democracies, is destined to be stronger, closer and tighter, as he hosted Prime Minister Narendra Modi at the White House for the first bilateral meeting and discussed a wide range of priority issues, including combating COVID-19, climate change, trade and the Indo-Pacific.Prime Minister Modi, who is visiting the US for the 7th time after assuming office in 2014, described Fr ..Read more at:https://economictimes.indiatimes.com/news/india/pm-modi-holds-first-bilateral-meeting-with-president-biden-discusses-indo-pacific-climate-and-covid/articleshow/86490254.cms?utm_source=contentofinterest&utm_medium=text&utm_campaign=cppst"))
