from p5 import *
import random
import time

white = [255,255,255]
lgray = [150,150,150]
gray = [100,100,100]
black = [0,0,0]
blue = [0,0,255]
green = [0,255,0]
red = [255,0,0]
dblue = [0,0,100]
dred = [100,0,0]
aqua = [0,200,200]
dgreen = [0,100,0]
# declaração do campo de jogo
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

# listas para as minas, espaços seguros, modos de checar bombas e ordem das cores
minas = []
safe = []
uncovered = []
flagged = []
range_mode = [(1,2),(0,2),(1,1),(1,0),(0,0),(-1,2)]
number_colors = [blue,green,red,dblue,dred,aqua,dgreen,black]
doIt = True
game_on = True

def setup():
    
    global bombs,start_time,face
    size(500,600)
    
    # for i in range (20): # seleção de casas para terem minas
        
    #     mX = random.randrange(10)
    #     mY = random.randrange(10)
       
    #     minas.add((mX,mY)) # inserção na lista "minas"
    
    casas = 0
    num_bombs = random.randrange(10,30) # ecolha aleatória do numero de bombas
    
    while casas != num_bombs: 
        
        mX = random.randrange(10) # escolha do X
        mY = random.randrange(10) # escolha do Y
        if (mX,mY) in minas: # verificação de essa casa ja foi escolhida
            
            pass
        else:
            
            minas.add((mX,mY)) # inserção na lista "minas"
            casas += 1 # diz quantas bombas ja foram colocadas 
        
    for y in range (len(campo)): # verificação das casas seguras
        
        for x in range (len(campo[y])):
            
            if (x,y) not in minas:
            
                safe.add((x,y)) # inserção na lista "safe"
            
    for mina in minas: # atualização do campo de jogo
        
        cX,cY = mina
        
        campo[cY][cX] = "bomb"
    
    bombs = 0   
    for line in campo: # contagem das bombas totais
        
        bombs = bombs + line.count("bomb")
        
    for space in safe:
        
        indX,indY = space
        count = 0
        # código para ver quantas bombas estão à votla de cada a quadrado
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
            
        campo[indY][indX] = count
    
    print(bombs,"\n")
    print(minas,"\n")
    print(safe,"\n")
    for line in campo:
        print(line)
    
    start_time = time.time()
    face = ":)"
    

# funções que correm o jogo
    
def check_line_abv(count,indX,indY,mode):
    
    global campo
    rng_neg,rng_pos = range_mode[mode] 
    for i in range (indX - rng_neg,indX + rng_pos):
            
        if campo[indY - 1][i] == "bomb":
                
            count += 1
        else:
                
            pass
    return count

def check_line(count,indX,indY,mode):  
    
    global campo  
    rng_neg,rng_pos = range_mode[mode]    
    for i in range (indX - rng_neg,indX + rng_pos):
            
        if campo[indY][i] == "bomb":
                
            count += 1
        else:
                
            pass
    return count
        
def check_line_blw(count,indX,indY,mode):
    
    global campo
    rng_neg,rng_pos = range_mode[mode]    
    for i in range (indX - rng_neg,indX + rng_pos):
            
        if campo[indY + 1][i] == "bomb":
                
            count += 1
        else:
                
            pass
    return count
   
def adj_mines(indX,indY):
    
    global safe,count,game_on
    
    if (indX,indY) in safe:   

        print("IndY:",indY)
        print("IndX:",indX)


        count = int(campo[indY][indX])
            
        if count == 0 and game_on:
        
            empty_spaces(indX,indY,count)
        
        
    else:
        
        game_over()
        
    print("Count:",count)
        
    return indX,indY,count    

