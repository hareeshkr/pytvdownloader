import tkinter as tk
from pytube import YouTube

root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("600x300")

yt_link = tk.StringVar()
yt_res = tk.StringVar()

def yt_download():
    video = YouTube(yt_link.get()).streams.filter(res=yt_res.get()).first()
    video.download("/home/hareesh/Downloads/")

tk.Label(root, text="Enter the Link:").pack()
tk.Entry(root, textvariable = yt_link).pack()

tk.Radiobutton(root, text="Standard", variable= yt_res, value="360p").pack()
tk.Radiobutton(root, text="HD", variable= yt_res, value="720p").pack()
tk.Radiobutton(root, text="FullHD", variable= yt_res, value="1080p").pack()

tk.Button(root, text="Download", command= yt_download).pack()


root.mainloop() 
