#SNAKE GAME
'''1. Import turtle module
2. How to create screen - Add properties , color, size, title
3. Creation of head - shpe, color , size
4. Creation of function
5. Keyboard binding- function 
6. Creation of food
7. food disappear
8. Adding List or new segment
9 move the end segment first in reverse order
9 move segment 0 to where the head is '''

####SNAKE GAME ########

#step 1 
'''Create Screen, Change color, size and add title '''
import turtle
import time
import random 

delay= 0.1 
screen=turtle.Screen()
screen.title('Snake Game by Arpita')
screen.bgcolor('light blue')
screen.setup(600,600)
screen.tracer(0)

#step 2
'''Creating snake head '''

head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,0)
head.direction='stop'


#step 2

'''Creating snake food '''

food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

# Step 3
'''Creation of function '''

def go_up():
    head.direction='up'
def go_down():
    head.direction='down'
def go_right():
    head.direction='right'
def go_left():
    head.direction='left'


def move():     # Define move function 
    if head.direction=='up':
        y= head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y= head.ycor()
        head.sety(y-20)
    if head.direction=='right':
        x= head.xcor()
        head.setx(x+20)
    if head.direction=='left':
        x= head.xcor()
        head.setx(x-20)

#Sanke Body Grow

segments=[]
#Keyboard Binding

screen.listen()
screen.onkeypress(go_up,"t")
screen.onkeypress(go_down,"b")
screen.onkeypress(go_left,"a")
screen.onkeypress(go_right,"l")
        
# main Game Loop
while True:
    screen.update()
    
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
      


        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('gray')
        new_segment.penup()
        segments.append(new_segment)
         

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segment[index].goto(x,y)

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    time.sleep(delay)



    
    

