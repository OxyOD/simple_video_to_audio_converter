# module
from moviepy.editor import VideoFileClip

#filename of video you want to work with
videofile= input("Enter video filename: ")

# Loads video file and extracts audio from it
# VideoFileClip [ loads the file ] and .audio [ extracts the audio ]
audio_clip= VideoFileClip(videofile).audio

# write the audio extracted to another file
audio_file = input("mp3 filename you wish to create: ")
audio_clip.write_audiofile(audio_file)

# Close the audio clip
# must do this in order to free up system resources
audio_clip.close()

print("Audio extraction successful!")