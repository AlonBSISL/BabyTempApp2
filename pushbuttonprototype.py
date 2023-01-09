from guizero import App, PushButton, Text
import random
counter = 0

def do_nothing():
    global counter
    print("Button was pressed")
    counter += 1
    clicker.value = counter
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    app.bg = [red, green, blue]



app = App()
clicker = Text(app, counter)
button = PushButton(app, command=do_nothing)
button.repeat(1, do_nothing)
app.display()
