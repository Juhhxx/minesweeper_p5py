from p5 import *
from myColorsShapes import *
import random
import time


# PENDENT PROBLEMS : when u flag a 0 space it doesn't allow you to remove the flag and when 
# you flag a number it doesn't reset the bombs score, when you lose you still see the "Game Win" 
# for some reason. I WANT TO KILL MYSELF AHHHHHHHHHHHHHHHH

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
doIt = True
game_on = True

def setup():
    
    global bombs,start_time,face
    size(500,600)
    
    rng_max = 8 # sets range minimum
    rng_min = 1 # sets range maximun
    num_bombs = random.randrange(rng_min,rng_max) # chooses the number of bombs randomly (from a set range)
    # range is multiplied by 5, making it only varying from multiples of 5
    while len(minas) != num_bombs*5: 
        
        mX = random.randrange(10) # choosing the X value
        mY = random.randrange(10) # choosing the Y value
        minas.add((mX,mY)) # insertion in the "mines" set
            
    for y in range (len(campo)): # checking all Y values (lines)
        
        for x in range (len(campo[y])): # checking through each X value (space in the line)
            
            if (x,y) not in minas: # check if the x,y value is in the "mines" set
            
                safe.add((x,y)) # insertion in the "safe" set
            
    for mina in minas: # updating the game board
        
        cX,cY = mina # taking the coordiantes from the tuples (x,y) inside the "mines" set
        
        campo[cY][cX] = "bomb" # writting 'bomb' in each of those coordinates
    
    bombs = 0 # reseting bombs to 0
    for line in campo: # going through each line in the game board
        
        bombs += line.count("bomb") # counting all bombs in each line and adding them up
        
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
    print(bombs,"\n")
    print(minas,"\n")
    print(safe,"\n")
    for line in campo:
        print(line)
    
    # starting game time and setting the face to :)
    start_time = time.time()
    face = ":)"
    

# functions that run the game
    
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

    if (indX,indY) in safe: # check if the space that was selected was a safe space

        # control prints
        print("IndY:",indY)
        print("IndX:",indX)

        count = int(campo[indY][indX]) # check count value in the specefied space
            
        if count == 0 and game_on: # check if count is 0
        
            empty_spaces(indX,indY) # if it is, do the special function
        else:

            draw_numbers(indX,indY,count) # if not, draw the specefied count value
          
    else: # if it isn't a safe space
        
        if (indX,indY) not in flagged: # check if the space was not flagged
            
            game_over() # if it wasn't, game over
        
        
    return indX,indY,count

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
    global game_on,face

    # for mine in minas:
            
    #         cX,cY = mine
    #         custom_rec(cX*50,cY*50,50,50,True,lgray,2,black)
    #         fill(255,0,0)
    #         strokeWeight(1)
    #         circle(25 + (cX * 50),25 + (cY * 50),40)
            
    # for space in safe:
        
    #     x,y = space
    #     isBomb(x,y)
    game_on = False
    face = ":("
    push()
    scale(4)
    strokeWeight(5)
    translate(35,50)
    fill(255,0,0)
    text("GAME OVER",0,0)
    pop()

def game_win():
    global game_on,face

    game_on = False
    face = "B)"
    scale(4)
    strokeWeight(5)
    translate(35,50)
    fill(0,255,0)
    text("YOU WIN!!",0,0)
       
def UI():
    
    global bombs,elapsed_time
    
    bombs = len(minas) - len(flagged)
    push()
    custom_rec(0,501,500,100,True,lgray,2,black)
    fill(0)
    strokeWeight(0)
    scale(2)
    translate(10,260)
    text("BOMBS:",0,0)
    translate(0,10)
    text(str(bombs),0,0)
    translate(200,0)
    text(str(elapsed_time),0,0)
    translate(0,-10)
    text("TIME:",0,0)
    pop()
    push()
    noStroke()
    translate(240,520)
    fill(0)
    scale(4)
    text(str(face),0,0)
    pop()               
         
# funções para definir formas
                
def draw_flag(x,y,color):
    
    
    translate(x,y)
    #custom_rec(0,0,50,50,True,lgray,2,black)
    r,g,b = color
    fill(r,g,b)
    stroke(0)
    strokeWeight(2)
    rect(17,15,5,30)
    triangle(17,10,17,30,37,20)
    
    flagged.add((int(x/50),int(y/50)))

def draw_numbers(indX,indY,count):
    
    r,g,b = number_colors[count - 1]
    
    if count == 0:
        
        custom_rec(int(indX)*50,int(indY)*50,50,50,True,lgray,2,black)
    else:
        
        custom_rec(int(indX)*50,int(indY)*50,50,50,True,lgray,2,black)
        fill(r,g,b)
        strokeWeight(3)
        text(str(count),20 + (indX * 50),20 + (indY * 50))

    uncovered.add((indX,indY))
    
    if (indX,indY) in flagged and not minas:
        
        flagged.remove((indX,indY))

# draw game
def draw():
    
    global doIt,count,game_on,bombs,start_time,face,elapsed_time

    end_time = time.time()
    elapsed_time = int(end_time - start_time)
    UI()

    # cheat codes
    
    if key == "ENTER":
        
        game_over()
    
    if key == "w":
        
        game_win()
    
    # draw game board
    while doIt:
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
            
        doIt = False
    
    if game_on:

        if  mouse_is_pressed and mouse_button == LEFT:
            
            isBomb(int(mouse_x/50),int(mouse_y/50))
            
            
        if  mouse_is_pressed and mouse_button == RIGHT:
            
            draw_flag(int(mouse_x/50)*50,int(mouse_y/50)*50,red)
        
        if uncovered == safe or flagged == minas:
            
            game_win()
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    else:

        print("GAME IS OFF")
    

run()