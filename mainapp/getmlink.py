


import urllib.request
import re
import sys
import youtube_dl
import requests


def getlink(str):
	search_keyword = urllib.parse.quote(str)
	html = requests.get("https://www.youtube.com/results?search_query=" + search_keyword)

	print(search_keyword)

	video_ids = re.findall(r"watch\?v=(\S{11})", html.text)

	print("The video ids are : ",video_ids)

	url = "https://www.youtube.com/watch?v=" + video_ids[0]

	print("Selected youtube url is ", url)

	ydl_opts = {
	    'format': 'bestaudio/best',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	}

	r = youtube_dl.YoutubeDL(ydl_opts)
	
	info = r.extract_info(url, download = False)

	return info['url']

