# -*- coding: utf-8 -*-
import pygame
import time

class Music:
    def __init__(self,notes, stime):
        self.notes = notes #מחרוזת תווי נגינה
        self.stime = stime #מחרוזת זמנים
        self.bool = True #משתנה בוליאני, אם נמצא במהלך הרצאת פונקציית play_music
        self.bre = True #משתנה בוליאני, אם מתקבל False נעצר הרצת פונקציית play_music

    def __init__(self,):
        self.notes = ""
        self.stime = ""
        self.bool = True
        self.bre = True

    def play_do(self):
        pygame.mixer.init()
        pygame.mixer.music.load("C.wav") #בחירת קובץ להשמעה
        pygame.mixer.music.play() #השמעת הקטע
        time.sleep(0.2) #דיליי עד סיום הנגינה

    def play_re(self):
        pygame.mixer.init()
        pygame.mixer.music.load("D.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_mi(self):
        pygame.mixer.init()
        pygame.mixer.music.load("E.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_fa(self):
        pygame.mixer.init()
        pygame.mixer.music.load("F.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_sol(self):
        pygame.mixer.init()
        pygame.mixer.music.load("G.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_la(self):
        pygame.mixer.init()
        pygame.mixer.music.load("A.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_ci(self):
        pygame.mixer.init()
        pygame.mixer.music.load("B.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_do2(self):
        pygame.mixer.init()
        pygame.mixer.music.load("C2.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)


    def play_db(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Db.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_eb(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Eb.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_gb(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Gb.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_ab(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Bb.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_bb(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Bb.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_click(self):
        pygame.mixer.init()
        pygame.mixer.music.load("click3.wav")
        pygame.mixer.music.play()
        time.sleep(0.2)

    def play_music(self):
        l = self.notes.split()
        stime2 = self.stime.split()
        if len(stime2) != 0:
            stime2[0] = 0

        self.bool = False
        num = 0
        #print (self.s)
        for i in l:
            start_time = time.time() #מאפס את זמן ההתחלה
            while num < len(stime2) and (time.time() - start_time) <= float(stime2[num]): #עיקוב עד לזמן הנדרש
                num = num

            num += 1
            if not self.bre: #התקבל לעצור את הנגנה
                self.bre = True
                self.bool = True
                break
            if(i == "do"):
                self.play_do()
            elif(i == "re"):
                self.play_re()
            elif(i == "mi"):
                self.play_mi()
            elif(i == "fa"):
                self.play_fa()
            elif(i == "sol"):
                self.play_sol()
            elif(i == "la"):
                self.play_la()
            elif(i == "ci"):
                self.play_ci()
            elif(i == "do2"):
                self.play_do2()
            elif(i == "#c"):
                self.play_db()
            elif(i == "#d"):
                self.play_eb()
            elif(i == "#f"):
                self.play_gb()
            elif(i == "#g"):
                self.play_ab()
            elif(i == "#a"):
                self.play_bb()

            #time.sleep(0.4)
            #pygame.display.set_mode(size)
        self.bool = True #נגמר הניגון


