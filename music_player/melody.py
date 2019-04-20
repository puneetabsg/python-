# (ctrl + alt + l) = for automatic formatted line for neat and clean code.
# we are importing  os module because this module only to show file name not path of file in bottom fo our Melody window.
import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import *

root = Tk()  # root is our variable where we are storing our windows that Tk() of tkinter

# creating  menu-bar
menubar = Menu(root)
root.config(menu=menubar)  # need to config because 1)it makes to stick menubar at the top at any condition.
# 2) makes it ready for sub menubar always
# creating sub-menu in menu-bar
submenu = Menu(menubar, tearoff=0)


def browse_file():  # this is browse option for other file selection.
    global filename  # this is for showing name of music file in our melody media player.
    filename = filedialog.askopenfilename()
    print(filename)


menubar.add_cascade(label="file", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit",
                    command=root.destroy)  # the root.destroy command go to root=Tk() and shutdown the window.


def about_us():
    tkinter.messagebox.showinfo("About Melody",
                                "Hi there ! Iam Puneet and this is my first project using tkinter Hope you like It.")


submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="help", menu=submenu)
submenu.add_command(label="About Us", command=about_us)

mixer.init()  # initializing mixer

# root.geometry("300x300")  # it is our windows size ,we can change it later on also
root.title("Melody")  # this is the title of our windows ie: Melody
root.iconbitmap(r"images/melody.ico")  # here python only supports (.ico) format
# so we can download any format ie: png,jpg,jpeg etc.
# but we have to convert that into .ico format ....& i know how to do it.


filelabel = Label(root, text="let's make some noise")  # everything which appears in window is widget.
# for that we have Label() fun.
# consists two parameter-1)where this widgets go.
# 2)text for the widgets.

filelabel.pack(pady=20)  # it will wind up Label() in text format.

# pady means padding in y direction.
# similarly padx means padding in x direction.

# playphoto=PhotoImage(file="play-button.png") # here PhotoImage is a type of label but----main container is Label()
# so our photo contains name of file.
# Labelphoto=Label(root,image=photo) # again using our container ie; Label()
# LabelPhoto again contains 2 paramaetrs 1)location of photo, 2)name of thing defined earlier ie:photo
# here LabelPhoto is just a variable.
# Labelphoto.pack()
lengthlabel = Label(root, text="Total Length : --:--")
lengthlabel.pack()


def show_details():
    filelabel["text"] = "Playing" + "-" + os.path.basename(filename)

    a = mixer.Sound(filename)
    total_length = a.get_length()
    # div - total_length/60 , mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = "{:02d}:{:02d}".format(mins, secs)
    lengthlabel["text"] = "Total_Length" + "-" + timeformat


def play_music():  # this 1st try/except make pause and replay from last moment we left music.
    global paused

    if paused:
        mixer.music.unpause()
        statusbar["text"] = "Music Resumed"
        paused = FALSE
    else:
        try:
            mixer.music.load(filename)  # filename for showing particular selected file by user
            mixer.music.play()
            statusbar["text"] = "Playing music" + "    " + os.path.basename(filename)
            show_details()
        except:
            tkinter.messagebox.showerror("file not found", "Melody could not find the file ! please select file again.")


def stop_music():
    mixer.music.stop()  # don't need to again load music because it is already loaded.
    statusbar["text"] = "Music Stopped"


paused = FALSE


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar["text"] = "Music Paused"


def rewind_music():
    play_music()
    statusbar["text"] = "Music Rewinded"


def set_vol(val):  # this is for volume control using pygame mixer module
    volume = int(
        val) / 100  # we are dividing by 100 because mixer takes input only in range from 0-1 ie: 0.1,0.54,0.67 etc.
    mixer.music.set_volume(volume)  # we are taking mixer and converting it with var() ie: 0-100


muted = FALSE


def mute_music():
    global muted
    if muted:  # unmute the music
        mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volumePhoto)
        scale.set(70)
        muted = FALSE
    else:  # mute the music
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE


middleframe = Frame(root)
middleframe.pack(pady=30, padx=30)

playPhoto = PhotoImage(file="images/play.png")
playBtn = Button(middleframe, image=playPhoto, command=play_music)  # creating play button
playBtn.grid(row=0, column=0, padx=15)

stopPhoto = PhotoImage(file="images/stop.png")
stopBtn = Button(middleframe, image=stopPhoto, command=stop_music)  # creating stop button
stopBtn.grid(row=0, column=1, padx=15)

pausePhoto = PhotoImage(file="images/pause.png")
pauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)  # creating pause button
pauseBtn.grid(row=0, column=2, padx=15)

bottomframe = Frame(root)
bottomframe.pack()

rewindPhoto = PhotoImage(file="images/rewind.png")
rewindBtn = Button(bottomframe, image=rewindPhoto, command=rewind_music)  # creating rewind button
rewindBtn.grid(row=0, column=0)

mutePhoto = PhotoImage(file="images/mute.png")
volumePhoto = PhotoImage(file="images/volume.png")
volumeBtn = Button(bottomframe, image=volumePhoto, command=mute_music)  # creating mute button
volumeBtn.grid(row=0, column=1)

scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(50)  # here we are making default value of 50 ie: our scale sets at 50 by default.
mixer.music.set_volume(0.7)
scale.grid(row=0, column=2, pady=15, padx=30)

statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN,
                  anchor=W)  # text in status bar will align at west side.
statusbar.pack(side=BOTTOM, fill=X)  # here we sticks our status bar at the bottom of the window.
# and this (fill)=X shows x- axis filling.

root.mainloop()  # this is for infinite loop to persist our windows all the time we want.
