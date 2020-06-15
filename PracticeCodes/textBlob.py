from textblob import TextBlob
line1='That is my Worst watch'
line2='The Car looks Great'
blob1=TextBlob(line1)
blob2=TextBlob(line2)
print(blob1.sentiment)
print(blob2.sentiment)
