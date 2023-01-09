from guizero import App, Box, Text, TextBox, ListBox, Picture, PushButton, Saving_box

def open_file():
    with open(file_name.value, "w") as f:
        f.write(writing_area.value)

app = App()
saving_box = Box(app, border=1, width='fill')
Text(Saving_box, text="Enter file name")
save_button = PushButton(saving_box, align='right', text='save', command= save_file)
writing_area = TextBox(app, align = 'bottom', width='fill', height='fill', )
app.display()
