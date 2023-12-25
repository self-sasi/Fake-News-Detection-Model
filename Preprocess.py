import Dependencies
import joblib


# loading the dataset train.csv to pandas dataframe

news_dataset = Dependencies.pd.read_csv('train.csv')



#checking dimensions of the dataset 

news_dataset.shape



#lets print the first five rows of the dataframe

news_dataset.head



#lets find out the number of missing values int he dataset

news_dataset.isnull().sum()



#replacing the null values with empty string

news_dataset = news_dataset.fillna('')



#we will combine the 'title' and the 'author' columns together

news_dataset['combined'] = news_dataset['author'] + ' ' + news_dataset['title']



#lets now separate the data & label

X = news_dataset.drop(columns='label', axis=1)
Y = news_dataset['label']



#STEMMING - reduces a word to it's root word

port_stem = Dependencies.PorterStemmer()
re = Dependencies.re

def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]',' ', content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in Dependencies.stopwords.words('english') ]
    stemmed_content = ' '.join(stemmed_content)
    
    return stemmed_content

news_dataset['combined'] = news_dataset['combined'].apply(stemming)



#separating data and label

X = news_dataset['combined'].values
Y = news_dataset['label'].values



# converting textual data to numerical data

vectorizer = Dependencies.TfidfVectorizer()

vectorizer.fit(X)
stored_vectorizer = vectorizer.fit(X)

X = vectorizer.transform(X)



#Splitting data into train and test to evaluate later on. 

X, X_t, Y, Y_t = Dependencies.train_test_split(X, Y, test_size = 0.2, stratify=Y, random_state=2)
#Training model: Logistic Regression

model = Dependencies.LogisticRegression()

model.fit(X, Y)

joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(model, 'model.pkl')


def predictNews(filepath):
    
    loaded_vectorizer = joblib.load('vectorizer.pkl')
    loaded_model = joblib.load('model.pkl')

    # Load and preprocess the new data
    news_dataset = Dependencies.pd.read_csv(filepath)
    news_dataset = news_dataset.fillna('')
    news_dataset['combined'] = news_dataset['Author'] + ' ' + news_dataset['Title']
        
    port_stem = Dependencies.PorterStemmer()
    re = Dependencies.re

    def stemming(content):
        stemmed_content = re.sub('[^a-zA-Z]',' ', content)
        stemmed_content = stemmed_content.lower()
        stemmed_content = stemmed_content.split()
        stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in Dependencies.stopwords.words('english') ]
        stemmed_content = ' '.join(stemmed_content)
            
        return stemmed_content
        
    news_dataset['combined'] = news_dataset['combined'].apply(stemming)

    # Transform the new data using the loaded vectorizer
    X_new = loaded_vectorizer.transform(news_dataset['combined'].values)

    # Make predictions using the loaded model
    predictions = loaded_model.predict(X_new)

    # Return the predictions as string
    return ' '.join(str(prediction) for prediction in predictions)


