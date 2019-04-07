# omdb

## To run locally, install python (tested on 2.7+), clone the repo, and run the following commands from inside the directory

### Case 1 - When movie exists and its data in Rotten Tomatoes also exists

`python omdb.py --movie 'mad max' --key <your-OMDB-key>`

`Rotten Tomatoes rating for the movie - "mad max" is 90%`

### Case 2 - When movies exists, but its data in Rotten Tomatoes does not exist

`python omdb.py --movie 'ja' --key <your-OMDB-key>`

`Sorry, your movie is not cataloged in Rotten Tomatoes`

### Case 3 - When movies does not exists

`python omdb.py --movie 'mzzx' --key <your-OMDB-key>`

`Sorry, either your movie does not exists or there is a typo in your input`

## To run without any setup, use the Docker image deployed to Docker Hub, it's open and free for all

`docker pull shreyanshr/omdb && docker run -it --rm shreyanshr/omdb omdb.py --movie 'mad max' --key <your-OMDB-key>`

##### You can use environment variables to pass movie and key

`docker pull shreyanshr/omdb && docker run -it --rm -e movie='mad max' -e key='<your-OMDB-key>' shreyanshr/omdb omdb.py`

###### Well, if you're bored of mad max, you can watch Tron
`docker pull shreyanshr/omdb && docker run -it --rm -e movie='tron' shreyanshr/omdb omdb.py --key <your-OMDB-key>`
