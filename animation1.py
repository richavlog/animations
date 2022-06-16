from tkinter import*
import time
root=Tk()
root.title("moving ball")
canvas=Canvas(root,width=800,height=600,bg="black")
canvas.pack()
ball=canvas.create_oval(10,10,60,60,fill="yellow")
'''for i in range(360):
 canvas.move(ball,1,0)
 root.update()
 time.sleep(0.001)'''
xspeed=1
yspeed=2
while True:
    canvas.move(ball,xspeed,yspeed)
    position=canvas.coords(ball)
    if position[3]>=600 or position[1]<=0:
        yspeed=-yspeed
    if position[2]>=800 or position[0]<=0:
        xspeed=-xspeed 
    root.update()
    time.sleep(0.001)
root.geometry("1000x1000")
root.mainloop()