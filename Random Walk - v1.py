import turtle
from turtle import *
import random
from tkinter import *
from tkinter import messagebox
import time
import tkinter as tk
import math

#Data as dictionary
#LDpTry_2 = ^2
dict = {"Deviation" : [], "Steps" : [], "LastDev_Per_Try" : [], "LDpTry_2" : []};

x=10 #pixels - not real
y=10 #pixels - not real
fs = 4 #font size
anim = bool

inwn = turtle.Screen()
trtl = turtle.Turtle()

inwn.setup(600, 600)

#Number of tries
tryinp = int(inwn.textinput("Random Walk parameters", "Number of TRIES"))
stinp = int(inwn.textinput("Random Walk parameters", "Number of max STEPS"))
anim_inp = inwn.textinput("Random Walk parameters", "Animations?" + "\n" + "('y' for yes, 'n' for no)")

if anim_inp == "y" or anim_inp == 1:
    anim = True
else:
    anim = False


if stinp < 1 or tryinp < 1:
    messagebox.showerror("SOMETHING's WRONG", "!!! Steps must be greater than 1 !!!" + "\n" + "!!! Number of tries must be greater than 0 !!!" + "\n" + "LOL")
    exit()


""" >>> >>> Coordinate system <<< <<< """

speed("fastest")
tracer(False)

num1 = int
num2 = int
num_co = int
z=20 #Changing value

goto(300, 0)
goto(-300, 0)
goto(0, 0)
goto(0, 300)
goto(0, -300)
goto(0, 0)

#| - zero (the origin) -|
penup()
goto(5, -20)
write(0)

#adjustable coo. system
if (stinp % 10) != 0:
    num1 = (stinp + (10 - stinp % 10)) / 10
    num2 = (stinp + (10 - stinp % 10)) / 10

elif (stinp % 10) == 0 and stinp != 0 and tryinp != 0:
    num1 = stinp / 10
    num2 = stinp / 10
    
else:
    messagebox.showerror("SOMETHING's WRONG", "!!! Steps must be greater than 0 !!!" + "\n" + "!!! Number of tries must be greater than 0 !!!" + "\n" + "LOL")
    exit()

z=20
num1 = num2
for i in range(10): # +x
    penup()
    goto(z, 5)
    pendown()
    goto(z, -5)
    
    penup()
    goto(z, -20)
    pendown()
    write(round(num1), font=("Arial", fs, "normal"))
    num1 = num1 + num2
    z=z+20
    
z=-20
num1 = num2 * -1
for i in range(10): # -x
    penup()
    goto(z, 5)
    pendown()
    goto(z, -5)
    
    penup()
    goto(z, -20)
    pendown()
    write(round(num1), font=("Arial", fs, "normal"))
    num1 = num1 - num2
    z=z-20

z=20
num1 = num2
for i in range(14): # +y
    penup()
    goto(5, z)
    pendown()
    goto(-5, z)
    
    penup()
    goto(-20, z)
    pendown()
    write(round(num1), font=("Arial", fs, "normal"))
    num1 = num1 + num2
    z=z+20

z=-20
num1 = num2 * -1
for i in range(10): # -y
    penup()
    goto(5, z)
    pendown()
    goto(-5, z)
    
    penup()
    goto(-20, z)
    pendown()
    write(round(num1), font=("Arial", fs, "normal"))
    num1 = num1 - num2
    z=z-20


""" =========== >>> Random values <<< =========== """
penup()

t = 0 #Step L/R
s = 0 #step

