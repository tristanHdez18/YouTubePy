from flask import Blueprint, render_template, request, send_file, redirect
from subprocess import call, check_output
import youtube_dl
import os
from werkzeug.utils import secure_filename


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/converting_video', methods=['POST', 'GET'])
def converting_video():
    video_url = request.form.get('url', type=str)
    if video_url == "":
        return redirect("/")

    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(etx)s',
        'quiet': False
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    
    for root, dirs, files in os.walk("/"):
        if str(filename) in files:
            newpath = os.path.join(root, str(filename))
    
    print("Download complete... {}".format(filename))
    print("fname: " + str(filename))
    return send_file(newpath,
                     attachment_filename=filename,
                     as_attachment=True)
