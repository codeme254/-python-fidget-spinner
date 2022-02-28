import turtle

win = turtle.Screen()
win.bgcolor('black')
win.setup(600, 600)
win.title("Fidget spinner by dennis otwoma")
# win.tracer(0)

# the border turtle will be responsible for the border
border = turtle.Turtle()
border.speed(8)
border.color("white")
border.width(5)
border.hideturtle()

# the text turtle will be responsible for the text
text = turtle.Turtle()
text.color('white')
text.hideturtle()

# the spinner turtle will be responsible for the spinner
spinner = turtle.Turtle()
spinner.color("white")
spinner.hideturtle()
spinner.width(2)

# the counter turtle will be responsible for the number of spaces the user has hit
counter = turtle.Turtle()
counter.color('white')
counter.hideturtle()
hits = 0

state = {'turn': 0}
length = 100
radius = 120

def spinnerr():
    spinner.clear()
    angle = state["turn"]/10
    spinner.right(angle)
    spinner.forward(length)
    # spinner.dot(radius, 'orange')
    # spinner.dot(20, 'crimson')
    spinner.dot(radius, 'blue')
    spinner.dot(20, 'crimson')
    spinner.back(length)

    spinner.right(120)
    spinner.forward(length)
    # spinner.dot(radius, 'orange')
    # spinner.dot(20, 'crimson')
    spinner.dot(radius, 'red')
    spinner.dot(20, 'crimson')
    spinner.back(length)

    spinner.right(120)
    spinner.forward(length)
    # spinner.dot(radius, 'orange')
    # spinner.dot(20, 'crimson')
    spinner.dot(radius, 'green')
    spinner.dot(20, 'crimson')
    spinner.back(length)
    spinner.dot(30, 'magenta')

# spinnerr()

def increase_hits():
    global hits
    hits += 1
    counter.goto(230, 260)
    counter.clear()
    counter.write(f"Hits: {hits}", align='center', font=('Arial', 15, 'bold'))

def flick():
    state['turn'] += 40
    increase_hits()
    

def animate():
    if state['turn']:
        state['turn'] -= 1
    
    spinnerr()
    win.ontimer(animate, 25)#calls the passed function after the passed time, eg it will call the animate function after 20 milliseconds


def main():
    border.penup()
    border.goto(-290, 290)
    border.pendown()
    for _ in range(4):
        border.forward(570)
        border.right(90)

    spinner.penup()
    spinner.goto(0, 100)
    spinner.pendown()

    text.penup()
    text.goto(0,-260)
    text.write("Figet spinner by otwoma dennis: press the space key", align='center', font=("Arial", 15, "normal"))

    win.tracer(False)
    win.listen()
    win.onkey(flick, 'space')
    animate()
main()

turtle.done()
# win.exitonclick()