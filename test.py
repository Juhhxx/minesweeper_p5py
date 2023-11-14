from p5 import *
mouse_presses = []
        
def setup():
    
    size(400,400)
          
def detectMouseRelease(mouse_button):
    
    cliked = False
    
    mouse_presses.append(mouse_button)
    
    if len(mouse_presses) > 2:
        
        mouse_presses.pop(0)
    
        if mouse_presses[1] is not mouse_presses[0]:
            
            cliked = True
    
    return cliked
    
    
    
def draw():
    
    
    if detectMouseRelease(mouse_button):
        
        rect(mouse_x,mouse_y,20,20)
        
    
    
run()