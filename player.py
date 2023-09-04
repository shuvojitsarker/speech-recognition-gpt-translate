import play_file as play_file
import re
import vlc


#Find URL
def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]

def palyVideo(url):
    video = play_file.pafy_search(url)
    # getting stream at index 0
    best = video.getbest()

    # creating vlc media player object
    media = vlc.MediaPlayer(best.url)

    # start playing video
    media.play()

    while True:
        pass