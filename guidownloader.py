import PySimpleGUI as os
from PySimpleGUI.PySimpleGUI import BUTTON_TYPE_BROWSE_FOLDER
from pytube import YouTube

layout = [
    [os.Text("YouTube Downloader", key="video_title")],
    [os.Text("Please enter a YouTube link: ")],
    [os.Input("", key="input"), os.Button("Submit"), os.Text("", key="error")],
    [os.Text("Download Type: ")],
    [os.Button("Mp4", button_color="gray")],
    [os.Button("Mp3", button_color="gray")],
    [os.Button("Download"), os.Button("Download Folder", BUTTON_TYPE_BROWSE_FOLDER)],
    [os.Text("", key="downloadfolder")],
    [os.Text("", key="DownloadStatus")]
]

window = os.Window(title='Yt Downloader', layout=layout, margins=(480, 270))

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
            window["video_title"].Update(f"Videotitle: {title}")
        except:
            print("Please use a VALID YouTube link!")
            window["error"].Update("Please use a VALID YouTube link!")
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
            window["DownloadStatus"].Update("Please select a download folder!", text_color="red")
            print("No download folder selected")
            break
        window["downloadfolder"].Update(f"Download Folder: {download_folder}")
        if not str(values["input"]):
            window["DownloadStatus"].Update("Please select everything CORRECTLY!", text_color="red")
            print("No download type selected")
            break
        if download_type == "":
            window["DownloadStatus"].Update("Please select everything CORRECTLY!", text_color="red")
            print("No download type selected")
            break
        if download_type == "mp3":
            window["DownloadStatus"].Update("Mp3 will be downloaded")
            ys = yt.streams.get_audio_only() 
            ys.download(download_folder)
            window["DownloadStatus"].Update("Download Complete!")
        elif download_type == "mp4":
            window["DownloadStatus"].Update("Mp4 will be downloaded")
            ys = yt.streams.get_highest_resolution()
            ys.download(download_folder)
            window["DownloadStatus"].Update("Download Complete!")
    if event == os.WIN_CLOSED:
        break

event, values = window.read()
print()
window.close()
