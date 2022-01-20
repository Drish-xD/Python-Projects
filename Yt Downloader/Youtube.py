from pytube import YouTube

url = input("enter url")
my_video = YouTube(url)

print(my_video.title)
print(my_video.thumbnail_url)
print(my_video.streams.all)

my_video.streams.first().download()
