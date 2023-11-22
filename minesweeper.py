from p5 import *
from myColorsShapes import *
import random, time, sys, os
import vispy.app.backends._glfw 

application_path = os.path.dirname(sys.executable)
# game board 
# campo = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

# sets for mines, safe spaces, uncovered spaces and flagged spaces, range modes for cheking spaces,
# number colors, boolean for drawing game board, boolean for running the game itself
# minas = set()
# safe = set()
# uncovered = set()
# flagged = set()
range_mode = [(1,2),(0,2),(1,1)]
number_colors = [blue,green,red,dblue,dred,aqua,dgreen,black]
# DrawBoard = True
# game_on = True
last_button_pressed = None
dificultyChoosen = False
loading_game = True


# width = len(campo[0]) * 50
# height = (len(campo)* 50) + 100

def dificulty_select(dificulty):
    
    if dificulty == "easy":
        
        #9x9
        campo = [[0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0]]
        rng_min = 1
        rng_max = 2
    elif dificulty == "intermediate":
        #16x16
        campo = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        rng_min = 5
        rng_max = 10
    elif dificulty == "hard":
        #16x30
        campo = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        rng_min = 10
        rng_max = 20
    elif dificulty == "expert":
        #16x30
        campo = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        rng_min = 20
        rng_max = 25
    
    return campo,rng_min,rng_max
        
def start_game(dificulty):
    global campo, game_on, minas, safe, uncovered, flagged, DrawBoard, height, width, start_time,face
    
    campo, min_bombs, max_bombs = dificulty_select(dificulty)
    
    width = len(campo[0]) * 50
    height = (len(campo)* 50) + 100
    size(width,height)
    
    minas = set()
    safe  = set()
    uncovered = set()
    flagged = set()
    
    setBombSpaces(min_bombs,max_bombs) # set minimum and maximum range of bombs (numbers are multiplied by 5)
    
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

        if indX > 0 and indY > 0 and indX < (len(campo[0]) - 1) and indY < (len(campo) - 1):    
            
            count = check_line_abv(count,indX,indY,0) + check_line(count,indX,indY,0) + check_line_blw(count,indX,indY,0)
        elif indY == 0 and indX > 0 and indX < (len(campo[0]) - 1):
            
            count = check_line(count,indX,indY,0) + check_line_blw(count,indX,indY,0)
        elif indY == (len(campo) - 1) and indX > 0 and indX < (len(campo[0]) - 1):
            
            count = check_line(count,indX,indY,0) + check_line_abv(count,indX,indY,0)
        elif indX == 0 and indY > 0 and indY < (len(campo) - 1):
            
            count = check_line_abv(count,indX,indY,1) + check_line(count,indX,indY,1) + check_line_blw(count,indX,indY,1)
        elif indX == (len(campo[0]) - 1) and indY > 0 and indY < (len(campo) - 1):
            
            count = check_line_abv(count,indX,indY,2) + check_line(count,indX,indY,2) + check_line_blw(count,indX,indY,2)
        elif indX == 0 and indY == 0:
            
            count = check_line(count,indX,indY,1) + check_line_blw(count,indX,indY,1)
        elif indX == (len(campo[0]) - 1) and indY == 0:
            
            count = check_line(count,indX,indY,2) + check_line_blw(count,indX,indY,2)
        elif indX == 0 and indY == (len(campo) - 1):
            
            count = check_line_abv(count,indX,indY,1) + check_line(count,indX,indY,1)
        elif indX == (len(campo[0]) - 1) and indY == (len(campo) - 1):
            
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
    DrawBoard = True
    game_on = True
    
def setup():
    global bombs, width, height, dificulty
    size(450,550)
    title("minesweeper p5")
    # set font
    font = create_font("joystix.monospace-regular.otf",15)
    text_font(font)
    
