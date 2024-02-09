import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")


df = pd.read_csv("50_states.csv")

#Converting it to a lower case
df ["state"]= df["state"].str.lower()

state_list = df.values.tolist()



pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
def print_state(state, x, y):
    pen.goto(x, y)
    pen.write(arg = state)
    

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = "Guess the State", prompt = f"State Name (Correct: {len(guessed_states)}/50) ")
    
    #Click cancel to exit
    if answer_state == None:
        missing_states = [state[0] for state in state_list if state[0] not in guessed_states]
        
        # missing_states = []
        # for state in state_list:
        #     if state[0] not in guessed_states:
        #         missing_states.append(state[0])
        
        print(f"Missing states: {missing_states}")
        screen.exitonclick()

    else:
        for state in state_list:
            if answer_state.lower() in state:
                guessed_states.append(answer_state)
                print_state(answer_state, state[1], state[2])
    

screen.exitonclick()