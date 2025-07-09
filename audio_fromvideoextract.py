#To extract audio from video. Use pip install moviepy
import moviepy.editor
cvt_video = moviepy.editor.VideoFileClip(".3gpp")
ext_audio = cvt_video.audio
ext_audio.write_audiofile("audio_Extacted.mp3")