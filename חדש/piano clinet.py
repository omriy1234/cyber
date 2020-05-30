# -*- coding: utf-8 -*-
import pygame
import sys
import socket
import time
from music import Music
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import  threading


def main():
    string = "" #מחרוזת תווים
    strtime = "" #מחרוזת זמנים
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [600, 210] #גודל המסך
    bg = [200, 200, 255] #צבע המסך
    font = pygame.font.Font('freesansbold.ttf', 27)  #סוגי הפונטים והגדלים השונים
    font2 = pygame.font.SysFont('Parchment', 82)
    font3 = pygame.font.Font('freesansbold.ttf', 23)
    bool1 = False #שולט על אילו כפתורים יפעלו (האדומים והכתומים או הפסנתר)
    note = Music()
    color = [255,0,0] #משתנה האחראי על צבע כפתור play/ stop

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Piano") #שם מסך
    white =[255, 255, 255]
    black = [0, 0, 0]
    green = [0, 255, 0]

#הגדרת מיקום וגודל כפתורים
    button_c = pygame.Rect(10, 10, 50, 150)
    button_d = pygame.Rect(70, 10, 50, 150)
    button_e = pygame.Rect(130, 10, 50, 150)
    button_f = pygame.Rect(190, 10, 50, 150)
    button_g = pygame.Rect(250, 10, 50, 150)
    button_a = pygame.Rect(310, 10, 50, 150)
    button_b = pygame.Rect(370, 10, 50, 150)
    button_c2 = pygame.Rect(430, 10, 50, 150)

    button_db = pygame.Rect(50, 10, 30, 110)
    button_eb = pygame.Rect(110, 10, 30, 110)
    button_gb = pygame.Rect(230, 10, 30, 110)
    button_ab = pygame.Rect(290, 10, 30, 110)
    button_bb = pygame.Rect(350, 10, 30, 110)

    button_send = pygame.Rect(500, 10, 95, 35)
    button_clear = pygame.Rect(500, 50, 95, 25)
    button_play = pygame.Rect(500, 80, 95, 25)
    button_revers = pygame.Rect(500, 110, 95, 25)
    button_file_selection = pygame.Rect(500, 140, 95, 25)
    button_play_stop = pygame.Rect(500, 170, 95, 35)




