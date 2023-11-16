from p5 import *
from myColorsShapes import *
import random
import time

# game board 
campo = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]

# sets for mines, safe spaces, uncovered spaces and flagged spaces, range modes for cheking spaces,
# number colors, boolean for drawing game board, boolean for running the game itself
minas = set()
safe = set()
uncovered = set()
flagged = set()
range_mode = [(1,2),(0,2),(1,1)]
number_colors = [blue,green,red,dblue,dred,aqua,dgreen,black]
DrawBoard = True
game_on = True
last_button_pressed = None

def restart_game():
    global campo, game_on, minas, safe, uncovered, flagged, DrawBoard
    campo = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]
    DrawBoard = True
    minas = set()
    safe  = set()
    uncovered = set()
    flagged = set()
    setup()
    game_on = True

def setup():
    
    global bombs,start_time,face
    size(500,600)

    setBombSpaces(1,6) # set minimum and maximum range of bombs (numbers are multiplied by 5)
            
    for y in range (len(campo)): # checking all Y values (lines)
        
        for x in range (len(campo[y])): # checking through each X value (space in the line)
            
            if (x,y) not in minas: # check if the x,y value is in the "mines" set
            
                safe.add((x,y)) # insertion in the "safe" set
            
    for mina in minas: # updating the game board
        
        cX,cY = mina # taking the coordiantes from the tuples (x,y) inside the "mines" set
        
        campo[cY][cX] = "bomb" # writting 'bomb' in each of those coordinates
        
    for space in safe:
        
        indX,indY = space # getting the x,y values from the tuples (x,y) in the "safe" set
        count = 0 # reseting count value to 0

        # seeing how many bombs are directly adjacent to each space that's in the "safe" set

        if indX > 0 and indY > 0 and indX < 9 and indY < 9:    
            
            count = check_line_abv(count,indX,indY,0) + check_line(count,indX,indY,0) + check_line_blw(count,indX,indY,0)
        elif indY == 0 and indX > 0 and indX < 9:
            
            count = check_line(count,indX,indY,0) + check_line_blw(count,indX,indY,0)
        elif indY == 9 and indX > 0 and indX < 9:
            
            count = check_line(count,indX,indY,0) + check_line_abv(count,indX,indY,0)
        elif indX == 0 and indY > 0 and indY < 9:
            
            count = check_line_abv(count,indX,indY,1) + check_line(count,indX,indY,1) + check_line_blw(count,indX,indY,1)
        elif indX == 9 and indY > 0 and indY < 9:
            
            count = check_line_abv(count,indX,indY,2) + check_line(count,indX,indY,2) + check_line_blw(count,indX,indY,2)
        elif indX == 0 and indY == 0:
            
            count = check_line(count,indX,indY,1) + check_line_blw(count,indX,indY,1)
        elif indX == 9 and indY == 0:
            
            count = check_line(count,indX,indY,2) + check_line_blw(count,indX,indY,2)
        elif indX == 0 and indY == 9:
            
            count = check_line_abv(count,indX,indY,1) + check_line(count,indX,indY,1)
        elif indX == 9 and indY == 9:
            
            count = check_line_abv(count,indX,indY,2) + check_line(count,indX,indY,2)
            
        campo[indY][indX] = count # insert the count value in the correct space in the game board
    
    # control prints
    print(minas,"\n")
    print(safe,"\n")
    for line in campo:
        print(line)
    
    # starting game time and setting the face to :)
    start_time = time.time()
    face = ":)"
    # set font
    font = create_font("joystix.monospace-regular.otf",15)
    text_font(font)
    
# functions that run the game

def setBombSpaces(rng_min,rng_max):

    rng_max += 1 # max is exclusive, so it adds 1
    num_bombs = random.randrange(rng_min,rng_max) # chooses the number of bombs randomly (from a set range)
    # range is multiplied by 5, making it only varying from multiples of 5
    while len(minas) != num_bombs*5: 
        
        mX = random.randrange(10) # choosing the X value
        mY = random.randrange(10) # choosing the Y value
        minas.add((mX,mY)) # insertion in the "mines" set
    
