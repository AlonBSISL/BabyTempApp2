from guizero import *

def open_window():
    window = Window(app, title="Baby profile")
    window.show(wait=True)
    Box(window, align="left", border=True)
    textwindow = Text(window, align="top", text="Baby name here")


app = App(layout="grid")
text = Text(app, align="top", text="Name                                Last Temp.", grid=[0, 1])
b1 = PushButton(app, grid=[0, 2], command=open_window, text="Baby 1                                37.5")
b2 = PushButton(app, grid=[0, 3], command=open_window, text="Baby 2                                37.2")
b3 = PushButton(app, grid=[0, 4], command=open_window, text="Baby 3                                36.9")
b4 = PushButton(app, grid=[0, 5], command=open_window, text="Baby 4                                36.5")
b5 = PushButton(app, grid=[0, 6], command=open_window, text="Baby 5                                36.6")


app.display()
