from youtube_dl import YoutubeDL
import re

yt_regex = re.compile(r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$")

ytdlopts = {
    'outtmpl': './downloads/%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': False,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpegopts = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -cwix -reconnect_delay_max 5',
    'options': '-vn'
}

ytdl = YoutubeDL(ytdlopts)

def url_checker(url):
    url_check = yt_regex.findall(url)
    value = 0
    try:
        for k in url_check[0]:
            if "list" in k or "&list" in k:
                value += 1
    except IndexError:
        return False
        
    if value > 1:
        return True
        
    if value < 1 or value == 1:
        return False

def yt_search(download=True):
    search = str(input("Input a search query: "))
    while True:
        if url_checker(search) is True:
            data = ytdl.extract_info(url=search, download=download)
            total = 0
            for data in data['entries']:
                file = ytdl.prepare_filename(data)
                total += 1
            
            return print(str(total) + " Video downloaded.")

        if url_checker(search) is False:
            file = ytdl.prepare_filename(ytdl.extract_info(url=search, download=download)['entries'][0])
            return print("Video downloaded.")

if __name__ == "__main__":
    yt_search()