def check_line_abv(count,indX,indY,mode):
    
    global campo

    rng_neg,rng_pos = range_mode[mode] # checks the range mode (if it is from -1 to +2, 0 to +2, -1 to 0)

    for i in range (indX - rng_neg,indX + rng_pos): # checks the spaces in the specefeid range
            
        if campo[indY - 1][i] == "bomb": # checks if the current space is a bomb, indY - 1 cause we're cheking the line above
                
            count += 1 # increase count by 1 if it is

    return count

def check_line(count,indX,indY,mode):  
    
    global campo  

    rng_neg,rng_pos = range_mode[mode] # checks the range mode (if it is from -1 to +2, 0 to +2, -1 to 0)   

    for i in range (indX - rng_neg,indX + rng_pos): # checks the spaces in the specefeid range
            
        if campo[indY][i] == "bomb": # checks if the current space is a bomb, indY cause we're cheking the line itself
                
            count += 1 # increase count by 1 if it is

    return count
        
def check_line_blw(count,indX,indY,mode):
    
    global campo

    rng_neg,rng_pos = range_mode[mode] # checks the range mode (if it is from -1 to +2, 0 to +2, -1 to 0)   

    for i in range (indX - rng_neg,indX + rng_pos): # checks the spaces in the specefeid range
            
        if campo[indY + 1][i] == "bomb": # checks if the current space is a bomb, indY + 1 cause we're cheking the line bellow
                
            count += 1 # increase count by 1 if it is

    return count
   
def isBomb(indX,indY):
    
    global safe,count,game_on

    if (indX,indY) not in flagged:
        
        if (indX,indY) in safe: # check if the space that was selected was a safe space

            # control prints
            #print("IndY:",indY)
            #print("IndX:",indX)

            count = int(campo[indY][indX]) # check count value in the specefied space
                
            if count == 0: # check if count is 0
            
                empty_spaces(indX,indY) # if it is, do the special function
            else:

                draw_numbers(indX,indY,count) # if not, draw the specefied count value
            
        elif (indX,indY) in minas: # if it isn't a safe space
            
            game_on = False
            game_over() # if it wasn't, game over

def check_button():
    global last_button_pressed
    if mouse_is_pressed:
        last_button_pressed = str(mouse_button)

def mouse_released():
    global last_button_pressed,game_on

    if game_on:
        if last_button_pressed == "MouseButton(LEFT)" or last_button_pressed == "MouseButton(LEFT,LEFT)":
                isBomb(int(mouse_x/50),int(mouse_y/50))

        if last_button_pressed == "MouseButton(RIGHT)" or last_button_pressed == "MouseButton(RIGHT,RIGHT)":
            draw_flag(int(mouse_x/50)*50,int(mouse_y/50)*50,red)
    
    if last_button_pressed == "MouseButton(LEFT)" or last_button_pressed == "MouseButton(LEFT,LEFT)":
            
            if mouse_x >= 217 and mouse_x <= 282 and mouse_y >= 517 and mouse_y <= 582:

                restart_game()

# x and y of the starting space, X difference from start, Y difference from start, how many times do repeat the two loops
def empty_spaces_modes(indX,indY,mX,mY,rng1,rng2): 
     
    indYb = indY + mY # goes to the next line (Y value)
    for i in range (rng1): # this loop controls the current line where to look for adjacent spaces
        
        indXb = indX + mX # goes to the next space (X value)
        
        for i in range (rng2): # this loop controls the adjacent spaces 
            
            count = int(campo[indYb][indXb]) 
            # if count == 0:
            #     fill(255,0,0)
            #     rect(indXb*50,indYb*50,10,10)
            #     adj_mines(indXb,indYb)
            
            if (indXb,indYb) not in uncovered:
                draw_numbers(indXb,indYb,count)
            
            uncovered.add((indXb,indYb))
            if(indXb,indYb) in flagged:
    
                flagged.remove((indXb,indYb))
                
            indXb -= 1
            
        indYb += 1

