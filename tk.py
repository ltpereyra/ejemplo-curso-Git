import tkinter as tk
from tkinter import filedialog
from tkinter import *
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

ventana = tk.Tk()
ventana.geometry("300x300")

## Titulo de la ventana
titulo = tk.Label(ventana, text = "Video Cutter", bg = "light blue")
titulo.grid(row=0, column=3)

## Caja de texto para ruta
def browse_button():
    video_in = filedialog.askopenfilename()
    print(video_in)

text1 = tk.Label(ventana, text="Ingrese el video")
text1.grid(row=1, column=0)
cajatext = tk.Entry(ventana)
cajatext.grid(row=1, column=1)

button2 = Button(text="Browse", command=browse_button())
button2.grid(row=1, column=3)

## Caja de texto para salida
def output_button():
    video_out = filedialog.askdirectory()
    print(video_out)

text2 = tk.Label(ventana, text="Ruta de salida")
text2.grid(row=2, column=0)
cajatext2 = tk.Entry(ventana)
cajatext2.grid(row=2, column=1)

button3 = Button(text="Output", command=output_button())
button3.grid(row=2, column=3)

## Tiempos
text3 = tk.Label(ventana, text="Inicio (segundos)")
text3.grid(row=3, column=0)
desde = tk.Entry(ventana)
desde.grid(row=3, column=1)

text4 = tk.Label(ventana, text="Fin (segundos)")
text4.grid(row=4, column=0)
hasta = tk.Entry(ventana)
hasta.grid(row=4, column=1)

## Cutter
def cutter():
    clip = VideoFileClip(browse_button()).subclip(desde, hasta)
    clip.write_videofile(output_button())

## Boton enter!
boton1 = tk.Button(ventana, text="Cortar", command =cutter())
boton1.grid(row=4, column=1)

ventana.mainloop()