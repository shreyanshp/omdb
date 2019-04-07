import requests
import os
import argparse

parser = argparse.ArgumentParser(description='omdb')
parser.add_argument('--movie', default=os.environ.get('movie', "mad max"))
parser.add_argument('--key')
args = parser.parse_args()
if not args.key:
    exit(parser.print_usage())
else:
    r = requests.get('http://www.omdbapi.com/?t='+args.movie+'&apikey='+args.key)
    if r.status_code == 200:
        rotten = r.json()
        if 'Ratings' not in rotten:
            print 'Sorry, either your movie does not exists or there is a typo in your input'
        else:
            for rating in rotten.get('Ratings'):
                if rating['Source'] == 'Rotten Tomatoes':
                    print 'Rotten Tomatoes rating for the movie - "'+args.movie+'" is '+rating['Value']
                    quit()
            print 'Sorry, your movie is not cataloged in Rotten Tomatoes'
    else:
        print 'Invalid Key, please enter valid Key from OMDB'