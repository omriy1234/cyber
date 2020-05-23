# -*- coding: utf-8 -*-
import socket
import select
import pygame
import sys
import threading
import time
import tkinter as tk
from tkinter import simpledialog
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import random
from music import Music


lmusic = []
server_socket = socket.socket()



def pysocket():
    global lmusic
    global server_socket

    mnow = ""
    lnow = []
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [480, 410]
    bg = [250, 250, 162]
    x1 = 80
    xsize = 50
    y = 80
    ysize = 50
    x2 =260
    note = Music("")
    nowb = ""

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("The main player")
    button_1a = pygame.Rect(x1, y, xsize, ysize)
    button_1l = pygame.Rect(x1 +50, y, xsize+40, ysize)
    button_2a = pygame.Rect(x1, y + 70, xsize, ysize)
    button_2l = pygame.Rect(x1+ xsize, y +70, xsize+40, ysize)
    button_3a = pygame.Rect(x1, y + 140, xsize, ysize)
    button_3l = pygame.Rect(x1 + xsize, y + 140, xsize+40, ysize)
    button_4a = pygame.Rect(x1, y + 210, xsize, ysize)
    button_4l = pygame.Rect(x1 + xsize, y + 210, xsize+40, ysize)
    button_5a = pygame.Rect(x2, y, xsize, ysize)
    button_5l = pygame.Rect(x2 +50 , y, xsize+40, ysize)
    button_6a = pygame.Rect(x2, y +70, xsize, ysize)
    button_6l = pygame.Rect(x2 + 50, y +70, xsize+40, ysize)
    button_7a = pygame.Rect(x2, y + 140, xsize, ysize)
    button_7l = pygame.Rect(x2 +50 , y +140, xsize+40, ysize)
    button_8a = pygame.Rect(x2, y + 210, xsize, ysize)
    button_8l = pygame.Rect(x2 +50 , y +210, xsize+40, ysize)
    button_melody = pygame.Rect(400, 10, 2*xsize -20, ysize)
    button_file_selection = pygame.Rect(320, 10, 2*xsize-20, ysize)
    button_revers = pygame.Rect(240, 10, 2*xsize-20, ysize)
    button_save = pygame.Rect(160, 10, 2*xsize-20, ysize)
    button_clear = pygame.Rect(80, 10, 2*xsize-20, ysize)
    button_delete_note = pygame.Rect(0, 10, 2*xsize-20, ysize)

    button_your_notes = pygame.Rect(320, 350, 2*xsize -20, ysize)
    button_enter = pygame.Rect(400, 350, 2*xsize -20, ysize)
    button_clear_sections = pygame.Rect(240, 350, 2*xsize-20, ysize)
    button_random = pygame.Rect(160, 350, 2*xsize-20, ysize)
    button_delete_last_added = pygame.Rect(80, 350, 2*xsize-20, ysize)
    button_open_piano = pygame.Rect(0, 350, 2*xsize-20, ysize)


    font = pygame.font.SysFont('Lucida Handwriting', 20)
    font2 = pygame.font.SysFont('Parchment', 62)
    font3 = pygame.font.SysFont('Parchment', 72)
    font4 = pygame.font.SysFont('Parchment', 56)
    font5 = pygame.font.SysFont('Parchment', 47)
    font6 = pygame.font.SysFont('Bauhaus 93', 32)


    textx = x1 -15
    texty = 100
    colortext = [0, 0, 255]
    colortext2 = [0, 0, 53]
    colortext3 = [117, 249, 134]

    text1 = font.render('1)', True, colortext)
    textRect1 = text1.get_rect()
    textRect1.center = (textx, texty)

    text2 = font.render('2)', True, colortext)
    textRect2 = text2.get_rect()
    textRect2.center = (textx, texty + 70)

    text3 = font.render('3)', True, colortext)
    textRect3 = text3.get_rect()
    textRect3.center = (textx, texty + 140)

    text4 = font.render('4)', True, colortext)
    textRect4 = text4.get_rect()
    textRect4.center = (textx, texty + 210)


    text5 = font.render('(5', True, colortext)
    textRect5 = text5.get_rect()
    textRect5.center = (textx + 345, texty)

    text6 = font.render('(6', True, colortext)
    textRect6 = text6.get_rect()
    textRect6.center = (textx + 345, texty + 70)


    text7 = font.render('(7', True, colortext)
    textRect7 = text7.get_rect()
    textRect7.center = (textx + 345, texty + 140)

    text8 = font.render('(8', True, colortext)
    textRect8 = text8.get_rect()
    textRect8.center = (textx + 345, texty + 210)


    text9 = font.render('add', True, colortext3)
    textRect91 = text9.get_rect()
    textRect91.center = (x1 +25, y + 25)

    textRect92 = text9.get_rect()
    textRect92.center = (x1 +25, y + 95)

    textRect93 = text9.get_rect()
    textRect93.center = (x1 +25, y + 165)

    textRect94 = text9.get_rect()
    textRect94.center = (x1 +25, y + 235)

    textRect95 = text9.get_rect()
    textRect95.center = (x2 +25, y + 25)

    textRect96 = text9.get_rect()
    textRect96.center = (x2 +25, y + 95)

    textRect97 = text9.get_rect()
    textRect97.center = (x2 +25, y + 165)

    textRect98 = text9.get_rect()
    textRect98.center = (x2 +25, y + 235)


    text10 = font.render('listen', True, colortext2)
    textRect101 = text10.get_rect()
    textRect101.center = (x1 + 95,y + 25)

    textRect102 = text10.get_rect()
    textRect102.center = (x1 + 95,y + 95)

    textRect103 = text10.get_rect()
    textRect103.center = (x1 + 95,y + 165)

    textRect104 = text10.get_rect()
    textRect104.center = (x1 + 95,y + 235)

    textRect105 = text10.get_rect()
    textRect105.center = (x2 + 95,y + 25)

    textRect106 = text10.get_rect()
    textRect106.center = (x2 + 95,y + 95)

    textRect107 = text10.get_rect()
    textRect107.center = (x2 + 95,y + 165)

    textRect108 = text10.get_rect()
    textRect108.center = (x2 + 95,y + 235)

    text11 = font3.render('play', True,[255,255,255])
    textRect11 = text11.get_rect()
    textRect11.center = (440,30)

    text12 = font3.render('revers', True,[255,255,255])
    textRect12 = text12.get_rect()
    textRect12.center = (280,30)

    text13 = font3.render('save', True,[255,255,255])
    textRect13 = text13.get_rect()
    textRect13.center = (200,30)

    text14 = font3.render('clear', True,[255,255,255])
    textRect14 = text14.get_rect()
    textRect14.center = (120,30)

    text151 = font2.render('delete', True,[255,255,255])
    text152 = font2.render('note', True,[255,255,255])
    textRect151 = text151.get_rect()
    textRect151.center = (40,23)
    textRect152 = text152.get_rect()
    textRect152.center = (40,45)


    text16 = font3.render('enter', True,[255,255,255])
    textRect16 = text16.get_rect()
    textRect16.center = (440,370)

    text171 = font2.render('clear', True,[255,255,255])
    text172 = font4.render('sections', True,[255,255,255])
    textRect171 = text171.get_rect()
    textRect171.center = (280,360)
    textRect172 = text172.get_rect()
    textRect172.center = (280,385)

    text18 = font4.render('random', True,[255,255,255])
    textRect18 = text18.get_rect()
    textRect18.center = (200,370)

    text191 = font5.render('delete last', True,[255,255,255])
    text192 = font2.render('section', True,[255,255,255])
    textRect191 = text191.get_rect()
    textRect191.center = (120,362)
    textRect192 = text192.get_rect()
    textRect192.center = (120,380)

    text201 = font2.render('open', True,[255,255,255])
    text202 = font3.render('piano', True,[255,255,255])
    textRect201 = text201.get_rect()
    textRect201.center = (40,355)
    textRect202 = text202.get_rect()
    textRect202.center = (40,375)

    text21 = font3.render('select', True,[255,255,255])
    textRect21 = text21.get_rect()
    textRect21.center = (360,30)

    text222 = font3.render('your', True,[255,255,255])
    text221 = font3.render('notes', True,[255,255,255])
    textRect221 = text221.get_rect()
    textRect221.center = (352,355)
    textRect222 = text222.get_rect()
    textRect222.center = (363,380)


    # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simpy type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom

    while True:
        for event in pygame.event.get():
            if note.bool == True:
                nowb = ""
            if event.type == pygame.QUIT:
                lmusic = ["False"]
                server_socket.close()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                # checks if mouse position is over the button
                list1 =  []
                for k in lnow:
                    str2 = ""
                    klist = k.split()
                    for j in klist:
                        if not(j != "do" and j != "re" and j != "mi" and j != "fa" and j != "sol" and j != "la" and j != "ci" and j != "do2" and j != "#c" and j != "#d" and j != "#f" and j != "#g" and j != "#a"):
                            str2 += " " + j
                    if str2.replace(" ","") != "":
                        list1.append(str2)

                lnow = list1



                if button_1l.collidepoint(mouse_pos):
                    if(len(lmusic)>=1):
                        if nowb == "l1" and note.bool == False:
                            note.play_click()
                            note.bre = False
                            print (note.bre)
                        elif note.bool == True:
                            note = Music(lmusic[0])
                            t2 = threading.Thread(target=note.play_music)
                            t2.start()
                            nowb = "l1"

                    else:
                        print("1l")
                elif button_1a.collidepoint(mouse_pos):
                    if(len(lmusic)>=1 and note.bool == True):
                        lnow.append(lmusic[0])
                        note.play_click()
                    else:
                        print("1a")
                elif button_2l.collidepoint(mouse_pos):
                    if(len(lmusic)>=2):
                        if nowb == "l2" and note.bool == False:
                            note.play_click()
                            note.bre = False
                            print (note.bre)
                        elif note.bool == True:
                            note = Music(lmusic[1])
                            t2 = threading.Thread(target= note.play_music)
                            t2.start()
                            nowb = "l2"
                    else:
                        print("21")
                elif button_2a.collidepoint(mouse_pos):
                    if(len(lmusic)>=2 and note.bool == True):
                        lnow.append(lmusic[1])
                        note.play_click()
                    else:
                        print("2a")
                elif button_3l.collidepoint(mouse_pos):
                    if(len(lmusic)>=3):
                        if nowb == "l3" and note.bool == False:
                            note.play_click()
                            note.bre = False
                            print (note.bre)
                        elif note.bool == True:
                            note = Music(lmusic[2])
                            t2 = threading.Thread(target= note.play_music)
                            t2.start()
                            nowb = "l3"
                    else:
                        print("31")
                elif button_3a.collidepoint(mouse_pos):
                    if(len(lmusic)>=3 and note.bool == True):
                        lnow.append(lmusic[2])
                        note.play_click()
                    else:
                        print("3a")
                elif button_4l.collidepoint(mouse_pos):
                    if(len(lmusic)>=4):
                        if nowb == "l4" and note.bool == False:
                            note.play_click()
                            note.bre = False
                            print (note.bre)
                        elif note.bool == True:
                            note = Music(lmusic[3])
                            t2 = threading.Thread(target= note.play_music)
                            t2.start()
                            nowb = "l4"
                    else:
                        print("41")
                elif button_4a.collidepoint(mouse_pos):
                    if(len(lmusic)>=4 and note.bool == True):
                        lnow.append(lmusic[3])
                        note.play_click()
                    else:
                        print("4a")
                elif button_5l.collidepoint(mouse_pos):
                    if(len(lmusic)>=5):
                        if nowb == "l5" and note.bool == False:
                            note.play_click()
                            note.bre = False
                            print (note.bre)
                        elif note.bool == True:
                            note = Music(lmusic[4])
                            t2 = threading.Thread(target= note.play_music)
                            t2.start()
                            nowb = "l5"
                    else:
                        print("51")
                elif button_5a.collidepoint(mouse_pos):
                    if(len(lmusic)>=5 and note.bool == True):
                        lnow.append(lmusic[4])
                        note.play_click()
                    else:
                        print("5a")
                elif button_6l.collidepoint(mouse_pos):
                    if(len(lmusic)>=6):
                        if nowb == "l6" and note.bool == False:
                            note.play_click()
                            note.bre = False
                            print (note.bre)
                        elif note.bool == True:
                            note = Music(lmusic[5])
                            t2 = threading.Thread(target= note.play_music)
                            t2.start()
                            nowb = "l6"
                    else:
                        print("61")
                elif button_6a.collidepoint(mouse_pos):
                    if(len(lmusic)>=6 and note.bool == True):
                        lnow.append(lmusic[5])
                        note.play_click()
                    else:
                        print("6a")
                elif button_7l.collidepoint(mouse_pos):
                    if(len(lmusic)>=7):
                        if nowb == "l7" and note.bool == False:
                            note.play_click()
                            note.bre = False
                            print (note.bre)
                        elif note.bool == True:
                            note = Music(lmusic[6])
                            t2 = threading.Thread(target= note.play_music)
                            t2.start()
                            nowb = "l7"
                    else:
                        print("71")
                elif button_7a.collidepoint(mouse_pos):
                    if(len(lmusic)>=7 and note.bool == True):
                        lnow.append(lmusic[6])
                        note.play_click()
                    else:
                        print("7a")
                elif button_8l.collidepoint(mouse_pos):
                    if(len(lmusic)>=8 and note.bool == True):
                        if nowb == "l8" and note.bool == False:
                            note.play_click()
                            note.bre = False
                            print (note.bre)
                        elif note.bool == True:
                            note = Music(lmusic[7])
                            t2 = threading.Thread(target= note.play_music)
                            t2.start()
                            nowb = "l8"
                    else:
                        print("81")
                elif button_8a.collidepoint(mouse_pos):
                    if(len(lmusic)>=8):
                        lnow.append(lmusic[7])
                        note.play_click()
                    else:
                        print("8a")


                elif button_melody.collidepoint(mouse_pos):
                    if nowb == "play" and note.bool == False:
                        note.bre = False
                    elif note.bool == True:
                        note.play_click()
                        note = Music(str(lnow).replace("[","").replace("]","").replace("'","").replace(",",""))
                        t2 = threading.Thread(target= note.play_music)
                        t2.start()
                        nowb = "play"

                elif note.bool == False:
                    break

                elif button_revers.collidepoint(mouse_pos):
                    lnow2 = []
                    for i in lnow:
                        lnow2.append(str(i.split()[::-1]).replace("[","").replace("]","").replace("'","").replace(",",""))
                    lnow = lnow2[::-1]
                    note = Music(str(lnow).replace("[","").replace("]","").replace("'","").replace(",",""))
                    note.play_click()

                elif button_save.collidepoint(mouse_pos):
                    note.play_click()
                    root2 = tk.Tk()
                    root2.withdraw() # we don't want a full GUI, so keep the root window from appearing
                    pygame.quit()
                    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
                    screen = pygame.display.set_mode(size)
                    root2.destroy()
                    print(filename)
                    if not(str(filename) == "" or str(filename)[::-1][0:4][::-1] != ".txt"):
                        input_file = open(r''+ filename,'a')
                        input_file.write((str(lnow).replace("[","").replace("]","").replace("'","").replace(",","").replace("  "," "))+ '\n')
                        input_file.close()
                    print ("save")



                elif button_clear.collidepoint(mouse_pos):
                    lnow = []
                    note.play_click()

                elif button_delete_note.collidepoint(mouse_pos):
                    print (lnow)
                    if (len(lnow) > 0):
                        lnow[-1] = str(lnow[-1]).split()
                        del(lnow[-1])[-1]
                        lnow[-1] = str(lnow[-1]).replace("[","").replace("]","").replace("'","").replace(",","")
                        print (lnow)
                    note.play_click()

                elif button_enter.collidepoint(mouse_pos):
                    note.play_click()
                    ROOT = tk.Tk()
                    ROOT.withdraw()

                    pygame.quit()
                    enter_notes = simpledialog.askstring(title="notes",prompt="enter notes")
                    ROOT.destroy()
                    screen = pygame.display.set_mode(size)
                    if str(enter_notes) != "None":
                        print (str(enter_notes))
                        lnow.append(enter_notes.lower())
                    print ("enter")

                elif button_clear_sections.collidepoint(mouse_pos):
                    note.play_click()
                    n = 0
                    while len(lmusic) != 0 and n < 8:
                        n += 1
                        del lmusic[0]
                    print ("clear sections")

                elif button_random.collidepoint(mouse_pos):
                    note.play_click()
                    lnow2 = []
                    if lnow != []:
                        nrandom=random.randint(0,len(lnow) -1)
                    while lnow != []:
                        lnow2.append(lnow.pop(nrandom))
                        if(len(lnow) != 0):
                            nrandom=random.randint(0,len(lnow)-1)
                    lnow = lnow2

                    print ("random")

                elif button_delete_last_added.collidepoint(mouse_pos):
                    if len(lnow) != 0:
                        del(lnow)[-1]
                    note.play_click()
                    print ("delete last added")

                elif button_open_piano.collidepoint(mouse_pos):
                    note.play_click()
                    pygame.quit()
                    exec(open("piano clinet.py").read())
                    screen = pygame.display.set_mode(size)
                    print ("open piano")

                elif button_file_selection.collidepoint(mouse_pos):
                    note.play_click()
                    root3 = tk.Tk()
                    root3.withdraw() # we don't want a full GUI, so keep the root window from appearing
                    pygame.quit()
                    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
                    screen = pygame.display.set_mode(size)
                    root3.destroy()
                    print(filename)
                    string = ""
                    if not(str(filename) == "" or str(filename)[::-1][0:4][::-1] != ".txt"):
                        input_file = open(r''+ filename,'r')
                        notes = input_file.read().replace('\n', " ").split()
                        for j in notes:
                            if not(j != "do" and j != "re" and j != "mi" and j != "fa" and j != "sol" and j != "la" and j != "ci" and j != "do2" and j != "#c" and j != "#d" and j != "#f" and j != "#g" and j != "#a"):
                                string += " " + j

                        input_file.close()
                    lnow.append(string)


                elif button_your_notes.collidepoint(mouse_pos):
                    note.play_click()
                    root = tk.Tk()
                    pygame.quit()
                    S = tk.Scrollbar(root)
                    T = tk.Text(root, height=4, width=50)
                    S.pack(side=tk.RIGHT, fill=tk.Y)
                    T.pack(side=tk.LEFT, fill=tk.Y)
                    S.config(command=T.yview)
                    T.config(yscrollcommand=S.set)
                    T.insert(tk.END, str(lnow).replace("]", '').replace("[","").replace("'","").replace(",  "," "))
                    tk.mainloop()
                    screen = pygame.display.set_mode(size)

                    print ("your_notes")



                print(lnow)
        screen.fill(bg)

        colorb1 = [17, 6, 70]
        colorb2 = [133, 252, 113]
        pygame.draw.rect(screen, colorb1, button_1a)  # draw button
        pygame.draw.rect(screen, colorb2, button_1l)  # draw button
        pygame.draw.rect(screen, colorb1, button_2a)  # draw button
        pygame.draw.rect(screen, colorb2, button_2l)  # draw button
        pygame.draw.rect(screen, colorb1, button_3a)  # draw button
        pygame.draw.rect(screen, colorb2, button_3l)  # draw button
        pygame.draw.rect(screen, colorb1, button_4a)  # draw button
        pygame.draw.rect(screen, colorb2, button_4l)  # draw button
        pygame.draw.rect(screen, colorb1, button_5a)  # draw button
        pygame.draw.rect(screen, colorb2, button_5l)  # draw button
        pygame.draw.rect(screen, colorb1, button_6a)  # draw button
        pygame.draw.rect(screen, colorb2, button_6l)  # draw button
        pygame.draw.rect(screen, colorb1, button_7a)  # draw button
        pygame.draw.rect(screen, colorb2, button_7l)  # draw button
        pygame.draw.rect(screen, colorb1, button_8a)  # draw button
        pygame.draw.rect(screen, colorb2, button_8l)  # draw button
        pygame.draw.rect(screen, [0, 0, 0], button_melody)  # draw button
        pygame.draw.rect(screen, [40, 40, 40], button_file_selection) # draw button
        pygame.draw.rect(screen, [80, 80, 80], button_revers)  # draw button
        pygame.draw.rect(screen, [130, 130, 130], button_save)  # draw button
        pygame.draw.rect(screen, [170, 170, 170], button_clear) # draw button
        pygame.draw.rect(screen, [200, 200, 200], button_delete_note) # draw button
        pygame.draw.rect(screen, [0, 0, 0], button_enter)  # draw button
        pygame.draw.rect(screen, [40, 40, 40], button_your_notes)  # draw button
        pygame.draw.rect(screen, [80, 80, 80], button_clear_sections)  # draw button
        pygame.draw.rect(screen, [130, 130, 130], button_random)  # draw button
        pygame.draw.rect(screen, [170, 170, 170], button_delete_last_added) # draw button
        pygame.draw.rect(screen, [200, 200, 200], button_open_piano) # draw button

        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        screen.blit(text4, textRect4)
        screen.blit(text5, textRect5)
        screen.blit(text6, textRect6)
        screen.blit(text7, textRect7)
        screen.blit(text8, textRect8)
        screen.blit(text9, textRect91)
        screen.blit(text9, textRect92)
        screen.blit(text9, textRect93)
        screen.blit(text9, textRect94)
        screen.blit(text9, textRect95)
        screen.blit(text9, textRect96)
        screen.blit(text9, textRect97)
        screen.blit(text9, textRect98)


        screen.blit(text10, textRect101)
        screen.blit(text10, textRect102)
        screen.blit(text10, textRect103)
        screen.blit(text10, textRect104)
        screen.blit(text10, textRect105)
        screen.blit(text10, textRect106)
        screen.blit(text10, textRect107)
        screen.blit(text10, textRect108)
        screen.blit(text11, textRect11)
        screen.blit(text12, textRect12)
        screen.blit(text13, textRect13)
        screen.blit(text14, textRect14)
        screen.blit(text151, textRect151)
        screen.blit(text152, textRect152)
        screen.blit(text16, textRect16)
        screen.blit(text171, textRect171)
        screen.blit(text172, textRect172)
        screen.blit(text18, textRect18)
        screen.blit(text191, textRect191)
        screen.blit(text192, textRect192)
        screen.blit(text201, textRect201)
        screen.blit(text202, textRect202)
        screen.blit(text21, textRect21)
        screen.blit(text222, textRect221)
        screen.blit(text221, textRect222)


        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    sys.exit


def socketpiano():
    global lmusic
    global server_socket
    server_socket.bind(('192.168.1.16',1729))
    server_socket.listen(5)
    open_client_sockets = []
    while len(lmusic) == 0 or lmusic[0] != "False":
        rlist, wlist, xlist = select.select( [server_socket] + open_client_sockets, [], [] )
        for current_socket in rlist:
            if(len(lmusic) != 0 and lmusic[0] == "False"):
                break
            elif current_socket is server_socket:
                (new_socket, address) = server_socket.accept()
                open_client_sockets.append(new_socket)
            else:
                data = current_socket.recv(1024)
                if data == "":
                    open_client_sockets.remove(current_socket)
                    print ("Connection with client closed.")
                else:
                    if data.decode() != '':
                        lmusic.append(data.decode())
                        print (lmusic)

    server_socket.close()



def main():


    t1 = threading.Thread(target=socketpiano)
    t1.start()
    pysocket()

    pygame.quit()
    sys.exit
if __name__ == '__main__':
    main()