def actual_tries():
    for i in range(stinp):

        global rsp
        global R
        global t
        global s
        global steps
        global dev

        rsp = 20/num2

        R = random.randint(1, 2) #1-left, 2-right
        if R == 1:
            
            t=t-rsp
            
            s=s+rsp
            
            pendown()
            goto(t, s)
            
            steps = s/rsp #real steps
            dev = t/rsp #deviation from the y axis
            
            dict["Steps"].append(round(steps))
            dict["Deviation"].append(round(dev))
            
        else:
            
            t=t+rsp
            
            s=s+rsp
            
            pendown()
            goto(t, s)
            
            steps = s/rsp #real steps
            dev = t/rsp #deviation from the y axis
            
            dict["Steps"].append(round(steps))
            dict["Deviation"].append(round(dev))

        penup()
        goto(t, s-2)
        pendown()
        fillcolor("black")
        begin_fill()
        circle(2)
        end_fill()
        goto(t, s)


for v in range(tryinp):
    s=0
    t=0
    tracer(False)
    penup()
    goto(0, 0)
    pendown()
    tracer(anim)
    actual_tries()

    LDpTry = dev
    LDpTry_2 = dev ** 2

    dict["LastDev_Per_Try"].append(round(LDpTry))
    dict["LDpTry_2"].append(round(LDpTry_2))
    
    print(round(LDpTry), round(LDpTry_2))


#Message box

sumdict = 0 #sum of all deviation values
sumdict = sum(dict["Deviation"])
multipdict = 1
arithmetic_mean = sumdict / (stinp * tryinp)

avrg_dev = sum(dict["LastDev_Per_Try"]) / (stinp * tryinp) #average dev ////// dev = deviation
avrg_dev_2 = sum(dict["LDpTry_2"]) / (stinp * tryinp) #avrg (dev^2)
avrg_2_dev = avrg_dev ** 2 #(average dev)^2

print(avrg_dev, avrg_dev_2, avrg_2_dev)

for Deviation in dict["Deviation"]:
##    list(map(int, dict["Deviation"]))
    multipdict = multipdict * Deviation
##print("geometric_mean = multipdict ** (1.0 / (stinp * tryinp))", multipdict)

geometric_mean = multipdict ** (1.0 / (stinp * tryinp))
variance_wN = arithmetic_mean / math.sqrt(stinp * tryinp)
    
result = messagebox.askquestion("RESULT",
                                "Tries: " + str(tryinp) + ";" + "\n" + \
                                "Steps per try: " + str(round(steps)) + ";" + "\n" + \
                                "Number of steps: " + str(round(stinp * tryinp)) + ";" + "\n" + "\n" + \
                                
                                "Average Deviation: " + str(round(avrg_dev)) + \
                                " (from the 'y' axis)" + "\n" + \
                                "avrg (dev^2): " + str(round(avrg_dev_2, 5)) + "\n" + \
                                "(avrg dev)^2: " + str(round(avrg_2_dev, 5)) + "\n" + "\n" + \

                                "Sum of all deviations: " + str(sumdict) + "\n" + \
                                "Arithmetic mean: " + str(round(arithmetic_mean, 5)) + "\n" + \
                                "Geometric mean: " + str(round(geometric_mean, 5)) + "\n" + "\n" + \

                                "Variance σ=√[<(a^2)> + (<a>)^2] : " + str(round(math.sqrt(avrg_dev_2 + avrg_2_dev), 5)) + "\n" + \
                                "Variance σ≈<a>/√N => " + str(round(variance_wN, 5)) + "\n" + "\n" + \
                                
                                
                                "Do you want to make .txt file of the data?")


#Create dict.
def dictdef():
    file = open("RW_database.txt", "w")
    file.write("%s = %s\n" %("Deviation", dict["Deviation"])) #(name, dictionary name[name of the subject])
    file.write("\n")
    file.write("%s = %s\n" %("Steps", dict["Steps"]))
    file.write("\n")
    file.write("%s = %s\n" %("LastDev_Per_Try", dict["LastDev_Per_Try"]))
    file.write("%s = %s\n" %("LastDev_Per_Try", dict["LDpTry_2"]))

    file.close()

if result == "yes":
    dictdef()
else:
    exit()

done()

#Made by Nodari Tcheishvili (NODARman)