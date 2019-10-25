# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random


#-----game configuration----
shape = "turtle"
size = 10
color = "orange"
score = 0
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
dude = trtl.Turtle(shape = shape)
dude.color(color)
dude.shapesize(size)

writer = trtl.Turtle()
writer.shapesize(2)
writer.color("green")
writer.penup()
writer.goto(-270, 330)
font = ("Arial", 30, "bold")
writer.write(score, font = font)
writer.ht()
counter = trtl.Turtle()
counter.up()
counter.goto(250,310)
counter.ht()
#-----game functions--------
def turtle_clicked(x,y):
    print("dude was clicked")
    change_position()
    score_counter()
# this is my customization
    size_down()
    '''colors = {"red","orange", "yellow", "green","blue","purple"}'''


def change_position():
    dude.penup()
    dude.ht()
    new_xpos = random.randint(-400, 400)
    new_ypos = random.randint(-300, 300)
    dude.goto(new_xpos, new_ypos)
    dude.showturtle()
    
      
      

def score_counter():
    global score
    score += 1
    print(score)
    writer.write(score,font = font)
    writer.clear()
    writer.write(score, font = font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    game_end()
    timer_up = True
    
  else:
    counter.write("Timer: " + str(timer), font = font)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def game_end():
  dude.ht()
  dude.goto(500,500)
  counter.goto(0,0)
  counter.write("Time's Up", font = font)
  wn.bgcolor("red")

def size_down():
  global size 
  size -= 1
  dude.shapesize(size)
#-----events----------------
dude.onclick(turtle_clicked)



wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()