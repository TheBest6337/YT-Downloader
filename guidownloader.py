from tkinter import *
import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import BUTTON_TYPE_BROWSE_FILES, BUTTON_TYPE_BROWSE_FOLDER
from pytube import YouTube
import time
import requests
import os

layout = [
    [gui.Text("Yt Downloader", key="video_title")],
    [gui.Text("Bitte gebe den Link zum Downloaden ein: ")],
    [gui.Input("", key="input"), gui.Button("Submit"), gui.Text("", key="error")],
    [gui.Text("Download Type: ")],
    [gui.Button("Mp4", button_color="gray")],
    [gui.Button("Mp3", button_color="gray")],
    [gui.Button("Download"), gui.Button("Download Folder", BUTTON_TYPE_BROWSE_FOLDER)],
    [gui.Text("", key="downloadfolder")],
    [gui.Text("", key="DownloadStatus")]
]

window = gui.Window(title='Yt Downloader', layout=layout, margins=(480, 270))

download_type = ""
download_folder = ""

while True:
    event, values = window.read()
    if event == "Submit":
        try:
            yt = YouTube(values["input"])
            print(str(values["input"]))
            window["Submit"].Update(button_color = "green")
            window["error"].Update("")
            title = yt.title
            window["video_title"].Update(f"Videotitel: {title}")
        except:
            print("Nutze bitte einen GÜLTIGEN YouTube Link!")
            window["error"].Update("Nutze bitte einen GÜLTIGEN YouTube Link!")
            window["Submit"].Update(button_color = "red")
    elif event == "Mp4":
        window["Mp4"].Update(button_color = "black")
        window["Mp3"].Update(button_color = "gray")
        download_type = "mp4"
    elif event == "Mp3":
        window["Mp3"].Update(button_color = "black")
        window["Mp4"].Update(button_color = "gray")
        download_type = "mp3"

    if event == "Download":
        download_folder = values["Download Folder"]
        if download_folder == "":
            window["DownloadStatus"].Update("Bitte Wähle einen Downloadordner aus!", text_color="red")
            print("Kein Download Ordner ausgewählt")
            break
        else:
            window["downloadfolder"].Update(f"Download Folder: {download_folder}")
            
        if not str(values["input"]):
            window["DownloadStatus"].Update("Bitte Wähle alles RICHTIG aus!", text_color="red")
            print("Kein Download Typ ausgewählt")
            break
        if download_type == "":
            window["DownloadStatus"].Update("Bitte Wähle alles RICHTIG aus!", text_color="red")
            print("Kein Download Typ ausgewählt")
            break
        if download_type == "mp3":
            window["DownloadStatus"].Update("Mp3 wird gedownloaded")
            ys = yt.streams.get_audio_only() 
            ys.download(download_folder)
            window["DownloadStatus"].Update("Download Complete!")
        elif download_type == "mp4":
            window["DownloadStatus"].Update("Mp4 wird gedownloaded")
            ys = yt.streams.get_highest_resolution()
            ys.download(download_folder)
            window["DownloadStatus"].Update("Download Complete!")
    if event == gui.WIN_CLOSED:
        break

event, values = window.read()
print()
window.close()