def main_menu():
    global width, height, game_on, DrawBoard
    
    custom_rec(0,0,width,height,True,gray,0,black)
    game_on = False
    DrawBoard = False
    
    push()
    translate(20,20)
    custom_rec(0,0,width - 40,200,True,dgray,0,black)
    custom_tr(0,200,10,200,10,190,True,lgray,0,black)
    custom_tr(width - 40,0,width - 40,10,width - 50,10,True,lgray,0,black)
    custom_rec(10,10,width - 50,190,True,lgray,0,black)
    custom_rec(10,10,width - 60,180,True,gray,0,black)
    title_screen = load_image("title_screen.png")
    image(title_screen,25,15)
    pop()
    
    push()
    translate(width/2 - 150,height/2 - 30)
    
    button = [("EASY",green),("INTERMEDIATE",blue),("HARD",red),("EXPERT",purple)]
    for i in range (4):
        mode,color = button[i]
        r,g,b = color
        custom_rec(0,0,300,50,True,lgray,0,black)
        custom_tr(300,0,290,10,300,10,True,dgray,0,black)
        custom_tr(0,50,10,50,10,40,True,dgray,0,black)
        custom_rec(10,10,290,40,True,dgray,0,black)
        custom_rec(10,10,280,30,True,gray,0,black)
        custom_rec(0,0,300,50,False,gray,2,black)
        fill(r,g,b)
        text_align(CENTER)
        text(mode,150,15)
        
        translate(0,65)
    pop()
    
    custom_rec(0,height - 23,width,23,True,dgray,0,black)
    fill(255)
    text("Game by: Juhxx_                 2023",5,height - 20)
    
    dificulty = main_menu_controls()
    
    return dificulty
    
def main_menu_controls():
    global dificultyChoosen, game_on, DrawBoard
    
    if mouse_button == LEFT:
        
        if mouse_x > width/2 - 150 and mouse_x < width/2 + 150 and mouse_y > height/2 - 30 and mouse_y < height/2 + 20:
            
            difc ="easy"
            dificultyChoosen = True
        elif mouse_x > width/2 - 150 and mouse_x < width/2 + 150 and mouse_y > height/2 + 35 and mouse_y < height/2 + 85:
            
            difc ="intermediate"
            dificultyChoosen = True
        elif mouse_x > width/2 - 150 and mouse_x < width/2 + 150 and mouse_y > height/2 + 100 and mouse_y < height/2 + 150:
            
            difc ="hard"
            dificultyChoosen = True
        elif mouse_x > width/2 - 150 and mouse_x < width/2 + 150 and mouse_y > height/2 + 165 and mouse_y < height/2 + 180:
            
            difc ="expert"
            dificultyChoosen = True
        else:
            difc = None
            
        
        return difc
        
# functions that run the game

def setBombSpaces(rng_min,rng_max):

    rng_max += 1 # max is exclusive, so it adds 1
    num_bombs = random.randrange(rng_min,rng_max) # chooses the number of bombs randomly (from a set range)
    # range is multiplied by 5, making it only varying from multiples of 5
    while len(minas) != num_bombs*5: 
        
        mX = random.randrange(len(campo[0])) # choosing the X value
        mY = random.randrange(len(campo)) # choosing the Y value
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
                
                isChord = check_chord(indX,indY)

                if not isChord: draw_numbers(indX,indY,count) # if not, draw the specefied count value
            
        elif (indX,indY) in minas: # if it isn't a safe space
            
            game_on = False
            game_over() # if it wasn't, game over

def check_chord_modes(indX,indY,mX,mY,rng1,rng2,count):

    flag_count = 0
    wrong_flag = []
    chord = []
    indYb = indY + mY # goes to the next line (Y value)
    for i in range (rng1): # this loop controls the current line where to look for adjacent spaces
        
        indXb = indX + mX # goes to the next space (X value)
        
        for i in range (rng2): # this loop controls the adjacent spaces 
            
            if (indXb,indYb) in flagged:
                
                flag_count += 1
                if (indXb,indYb) in safe: wrong_flag.append((indXb,indYb))

            elif (indXb,indYb) not in uncovered:
                chord.append((indXb,indYb))

            indXb -= 1
            
        indYb += 1
    
    if flag_count == count:
        
        return True,chord,wrong_flag
    else:
        
        return False,chord,wrong_flag