def empty_spaces(indX,indY):
        
    if indX > 0 and indY > 0 and indX < 9 and indY < 9:    
            
        empty_spaces_modes(indX,indY,1,-1,3,3)
    elif indY == 0 and indX > 0 and indX < 9:
        
        empty_spaces_modes(indX,indY,1,0,2,3)
    elif indY == 9 and indX > 0 and indX < 9:
        
        empty_spaces_modes(indX,indY,1,-1,2,3)
    elif indX == 0 and indY > 0 and indY < 9:
        
        empty_spaces_modes(indX,indY,1,-1,3,2)
    elif indX == 9 and indY > 0 and indY < 9:
        
        empty_spaces_modes(indX,indY,0,-1,3,2)
    elif indX == 0 and indY == 0:
        
        empty_spaces_modes(indX,indY,1,0,2,2)
    elif indX == 9 and indY == 0:
        
        empty_spaces_modes(indX,indY,0,0,2,2)
    elif indX == 0 and indY == 9:
        
        empty_spaces_modes(indX,indY,1,-1,2,2)
    elif indX == 9 and indY == 9:
        
        empty_spaces_modes(indX,indY,0,-1,2,2)
                
def game_over():
    global face
    
    for mine in minas:
            
            cX,cY = mine
            push()
            translate(cX*50,cY*50)
            custom_rec(0,0,50,50,True,gray,1,black)
            strokeCap(ROUND)
            custom_ln(25,10,25,40,4,ddgray)
            custom_ln(10,25,40,25,4,ddgray)
            custom_ln(15,15,35,35,5,ddgray)
            custom_ln(15,35,35,15,5,ddgray)
            custom_cr(25,25,20,True,ddgray,2,black)
            pop()
    for space in safe:
        
        x,y = space
        count = campo[y][x]
        push()
        translate(x*50,y*50)
        custom_rec(0,0,50,50,True,gray,1,black)
        pop()
        draw_numbers(x,y,count)
        print(space)
    print("Spaces DONE")
    
    face = ":("
    push()
    strokeWeight(5)
    translate(140,230)
    fill(255,0,0)
    scale(2)
    text("GAME OVER",0,0)
    pop()

def game_win():
    global game_on,face

    game_on = False
    face = "B)"
    push()
    strokeWeight(5)
    translate(140,230)
    fill(0,255,0)
    scale(2)
    text("YOU WIN!!",0,0)
    pop()
       
def UI():
    global bombs,elapsed_time
    
    bombs = len(minas) - len(flagged)
    push()
    translate(0,501)
    custom_rec(0,0,500,100,True,gray,2,black)
    custom_rec(10,10,480,80,True,dgray,0,black)
    custom_rec(15,15,475,75,True,lgray,0,black)
    custom_tr(10,90,20,90,20,80,True,lgray,0,black)
    custom_tr(490,10,480,20,490,20,True,lgray,0,black)
    custom_rec(15,15,470,70,True,gray,0,black)
    fill(0)
    strokeWeight(5)
    stroke(255,255,255)
    translate(20,25)
    text("BOMBS :",0,0)
    translate(0,20)
    text(str(bombs),0,0)
    translate(380,0)
    text(str(elapsed_time),0,0)
    translate(0,-20)
    text("TIME :",0,0)
    pop()
    push()
    noStroke()
    translate(217,517)
    fill(0)
    draw_face(face)
    pop()               
         
# drawing functions
                
