import pytube
from pytube import YouTube
import customtkinter
import tkinter

#theme and color options/basic sizing
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#root
root = customtkinter.CTk()
root.geometry("600x400")
root.title("YourTube")

# logic
desktop_path = "/mnt/c/Users/Sean/Desktop/YT Downloads"

def start_download():
        
    try:
        # progress_bar.start()

        url = link_field.get()

        #go find the video
        yt = YouTube(url)

        #print the title and author
        progress_label.configure(text="Download complete.")
        title_label.configure(text = f"Title: {yt.title}")
        creator_label.configure(text = f"Creator: {yt.author}")

        #get the highest quality available
        yd = yt.streams.get_highest_resolution()

        #download the video
        yd.download(desktop_path)

    except Exception as e:
        print("An error occurred", str(e))

    # finally:
        # progress_bar.stop()

#define widgets
intro_label = customtkinter.CTkLabel(root, 
                                     text="Desktop YouTube Downloader",
                                     font = ("Times New Roman", 30, "bold"))

path_field = customtkinter.CTkEntry(root, 
                                    width = 250, 
                                    height = 50, 
                                    corner_radius = 10, 
                                    placeholder_text = "Choose download location")

link_field = customtkinter.CTkEntry(root, 
                                    width = 250, 
                                    height = 50, 
                                    corner_radius = 10, 
                                    placeholder_text = "Paste link to download")

# progress_bar = customtkinter.CTkProgressBar(root, 
#                                             corner_radius = 10,
#                                             mode = "indeterminate",)

progress_label = customtkinter.CTkLabel(root,
                                        text="")

title_label = customtkinter.CTkLabel(root, 
                                     text="",)

creator_label = customtkinter.CTkLabel(root, 
                                     text="",)

download_button = customtkinter.CTkButton(root,
                                          height = 65, 
                                          text = "Download",
                                          command = start_download)

#call widgets
intro_label.pack(pady=20)
link_field.pack()
# path_field.pack(pady=5)
# progress_bar.pack(pady=10)
progress_label.pack(pady=10)
title_label.pack()
creator_label.pack()
download_button.pack(pady=30)


root.mainloop()
# Code in the venv! pipenv shell
# https://pytube.io/en/latest/index.html
# https://customtkinter.tomschimansky.com/documentation/