import streamlit as st
from pytube import YouTube

def download_youtube_video(video_url, download_path):
    try:
        yt = YouTube(video_url)
        st.write(f"Downloading {yt.title}...")
        yt.streams.get_highest_resolution().download(download_path)
        st.success("Download complete!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def main():
    st.title("YouTube Video Downloader")

    # Input field for the user to enter the YouTube video URL
    video_url = st.text_input("Enter the YouTube video URL:")

    if st.button("Download"):
        if video_url:
            download_youtube_video(video_url, "downloads")
        else:
            st.warning("Please enter a YouTube video URL.")

if __name__ == "__main__":
    main()
