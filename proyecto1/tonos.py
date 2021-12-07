import pygame 
import time 

pygame.init() 
pygame.mixer.init()

def tono(numero): 
    for digito in numero:
        if digito == 1:
            pygame.mixer.music.load("./Tonos/1.wav")
            pygame.mixer.music.play() 
            time.sleep(0.5)
            
        if digito == 2: 
            pygame.mixer.music.load("./Tonos/2.wav")
            pygame.mixer.music.play() 
            time.sleep(0.5)
                
        if digito == 3: 
            pygame.mixer.music.load("./Tonos/3.wav")
            pygame.mixer.music.play() 
            time.sleep(0.5)
                
        if digito == 4: 
            pygame.mixer.music.load("./Tonos/4.wav")
            pygame.mixer.music.play() 
            time.sleep(0.5)
                
        if digito == 5: 
            pygame.mixer.music.load("./Tonos/5.wav")
            pygame.mixer.music.play() 
            time.sleep(0.5)
                
        if digito == 6: 
            pygame.mixer.music.load("./Tonos/6.wav")
            pygame.mixer.music.play() 
            time.sleep(0.5)
        if digito == 7: 
            pygame.mixer.music.load("./Tonos/7.wav")
            pygame.mixer.music.play() 
            time.sleep(0.5)
                
        if digito == 8: 
            pygame.mixer.music.load("./Tonos/8.wav")
            pygame.mixer.music.play() 
            time.sleep(0.5)
                
        if digito == 9: 
            pygame.mixer.music.load("./Tonos/9.wav")
            pygame.mixer.music.play() 
            time.sleep(0.5)
                
        if digito == 0: 
            pygame.mixer.music.load("./Tonos/0.wav")
            pygame.mixer.music.play() 
            time.sleep(0.5)
    