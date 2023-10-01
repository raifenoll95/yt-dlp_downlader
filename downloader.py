from __future__ import unicode_literals
import yt_dlp
import os

url = input("URL de la cancion a descargar >>")

#Parametros del comando
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '320'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': True
}

#Nos cambiamos de directorio para descargar
os.chdir('D:/Música')

#Aqui se descarga
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download({url})