def draw_flag(x,y,color):
    global bombs
        
    if (x/50,y/50) not in uncovered:
        if (x/50,y/50) not in flagged:
            if bombs > 0:
                push()
                translate(x,y)
                #custom_rec(0,0,50,50,True,lgray,2,black)
                translate(15,11)
                r,g,b = color
                fill(r,g,b)
                stroke(0)
                strokeWeight(2)
                rect(0,5,4,25)
                triangle(0,0,0,20,20,10)
                pop()
                flagged.add((int(x/50),int(y/50)))
        else:
            push()
            translate(x,y)
            custom_tr(0,0,50,0,0,50,True,lgray,0,black)
            custom_tr(50,0,50,50,0,50,True,dgray,0,black)
            custom_rec(8,8,34,34,True,gray,0,black)
            custom_rec(0,0,50,50,False,black,1,black)
            pop()        
            flagged.remove((int(x/50),int(y/50)))

def draw_numbers(indX,indY,count):
    
    r,g,b = number_colors[count - 1]
    
    if count == 0:
        
        custom_rec(int(indX)*50,int(indY)*50,50,50,True,gray,1,black)
    else:
        
        custom_rec(int(indX)*50,int(indY)*50,50,50,True,gray,1,black)
        fill(r,g,b)
        strokeWeight(2)
        stroke(0,0,0)
        text(str(count),15 + (indX * 50),15 + (indY * 50))

    uncovered.add((indX,indY))

def draw_face(face):

    push()
    custom_tr(0,0,66,0,0,66,True,lgray,0,black)
    custom_tr(66,0,66,66,0,66,True,dgray,0,black)
    custom_rec(8,8,50,50,True,gray,0,black)
    custom_rec(0,0,66,66,False,black,2,black)
    pop()
    
    if face == ":)":
        push()
        translate(8,8)
        custom_cr(25,25,40,True,yellow,4,black)
        custom_cr(17,20,6,True,black,0,black)
        custom_cr(33,20,6,True,black,0,black)
        custom_arc(25,30,20,10,(0,180),False,black,4,black)
        pop()
    elif face == ":(":
        push()
        translate(8,8)
        custom_cr(25,25,40,True,yellow,4,black)
        custom_arc(25,35,20,10,(180,360),False,black,4,black)
        custom_ln(12,15,22,25,3,black)
        custom_ln(12,25,22,15,3,black)
        translate(15,0)
        custom_ln(12,15,22,25,3,black)
        custom_ln(12,25,22,15,3,black)
        pop()
    elif face == "B)":
        push()
        translate(8,8)
        custom_cr(25,25,40,True,yellow,4,black)
        custom_arc(25,30,20,10,(0,180),False,black,4,black)
        translate(25,13)
        custom_arc(-9,0,20,25,(0,180),True,black,2,black)
        custom_arc(9,0,20,25,(0,180),True,black,2,black)
        custom_ln(12,0,5,12,2,white)
        custom_ln(-5,0,-12,12,2,white)
        pop()
# draw game
def draw():
    
    global DrawBoard,count,game_on,bombs,start_time,face,elapsed_time

    end_time = time.time()
    elapsed_time = int(end_time - start_time)
    UI()
    check_button()

    # cheat codes

    if key == "r":

        restart_game()
    
    if key == "ENTER":
        
        game_over()
    
    if key == "w":
        
        game_win()
    
    # draw game board
    while DrawBoard:
        push()
        for i in range (11):
            push()
            for i in range (11):
                push()
                custom_tr(0,0,50,0,0,50,True,lgray,0,black)
                custom_tr(50,0,50,50,0,50,True,dgray,0,black)
                custom_rec(8,8,34,34,True,gray,0,black)
                pop()
                translate(50,0,0)
            pop()
            translate(0,50,0)
        pop()
        
        for i in range (10):
            
            for i in range (10):
                
                custom_rec(50 * i,0,50,50,False,lgray,1,black)
            translate(0,50)
            
        DrawBoard = False
    

    if game_on:
        
        if uncovered == safe or flagged == minas:
            
            game_win()
            #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    

run()