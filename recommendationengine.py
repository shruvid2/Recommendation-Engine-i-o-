#Importing libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

#Reading the Files
df=pd.read_csv(r'C:\Users\Admin\Downloads\owncsv.csv')
df=df[['Title','Genre','Ratings']]

#Getting different genres
Genre=[]
for i in df['Genre']:
    i = str(i)
    m = list(i.split(sep=','))
    for j in m:
        Genre.append(j)
Genre=list(set(Genre))
#print(Genre)

#Creating page profile matrix
page_profile_matrix=[]
for i in range(len(df['Title'])):
    page_profile_matrix.append(list())

for i in range(len(df['Title'])):
    for j in range(len(Genre)):
        if Genre[len(Genre)-j-1] in df['Genre'][i]:
            page_profile_matrix[i].append(1)
        else:
            page_profile_matrix[i].append(0)

#computing cosine similarity matrix using sklearn
cosine_sim=cosine_similarity(page_profile_matrix)
#print(cosine_sim)

#Asking user for input of their interest
print('GENRES:','\n','1. science fiction','\n','2.Romance','\n','3.Mysetry','\n','4.detective','\n','5.biography')
print(' 6.Fantasy','\n','7.mythology','\n','8.Thriller','\n','9.Philosophy')
k=int(input("Enter the Genre of your Choice: "))
if k==1:
    m=1
elif k==2:
    m=10
elif k==3:
    m=23
elif k==4:
    m=27
elif k==5:
    m=40
elif k==6:
    m=31
elif k==7:
    m=43
elif k==8:
    m=21
elif k==9:
    m=50

#recommending baesd on cosine similarity
scores_series=pd.Series(cosine_sim[m]).sort_values(ascending=False)
recommended_books_indexes=list(scores_series[0:3].index)
#print(recommended_books_indexes)

#creating a list of recommended books
recommended_books=[]
for i in recommended_books_indexes:
    recommended_books.append(df['Title'][i])
#print(recommended_books)

#creating a list of Ratings
ratings=[]
for r in recommended_books_indexes:
    ratings.append(df['Ratings'][r])
#print(ratings)

#create a zipped list from above lists
zippedlist=list(zip(recommended_books,ratings))

#create a dataframe from zipped list
data1=pd.DataFrame(zippedlist, columns=['Books','Rating'])

#Sorting based on ratings that each book got.
data2=data1.sort_values(by='Rating', ascending=False)

#Printing without showing index values
print(data2.to_string(index=False))