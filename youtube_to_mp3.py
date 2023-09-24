from pytube import YouTube

youtube_url = input("Enter your YouTube URL: ")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    num_equals = int(percentage) // 2
    num_spaces = 50 - num_equals if percentage < 100 else 0
    print(f"\rDownloading: [{int(percentage)}% {'=' * num_equals}{' ' * num_spaces}]", end='')

def on_complete(stream, file_handle):
    print(f"\nFile saved as: {file_handle.name}")
    input("Press any key to exit")

video = YouTube(youtube_url, on_progress_callback=on_progress)
stream = video.streams.get_audio_only()
print(f"\nVideo: {video.title}")
downloaded_file = stream.download(filename=stream.title + ".mp3")

# Call the on_complete callback with the file handle
on_complete(stream, open(downloaded_file, "wb"))
