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
    string = ""
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [600, 200]
    bg = [200, 200, 255]
    font = pygame.font.Font('freesansbold.ttf', 27)
    font2 = pygame.font.SysFont('Parchment', 82)

    note = Music(size)

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Piano")


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

    button_send = pygame.Rect(500, 10, 95, 45)
    button_clear = pygame.Rect(500, 60, 95, 30)
    button_play = pygame.Rect(500, 95, 95, 30)
    button_revers = pygame.Rect(500, 130, 95, 30)
    button_file_selection = pygame.Rect(500, 165, 95, 30)




    cw = font.render('C',True , [0, 0, 0])
    cRect = cw.get_rect()
    cRect.center = (30, 130)

    dw = font.render('D', True, [0, 0, 0])
    dRect = dw.get_rect()
    dRect.center = (95, 130)

    ew = font.render('E', True, [0, 0, 0])
    eRect = ew.get_rect()
    eRect.center = (155, 130)

    fw = font.render('F', True, [0, 0, 0])
    fRect = fw.get_rect()
    fRect.center = (215, 130)

    gw = font.render('G', True, [0, 0, 0])
    gRect = gw.get_rect()
    gRect.center = (275, 130)

    aw = font.render('A', True, [0, 0, 0])
    aRect = aw.get_rect()
    aRect.center = (335, 130)

    bw = font.render('B', True, [0, 0, 0])
    bRect = bw.get_rect()
    bRect.center = (395, 130)

    cRect2 = cw.get_rect()
    cRect2.center = (455, 130)

    send = font.render('send', True, [255, 255, 255])
    sendRect = send.get_rect()
    sendRect.center = (547, 35)

    clear = font.render('clear', True, [255, 255, 255])
    clearRect = clear.get_rect()
    clearRect.center = (547, 75)

    play = font.render('play', True, [255, 255, 255])
    playRect = play.get_rect()
    playRect.center = (547, 110)

    revers = font.render('revers', True, [255, 255, 255])
    reversRect = revers.get_rect()
    reversRect.center = (547, 145)

    file_selection = font.render('select', True, [255, 255, 255])
    file_selectionRect = file_selection.get_rect()
    file_selectionRect.center = (547, 180)

    db = font2.render('c#', True, [255, 255, 255])
    dbRect = db.get_rect()
    dbRect.center = (65, 90)

    eb = font2.render('d#', True, [255, 255, 255])
    ebRect = eb.get_rect()
    ebRect.center = (126, 90)

    gb = font2.render('f#', True, [255, 255, 255])
    gbRect = gb.get_rect()
    gbRect.center = (245, 90)

    ab = font2.render('g#', True, [255, 255, 255])
    abRect = ab.get_rect()
    abRect.center = (307, 90)

    bb = font2.render('a#', True, [255, 255, 255])
    bbRect = bb.get_rect()
    bbRect.center = (366, 90)
      # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simpy type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                # checks if mouse position is over the button
                if button_play.collidepoint(mouse_pos):
                    note.play_click()
                    if note.bool == False:
                        note.bre = False
                    else:
                        note = Music(string)
                        t1 = threading.Thread(target=note.play_music)
                        t1.start()
                elif note.bool == False:
                    break
                elif button_db.collidepoint(mouse_pos):
                    string += " " + "#c"
                    note.play_db()
                elif button_eb.collidepoint(mouse_pos):
                    string += " " +"#d"
                    note.play_eb()
                elif button_gb.collidepoint(mouse_pos):
                    string += " " +"#f"
                    note.play_gb()
                elif button_ab.collidepoint(mouse_pos):
                    string += " " +"#g"
                    note.play_ab()
                elif button_bb.collidepoint(mouse_pos):
                    string += " " +"#a"
                    note.play_bb()
                elif button_c.collidepoint(mouse_pos):
                    # prints current location of mouse
                    string += " " +"do"
                    note.play_do()
                elif button_d.collidepoint(mouse_pos):
                    string += " " +"re"
                    note.play_re()
                elif button_e.collidepoint(mouse_pos):
                    string += " " +"mi"
                    note.play_mi()
                elif button_f.collidepoint(mouse_pos):
                    string += " " +"fa"
                    note.play_fa()
                elif button_g.collidepoint(mouse_pos):
                    string += " " +"sol"
                    note.play_sol()
                elif button_a.collidepoint(mouse_pos):
                    string += " " +"la"
                    note.play_la()
                elif button_b.collidepoint(mouse_pos):
                    string += " " +"ci"
                    note.play_ci()
                elif button_c2.collidepoint(mouse_pos):
                    string += " " +"do2"
                    note.play_do2()
                elif button_send.collidepoint(mouse_pos):
                    my_socket = socket.socket()
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    ipsocket = ('192.168.1.16',1729)
                    result = sock.connect_ex(ipsocket)
                    if result == 0:
                        my_socket.connect(ipsocket)
                        my_socket.send( string.encode())
                        string = ""
                        note.play_click()
                elif button_clear.collidepoint(mouse_pos):
                    string = ""
                    note.play_click()


                elif button_revers.collidepoint(mouse_pos):
                    listnote = string.split()
                    listnote = listnote[::-1]
                    string = str(listnote).replace("[","").replace("]","").replace("'","").replace(",","")
                    note.play_click()

                elif button_file_selection.collidepoint(mouse_pos):
                    note.play_click()
                    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
                    pygame.quit()
                    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
                    print(filename)
                    screen = pygame.display.set_mode(size)
                    if not(str(filename) == "" or str(filename)[::-1][0:4][::-1] != ".txt"):
                        input_file = open(r''+ filename,'r')
                        notes = input_file.read().replace('\n', " ").split()
                        for j in notes:
                            if not(j != "do" and j != "re" and j != "mi" and j != "fa" and j != "sol" and j != "la" and j != "ci" and j != "do2" and j != "#c" and j != "#d" and j != "#f" and j != "#g" and j != "#a"):
                                string += " " + j
                        input_file.close()






        screen.fill(bg)
        pygame.draw.rect(screen, [255, 255, 255], button_c)  # draw button
        pygame.draw.rect(screen, [255, 255, 255], button_d)  # draw button
        pygame.draw.rect(screen, [255, 255, 255], button_e)  # draw button
        pygame.draw.rect(screen, [255, 255, 255], button_f)  # draw button
        pygame.draw.rect(screen, [255, 255, 255], button_g)  # draw button
        pygame.draw.rect(screen, [255, 255, 255], button_a)  # draw button
        pygame.draw.rect(screen, [255, 255, 255], button_b)  # draw button
        pygame.draw.rect(screen, [255, 255, 255], button_c2)  # draw button
        pygame.draw.rect(screen, [0, 0, 0], button_db)  # draw button
        pygame.draw.rect(screen, [0, 0, 0], button_eb)  # draw button
        pygame.draw.rect(screen, [0, 0, 0], button_gb)  # draw button
        pygame.draw.rect(screen, [0, 0, 0], button_ab)  # draw button
        pygame.draw.rect(screen, [0, 0, 0], button_bb)  # draw button
        pygame.draw.rect(screen, [255, 0, 0], button_send)  # draw button
        pygame.draw.rect(screen, [255, 120, 0], button_clear)  # draw button
        pygame.draw.rect(screen, [255, 120, 0], button_play)  # draw button
        pygame.draw.rect(screen, [255, 120, 0], button_revers)  # draw button
        pygame.draw.rect(screen, [255, 120, 0], button_file_selection)  # draw button


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

        pygame.display.update()
        clock.tick(fps)

    my_socket.close()
    pygame.quit()
    sys.exit

if __name__ == '__main__':
    main()