def check_chord(indX,indY):

    count = campo[indY][indX]

    if indX > 0 and indY > 0 and indX < (len(campo[0]) - 1) and indY < (len(campo) - 1):    
            
        isChord,chords,wrong_flags = check_chord_modes(indX,indY,1,-1,3,3,count)
    elif indY == 0 and indX > 0 and indX < (len(campo[0]) - 1):
        
        isChord,chords,wrong_flags = check_chord_modes(indX,indY,1,0,2,3,count)
    elif indY == (len(campo) - 1) and indX > 0 and indX < (len(campo[0]) - 1):
        
        isChord,chords,wrong_flags = check_chord_modes(indX,indY,1,-1,2,3,count)
    elif indX == 0 and indY > 0 and indY < (len(campo) - 1):
        
        isChord,chords,wrong_flags = check_chord_modes(indX,indY,1,-1,3,2,count)
    elif indX == (len(campo[0]) - 1) and indY > 0 and indY < (len(campo) - 1):
        
        isChord,chords,wrong_flags = check_chord_modes(indX,indY,0,-1,3,2,count)
    elif indX == 0 and indY == 0:
        
        isChord,chords,wrong_flags = check_chord_modes(indX,indY,1,0,2,2,count)
    elif indX == (len(campo[0]) - 1) and indY == 0:
        
        isChord,chords,wrong_flags = check_chord_modes(indX,indY,0,0,2,2,count)
    elif indX == 0 and indY == (len(campo) - 1):
        
        isChord,chords,wrong_flags = check_chord_modes(indX,indY,1,-1,2,2,count)
    elif indX == (len(campo[0]) - 1) and indY == (len(campo) - 1):
        
        isChord,chords,wrong_flags = check_chord_modes(indX,indY,0,-1,2,2,count)

    if isChord:

        chord(chords,wrong_flags)
        return True
    else:
        return False

def chord(chord,wrong_flags):

    for space in chord:

        indX, indY = space
        count = campo[indY][indX]

        if (indX,indY) in safe:
            draw_numbers(indX,indY,count)
            
            if count == 0:
                empty_spaces(indX,indY)
                
            uncovered.add((indX,indY))

        elif (indX,indY) in minas:
            game_over()
            for flag in wrong_flags:
                x,y = flag
                push()
                translate(x*50,y*50)
                custom_rec(8,8,34,34,True,lred,0,black)
                translate(15,11)
                fill(255,0,0)
                stroke(0)
                strokeWeight(2)
                rect(0,5,4,25)
                triangle(0,0,0,20,20,10)
                pop()
                
def check_button():
    global last_button_pressed
    if mouse_is_pressed:
        last_button_pressed = str(mouse_button)

def mouse_released():
    global last_button_pressed,game_on, width, height, dificulty

    if game_on:
        if last_button_pressed == "MouseButton(LEFT)" or last_button_pressed == "MouseButton(LEFT,LEFT)":
                isBomb(int(mouse_x/50),int(mouse_y/50))

        if last_button_pressed == "MouseButton(RIGHT)" or last_button_pressed == "MouseButton(RIGHT,RIGHT)":
            draw_flag(int(mouse_x/50)*50,int(mouse_y/50)*50,red)
    
    if last_button_pressed == "MouseButton(LEFT)" or last_button_pressed == "MouseButton(LEFT,LEFT)":
            
            if mouse_x >= (width/2 - 33) and mouse_x <= (width/2 + 33) and mouse_y >= (height - 83) and mouse_y <= (height - 18):

                start_game(dificulty)

# x and y of the starting space, X difference from start, Y difference from start, how many times do repeat the two loops
def empty_spaces_modes(indX,indY,mX,mY,rng1,rng2): 

    indYb = indY + mY # goes to the next line (Y value)
    for i in range (rng1): # this loop controls the current line where to look for adjacent spaces
        
        indXb = indX + mX # goes to the next space (X value)
        
        for i in range (rng2): # this loop controls the adjacent spaces 
            
            count = int(campo[indYb][indXb]) 
            
            if (indXb,indYb) not in uncovered:
                draw_numbers(indXb,indYb,count)
                
                if count == 0:
                    empty_spaces(indXb,indYb)
            
            uncovered.add((indXb,indYb))
            if(indXb,indYb) in flagged:

                flagged.remove((indXb,indYb))
                
            indXb -= 1
            
        indYb += 1

