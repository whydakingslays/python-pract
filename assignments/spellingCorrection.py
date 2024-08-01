from textblob import TextBlob
def Convert(string):
    li = list(string.split())
    return li

str1 = input('Enter your word : ')
words = Convert(str1)
corectedWords = []
for i in words: 
    corectedWords.append(TextBlob(i))
print("Wrong words : ", words)

for i in corectedWords:
    print("Corrected words are : ",i.correct())
    
    