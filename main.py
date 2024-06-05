import pandas
from turtle import *
us_screen = Screen()
us_screen.title("U.S. States Game")

image = "blank_states_img.gif"
us_screen.addshape(image)
Turtle().shape(image)
not_end = 0

datas = pandas.read_csv("50_states.csv")
data_dict = datas.to_dict()
all_states = datas.state.to_list()
guesses_list = []
list_states = []

for index in range(len(data_dict["state"])):
    list_states.append(data_dict["state"][index])

while not_end < 50:
    us_screen_turtle = Turtle()
    us_screen_turtle.penup()
    us_screen_turtle.ht()
    guess = us_screen.textinput(f"Guess a state {not_end}/50",prompt="What's another state's name?")
    if guess == "exit":
        result = [states for states in all_states if states not in guesses_list]
        print(f"those are the states that you forgot in your previous try{"\n".join(result)}")
        break
    if guess in guesses_list:
        print("You already guessed this state")
    elif guess not in guesses_list:
        if guess in list_states:
            not_end += 1
            guesses_list.append(guess)
            us_screen_turtle.goto(data_dict["x"][list_states.index(guess)], data_dict["y"][list_states.index(guess)])
            us_screen_turtle.write(f"{guess}", align="center", font=("Courier",12,"normal"))







































































