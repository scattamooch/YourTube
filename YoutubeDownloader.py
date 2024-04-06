from pytube import YouTube
import time
import os
import sys

desktop_path = "/mnt/c/Users/Sean/Desktop/YT Downloads"

print("This program will continue asking for download links until the user enters 'quit'. Type 'quit' at any time to close the program.")
time.sleep(3)

while True:

    try: 
        url = input("Enter a YouTube URL: ")

        if url == "quit": 
            break

        #go find the video
        yt = YouTube(url)

        #print the title and author
        print("Title: ", yt.title)
        print("Creator: ", yt.author)

        #get the highest quality available
        yd = yt.streams.get_highest_resolution()

        #download the video
        print("Downloading...")
        yd.download(desktop_path)
        print(f'Download complete. <{yt.title}> downloaded successfully.')

    except Exception as e:
        print("An error occurred", str(e))