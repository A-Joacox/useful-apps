from moviepy.editor import VideoFileClip #in console: pip install moviepy


def extraer_audio_mp3(file_mp4, file_mp3):
    video = VideoFileClip(file_mp4)
    audio = video.audio
    audio.write_audiofile(file_mp3)

file_mp4 = ("name_video.mp4") #path or file name
file_mp3 = ("name_audio.mp3") # e.g., '/path/to/download/folder'

extraer_audio_mp3(file_mp4, file_mp3)
