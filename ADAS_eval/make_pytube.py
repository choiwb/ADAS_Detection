from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=Wu0s7xZsgfI').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=Wu0s7xZsgfI')
yt.streams.all()
