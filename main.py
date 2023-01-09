from guizero import *
from threading import Timer


def start_count():
    if counter >= 2:
        app.warn("Warning!", "Baby's temperature has been to high or too low twice in the last three hours!")


timer = Timer(30, start_count)
timerstarted = False

babies = []
temps = []
current_temp_box = None
id = 0
current_time = ()
add_new_baby = None
baby_list_window = None
counter = 0


#This function saves the new baby into the system and
def save_baby():
    global add_new_baby, app, baby, babies, time, current_time, timerstarted, counter, id
    baby = [add_new_baby.name_box.value, id, add_new_baby.current_temp_box.value]
    babies.append(baby)
    print(babies)
    if 36.0 <= float(add_new_baby.current_temp_box.value) <= 37.5:
        pass
    else:
        app.warn("Warning!", "Baby's temperature is under 36.0 or above 37.5. Consider calling a doctor.")
        counter += 1
    print(str(id))
    id += 1
    add_new_baby.hide()
    app.show()
    app.focus()


def open_add_new_baby():
    global name_box, parent_name_box, current_temp_box, add_new_baby, save_button, id_show
    add_new_baby = Window(app, title="Add new baby", bg="#f7ff00")
    main_title_add = Text(add_new_baby, text="Baby temperature app", align="top", color="#7700C0",
                          font="Green London", size=50)
    pushdown_9 = Box(add_new_baby, align="top", height=45)
    name_box_text = Text(add_new_baby, font="Noto Serif Telugu", text="Name: ", size=14, color="#7700C0")
    add_new_baby.name_box = TextBox(add_new_baby, height=20, width=30)
    current_temp = Text(add_new_baby, font="Noto Serif Telugu", text="Current body temperature: ", size=14,
                        color="#7700C0")
    add_new_baby.current_temp_box = TextBox(add_new_baby, height=20, width=30)
    print("Alon" + str(id))
    id_show = Text(add_new_baby, font="Noto Serif Telugu", text="Baby's ID is: " + str(id), size=14,
                   color="#7700C0")
    save_button = PushButton(add_new_baby, command=save_baby, text="Save and close")
   # add_new_baby.set_full_screen()

    add_new_baby.name_box.clear()
    add_new_baby.current_temp_box.clear()
    add_new_baby.focus()
    add_new_baby.show(wait=True)


def clear_list_window():
    global baby_list_window, app
    baby_list_window.hide()
    app.show()
    app.focus()


def open_baby_list():
    global baby_list_window
    baby_list_window = Window(app, title="Baby list", bg="#f7ff00")

    #baby_list_window.set_full_screen()
    main_title_list = Text(baby_list_window, text="Baby temperature app", align="top", color="#7700C0",
                           font="Green London", size=50)
    pushdown_4 = Box(baby_list_window, align="top", height=50)
    baby_list_window.baby_list = ListBox(baby_list_window, command=add_temp_check, items=babies)
    baby_list_window.baby_list.font = "Noto Serif Telugu"
    exit_button = PushButton(baby_list_window, command=clear_list_window, text="Close")
    baby_list_window.show(wait=True)
    baby_list_window.focus()


def save_temp():
    global current_baby, add_temp, babies, baby_list_window, baby_list, counter
    idx = babies.index(current_baby)
    current_baby.append(add_temp.value)
    babies[idx] = current_baby
    baby_list_window.baby_list.clear()
    for b in babies:
        baby_list_window.baby_list.append(b)
        print(b)
    if 36.0 <= float(add_temp.value) <= 37.5:
        pass
    else:
        app.warn("Warning!", "Baby's temperature is under 36.0 or above 37.5. Consider calling a doctor.")
        counter += 1
    n = len(current_baby)
    print(str(n) + ", Alon")
    print(current_baby[n - 1])
    n = len(current_baby) - 1
    print(str(n) + "This is n-1")
    if current_baby[n] > (current_baby[n - 1]) or current_baby[n] < current_baby[n - 1]:
        a = float(current_baby[n])
        print(a)
        b = float(current_baby[n - 1])
        print(b)
        c = float(abs(a - b))
        print(c)
        if c >= 1:
            app.warn("Warning!", "Baby's temperature difference is too high!")
            print("Warning!", "Baby's temperature difference is too high!")
    add_temp_check_window.hide()


def add_temp_check(x):
    global current_temp_box_add, add_temp_check_window, baby_id_check, list_id, current_baby, add_temp
    print(x)
    print(type(x))
    list_id = x[0]
    current_baby = list(x)
    current_id = current_baby[1]
    add_temp_check_window = Window(app, title="ID", bg="#f7ff00")
    add_temp_check_window.show(wait=True)
    #add_temp_check_window.set_full_screen()
    main_title_list = Text(add_temp_check_window, text="Baby temperature app", align="top", color="#7700C0",
                           font="Green London", size=50)
    pushdown_5 = Box(add_temp_check_window, align="top", height=50)
    highest_temp = Text(add_temp_check_window, font="Noto Serif Telugu",
                        text="Baby's highest temperature recorded: " + max(current_baby[2:]))
    lowest_temp = Text(add_temp_check_window, font="Noto Serif Telugu",
                       text="Baby's lowest temperature recorded: " + min(current_baby[2:]))
    add_temp_text = Text(add_temp_check_window, text="Add new temperature:", font="Noto Serif Telugu", size=14,
                         color="#7700C0")
    add_temp = TextBox(add_temp_check_window, height=20, width=30)
    save_new_temp = PushButton(add_temp_check_window, text="Save and close", command=save_temp)


app = App(layout="auto", title="Baby Temperature app", bg="#f7ff00")
#app.set_full_screen()
main_title = Text(app, text="Baby temperature app", align="top", color="#7700C0", font="Green London", size=100)

pushdown_1 = Box(app, align="top", height=220)
add_new_baby_button = PushButton(app, text="+ Add new baby", height=2, width=15, command=open_add_new_baby)
add_new_baby_button.bg = "#7700C0"
add_new_baby_button.text_color = "#f7ff00"
add_new_baby_button.text_size = 14
add_new_baby_button.font = "Noto Serif Telugu"

pushdown_2 = Box(app, align="top", height=8)
baby_list_button = PushButton(app, text="Baby list", height=2, width=15, command=open_baby_list)
baby_list_button.bg = "#7700C0"
baby_list_button.text_color = "#f7ff00"
baby_list_button.text_size = 14
baby_list_button.font = "Noto Serif Telugu"

pushdown_3 = Box(app, align="top", height=8)
quit_button = PushButton(app, text="Quit", height=2, width=15, command=app.destroy)
quit_button.bg = "#7700C0"
quit_button.text_color = "#f7ff00"
quit_button.text_size = 14
quit_button.font = "Noto Serif Telugu"

if timerstarted is False:
    timer.start()
    timerstarted = True


app.display()