def empty_spaces(indX,indY):
        
    if indX > 0 and indY > 0 and indX < (len(campo[0]) - 1) and indY < (len(campo) - 1):    
            
        empty_spaces_modes(indX,indY,1,-1,3,3)
    elif indY == 0 and indX > 0 and indX < (len(campo[0]) - 1):
        
        empty_spaces_modes(indX,indY,1,0,2,3)
    elif indY == (len(campo) - 1) and indX > 0 and indX < (len(campo[0]) - 1):
        
        empty_spaces_modes(indX,indY,1,-1,2,3)
    elif indX == 0 and indY > 0 and indY < (len(campo) - 1):
        
        empty_spaces_modes(indX,indY,1,-1,3,2)
    elif indX == (len(campo[0]) - 1) and indY > 0 and indY < (len(campo) - 1):
        
        empty_spaces_modes(indX,indY,0,-1,3,2)
    elif indX == 0 and indY == 0:
        
        empty_spaces_modes(indX,indY,1,0,2,2)
    elif indX == (len(campo[0]) - 1) and indY == 0:
        
        empty_spaces_modes(indX,indY,0,0,2,2)
    elif indX == 0 and indY == (len(campo) - 1):
        
        empty_spaces_modes(indX,indY,1,-1,2,2)
    elif indX == (len(campo[0]) - 1) and indY == (len(campo) - 1):
        
        empty_spaces_modes(indX,indY,0,-1,2,2)
                
def game_over():
    global face, width, height
    
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
    
    face = ":("
    push()
    strokeWeight(5)
    translate(width/2 - 125,(height - 100)/2 - 20)
    fill(255,0,0)
    scale(2)
    text("GAME OVER",0,0)
    pop()

def game_win():
    global game_on, face, width, height

    game_on = False
    face = "B)"
    push()
    strokeWeight(5)
    translate(width/2 - 120,(height - 100)/2 - 20)
    fill(0,255,0)
    scale(2)
    text("YOU WIN!!",0,0)
    pop()
 
 
# drawing functions      
def UI():
    global bombs,elapsed_time,width,height
    
    bombs = len(minas) - len(flagged)
    push()
    translate(0,height - 99)
    custom_rec(0,0,width,100,True,gray,2,black)
    custom_rec(10,10,width - 20,80,True,dgray,0,black)
    custom_rec(15,15,width - 25,75,True,lgray,0,black)
    custom_tr(10,90,20,90,20,80,True,lgray,0,black)
    custom_tr(width - 10,10,width - 20,20,width - 10,20,True,lgray,0,black)
    custom_rec(15,15,width - 30,70,True,gray,0,black)
    fill(0)
    strokeWeight(5)
    stroke(255,255,255)
    translate(20,25)
    text("BOMBS :",0,0)
    translate(0,20)
    text(str(bombs),0,0)
    translate(width - 120,0)
    text(str(elapsed_time),0,0)
    translate(0,-20)
    text("TIME :",0,0)
    pop()
    push()
    noStroke()
    translate(width/2 - 33,height - 83)
    fill(0)
    draw_face(face)
    pop()               
                
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
    global DrawBoard,count,game_on,bombs,start_time,face,elapsed_time,dificultyChoosen, dificulty, loading_game

    if not dificultyChoosen:
        
        dificulty = main_menu()
        
    else:
        
        
        while loading_game:
            
            start_game(dificulty)
            loading_game = False
            
        end_time = time.time()
        elapsed_time = int(end_time - start_time)
        check_button()
        UI()

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
            for i in range (len(campo)):
                push()
                for i in range (len(campo[0])):
                    push()
                    custom_tr(0,0,50,0,0,50,True,lgray,0,black)
                    custom_tr(50,0,50,50,0,50,True,dgray,0,black)
                    custom_rec(8,8,34,34,True,gray,0,black)
                    pop()
                    translate(50,0,0)
                pop()
                translate(0,50,0)
            pop()
            
            for i in range (len(campo)):
                
                for i in range (len(campo[0])):
                    
                    custom_rec(50 * i,0,50,50,False,lgray,1,black)
                translate(0,50)
                
            DrawBoard = False
        

        if game_on:
            
            
            if uncovered == safe:
                
                game_win()
                #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    

run()