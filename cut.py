from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

print("Ingrese ruta de archivo: ")
video = str(input())
print("Ingrese nombre nuevo: ")
output = str(input())
print("Desde (segundos): ")
desde = input()
print("Hasta (segundos): ")
hasta = input()

clip = VideoFileClip("C:/Users/ltper/Videos/Radeon ReLive/unknown/unknown_replay_2021.05.05-19.45.mp4").subclip(85, 180)
clip.write_videofile("C:/Users/ltper/Videos/Radeon ReLive/unknown/output.mp4")
