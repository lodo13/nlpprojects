"""program will calculate the similarity between a group of movies and planet hulk movie"""

#importing module and dictionary
import spacy
nlp = spacy.load("en_core_web_md")

#planet hulk movie description, to compare other titles in movies
planethulk = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

#lists 
movies = []
movielist = []
similar_list = []
end_list = []

def similar(movie, description):
    """the function calculates the similarity between movies and planet hulk"""
    similarity = nlp(description).similarity(planethulk)
    movielist.append(movie)
    similar_list.append(similarity)
    check = f"{movie},{similarity}"
    check = check.split(",")
    end_list.append(check)
    high_sim = str(max(similar_list))

    for line in end_list:
        if high_sim in line:
            suggested_movie = line[0]

    for line in movies:
        if suggested_movie in line:
            result = (f"""
       
Because you watched Planet Hulk, you may like this movie: 
        
{suggested_movie}: {line[1]}
""")
    return result

#extracting movies list from the file
with open ("movies.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        line = line.split(":")
        movies.append(line)

for line in movies:
    result = similar(line[0], line[1])

print (result)