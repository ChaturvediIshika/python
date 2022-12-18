import turtle
import pandas

screen=turtle.Screen()

screen.title("U.S. STATES")

shape="blank_states_img.gif"
screen.addshape(shape)
turtle.shape(shape)

data=pandas.read_csv("50_states.csv")
all_states=data.states.to_list()
guessed_state=[]
unguessed_state=[]

# def get_mouse_click_coor(x,y):
#     print(x,y)


# turtle.onscreenclick(get_mouse_click_coor)
c=1
while c<=50:
    user_state=turtle.textinput(title=f"{c}/50 STATES", prompt="What's another state?")
    user_state=user_state.title()
    guessed_state.append(user_state)

    if user_state=="Exit":
        for st in data.states:
            if st in guessed_state:
                pass
            else:
                unguessed_state.append(st)

        u=pandas.DataFrame(unguessed_state)
        u.to_csv("states_to_learn.csv")

        break

    if user_state in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        s=data[data.states==user_state]
        t.goto(int(s.x),int(s.y))
        t.write(user_state)
        c+=1

