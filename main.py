from tkinter import *
import random as r


# functions
def destroy():
    window.destroy()


def game(usr_inp):
    pc_choices = ['Rock', 'Paper', "Scissor"]
    global pc_pick, n
    n = 0
    pc_pick = r.choices(pc_choices)
    win = 'You won | pc loses'
    lose = 'You lose | pc Won'
    tie = 'Its an Tie'
    pc_pick = pc_pick[0]
    print(pc_pick)
    if usr_inp == pc_pick:
        if usr_inp == 'Rock':
            label_pc.configure(image=rock_img)
            label_player.configure(image=rock_img)
        elif usr_inp == 'Scissor':
            label_pc.configure(image=scissor_img)
            label_player.configure(image=scissor_img)
        elif usr_inp == 'Paper':
            label_pc.configure(image=pap_img)
            label_player.configure(image=pap_img)
        print('Tie')
        label_pc.configure(text=pc_pick)
        label_player.configure(text=usr_inp)
        lbl_cmt.configure(text=tie)
        n = 1
    elif usr_inp == 'Rock':
        label_player.configure(image=rock_img)
        if pc_pick == 'Paper':
            print(lose)
            n = 2
            label_pc.configure(image=pap_img)
            lbl_cmt.configure(text=lose)
        elif pc_pick == 'Scissor':
            print(win)
            n = 3
            label_pc.configure(image=scissor_img)
            lbl_cmt.configure(text=win)
    elif usr_inp == 'Paper':
        label_player.configure(image=pap_img)
        if pc_pick == 'Rock':
            print(win)
            n = 3
            label_pc.configure(image=rock_img)
            lbl_cmt.configure(text=win)
        elif pc_pick == 'Scissor':
            print(lose)
            n = 2
            label_pc.configure(image=scissor_img)
            lbl_cmt.configure(text=lose)
    elif usr_inp == 'Scissor':
        label_player.configure(image=scissor_img)
        if pc_pick == 'Paper':
            print(win)
            n = 3
            label_pc.configure(image=pap_img)
            lbl_cmt.configure(text=win)
        elif pc_pick == 'Rock':
            print(lose)
            n = 2
            label_pc.configure(image=rock_img)
            lbl_cmt.configure(text=lose)
    print(n)


def move_app(e):
    window.geometry(f'+{e.x_root}+{e.y_root}')


# Window Starting
window = Tk()
window.geometry("650x450")
window.configure(bg="#ffffff")

# canvas | Frame
canvas = Canvas(
    window,
    bg="#ffffff",
    height=450,
    width=650,
    bd=0,
    highlightthickness=0,
    relief="ridge")

# importing files
background_img = PhotoImage(file=r"resourses\background.png")
back_img = PhotoImage(file=r"resourses\Frame 3.png")
taskbar_img = PhotoImage(file=r'resourses\Frame 4.png')
img0 = PhotoImage(file=r"resourses\img0.png")
img1 = PhotoImage(file=r"resourses\img1.png")
img2 = PhotoImage(file=r"resourses\img2.png")
img3 = PhotoImage(file=r"resourses\img5.png")
pap_img = PhotoImage(file=r'resourses\Paper.png')
rock_img = PhotoImage(file=r'resourses\Rock.png')
scissor_img = PhotoImage(file=r'resourses\Scissors.png')
chose_img = PhotoImage(file=r'resourses\Choose.png')

# Labels ,Images ,Buttons assigning buttons

# Images
background = canvas.create_image(
    325.0, 225.0,
    image=background_img)

back_lbl = Label(canvas,
                 image=back_img,
                 bg='#EEA2D5')

label_pc = Label(canvas,
                 text=' ',
                 bg='#C4C4C4',
                 image=chose_img)

label_player = Label(canvas,
                     text=' ',
                     bg='#C4C4C4',
                     image=chose_img)

# Buttons
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: game('Scissor'),
    relief="flat",
    activebackground="#EEA2D5",
    bg="#EEA2D5")

b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: game('Paper'),
    relief="flat",
    activebackground="#EEA2D5",
    bg="#EEA2D5")

b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: game('Rock'),
    relief="flat",
    activebackground="#EEA2D5",
    bg="#EEA2D5")

b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=destroy,
    relief="flat",
    activebackground="#F054BB",
    bg="#F054BB")

# Labels
lbl_cmt = Label(canvas,
                text="Select your option",
                bg='#C4C4C4',
                font=("Helvetica", "11"))

# Placing Elements
canvas.place(x=0,
             y=0)

b0.place(
    x=453,
    y=347,
    width=124,
    height=91)

b1.place(
    x=247,
    y=347,
    width=124,
    height=91)

b2.place(
    x=41,
    y=343,
    width=124,
    height=91)

b3.place(
    x=0, y=0,
    width=36,
    height=42)

back_lbl.place(x=125,
               y=80)

lbl_cmt.place(x=255,
              y=263,
              height=20)

label_pc.place(x=213, y=168)

label_player.place(x=337, y=168)

# Ending
canvas.bind("<B1-Motion>", move_app)

window.overrideredirect(True)

window.resizable(False, False)

window.mainloop()
