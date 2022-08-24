from textblob import TextBlob

blob=TextBlob("comment vas-tu")

print(blob.detect_language())

print(blob.tranlate(to='en'))
print(blob.translate(to='es'))