import os
import pickle


from catboost import CatBoostClassifier
from nltk.stem import WordNetLemmatizer
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


class Interactor:
    def __init__(self, models_path: str):
        """
        Initializes the Models object.

        Args:
            models_path (str): Path to the folder containing the models.
                               All models must begin with "model_".
        """
        self.models = dict()
        self.load_models(models_path)
        self.lemmatizer = WordNetLemmatizer()

    def load_models(self, models_path: str):
        """
        Load all models from the specified path and store them in the self.models dictionary.

        Args:
            models_path (str): Path to the folder containing the models.
                               All models must begin with "model_".
        """
        model_files = [
            file for file in os.listdir(models_path)
            if os.path.isfile(os.path.join(models_path, file)) and file.startswith("model_")
        ]

        for model_file in model_files:
            # Each model file is expected to have the format "model_<name>"
            model_name = model_file[6:]  # Extracting the model name after "model_"
            match model_name:
                case "catboost":
                    with open(f"models/model_{model_name}", 'rb') as file:
                        model: CatBoostClassifier = pickle.load(file)
                        self.models["catboost"] = model
                case "vectorizer":
                    with open(f"models/model_{model_name}", 'rb') as file:
                        bow: CountVectorizer = pickle.load(file)
                        self.models["vectorizer"] = bow
                case "randomforest":
                    with open(f"models/model_{model_name}", 'rb') as file:
                        rf: RandomForestClassifier = pickle.load(file)
                        self.models["randomforest"] = rf
                case "logisticregression":
                    with open(f"models/model_{model_name}", 'rb') as file:
                        lr: LogisticRegression = pickle.load(file)
                        self.models["logisticregression"] = lr
                case _:
                    print(f"Unknown model: {model_name}")

    def predict(self, model_name: str, sentence: str):
        """
        Make a prediction using the specified model for the given sentence.

        Args:
            model_name (str): The name of the model to use for prediction.
            sentence (str): The input sentence to be predicted.

        Returns:
            numpy.ndarray: The prediction result from the model.
        """
        vectorizer = self.models["vectorizer"]
        model = self.models[model_name]
        sentence = self._lemmatize([sentence])
        sentence_vectorized = vectorizer.transform(sentence)
        return model.predict(sentence_vectorized)

    def _lemmatize(self, texts):
        """
        Lemmatize the input text(s).

        Args:
            texts (iterable): An iterable containing text(s) to be lemmatized.

        Returns:
            numpy.ndarray: An array of lemmatized text(s).
        """
        lemmatized_texts = map(lambda text: ' '.join([self.lemmatizer.lemmatize(word.lower()) for word in text.split()]), texts)
        return np.array(list(lemmatized_texts))
