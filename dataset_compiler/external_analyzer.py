import json

from textblob import TextBlob

with open('comments.json', 'r', encoding='utf-8') as file:
    comments = json.load(file)

classes = []

for comment in comments:
    blob = TextBlob(comment)

    polarity = blob.sentiment.polarity

    if polarity < -0.1:
        classes.append(-1)
    elif polarity > 0.1:
        classes.append(1)
    else:
        classes.append(0)

with open('comments_processed.json', 'w', encoding='utf-8') as file:
    json.dump(list(zip(comments, classes)), file, ensure_ascii=False, indent=4)