def empty_spaces(indX,indY,count):
        
    if indX > 0 and indY > 0 and indX < 9 and indY < 9:    
            
        indYb = indY - 1
        for i in range (3):
            
            indXb = indX + 1
            
            for i in range (3):
                
                count = int(campo[indYb][indXb])
                draw_numbers(indXb,indYb,count)
                
                
                uncovered.add((indXb,indYb))
                if(indXb,indYb) in flagged:
        
                    flagged.remove((indXb,indYb))
                    
                indXb -= 1
                print("DONE A")
                
            indYb += 1
            print("DONE B")
        
        print("CARALHO")
    elif indY == 0 and indX > 0 and indX < 9:
        
        indYb = indY
        for i in range (2):
            
            indXb = indX + 1
            
            for i in range (3):
                
                count = int(campo[indYb][indXb])
                draw_numbers(indXb,indYb,count)
                
                
                uncovered.add((indXb,indYb))
                if(indXb,indYb) in flagged:
        
                    flagged.remove((indXb,indYb))
                    
                indXb -= 1
                print("DONE A")
                
            indYb += 1
            print("DONE B")
        
        print("CARALHO")
    elif indY == 9 and indX > 0 and indX < 9:
        
        indYb = indY - 1
        for i in range (2):
            
            indXb = indX + 1
            
            for i in range (3):
                
                count = int(campo[indYb][indXb])
                draw_numbers(indXb,indYb,count)
                
                
                uncovered.add((indXb,indYb))
                if(indXb,indYb) in flagged:
        
                    flagged.remove((indXb,indYb))
                    
                indXb -= 1
                print("DONE A")
                
            indYb += 1
            print("DONE B")
        
        print("CARALHO")
    elif indX == 0 and indY > 0 and indY < 9:
        
        indYb = indY - 1
        for i in range (3):
            
            indXb = indX + 1
            
            for i in range (2):
                
                count = int(campo[indYb][indXb])
                draw_numbers(indXb,indYb,count)
                
                
                uncovered.add((indXb,indYb))
                if(indXb,indYb) in flagged:
        
                    flagged.remove((indXb,indYb))
                    
                indXb -= 1
                print("DONE A")
                
            indYb += 1
            print("DONE B")
        
        print("CARALHO")
    elif indX == 9 and indY > 0 and indY < 9:
        
        indYb = indY - 1
        for i in range (3):
            
            indXb = indX
            
            for i in range (2):
                
                count = int(campo[indYb][indXb])
                draw_numbers(indXb,indYb,count)
                
                
                uncovered.add((indXb,indYb))
                if(indXb,indYb) in flagged:
        
                    flagged.remove((indXb,indYb))
                    
                indXb -= 1
                print("DONE A")
                
            indYb += 1
            print("DONE B")
        
        print("CARALHO")
    elif indX == 0 and indY == 0:
        
        indYb = indY
        for i in range (2):
            
            indXb = indX + 1
            
            for i in range (2):
                
                count = int(campo[indYb][indXb])
                draw_numbers(indXb,indYb,count)
                
                
                uncovered.add((indXb,indYb))
                if(indXb,indYb) in flagged:
        
                    flagged.remove((indXb,indYb))
                    
                indXb -= 1
                print("DONE A")
                
            indYb += 1
            print("DONE B")
        
        print("CARALHO")
    elif indX == 9 and indY == 0:
        
        indYb = indY
        for i in range (2):
            
            indXb = indX
            
            for i in range (2):
                
                count = int(campo[indYb][indXb])
                draw_numbers(indXb,indYb,count)
                
                
                uncovered.add((indXb,indYb))
                if(indXb,indYb) in flagged:
        
                    flagged.remove((indXb,indYb))
                    
                indXb -= 1
                print("DONE A")
                
            indYb += 1
            print("DONE B")
        
        print("CARALHO")
    elif indX == 0 and indY == 9:
        
        indYb = indY - 1

        for i in range (2):
            
            indXb = indX + 1
            
            for i in range (2):
                
                count = int(campo[indYb][indXb])
                draw_numbers(indXb,indYb,count)
                
                
                uncovered.add((indXb,indYb))
                if(indXb,indYb) in flagged:
        
                    flagged.remove((indXb,indYb))
                    
                indXb -= 1
                print("DONE A")
                
            indYb += 1
            print("DONE B")
        
        print("CARALHO")
    elif indX == 9 and indY == 9:
        
        indYb = indY - 1

        for i in range (2):
            
            indXb = indX
            
            for i in range (2):
                
                count = int(campo[indYb][indXb])
                draw_numbers(indXb,indYb,count)
                
                
                uncovered.add((indXb,indYb))
                if(indXb,indYb) in flagged:
        
                    flagged.remove((indXb,indYb))
                    
                indXb -= 1
                print("DONE A")
                
            indYb += 1
            print("DONE B")
        
        print("CARALHO")
                
