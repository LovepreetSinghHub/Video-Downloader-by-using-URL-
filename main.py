# Lovepreet Singh ~ 21.05.2022

from pytube import YouTube
#Variables
link = input("Enter the link of YouTube video you want to download:  ")
YT = YouTube(link)
#details of the Video
print("Title: ",YT.title)
print("Number of views: ",YT.views)
print("Length of video: ",YT.length)
print("Rating of video: ",YT.rating)
print("-------------------------------")
# Video Downloader
Video = YT.streams.get_highest_resolution()
print("Downloading...")
Video.download()
print("Download completed!!")

