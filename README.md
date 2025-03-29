# YouTube Video Downloader

A simple and user-friendly YouTube video downloader built with Python and Tkinter. This application allows users to download YouTube videos in their preferred quality with just a few clicks.

## Features

- **Graphical User Interface (GUI):** Built with Tkinter for an intuitive and responsive user experience.
- **Quality Selection:** Fetch and display available video qualities for the provided YouTube URL.
- **Multithreaded Downloads:** Downloads run in the background to keep the application responsive.
- **Open Downloads Folder:** Quickly access the downloaded videos with a single button click.

## How It Works

1. Enter the YouTube video URL in the input field.
2. Click the "Fetch Qualities" button to retrieve available video qualities.
3. Select the desired quality from the dropdown menu.
4. Click the "Download" button to start downloading the video.
5. Use the "Open Downloads" button to access the downloaded videos.

## Requirements

- Python 3.x
- Required Python libraries:
  - `tkinter`
  - `threading`
  - Custom module: `youtube_downloader` (must include `download_video` and `get_available_qualities` functions)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/yt-video-downloader.git
   cd yt-video-downloader
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python GUI.py
   ```

## Folder Structure

- GUI.py: Main application file with the Tkinter GUI.
- `youtube_downloader.py`: Module for handling video downloads and fetching qualities.
- `downloads/`: Directory where downloaded videos are saved.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.