def game_over():
    global game_on,face
    
    game_on = False
    
    for mine in minas:
            
            cX,cY = mine
            fill(255,0,0)
            strokeWeight(1)
            circle(25 + (cX * 50),25 + (cY * 50),40)
            
    for space in safe:
        
        x,y = space
        _,_,c = adj_mines(x,y)
        draw_numbers(x,y,c)
    
    face = ":("
    scale(4)
    strokeWeight(5)
    translate(35,50)
    fill(255,0,0)
    text("GAME OVER",0,0)

def game_win():
    
    global game_on,face
    
    face = "B)"
    scale(4)
    strokeWeight(5)
    translate(35,50)
    fill(0,255,0)
    text("YOU WIN!!",0,0)
    game_on = False
    
def UI():
    
    global bombs,elapsed_time
    push()
    custom_rec(0,501,500,100,True,lgray,0,black)
    fill(0)
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
                
def custom_rec(x1,y1,width,height,inside,color,thicc,lcolor):
    
    r,g,b = color # define a cor
    lr,lg,lb = lcolor # define a cor do traçado
    stroke(lr,lg,lb) 
    
    if (thicc > 0):
        
        strokeWeight(thicc) # define a grossura do traçado
    else:
        noStroke() # sem traçado
        
    if (inside): # define se a forma será preenchida ou não
        
        fill(r,g,b) # define a cor
    else:
        noFill() # sem preenchimento
    
    rect(x1,y1,width,height)

def draw_flag(x,y,color):
    
    translate(x,y)
    custom_rec(0,0,50,50,True,white,2,black)
    r,g,b = color
    fill(r,g,b)
    stroke(0)
    strokeWeight(2)
    rect(17,15,5,30)
    triangle(17,10,17,30,37,20)
    
    if (x/50,y/50) not in flagged:
        
        flagged.add((x/50,y/50))

def draw_numbers(indX,indY,count):
    
    r,g,b = number_colors[count - 1]
    custom_rec(int(indX)*50,int(indY)*50,50,50,True,white,2,black)
    fill(r,g,b)
    strokeWeight(3)
    
    if count == 0:
        
        pass
    else:
        text(str(count),20 + (indX * 50),20 + (indY * 50))
    
    if(indX,indY) in flagged:
        
        flagged.remove((indX,indY))
    
    if (indX,indY) not in uncovered:
        
        uncovered.add((indX,indY))

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
    
    while doIt:
        
        push()
        translate(0,-500)
        for i in range (10):
            
            for i in range (10):
                
                custom_rec(50 * i,50 * i,50,50,True,gray,0,black)
                
            translate(0,100)
        translate(0,-(2*500))
        for i in range (10):
            
            for i in range (10):
                
                custom_rec(50 * i,50 * i + 50,50,50,True,lgray,0,black)
                
            translate(0,100)
        pop()
        
        
        for i in range (10):
            
            for i in range (10):
                
                custom_rec(50 * i,0,50,50,False,lgray,2,black)
            translate(0,50)
            
        doIt = False
    
    if  mouse_is_pressed and game_on and mouse_button == LEFT:
        
        x,y,c = adj_mines(int(mouse_x/50),int(mouse_y/50))
        draw_numbers(x,y,c)
        
    if  mouse_is_pressed and game_on and mouse_button == RIGHT:
        
        draw_flag(int(mouse_x/50)*50,int(mouse_y/50)*50,red)
    
    if uncovered == safe or flagged == minas:
        
        game_win()


run()