from flask import Flask, render_template, request, jsonify
from moduleapp import recommend_movie, movies_list


app=Flask(__name__)

movies_lst=movies_list()

@app.route("/")
def home():
    return render_template('index.html',key="NO",movies_list=movies_lst)
# print(recommend_movie("Towering"))

@app.route("/movies",methods=["POST"])
def movies():
    movie=request.form.get("Movie_Name")
    df=recommend_movie(movie)
    # print(movie,df)
    if type(df)==str:
        return render_template('index.html',data=df,key="NO")
        
    headers=['Movies Recommended',"Director",'Year']
    Movies=[]
    director_name=[]
    Year=[]
    for j in range(10):
        Movies.append((df['Movies Recommended'][j],df['director_name'][j],df['Year'][j]))
        
    # print(Movies)
    return render_template('index.html'
    ,headers=headers,Movies=Movies,key="Yes",movies_list=movies_lst
    )


if __name__ == "__main__":
    app.run(debug=True)  
