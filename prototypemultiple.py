from guizero import App, Window, PushButton


def open_window():
    window = Window(app, title="Second window")
    window.show(wait=True)


app = App(title="Main window")
open_button = PushButton(app, text="Open", command=open_window)
app.display()
