
# We train a simple text classifier using:
#   - TfidfVectorizer: converts text into numbers
#   - MultinomialNB: a fast and simple text classification algorithm
# Labels: 1 = Positive, 0 = Negative, 2 = Neutral

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# ---- TRAINING DATA ----

positive_reviews = [
    "Excellent product, highly recommended",
    "Best purchase ever",
    "Amazing quality",
    "Very satisfied",
    "Works perfectly",
    "Great value for money",
    "Love this product",
    "Super fast delivery",
    "Outstanding performance",
    "Exceeded my expectations",
    "Worth every penny",
    "Five stars",
]

negative_reviews = [
    "Terrible quality, broke in 2 days",
    "Worst product ever",
    "Complete waste of money",
    "Very disappointed",
    "Don't buy this",
    "Poor build quality",
    "Cheap materials",
    "Not worth the price",
    "Arrived damaged",
    "False advertising",
    "Useless product",
    "Never again",
]

neutral_reviews = [
    "It's okay for the price",
    "Average product",
    "Nothing special",
    "Works but has issues",
    "Decent but overpriced",
    "Good but not great",
    "Could be better",
    "Fine for temporary use",
]

# Combine all reviews and labels
texts = positive_reviews + negative_reviews + neutral_reviews
labels = [1] * len(positive_reviews) + [0] * len(negative_reviews) + [2] * len(neutral_reviews)

# ---- VECTORIZE TEXT ----
# TfidfVectorizer converts sentences to numerical feature vectors
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(texts)

# ---- TRAIN MODEL ----
# MultinomialNB is well-suited for text classification with word counts
model = MultinomialNB()
model.fit(X, labels)

# ---- EVALUATE ----
predictions = model.predict(X)
accuracy = accuracy_score(labels, predictions)
print(f"Training Accuracy: {accuracy * 100:.2f}%")

# ---- SAVE MODEL AND VECTORIZER ----
# We save both so the API can load and use them without retraining
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved as model.pkl and vectorizer.pkl")