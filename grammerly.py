from textblob import TextBlob
while True:
 a= TextBlob(input("Please enter here:-"))
 a=a.correct()
 print(a)
 b=input("Press Y or N :")
 if b=="y":
    quit()
 elif b=='n':
    c=input("Please enter again:")
    