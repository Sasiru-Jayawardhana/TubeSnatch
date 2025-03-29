from tkinter import *
from tkinter import ttk  # Import ttk for Combobox
from youtube_downloader import download_video  # Import the download function
from youtube_downloader import get_available_qualities  # Import the function to fetch qualities
import threading  # Import threading for running tasks in the background
import os  # Import os for opening the downloads directory

root = Tk()

root.title("Youtube Video Downloader")
root.geometry("600x300")
root.config(bg="black")

mainLabel = Label(root, text="Youtube Video Downloader", font="Arial 20 bold", fg="white", bg="black")
mainLabel.grid(row=0, column=1, pady=20)

lbl = Label(root, text="Enter the URL:", font="Arial 12 bold", fg="white", bg="black")
lbl.grid(row=1, column=0)

txt = Entry(root, width=50)
txt.grid(row=1, column=1)

quality_lbl = Label(root, text="Select Quality:", font="Arial 12 bold", fg="white", bg="black")
quality_lbl.grid(row=2, column=0)

# Add a Combobox for quality selection
quality_dropdown = ttk.Combobox(root, width=20, state="readonly")
quality_dropdown.grid(row=2, column=1)

status_lbl = Label(root, text="", font="Arial 12 bold", fg="white", bg="black")
status_lbl.grid(row=5, column=1)


def fetch_qualities():
    """Fetch available qualities for the given URL."""
    url = txt.get()
    if not url:
        status_lbl.config(text="Please enter a URL.", fg="red")
        return

    status_lbl.config(text="Fetching qualities...", fg="yellow")
    root.update_idletasks()

    try:
        # Fetch available qualities from youtube_downloader.py
        qualities = get_available_qualities(url)
        if qualities:
            quality_dropdown['values'] = qualities  # Populate the dropdown
            quality_dropdown.current(0)  # Set the first quality as default
            status_lbl.config(text="Qualities fetched successfully!", fg="green")
        else:
            status_lbl.config(text="No qualities available for this video.", fg="red")
    except Exception as e:
        status_lbl.config(text=f"Error: {str(e)}", fg="red")


def start_download():
    """Start the download process in a separate thread."""
    url = txt.get()
    quality = quality_dropdown.get()
    if not url:
        status_lbl.config(text="Please enter a URL.", fg="red")
        return

    if not quality:
        status_lbl.config(text="Please select a quality.", fg="red")
        return

    # Update the status label to show "Processing..."
    status_lbl.config(text="Processing...", fg="yellow")
    root.update_idletasks()

    # Run the download in a separate thread
    threading.Thread(target=download_video_thread, args=(url, quality)).start()


def download_video_thread(url, quality):
    """Run the download_video function in a separate thread."""
    try:
        # Call the download function
        download_video(url, preferred_quality=quality, output_path='downloads')
        # Update the status label on success
        status_lbl.config(text="Download completed successfully!", fg="green")
    except Exception as e:
        # Update the status label on error
        status_lbl.config(text=f"Error: {str(e)}", fg="red")


def open_downloads_directory():
    """Open the downloads directory."""
    try:
        os.startfile('downloads')  # Open the downloads folder
    except Exception as e:
        status_lbl.config(text=f"Error: {str(e)}", fg="red")


# Add buttons for fetching qualities, downloading, and opening downloads directory
fetch_btn = Button(root, text="Fetch Qualities", fg="white", font="Arial 10 bold", bg="blue", command=fetch_qualities)
fetch_btn.grid(row=4, column=0, pady=30)

open_dir_btn = Button(root, text="Open Downloads", fg="white", font="Arial 10 bold", bg="purple", command=open_downloads_directory)
open_dir_btn.grid(row=4, column=1, pady=30)

btn = Button(root, text="Download", fg="white", font="Arial 10 bold", bg="green", command=start_download)
btn.grid(row=4, column=2, pady=40)

root.mainloop()