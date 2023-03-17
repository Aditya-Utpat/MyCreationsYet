Retrieving, analyzing and visualizing YouTube video and channel data from YouTube data API

This project is a fairly simple project. Its structure an be understood by having a look at the provided
image file.

To run the project on your own system you will need -
1. Python 3
2. API key
3. bokeh package

to get API key -
https://console.cloud.google.com/apis/library/youtube.googleapis.com
you will need your google account for this

the visualization process requires a python module named bokeh.
to install bokeh on your system use command to install it ( installs into python ) -

python -m pip install bokeh (tested on windows)

step 1
fetch.py

you will need to paste your API key in the variable to run this.
on running it will create a database file named youtube_data.sqlite
then it will ask for a channel name and no. of videos to retrieve (limit for videos: 50)
if the channel name is valid and not in database it will produce this output-


Enter channel name:danooct1
How many videos to retrive5
retrived https://www.googleapis.com/youtube/v3/channels?key=....&part=statistics%2Csnippet&forUsername=danooct1
Retrieved channel info
retrived https://www.googleapis.com/youtube/v3/activities?key=....&part=snippet&maxResults=5&channelId=UCqbkm47qBxDj-P3lI9voIAw
retrived recent activity len 5
https://www.googleapis.com/youtube/v3/videos?key=....&part=statistics%2Csnippet&id=y_goHl-GuNk
https://www.googleapis.com/youtube/v3/videos?key=....&part=statistics%2Csnippet&id=S3PB9Zx13j0
https://www.googleapis.com/youtube/v3/videos?key=....&part=statistics%2Csnippet&id=M4EVjQclnc8
https://www.googleapis.com/youtube/v3/videos?key=....&part=statistics%2Csnippet&id=M4EVjQclnc8
https://www.googleapis.com/youtube/v3/videos?key=....&part=statistics%2Csnippet&id=whl09IIG_S8
retrived video info

the ids at the end stand for the channelId or the videoId accordingly
it retrieves the following data points-

video_id TEXT,
title TEXT,
likes INTEGER,
dislikes INTEGER,
views INTEGER,
date DATE,
channel_id INTEGER

id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
youtubeid TEXT,
name TEXT,
subscribers INTEGER,
videocount INTEGER,
category TEXT,
retrieved_at DATE

you can go to the following link and understand about URLs and working of API-
https://developers.google.com/youtube/v3/docs/

here is a sample JSON that we get from accessing video data-

{
  "kind": "youtube#videoListResponse",
  "etag": "d8rXL...z5L3CMtOISpF6V4",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "m_a2AXI...VgogwwpIoBjOkKdQ",
      "id": "y_goHl-GuNk",
      "snippet": {
        "publishedAt": "2011-09-17T09:27:28Z",
        "channelId": "UCD9fMVm4yPFv63goCFEj9jQ",
        "title": "Francisco Tárrega - Capricho árabe",
        "description": "Francisco de Asís Tárrega y Eixea (21 November 1852 - 15 December 1909) was an influential Spanish composer and guitarist of the Romantic period.\r\n\r\nGuitar: David Russell",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/y_goHl-GuNk/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/y_goHl-GuNk/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/y_goHl-GuNk/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/y_goHl-GuNk/sddefault.jpg",
            "width": 640,
            "height": 480
          }
        },
        "channelTitle": "Fledermaus1990",
        "tags": [
          "Francisco",
          "Tárrega",
          "Tarrega",
          "Capricho",
          "árabe",
          "Arab",
          "Capriccio",
          "classical music",
          "Classical",
          "Music",
          "Spain",
          "Guitar"
        ],
        "categoryId": "10",
        "liveBroadcastContent": "none",
        "localized": {
          "title": "Francisco Tárrega - Capricho árabe",
          "description": "Francisco de Asís Tárrega y Eixea (21 November 1852 - 15 December 1909) was an influential Spanish composer and guitarist of the Romantic period.\r\n\r\nGuitar: David Russell"
        }
      },
      "statistics": {
        "viewCount": "24504558",
        "likeCount": "350821",
        "dislikeCount": "3533",
        "favoriteCount": "0",
        "commentCount": "7598"
      }
    }
  ],
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 1
  }
}

step2
analysis.py

this creates simple analysis from the data and prints it out
sample output-

video stats
Most viewed video of all :
Francisco Tárrega - Capricho árabe   ===   24503467 views   ===   danooct1

Most liked video of all :
Francisco Tárrega - Capricho árabe   ===   350800 likes   ===    danooct1

Most disliked video of all :
Francisco Tárrega - Capricho árabe    ===    3533 dislikes   ===   danooct1

Oldest video of all :
Francisco Tárrega - Capricho árabe    ===    2011-09-17   ===   danooct1

channel with most subscribers:
Linus Tech Tips===   subscribers   ===   12900000

channel with most videocount:
Linus Tech Tips===   videos   ===   5246

step 3
graph.py

this creates a visualization in a html file named 'graph.html'
the file will be automatically opened
to learn more about bokeh visit www.bokeh.com

-- created by Aditya Utpat
