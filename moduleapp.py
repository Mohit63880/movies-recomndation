import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle


filename='finalized_model.pkl'
vec_matrix = pickle.load(open(filename, 'rb'))
similarity = cosine_similarity(vec_matrix)
# print(loaded_model)
df2=pd.read_csv("newDataSets.csv")

# print(df2.columns)
def movies_list():
    return df2['movie_title']


def recommend_movie(movie):
    for i in df2.movie_title:
        if movie in i:
            movie = i
            i = df2.loc[df2['movie_title']==movie].index[0]
            lst = list(enumerate(similarity[i]))
            lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
            lst = lst[0:10] # excluding first item since it is the requested movie itself
            l = []
            year=[]
            director=[]
            for i in range(len(lst)):
                a = lst[i][0]
                l.append(df2['movie_title'][a])
                year.append(df2['title_year'][a])
                director.append(df2['director_name'][a])
            df3 = pd.DataFrame({'Movies Recommended':l,"director_name":director, 'Year':year})
            df3.drop_duplicates
            return df3
        else:
            return('Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies')
# print(recommend_movie('Avatar'))

