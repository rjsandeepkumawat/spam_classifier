
# SMS/Email Spam Classifier

This project is a web application for classifying SMS or email messages as spam or not spam. The application is built using Streamlit for the frontend, and it utilizes machine learning techniques to perform the classification. The Naive Bayes algorithm, specifically the Multinomial Naive Bayes variant, is employed for this task. The project also involves Natural Language Processing (NLP) tasks using NLTK to preprocess and prepare the data.

## Project Components

1. **`app.py`**: The main Streamlit application script. This file contains the code for the web interface and handles user input and display of classification results.

2. **`model.py`**: This script is responsible for training the Naive Bayes model using the provided dataset. It saves the trained model for use in the web application.

3. **`vectorizer.py`**: This script contains the code for text vectorization. It prepares the text data for the model by converting it into a numerical format that the machine learning algorithm can process.

4. **Data Files**: The dataset used for training and evaluation is sourced from Kaggle. The data files should be placed in the project directory.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rjsandeepkumawat/spam_classifier.git
   cd spam_classifier
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.x installed. Install the required libraries using pip:
   ```bash
   pip install streamlit scikit-learn nltk pandas
   ```
   
3. **Run the Application**:
   Start the Streamlit web application by running:
   ```bash
   streamlit run app.py
   ```

## Usage

- Open your browser and navigate to the local server address provided by Streamlit (usually `http://localhost:8501`).
- Enter the SMS or email message you want to classify into the text input box.
- Click the "Predict" button to see if the message is classified as "SPAM" or "NOT SPAM".

## Model Details

- **Algorithm**: Multinomial Naive Bayes
- **Library**: scikit-learn
- **NLP Tasks**: Tokenization, stopword removal, stemming (using NLTK)

## Notes

- Ensure that the NLTK resources (`punkt` and `stopwords`) are downloaded before running the application.
- The data used is publicly available on Kaggle and should be appropriately licensed for use.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request with your changes.
