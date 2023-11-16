from p5 import *
#colors
white = (255,255,255)
lgray = (250,250,250)
gray = (200,200,200)
dgray = (150,150,150)
ddgray = (100,100,100)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
dblue = (0,0,100)
dred = (100,0,0)
aqua = (0,200,200)
dgreen = (0,100,0)
yellow = (235, 207, 30)

#shapes
def set_bg(color):
    
    r,g,b = color # define a cor
    
    background(r,g,b)

def custom_ln(x1,y1,x2,y2,thicc,color):
    
    r,g,b = color # define a cor
    stroke(r,g,b)
    strokeWeight(thicc) # define a grossura
    line(x1,y1,x2,y2)

def custom_ln_tr(x1,y1,x2,y2,origin,angle,thicc):
    
    x,y = origin # define o ponto de origem
    
    with push_matrix(): #cria uma nova linha num angulo
            
        translate(x,y)
        rotate(radians(angle))
    
        custom_ln(x1,y1,x2,y2,thicc,black)

def custom_tr(x1,y1,x2,y2,x3,y3,inside,color,thicc,lcolor):
    
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
        
    triangle(x1,y1,x2,y2,x3,y3)
       
def custom_cr(x,y,d,inside,color,thicc,lcolor):
    
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
        
    circle(x,y,d)
 
def custom_arc(x1,y1,rdx,rdy,angle,inside,color,thicc,lcolor):
    
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
        
    start,end = angle # define o principio e o fim do angulo
    
    arc((x1, y1), rdx, rdy, radians(start), radians(end))
    
def custom_sq(x1,y1,size,inside,color,thicc,lcolor):
    
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
            
    square(x1,y1,size)

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
    