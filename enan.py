from recommender.api import Recommender

recommender = Recommender("9bbf9f05bd0e4bad82e704bd2b68fe79","04a0977a9d9e4488aaa5a18073af7a3c")
recommender.artists = 'EMENIEM'
recommender.genres = [
    'rap',
    'pop',
]
recommender.track_attributes = {
    'danceability': 0.2,
    'name':'Godzilla',
    'albumName': 'Music to Be Murdered By'
}

recommendations = recommender.find_recommendations()

for recommendation in recommendations['tracks']:
    print("%s - %s" % (recommendation['name'], recommendation['artists'][0]['name']))