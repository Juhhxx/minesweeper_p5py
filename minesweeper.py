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
range_mode = [(1,2),(0,2),(1,1)]
number_colors = [blue,green,red,dblue,dred,aqua,dgreen,black]
doIt = True
game_on = True

def setup():
    
    global bombs,start_time,face
    size(500,600)
    
    for i in range (20): # seleção de casas para terem minas
        
        mX = random.randrange(10)
        mY = random.randrange(10)
        
        minas.append((mX,mY)) # inserção na lista "minas"
        
    for y in range (len(campo)): # verificação das casas seguras
        
        for x in range (len(campo[y])):
            
            if (x,y) in minas:
                
                pass
            else:
            
                safe.append((x,y)) # inserção na lista "safe"
            
    for mina in minas: # atualização do campo de jogo
        
        cX,cY = mina
        
        campo[cY][cX] = "bomb"
    
    bombs = 0   
    for line in campo: # contagem das bombas totais
        
        bombs = bombs + line.count("bomb")
    
    print(bombs,"\n")
    print(minas,"\n")
    print(safe,"\n")
    print(campo,"\n")
    
    start_time = time.time()
    face = ":)"
    

    
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
    
    global safe,count
    
    if (indX,indY) in safe:   
         
        count = 0

        print("IndY:",indY)
        print("IndX:",indX)


        # código para ver quantas bombas estão à votla de cada a quadrado
        if indX > 0 and indY > 0 and indX < 9 and indY < 9:    
            
            count = check_line_abv(count,indX,indY,0) + check_line(count,indX,indY,0) + check_line_blw(count,indX,indY,0)
            draw_numbers(indX,indY,count)
        elif indY == 0 and indX > 0 and indX < 9:
            
            count = check_line(count,indX,indY,0) + check_line_blw(count,indX,indY,0)
            draw_numbers(indX,indY,count)
        elif indY == 9 and indX > 0 and indX < 9:
            
            count = check_line(count,indX,indY,0) + check_line_abv(count,indX,indY,0)
            draw_numbers(indX,indY,count)
        elif indX == 0 and indY > 0 and indY < 9:
            
            count = check_line_abv(count,indX,indY,1) + check_line(count,indX,indY,1) + check_line_blw(count,indX,indY,1)
            draw_numbers(indX,indY,count)
        elif indX == 9 and indY > 0 and indY < 9:
            
            count = check_line_abv(count,indX,indY,2) + check_line(count,indX,indY,2) + check_line_blw(count,indX,indY,2)
            draw_numbers(indX,indY,count)
        elif indX == 0 and indY == 0:
            
            count = check_line(count,indX,indY,1) + check_line_blw(count,indX,indY,1)
            draw_numbers(indX,indY,count)
            
        elif indX == 9 and indY == 0:
            
            count = check_line(count,indX,indY,2) + check_line_blw(count,indX,indY,2)
            draw_numbers(indX,indY,count)
            
        elif indX == 0 and indY == 9:
            
            count = check_line_abv(count,indX,indY,1) + check_line(count,indX,indY,1)
            draw_numbers(indX,indY,count)
            
        elif indX == 9 and indY == 9:
            
            count = check_line_abv(count,indX,indY,2) + check_line(count,indX,indY,2)
            draw_numbers(indX,indY,count)
    else:
        
        game_over()
                    
def draw_numbers(indX,indY,count):
    
    r,g,b = number_colors[count - 1]
    fill(r,g,b)
    strokeWeight(3)
    
    if count == 0:
        
        pass
    else:
        text(str(count),20 + (indX * 50),20 + (indY * 50))
                
def game_over():
    global game_on,face
    
    for mine in minas:
            
            cX,cY = mine
            fill(255,0,0)
            strokeWeight(1)
            circle(25 + (cX * 50),25 + (cY * 50),40)
    for space in safe:
        
        x,y = space
        adj_mines(x,y)
    
    face = ":("
    scale(4)
    strokeWeight(5)
    translate(35,50)
    fill(255,0,0)
    text("GAME OVER",0,0)
    game_on = False
           
                
                
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



def draw():
    global doIt,count,game_on,bombs,start_time,face
    end_time = time.time()
    elapsed_time = int(end_time - start_time)
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
    
    if key == "ENTER":
        
        game_over()
    
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
    
    if  mouse_is_pressed and game_on:
        
        custom_rec(int(mouse_x/50)*50,int(mouse_y/50)*50,50,50,True,white,2,black)
        adj_mines(int(mouse_x/50),int(mouse_y/50))


run()