#הגדרת הכתבים
    cw = font.render('C',True , black)
    cRect = cw.get_rect()
    cRect.center = (30, 130)

    dw = font.render('D', True, black)
    dRect = dw.get_rect()
    dRect.center = (95, 130)

    ew = font.render('E', True, black)
    eRect = ew.get_rect()
    eRect.center = (155, 130)

    fw = font.render('F', True, black)
    fRect = fw.get_rect()
    fRect.center = (215, 130)

    gw = font.render('G', True, black)
    gRect = gw.get_rect()
    gRect.center = (275, 130)

    aw = font.render('A', True, black)
    aRect = aw.get_rect()
    aRect.center = (335, 130)

    bw = font.render('B', True, black)
    bRect = bw.get_rect()
    bRect.center = (395, 130)

    cRect2 = cw.get_rect()
    cRect2.center = (455, 130)

    send = font.render('send', True, white)
    sendRect = send.get_rect()
    sendRect.center = (547, 30)

    clear = font.render('clear', True, white)
    clearRect = clear.get_rect()
    clearRect.center = (547, 65)

    play = font.render('play', True, white)
    playRect = play.get_rect()
    playRect.center = (547, 92)

    revers = font.render('revers', True, white)
    reversRect = revers.get_rect()
    reversRect.center = (547, 123)

    file_selection = font.render('select', True, white)
    file_selectionRect = file_selection.get_rect()
    file_selectionRect.center = (547, 155)

    play_stop1 = font3.render('play/', True, white)
    play_stopRect1 = play_stop1.get_rect()
    play_stopRect1.center = (540, 180)
    play_stop2 = font3.render('stop', True, white)
    play_stopRect2 = play_stop2.get_rect()
    play_stopRect2.center = (560, 195)

    db = font2.render('c#', True, white)
    dbRect = db.get_rect()
    dbRect.center = (65, 90)

    eb = font2.render('d#', True, white)
    ebRect = eb.get_rect()
    ebRect.center = (126, 90)

    gb = font2.render('f#', True, white)
    gbRect = gb.get_rect()
    gbRect.center = (245, 90)

    ab = font2.render('g#', True, white)
    abRect = ab.get_rect()
    abRect.center = (307, 90)

    bb = font2.render('a#', True, white)
    bbRect = bb.get_rect()
    bbRect.center = (366, 90)
      # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simpy type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom
    start_time = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #עצירת הרצת המסך
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                # checks if mouse position is over the button
                if button_play.collidepoint(mouse_pos) and not bool1:
                    pygame.draw.rect(screen, green, button_play)  #שינוי צבע כפתור בזמן לחיצה
                    pygame.display.update()
                    clock.tick(fps)
                    if note.bool == False: #אם נלחץ הכפתור פעם שנייה
                        note.bre = False #נעצר הרצת המוזיקה על ידי המחלקה
                    else:
                        note = Music(string, strtime)
                        t1 = threading.Thread(target=note.play_music)  #הרצת השמעת המוזיקה במקביל להצגת המסך
                        t1.start()
                elif note.bool == False: #מניעת לחיצת כפתורים בזמן שמיעת מוזיקה
                    break
                elif button_db.collidepoint(mouse_pos)and bool1:
                    string += " " + "#c" #הוספת תו למחרוזת תווים שנוגנו
                    strtime += str(time.time() - start_time) + " " #הוספת זמן מרווח למחרוזת הזמנים
                    start_time = time.time() #איפוס זמן התחלת המרווח
                    note.play_db() #השמעת צליל
                elif button_eb.collidepoint(mouse_pos)and bool1:
                    string += " " +"#d"
                    strtime += str(time.time() - start_time) + " "
                    start_time = time.time()
                    note.play_eb()
                elif button_gb.collidepoint(mouse_pos)and bool1:
                    string += " " +"#f"
                    strtime += str(time.time() - start_time) + " "
                    start_time = time.time()
                    note.play_gb()
                elif button_ab.collidepoint(mouse_pos)and bool1:
                    string += " " +"#g"
                    strtime += str(time.time() - start_time) + " "
                    start_time = time.time()
                    note.play_ab()
                elif button_bb.collidepoint(mouse_pos)and bool1:
                    string += " " +"#a"
                    note.play_bb()
                elif button_c.collidepoint(mouse_pos)and bool1:
                    # prints current location of mouse
                    string += " " +"do"
                    strtime += str(time.time() - start_time) + " "
                    start_time = time.time()
                    note.play_do()
                elif button_d.collidepoint(mouse_pos)and bool1:
                    string += " " +"re"
                    strtime += str(time.time() - start_time) + " "
                    start_time = time.time()
                    note.play_re()
                elif button_e.collidepoint(mouse_pos)and bool1:
                    string += " " +"mi"
                    strtime += str(time.time() - start_time) + " "
                    start_time = time.time()
                    note.play_mi()
                elif button_f.collidepoint(mouse_pos)and bool1:
                    string += " " +"fa"
                    strtime += str(time.time() - start_time) + " "
                    start_time = time.time()
                    note.play_fa()
                elif button_g.collidepoint(mouse_pos)and bool1:
                    string += " " +"sol"
                    strtime += str(time.time() - start_time) + " "
                    start_time = time.time()
                    note.play_sol()
                elif button_a.collidepoint(mouse_pos)and bool1:
                    string += " " +"la"
                    strtime += str(time.time() - start_time) + " "
                    start_time = time.time()
                    note.play_la()
                elif button_b.collidepoint(mouse_pos)and bool1:
                    string += " " +"ci"
                    strtime += str(time.time() - start_time) + " "
                    start_time = time.time()
                    note.play_ci()
                elif button_c2.collidepoint(mouse_pos)and bool1:
                    string += " " +"do2"
                    strtime += str(time.time() - start_time) + " "
                    start_time = time.time()
                    note.play_do2()
                elif button_send.collidepoint(mouse_pos)and not bool1:
                    #התקשרות לשרת
                    my_socket = socket.socket()
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    ipsocket = ('192.168.1.16',1729)
                    result = sock.connect_ex(ipsocket)
                    if result == 0: #בדיקה עם השרת פועל
                        my_socket.connect(ipsocket)
                        listtime = strtime.split()
                        if len(listtime) != 0:
                            listtime[0] = "0.0" #איפוס הזמן הראשון (שיתחיל את הנגינה)
                        strtime = str(listtime).replace("[","").replace("]","").replace("'","").replace(",","")
                        string += " stop " + strtime #חיבור 2 המחרוזות למחרוזת אחת. שמפריד בניהן המילה stop
                        my_socket.send( string.encode()) #שליחת המחרוזות לשרת
                        string = "" #איפוס המחרוזות
                        strtime = ""
                        pygame.draw.rect(screen, green, button_send)  # draw button
                        pygame.display.update()
                        clock.tick(fps)

                elif button_clear.collidepoint(mouse_pos)and not bool1:
                    pygame.draw.rect(screen, green, button_clear)  # draw button
                    pygame.display.update()
                    clock.tick(fps)
                    string = "" #איפוס המחרוזות
                    strtime = ""



                elif button_revers.collidepoint(mouse_pos)and not bool1:
                    pygame.draw.rect(screen, green, button_revers)  # draw button
                    pygame.display.update()
                    clock.tick(fps)
                    listnote = string.split()
                    listnote = listnote[::-1] #היפוך התווים
                    string = str(listnote).replace("[","").replace("]","").replace("'","").replace(",","")
                    listtime = strtime.split()
                    listtime = listtime[::-1] #היפוך הזמנים
                    strtime = str(listtime).replace("[","").replace("]","").replace("'","").replace(",","")

                elif button_file_selection.collidepoint(mouse_pos)and not bool1:
                    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
                    pygame.quit()
                    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
                    print(filename)
                    screen = pygame.display.set_mode(size)
                    if not(str(filename) == "" or str(filename)[::-1][0:4][::-1] != ".txt"): #בדיקה שסוג הקובץ תקין
                        input_file = open(r''+ filename,'r') #פתיחת קובץ לקריאה
                        notes = input_file.read().replace('\n', " ").split()
                        if len(strtime.split()) != len(string.split()):
                            strtime += "0.0 "
                        for j in notes:
                            if not(j != "do" and j != "re" and j != "mi" and j != "fa" and j != "sol" and j != "la" and j != "ci" and j != "do2" and j != "#c" and j != "#d" and j != "#f" and j != "#g" and j != "#a"):
                                string += " " + j
                            else:
                                num2 = ""
                                point = True
                                for i in j:#מציאת מספרים בקובץ
                                    if (i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8"or i == "9"):
                                        num2 += i
                                    elif i == "." and point:
                                        num2 += i
                                        point = False
                                if(num2 != ""):
                                    strtime += num2 + " "
                                                                        #טיפול במצבים בהם מספר הממעברים לא תואם למספר התווים שהוכנסו

                        if len(strtime.split()) < len(string.split()):
                            while len(strtime.split()) != len(string.split()):
                                strtime += "0.8 "
                        elif len(strtime.split()) > len(string.split()):
                            strtime = strtime.split()
                            while len(strtime) != len(string.split()):
                                del strtime[-1]
                            strtime = str(strtime).replace("[","").replace("]","").replace("'","").replace(",","")
                        input_file.close() #סגירת עריכת קובץ
                    strtime += " "
                    print (strtime)
                    print (string)

                elif button_play_stop.collidepoint(mouse_pos):
                    bool1 = not bool1
                    start_time = time.time()
                    if bool1: #שינוי צבע הכפתור
                        color = [0,255,0]
                    else:
                        color = [255,0,0]









        screen.fill(bg)
        #הרצת הכפתורים
        pygame.draw.rect(screen, white, button_c)  # draw button
        pygame.draw.rect(screen, white, button_d)  # draw button
        pygame.draw.rect(screen, white, button_e)  # draw button
        pygame.draw.rect(screen, white, button_f)  # draw button
        pygame.draw.rect(screen, white, button_g)  # draw button
        pygame.draw.rect(screen, white, button_a)  # draw button
        pygame.draw.rect(screen, white, button_b)  # draw button
        pygame.draw.rect(screen, white, button_c2)  # draw button
        pygame.draw.rect(screen, black, button_db)  # draw button
        pygame.draw.rect(screen, black, button_eb)  # draw button
        pygame.draw.rect(screen, black, button_gb)  # draw button
        pygame.draw.rect(screen, black, button_ab)  # draw button
        pygame.draw.rect(screen, black, button_bb)  # draw button
        pygame.draw.rect(screen, [255, 100, 0], button_send)  # draw button
        pygame.draw.rect(screen, [255, 170, 0], button_clear)  # draw button
        pygame.draw.rect(screen, [255, 170, 0], button_play)  # draw button
        pygame.draw.rect(screen, [255, 170, 0], button_revers)  # draw button
        pygame.draw.rect(screen, [255, 170, 0], button_file_selection)  # draw button
        pygame.draw.rect(screen, color, button_play_stop)  # draw button

#הרצת הכתבים
        screen.blit(cw, cRect)
        screen.blit(dw, dRect)
        screen.blit(ew, eRect)
        screen.blit(fw, fRect)
        screen.blit(gw, gRect)
        screen.blit(aw, aRect)
        screen.blit(bw, bRect)
        screen.blit(cw, cRect2)
        screen.blit(send, sendRect)
        screen.blit(clear, clearRect)
        screen.blit(play, playRect)
        screen.blit(revers, reversRect)
        screen.blit(file_selection, file_selectionRect)
        screen.blit(db, dbRect)
        screen.blit(eb, ebRect)
        screen.blit(gb, gbRect)
        screen.blit(ab, abRect)
        screen.blit(bb, bbRect)
        screen.blit(play_stop1, play_stopRect1)
        screen.blit(play_stop2, play_stopRect2)


        pygame.display.update()
        clock.tick(fps)

#סגירת הרשתות והpygame
    my_socket.close()
    pygame.quit()
    sys.exit

if __name__ == '__main__':
    main()