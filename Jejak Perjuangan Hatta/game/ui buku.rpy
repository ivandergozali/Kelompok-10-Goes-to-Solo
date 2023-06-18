define blink = 0 
define unlock = 0 

image notifikasi:
    "notif 1"
    pause 0.6
    "notif 2"
    pause 0.6
    repeat

screen buku:
    frame:
        xpos 1120 ypos 30
        vbox:
            imagebutton:
                if blink == 0:
                    idle "buku 1"
                elif blink == 1:
                    idle "notifikasi"
                action [SetVariable("blink", 0), SetVariable("quick_menu", False), ShowMenu("pilihanbuku")]

screen bantuan:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan"), Show("pilihanbuku")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen pilihanbuku: 
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 180
            button:
                text "Karakter" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B" hover_underline True
                action [Hide("pilihanbuku"), Show("karakter")]   
            button:
                text "Peristiwa" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B" hover_underline True 
                action [Hide("pilihanbuku"), Show("peristiwa")]
            button:
                text "Organisasi" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B" hover_underline True
                action [Hide("pilihanbuku"), Show("organisasi")]
            button:
                text "Negara" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B" hover_underline True
                action [Hide("pilihanbuku"), Show("negara")]
            button:
                text "Bacaan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B" hover_underline True
                action [Hide("pilihanbuku"), Show("bacaan")]
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("pilihanbuku"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("pilihanbuku"), Show("bantuan")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
    
screen bantuan_karakter:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_karakter"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter"), Show("karakter")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen karakter:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")    
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"    
        if unlock == 0:
            vbox:
                xpos 780 ypos 150
                spacing 15  
                text "Karakter" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "Soekarno" size 28 hover_underline True color "#000000" 
                    action [Hide("karakter"), Show("karakter1")]
                button:
                    text "Hatta" size 28 hover_underline True color "#000000" 
                    action [Hide("karakter"), Show("karakter2_1")]
                button:
                    text "Adolf Hitler" size 28 hover_underline True color "#000000" 
                    action [Hide("karakter"), Show("karakter3")]
                button:
                    text "Marx dan Engels" size 28 hover_underline True color "#7F7F7F"
                    action [Play("sound","audio/SFX/invalid.mp3")]
                button:
                    text "Douglas MacArthur" size 28 hover_underline True color "#7F7F7F"
                    action [Play("sound","audio/SFX/invalid.mp3")]
                button:
                    text "Chester W. Nimitz" size 28 hover_underline True color "#7F7F7F"
                    action [Play("sound","audio/SFX/invalid.mp3")]
                add "images/Icon/lock.png" xpos -30 ypos -155
                add "images/Icon/lock.png" xpos -30 ypos -147
                add "images/Icon/lock.png" xpos -30 ypos -140
        elif unlock == 1 or unlock == 2 or unlock == 3 or unlock == 4 or unlock == 5:
            vbox:
                xpos 780 ypos 150
                spacing 15  
                text "Karakter" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "Soekarno" size 28 hover_underline True color "#000000" 
                    action [Hide("karakter"), Show("karakter1")]
                button:
                    text "Hatta" size 28 hover_underline True color "#000000" 
                    action [Hide("karakter"), Show("karakter2_1")]
                button:
                    text "Adolf Hitler" size 28 hover_underline True color "#000000"
                    action [Hide("karakter"), Show("karakter3")]
                button:
                    text "Marx dan Engels" size 28 hover_underline True color "#000000"
                    action [Hide("karakter"), Show("karakter4")]
                button:
                    text "Douglas MacArthur" size 28 hover_underline True color "#7F7F7F"
                    action [Play("sound","audio/SFX/invalid.mp3")]
                button:
                    text "Chester W. Nimitz" size 28 hover_underline True color "#7F7F7F"
                    action [Play("sound","audio/SFX/invalid.mp3")]
                add "images/Icon/lock.png" xpos -30 ypos -104
                add "images/Icon/lock.png" xpos -30 ypos -96
        else:
            vbox:
                xpos 780 ypos 150
                spacing 15  
                text "Karakter" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "Soekarno" size 28 hover_underline True color "#000000" 
                    action [Hide("karakter"), Show("karakter1")]
                button:
                    text "Hatta" size 28 hover_underline True color "#000000" 
                    action [Hide("karakter"), Show("karakter2_1")]
                button:
                    text "Adolf Hitler" size 28 hover_underline True color "#000000" 
                    action [Hide("karakter"), Show("karakter3")]
                button:
                    text "Marx dan Engels" size 28 hover_underline True color "#000000"
                    action [Hide("karakter"), Show("karakter4")]
                button:
                    text "Douglas MacArthur" size 28 hover_underline True color "#000000"
                    action [Hide("karakter"), Show("karakter5")]
                button:
                    text "Chester W. Nimitz" size 28 hover_underline True color "#000000"
                    action [Hide("karakter"), Show("karakter6")]
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("karakter"), Return()]   
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter"), Show("bantuan_karakter")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter"), Show("pilihanbuku")]

    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_karakter1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_karakter1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter1"), Show("karakter1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen karakter1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Soekarno" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/foto soekarno.png"
        vbox:
            xpos 385 ypos 455
            text "Sumber:\nhttps://id.wikipedia.org/wiki/Soekarno" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Lahir di Surabaya pada 6 Juni 1901, ayahnya bernama Raden Soekemi Sosrodihardjo dan ibunya Ida Njoman Rai. Nama awalnya adalah Koesno tetapi diganti Soekarno karena waktu masih muda beliau sempat sakit. Setelah menamati pendidikan teknik sipil di Bandung pada tahun 1927, Soekarno mulai turun ke dalam perpolitikan Hindia Belanda, karena perpolitikan juga Soekarno sempat dibuang oleh pemerintah Hindia Belanda di Flores dan Sumatra. Dengan datangnya Jepang di Hindia Belanda, Soekarno sempat ingin dipindahkan ke Australia, namun Jepang dapat menghentikan rencana tersebut dan membawa Soekarno kembali ke Jakarta pada Juli 1942. Dengan bekerjasama dengan Jepang. Soekarno diberi wadah untuk menyebarkan gagasan kenegaraan dan nasionalisme ke seluruh penjuru Indonesia. Dalam pergerakan kemerdekaan Indonesia Soekarno dan Hatta merupakan tokoh sentral dalam perjuangan tersebut." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("karakter1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter1"), Show("bantuan_karakter1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter1"), Show("karakter")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_karakter2_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_karakter2_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter2_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter2_1"), Show("karakter2_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen karakter2_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Hatta" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/foto hatta.png"
        vbox:
            xpos 385 ypos 455
            text "Sumber:\nhttps://id.wikipedia.org/wiki/Mohammad_Hatta" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Lahir di Bukittinggi pada 12 Agustus 1902. Lahir dengan keluarga ibu yang merupakan pebisnis dan keluarga ayah yang keturunan ulama membuat Hatta dari kecil sudah mendalami Islam dan ekonomi. Setelah menyelesaikan sekolah di Batavia, Hatta melanjutkan studinya di Belanda lebih tepatnya di Sekolah Bisnis Rotterdam. Saat mengenyam pendidikan di Belanda inilah Hatta mulai aktif dalam pergerakan kemerdekaan Indonesia dengan berga Perhimpunan Indonesia. Ketika aktivitas perpolitikan PI mulai meresahkan Belanda, otoritas Belanda menangkap tokoh-tokoh PI termasuk Hatta dan memenjarakannya di Den Hag pada Juni 1927. Hatta memanfaatkan sidang pembelaannya untuk membela kemerdekaan Indonesia, pidatonya itu berjudul Indonesia Vrij (Indonesia Merdeka) berhasil terkenal di Belanda. Pada tahun 1932, Hatta kembali ke Hindia Belanda dan menjadi ketua dari PNI Baru (Pendidikan Nasional Indonesia) setelah PNI (Partai" size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("karakter2_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter2_1"), Show("bantuan_karakter2_1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter2_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter2_1"), Show("karakter")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("karakter2_1"), Show("karakter2_2")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("karakter2_1"), Show("karakter2_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_karakter2_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_karakter2_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter2_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter2_2"), Show("karakter2_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen karakter2_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Hatta" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/foto hatta.png"
        vbox:
            xpos 385 ypos 455
            text "Sumber:\nhttps://id.wikipedia.org/wiki/Mohammad_Hatta" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Nasional Indonesia) dibubarkan oleh pemerintah kolonial. Karirnya tidak bertahan lama, karena pada Februari 1934 ia ditangkap dan beberapa tahun kemudian berpindah pindah dari Glodok ke Boven Digoel ke Banda Neira dan terakhir ke Sukabumi sebelum Jepang datang. Hatta dari awal sudah curiga dengan kedatangan Jepang sebagai “pembebas”, tapi pada akhirnya Hatta setuju bekerja sama dengan Jepang bersama Soekarno. Dalam pergerakan kemerdekaan Indonesia Soekarno dan Hatta merupakan tokoh sentral dalam perjuangan tersebut." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("karakter2_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter2_2"), Show("bantuan_karakter2_2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter2_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter2_2"), Show("karakter")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("karakter2_2"), Show("karakter2_1")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("karakter2_2"), Show("karakter2_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_karakter3:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_karakter3"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter3"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter3"), Show("karakter3")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen karakter3:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Adolf Hitler" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/foto hitler.png"
        vbox:
            xpos 385 ypos 455
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Adolf_Hitler\nhttps://www.history.com/topics/world-war-ii/adolf-\nhitler-1#section_4\nhttps://kumparan.com/ciptalennon/bung-hatta-dan-\nhewan-peliharaan-kesayangannya-1wO1XVyKngS" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Lahir pada tanggal 20 April 1889, Hitler dikenal sebagai sosok yang membawa dunia ke Perang Dunia II. Hitler sebelumnya berusaha mengambil alih kekuasaan dengan revolusi yang disebut “Beer Hall Putsch” pada tahun 1923. Hitler berhasil mendapatkan posisi Kanselir pada tahun 1933 dibawah Presiden Paul von Hindenburg, tetapi setahun kemudian Paul meninggal sehingga Jerman jatuh pada kendali Hitler seutuhnya pada tahun 1934. Pada 1 September 1939, Jerman dibawah arahan Hitler menginvasi Polandia, invasi inilah pemicu Perang Dunia II di Eropa. Hitler berhasil menguasai setengah eropa termasuk Belanda pada puncak kekuatannya, namun tetap saja Hitler dapat dikalahkan dan Hitler sendiri tewas pada 30 April 1945. Hatta sangat membenci Hitler karena kekejaman dan pandangan politiknya, sampai-sampai salah satu kucing beliau ia beri nama Hitler." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("karakter3"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter3"), Show("bantuan_karakter3")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter3"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter3"), Show("karakter")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_karakter4:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_karakter4"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter4"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter4"), Show("karakter4")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen karakter4:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Marx dan Engels" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/foto marx dan engels.png"
        vbox:
            xpos 385 ypos 345
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Karl_Marx\nhttps://en.wikipedia.org/wiki/Friedrich_Engels" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Kedua tokoh sosialisme eropa ini berasal dari Jerman, dimana Marx lahir pada 1818 dan Engels pada tahun 1820. Keduanya bertemu di Paris pada tahun 1844 dan segera menjadi rekan seperjuangan, keduanya sama-sama mengkritisi sistem ekonomi kapitalisme dan eksploitasi kaum buruh di tangan kaum pemodal. Keduanya yakin akan adanya perlawanan berupa revolusi dari kaum buruh yang akan menghancurkan sistem perekonomian kapitalisme dan menjadikan kaum buruh sebagai penguasa sistem perekonomian baru. Gagasannya ini disebut sebagai Sosialisme Revolusioner dan gerakan sosialisme revolusioner ini terjadi di Rusia pada tahun 1917." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("karakter3"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter4"), Show("bantuan_karakter4")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter4"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter4"), Show("karakter")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_karakter5:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_karakter5"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter5"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter5"), Show("karakter5")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen karakter5:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Douglas MacArthur" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/foto macarthur.png"
        vbox:
            xpos 385 ypos 455
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Douglas_MacArthur" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Doughlas MacArthur adalah Panglima Sekutu pada masa Perang Dunia II, beliau lahir pada 26 Januari 1880 di Amerika Serikat. MacArthur sedang berada di Filipina saat Jepang menginvasi negara tersebut, tetapi beliau mengundurkan diri ke Australia saat keadaan di Filipina semakin buruk pada Februari 1942. Setelah itu MacArthur bertanggung jawab dengan kampanye perang Sekutu di daerah Asia Barat Daya, bersama Nimitz keduanya melakukan kampanye-kampanye besar di Papua Nugini, pulau-pulau luar Jepang, berhasil merebut kembali Filipina pada Juli 1945, dan sempat melakukan operasi di bagian utara Borneo sampai 15 Agustus 1945. Pada akhirnya MacArthur menerima secara formal menyerahnya Jepang pada Sekutu di kapal USS Missouri pada 2 September 1945." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("karakter5"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter5"), Show("bantuan_karakter5")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter5"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter5"), Show("karakter")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_karakter6:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_karakter6"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter6"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_karakter6"), Show("karakter6")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen karakter6:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Chester W. Nimitz" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/foto nimitz.png"
        vbox:
            xpos 385 ypos 455
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Chester_W._Nimitz" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Chester W. Nimitz lahir pada 24 Februari 1885. Setelah serangan Jepang pada Pearl Harbor pada 7 Desember 1941, Nimitz diangkan menjadi komando Armada Pasifik Amerika Serikat. Nimitz memulai kampanyenya di laut Pasifik, dengan cara merebut pulau-pulau Pasifik yang dikuasai Jepang. Nimitz berhasil memorak-morandakan Angkatan Laut Jepang di pertempuran Midway pada tahun 1942, kemenangan ini membuat Jepang semakin berhati-hati untuk mengeluarkan Armadanya sehingga memudahkan Nimitz melakukan kampanye Pasifiknya. Jepang semakin terpojok dengan jatuhnya Iwo Jima pada Maret 1945 dan Okinawa pada Juni 1945 oleh Nimitz, ditambah dengan dua bom atom dan invasi Rusia, Jepang akhirnya menyerah pada 15 Agustus 1945. Nimitz menjadi salah satu perwakilan Sekutu dalam kapalnya USS Missouri untuk menerima secara formal menyerahnya Jepang." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("karakter5"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter6"), Show("bantuan_karakter6")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter6"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("karakter6"), Show("karakter")]

    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_peristiwa:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_peristiwa"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa"), Show("peristiwa")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen peristiwa:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")    
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"    
        if unlock == 0 or unlock == 1 or unlock == 2 or unlock == 3:
            vbox:
                xpos 780 ypos 165
                spacing 15  
                text "Peristiwa" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "Pemboman Hiroshima \ndan Nagasaki" size 28 hover_underline True color "#000000" 
                    action [Hide("peristiwa"), Show("peristiwa1_1")]
                button:
                    text "Sidang Pertama \nBPUPKI" size 28 hover_underline True color "#7F7F7F" 
                    action [Play("sound","audio/SFX/invalid.mp3")]
                button:
                    text "Invasi Rusia di Asia" size 28 hover_underline True color "#7F7F7F"
                    action [Play("sound","audio/SFX/invalid.mp3")]
                button:
                    text "Beer Hall Putsch" size 28 hover_underline True color "#7F7F7F" 
                    action [Play("sound","audio/SFX/invalid.mp3")]
                add "images/Icon/lock.png" xpos -30 ypos -170
                add "images/Icon/lock.png" xpos -30 ypos -150
                add "images/Icon/lock.png" xpos -30 ypos -140
        elif unlock == 4:
            vbox:
                xpos 780 ypos 165
                spacing 15  
                text "Peristiwa" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "Pemboman Hiroshima \ndan Nagasaki" size 28 hover_underline True color "#000000" 
                    action [Hide("peristiwa"), Show("peristiwa1_1")]
                button:
                    text "Sidang Pertama \nBPUPKI" size 28 hover_underline True color "#000000" 
                    action [Hide("peristiwa"), Show("peristiwa2_1")]
                button:
                    text "Invasi Rusia di Asia" size 28 hover_underline True color "#7F7F7F"
                    action [Play("sound","audio/SFX/invalid.mp3")]
                button:
                    text "Beer Hall Putsch" size 28 hover_underline True color "#7F7F7F" 
                    action [Play("sound","audio/SFX/invalid.mp3")]
                add "images/Icon/lock.png" xpos -30 ypos -105
                add "images/Icon/lock.png" xpos -30 ypos -95
        elif unlock == 5 or unlock == 6:
            vbox:
                xpos 780 ypos 165
                spacing 15  
                text "Peristiwa" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "Pemboman Hiroshima \ndan Nagasaki" size 28 hover_underline True color "#000000" 
                    action [Hide("peristiwa"), Show("peristiwa1_1")]
                button:
                    text "Sidang Pertama \nBPUPKI" size 28 hover_underline True color "#000000" 
                    action [Hide("peristiwa"), Show("peristiwa2_1")]
                button:
                    text "Invasi Rusia di Asia" size 28 hover_underline True color "#000000"
                    action [Hide("peristiwa"), Show("peristiwa3")]
                button:
                    text "Beer Hall Putsch" size 28 hover_underline True color "#7F7F7F" 
                    action [Play("sound","audio/SFX/invalid.mp3")]
                add "images/Icon/lock.png" xpos -30 ypos -51
        else:
            vbox:
                xpos 780 ypos 165
                spacing 15  
                text "Peristiwa" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "Pemboman Hiroshima \ndan Nagasaki" size 28 hover_underline True color "#000000" 
                    action [Hide("peristiwa"), Show("peristiwa1_1")]
                button:
                    text "Sidang Pertama \nBPUPKI" size 28 hover_underline True color "#000000" 
                    action [Hide("peristiwa"), Show("peristiwa2_1")]
                button:
                    text "Invasi Rusia di Asia" size 28 hover_underline True color "#000000"
                    action [Hide("peristiwa"), Show("peristiwa3")]
                button:
                    text "Beer Hall Putsch" size 28 hover_underline True color "#000000" 
                    action [Hide("peristiwa"), Show("peristiwa4_1")]
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("peristiwa"), Return()]   
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa"), Show("bantuan_peristiwa")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa"), Show("pilihanbuku")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_peristiwa1_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_peristiwa1_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa1_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa1_1"), Show("peristiwa1_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen peristiwa1_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Pemboman Hiroshima \ndan Nagasaki" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 180
            add "images/Konten/peristiwa pemboman hiroshima nagasaki.png"
        vbox:
            xpos 385 ypos 390
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Atomic_bombings_of_\nHiroshima_and_Nagasaki" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Pada pertengahan 1945, Jepang sudah berada diujung tanduk. Mereka terus menerus menerima berita kekalahan dimanapun, tetapi mereka masih menolak untuk menyerah. Sekutu sudah mulai mempersiapkan rencana invasi kepulauan inti Jepang, invasi ini diestimasikan akan menjadi invasi yang sangat mahal dan akan membuat kehancuran dan korban yang sangat besar pada kedua kubu. Rencana alternatif adalah menggunakan senjata baru yang dikembangkan oleh Sekutu, yaitu bom atom. Pembuatan bom atom ini berada dibawah “Projek Manhattan”, proyek ini melibatkan banyak ilmuan-ilmuan internasional termasuk ilmuan-ilmuan dari kubu Jerman yang membelot, Setelah menghasilkan dua bom atom bernama “Little Boy” dan “Fat Man”, langkah selanjutnya bagi Sekutu adalah menentukan dimana bom ini akan dijatuhkan. Hiroshima adalah korban pertama bom “Little Boy” pada 6 Agustus 1945, kota ini dipilih karena memiki industri militer dan merupakan titik temu komunikasi" size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("peristiwa1_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa1_1"), Show("bantuan_peristiwa1_1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa1_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa1_1"), Show("peristiwa")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("peristiwa1_1"), Show("peristiwa1_2")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("peristiwa1_1"), Show("peristiwa1_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_peristiwa1_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_peristiwa1_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa1_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa1_2"), Show("peristiwa1_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen peristiwa1_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Pemboman Hiroshima \ndan Nagasaki" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 180
            add "images/Konten/peristiwa pemboman hiroshima nagasaki.png"
        vbox:
            xpos 385 ypos 390
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Atomic_bombings_of_\nHiroshima_and_Nagasaki" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "bagian selatan Jepang. 70.000-80.000 jiwa meninggal karena bom ini, tetapi Jepang masih menolak untuk menyerah. Pada 9 Agustus “Fat Man” diledakan di Nagasaki dan 30.000-45.000 jiwa meninggal dalam ledakan ini, Nagasaki dipilih karena merupakan kota pelabuhan terbesar di selatan Jepang. Jepang awalnya masih belum mau menyerah, tapi dengan ancaman akan lebih banyak bom diledakan dan invasi Rusia di Manchuria Jepang memutuskan untuk menyerah." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("peristiwa1_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa1_2"), Show("bantuan_peristiwa1_2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa1_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa1_2"), Show("peristiwa")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("peristiwa1_2"), Show("peristiwa1_1")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("peristiwa1_2"), Show("peristiwa1_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_peristiwa2_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_peristiwa2_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa2_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa2_1"), Show("peristiwa2_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen peristiwa2_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Sidang Pertama \nBPUPKI" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 180
            add "images/Konten/peristiwa sidang pertama bpupki.png"
        vbox:
            xpos 385 ypos 390
            text "Sumber:\nhttps://id.wikipedia.org/wiki/Badan_Penyelidik_Usaha-\nUsaha_Persiapan_Kemerdekaan#Sidang_resmi_pertama" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Setelah BPUPKI didirikan pada 29 April, BPUPKI mengadakan sidang pertamanya pada 28 Mei sampai 1 Juni 1945 di gedung Chou Sangi In yang sekarang menjadi Gedung Pancasila, sidang ini diadakan untuk menentukan dasar negara Indonesia. Semuanya sepakat dengan negara kesatuan dan konstitusi segera dirumuskan, dengan inilah Undang-Undang Dasar Indonesia dirumuskan. Dalam rapat ini tiga tokoh pergerakan nasional memberikan pidato pandangannya masing-masing, ketiga tokoh itu adalah Mohammad Yamin. Soepomo, dan Soekarno. Pada 29 Mei 1945 Mohammad Yamin menyampaikan lima asas dasar negara yaitu “1. Peri Kebangsaan, 2. Peri Kemanusiaan, 3. Peri Ketuhanan, 4. Peri Kerakyatan, dan 5. Kesejahteraan Rakyat”. Pada 31 Mei Soepomo memberikan gagasannya yang ia namakan “Dasar Negara Indonesia Merdeka” yang berisikan “1. Persatuan, 2. Kekeluargaan, 3. Keseimbangan lahir batin, 4. Musyawarah, dan 5. Keadilan Sosial”." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("peristiwa2_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa2_1"), Show("bantuan_peristiwa2_1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa2_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa2_1"), Show("peristiwa")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("peristiwa2_1"), Show("peristiwa2_2")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("peristiwa2_1"), Show("peristiwa2_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_peristiwa2_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_peristiwa2_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa2_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa2_2"), Show("peristiwa2_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen peristiwa2_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Sidang Pertama \nBPUPKI" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 180
            add "images/Konten/peristiwa sidang pertama bpupki.png"
        vbox:
            xpos 385 ypos 390
            text "Sumber:\nhttps://id.wikipedia.org/wiki/Badan_Penyelidik_Usaha-\nUsaha_Persiapan_Kemerdekaan#Sidang_resmi_pertama" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Terakhir pada tanggal 1 Juni 1945 Soekarno menyatakan gagasannya yang bernama “Pancasila” yang berisikan “1. Kebangsaan Indonesia, 2. Internasionalisme dan Peri Kemanusiaan, 3. Mufakat atau Demokrasi, 4. Kesejahteraan Sosial, dan 5. Ketuhanan Yang Maha Esa”. Pidato Soekarno mengakhiri masa sidang BPUPKI, hari itu sampai sekarang dikenal sebagai Hari Lahirnya Pancasila." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("peristiwa2_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa2_2"), Show("bantuan_peristiwa2_2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa2_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa2_2"), Show("peristiwa")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("peristiwa2_2"), Show("peristiwa2_1")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("peristiwa2_2"), Show("peristiwa2_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_peristiwa3:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_peristiwa3"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa3"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa3"), Show("peristiwa3")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen peristiwa3:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Invasi Rusia di Asia" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/peristiwa invasi rusia di asia.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Soviet%E2%80%93Japanese_\nWar#" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Pada 9 Agustus 1945, Rusia akhirnya bergerak melawan Jepang di Asia. Sebelumnya Jepang dan Rusia sudah memiliki perjanjian tidak saling serang pada tahun 1941, tapi Rusia setuju akan permintaan Sekutu untuk membantu melawan Jepang pasca kekalahan Jerman di Eropa. Rusia dengan cepat menembus pertahanan Jepang di Mancuko karena tipisnya pertahan Jepang, tetapi Jepang tidak mudah ditundukkan karena tentaranya yang fanatik sama seperti di Pasifik. Jepang tidak ragu menggunakan unit bunuh diri untuk menghentikan invasi Rusia, tetap saja dalam seminggu Rusia sudah berada didalam Mancuko. Walaupun Jepang menyerah pada 15 Agustus dengan pidato Kaisar Jepang, banyak tentara Jepang yang berada diluar Jepang tidak percaya sehingga perang masih berlanjut.Rusia tidak hanya menguasai daerah Manchuria, tetapi juga bagian utara Korea dan pulau-pulau kecil utara Jepang sebelum Jepang menyerah pada 20 Agustus." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("peristiwa3"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa3"), Show("bantuan_peristiwa3")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa3"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa3"), Show("peristiwa")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_peristiwa4_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_peristiwa4_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa4_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa4_1"), Show("peristiwa4_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen peristiwa4_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Beer Hall Putsch" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/peristiwa beer hall putsch.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Beer_Hall_Putsch#" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Beer Hall Putsch adalah usaha gagal Adolf Hitler dalam mengambil alih kendali atas negara Jerman pada 8-9 November 1923 di Munich, provinsi Bavaria Jerman. 1923 merupakan tahun yang sulit bagi rakyat Jerman, uang mereka tidak ada harganya sehingga radikalisme dapat berkembang dengan pesat. Salah satu tokoh radikal itu adalah Adolf Hitler, Hitler berniat mencari dukungan di Munich dan mulai bergerak ke Berlin menuntut dibubarkannya pemerintah. Kesuksesan gerakan Hitler ini bergantung pada tiga orang yang mengontrol Bavaria pada saat itu yaitu Kahr sebagai komisaris negara, Seisser sebagai kepala polisi Bavaria, dan Lossow sebagai Jenderal tentara Bavaria. Pada 8 November 1923 Hitler memasuki rumah minum bir Bürgerbräukeller, disana ketiga tokoh Bavaria sedang berada disana untuk memberikan pidato. Awalnya Hitler berhasil mendapatkan bantuan dari ketiga tokoh tersebut, sayangnya Hitler meninggalkan mereka sebentar untuk mengurus masalah lain." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("peristiwa4_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa4_1"), Show("bantuan_peristiwa4_1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa4_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa4_1"), Show("peristiwa")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("peristiwa4_1"), Show("peristiwa4_2")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("peristiwa4_1"), Show("peristiwa4_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_peristiwa4_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_peristiwa4_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa4_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_peristiwa4_2"), Show("peristiwa4_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen peristiwa4_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Beer Hall Putsch" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/peristiwa beer hall putsch.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Beer_Hall_Putsch#" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Absennya Hitler dimanfaatkan tiga tokoh tersebut untuk melarikan diri dan mencabut dukungan mereka pada aksinya Hitler, Hitler kebingungan tetapi tetap memaksakan bergerak ke Berlin besoknya. Pada 9 November 1923 dengan massa berjumlah 2000 orang, Hitler bergerak menuju Berlin. Sayangnya Hitler berhasil dihentikan oleh polisi dan gerakannya ini dianggap gagal, walaupun gagal aksinya Hitler berhasil menjadikan dia tokoh nasional yang nantinya mempermudah diri dan pengikutnya naik dalam perpolitikan Jerman." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("peristiwa4_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa4_2"), Show("bantuan_peristiwa4_2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa4_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("peristiwa4_2"), Show("peristiwa")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("peristiwa4_2"), Show("peristiwa4_1")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("peristiwa4_2"), Show("peristiwa4_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_organisasi:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_organisasi"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi"), Show("organisasi")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen organisasi:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")    
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"    
        if unlock == 0 or unlock == 1 or unlock == 2:
            vbox:
                xpos 780 ypos 190
                spacing 15  
                text "Organisasi" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "PUTERA" size 28 hover_underline True color "#000000" 
                    action [Hide("organisasi"), Show("organisasi1")]
                button:
                    text "PPKI" size 28 hover_underline True color "#7F7F7F" 
                    action [Play("sound","audio/SFX/invalid.mp3")]
                button:
                    text "BPUPKI" size 28 hover_underline True color "#7F7F7F"
                    action [Play("sound","audio/SFX/invalid.mp3")]
                button:
                    text "Kempeitai" size 28 hover_underline True color "#7F7F7F" 
                    action [Play("sound","audio/SFX/invalid.mp3")]
                add "images/Icon/lock.png" xpos -30 ypos -155
                add "images/Icon/lock.png" xpos -30 ypos -149
                add "images/Icon/lock.png" xpos -30 ypos -141
        elif unlock == 3:
            vbox:
                xpos 780 ypos 190
                spacing 15  
                text "Organisasi" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "PUTERA" size 28 hover_underline True color "#000000" 
                    action [Hide("organisasi"), Show("organisasi1")]
                button:
                    text "PPKI" size 28 hover_underline True color "#000000" 
                    action [Hide("organisasi"), Show("organisasi2")]
                button:
                    text "BPUPKI" size 28 hover_underline True color "#7F7F7F"
                    action [Play("sound","audio/SFX/invalid.mp3")]
                button:
                    text "Kempeitai" size 28 hover_underline True color "#7F7F7F" 
                    action [Play("sound","audio/SFX/invalid.mp3")]
                add "images/Icon/lock.png" xpos -30 ypos -105
                add "images/Icon/lock.png" xpos -30 ypos -96
        elif unlock == 4 or unlock == 5 or unlock == 6 or unlock == 7:
            vbox:
                xpos 780 ypos 190
                spacing 15  
                text "Organisasi" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "PUTERA" size 28 hover_underline True color "#000000" 
                    action [Hide("organisasi"), Show("organisasi1")]
                button:
                    text "PPKI" size 28 hover_underline True color "#000000" 
                    action [Hide("organisasi"), Show("organisasi2")]
                button:
                    text "BPUPKI" size 28 hover_underline True color "#000000"
                    action [Hide("organisasi"), Show("organisasi3_1")]
                button:
                    text "Kempeitai" size 28 hover_underline True color "#7F7F7F" 
                    action [Play("sound","audio/SFX/invalid.mp3")]
                add "images/Icon/lock.png" xpos -30 ypos -50
        else:
            vbox:
                xpos 780 ypos 190
                spacing 15  
                text "Organisasi" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "PUTERA" size 28 hover_underline True color "#000000" 
                    action [Hide("organisasi"), Show("organisasi1")]
                button:
                    text "PPKI" size 28 hover_underline True color "#000000" 
                    action [Hide("organisasi"), Show("organisasi2")]
                button:
                    text "BPUPKI" size 28 hover_underline True color "#000000"
                    action [Hide("organisasi"), Show("organisasi3_1")]
                button:
                    text "Kempeitai" size 28 hover_underline True color "#000000" 
                    action [Hide("organisasi"), Show("organisasi4")]
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("organisasi"), Return()]   
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi"), Show("bantuan_organisasi")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi"), Show("pilihanbuku")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_organisasi1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_organisasi1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi1"), Show("organisasi1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen organisasi1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "PUTERA" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/organisasi putera.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Center_of_the_People%27s_\nPower#" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Pusat Tenaga Rakyat didirikan pada Maret 1943, PUTERA merupakan organisasi buatan Jepang sebagai alat propaganda Jepang yang menggantikan gerakan 3A yang sebelumnya gagal. Organisasi ini menggandeng tokoh nasional seperti Soekarno, Hatta, Ki Hajar Dewantara, dan K.H, Mas Mansoer, organisasi ini diharapkan dapat mendukung pendudukan Jepang sebagai pembebas mereka dan membantu Jepang dalam Perang Pasifik. PUTERA juga dianggap gagal karena rakyat terutama pemuda walaupun Jepang juga terus melakukan kekerasan di desa dan perekrutan romusha masih dilakukan, akhirnya PUTERA dibubarkan pada 1944 karena lebih menguntungkan tokoh nasional daripada Jepang sendiri." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("organisasi1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi1"), Show("bantuan_organisasi1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi1"), Show("organisasi")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_organisasi2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_organisasi2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi2"), Show("organisasi2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen organisasi2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "PPKI" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/organisasi ppki.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://id.wikipedia.org/wiki/Badan_Penyelidik_Usaha-\nUsaha_Persiapan_Kemerdekaan#Persiapan_kemerdekaan_\ndilanjutkan_oleh_PPKI" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Panitia Persiapan Kemerdekaan Indonesia yang diresmikan pada tanggal 9 Agustus 1945 dengan dilantiknya Soekarno dan Hatta sebagai ketua dan wakil organisasi tersebut di Saigon, tugas PPKI adalah melanjutkan tugas BPUPKI yaitu membawa Indonesia pada gerbang kemerdekaan yang dijanjikan oleh Marsekal Terauchi pada 24 Agustus 1945. PPKI beranggotakan 21 orang yang mewakili seluruh Indonesia dan nantinya ditambah 6 orang lagi tanpa sepengetahuan Jepang, PPKI dapat bekerja dengan leluasa walaupun masih organisasi bentukan Jepang. Sebelum kemerdekaan PPKI tidak pernah melaksanakan rapat karena rapat yang rencanakan tanggal 16 Agustus gagal karena Peristiwa Rengasdengklok dan rapat dinihari tanggal 17 Agustus terlalu banyak tokoh lain sehingga tidak bisa dibilang rapat PPKI." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("organisasi2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi2"), Show("bantuan_organisasi2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi2"), Show("organisasi")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_organisasi3_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_organisasi3_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi3_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi3_1"), Show("organisasi3_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen organisasi3_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "BPUPKI" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/organisasi bpupki.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://id.wikipedia.org/wiki/Badan_Penyelidik_Usaha-\nUsaha_Persiapan_Kemerdekaan#" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Badan Penyelidik Usaha-Usaha Persiapan Kemerdekaan atau BPUPKI adalah badan buatan Jepang untuk mendapatkan bantuan Indonesia dengan janji Jepang akan membantu proses kemerdekaan Indonesia. Diresmikan pada tanggal 29 April bertepatan dengan hari ulang tahunnya Kaisar Jepang, BPUPKI ini beranggotakan 67 orang dan diketuai oleh Radjiman Wedyodiningrat. ORganisasi ini berperan besar dalam kemerdekaan Indonesia, karena selama organisasi ini berdiri banyak rancangan dasar-dasar negara sudah terbentuk dan disiapkan. Diawali dengan sidang pertama yang berhasil menghasilkan rancangan undang-undang dasar dan lahirnya gagasan Pancasila pada 1 Juni 1945, dibuatnya Piagam Jakarta oleh Panitia Sembilan pada 10 Juli 1945, dan terakhir rapat kedua membahas tentang wilayah, kewarganegaraan, rancangan Undang-Undang Dasar, ekonomi, pembelaan negara, dan pendidikan yang dilaksanakan dari 10 Juli sampai 17 Juli 1945. Organisasi ini dibubarkan" size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("organisasi3_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi3_1"), Show("bantuan_organisasi3_1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi3_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi3_1"), Show("organisasi")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("organisasi3_1"), Show("organisasi3_2")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("organisasi3_1"), Show("organisasi3_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_organisasi3_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_organisasi3_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi3_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi3_2"), Show("organisasi3_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen organisasi3_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "BPUPKI" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/organisasi bpupki.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://id.wikipedia.org/wiki/Badan_Penyelidik_Usaha-\nUsaha_Persiapan_Kemerdekaan#" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "pada tanggal 7 Agustus karena dianggap telah melaksanakan tugasnya dengan baik, kegiatan persiapan kemerdekaan dilanjutkan oleh PPKI." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("organisasi3_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi3_2"), Show("bantuan_organisasi3_2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi3_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi3_2"), Show("organisasi")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("organisasi3_2"), Show("organisasi3_1")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("organisasi3_2"), Show("organisasi3_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_organisasi4:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_organisasi4"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi4"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_organisasi4"), Show("organisasi4")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen organisasi4:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Kempeitai" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/organisasi kempeitai.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://id.wikipedia.org/wiki/Kempeitai" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Satuan Polisi Militer atau Kempetai adalah polisi rahasia milik Kekaisaran Jepang yang berada diseluruh daerah jajahan Jepang termasuk Hindia Belanda. Didirikan pada 4 Januari 1881, Kempeitai sangat ditakuti keberadaannya karena tidak segan membunuh warga yang menentang pendudukan Jepang di wilayah jajahannya selama Perang Pasifik. Markas Kempeitai saat berada di Hindia Belanda berada di Gedung Keadilan, anggota Kempeitai sering pamer kekuatan agar warga lokal tidak berani melakukan hal-hal yang merugikan nyawa mereka sendiri. Kempeitai juga bertanggung jawab untuk memperlambat atau bahkan menghalau semangat kemerdekaan Indonesia dengan memasang kontrol ketat pada penyebaran informasi, sarana mobilitas masyarakat, dan juga tempat tempat keramaian seperti misalnya tempat ibadah. Kempeitai berakhir dengan menyerahnya Jepang pada Agustus 1945, banyak anggota Kempeitai yang dihukum karena melakukan kejahatan perang." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("organisasi4"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi4"), Show("bantuan_organisasi4")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi4"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("organisasi4"), Show("organisasi")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara"), Show("negara")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")    
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"    
        if unlock == 0 or unlock == 1 or unlock == 2 or unlock == 3 or unlock == 4:
            vbox:
                xpos 780 ypos 150
                spacing 15  
                text "Negara" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "Jerman" size 28 hover_underline True color "#000000" 
                    action [Hide("negara"), Show("negara1_1")]
                button:
                    text "Jepang" size 28 hover_underline True color "#000000"
                    action [Hide("negara"), Show("negara2_1")]
                button:
                    text "Hindia Belanda" size 28 hover_underline True color "#000000"
                    action [Hide("negara"), Show("negara3_1")]
                button:
                    text "Amerika Serikat" size 28 hover_underline True color "#000000"
                    action [Hide("negara"), Show("negara4_1")]
                button:
                    text "Rusia" size 28 hover_underline True color "#7F7F7F" 
                    action [Play("sound","audio/SFX/invalid.mp3")]
                button:
                    text "Mancuko" size 28 hover_underline True color "#7F7F7F"
                    action [Play("sound","audio/SFX/invalid.mp3")]
                add "images/Icon/lock.png" xpos -30 ypos -104
                add "images/Icon/lock.png" xpos -30 ypos -96
        else:
            vbox:
                xpos 780 ypos 150
                spacing 15  
                text "Negara" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "Jerman" size 28 hover_underline True color "#000000" 
                    action [Hide("negara"), Show("negara1_1")]
                button:
                    text "Jepang" size 28 hover_underline True color "#000000"
                    action [Hide("negara"), Show("negara2_1")]
                button:
                    text "Hindia Belanda" size 28 hover_underline True color "#000000"
                    action [Hide("negara"), Show("negara3_1")]
                button:
                    text "Amerika Serikat" size 28 hover_underline True color "#000000"
                    action [Hide("negara"), Show("negara4_1")]
                button:
                    text "Rusia" size 28 hover_underline True color "#000000"
                    action [Hide("negara"), Show("negara5_1")]
                button:
                    text "Mancuko" size 28 hover_underline True color "#000000"
                    action [Hide("negara"), Show("negara6_1")]
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara"), Return()]   
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara"), Show("bantuan_negara")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara"), Show("pilihanbuku")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara1_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara1_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara1_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara1_1"), Show("negara1_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara1_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Jerman" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera jerman.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Nazi_Germany#World_War_\nII" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Setelah Jerman kalah di Perang Dunia I, Jerman menjadi negara yang miskin dan terhina. Rakyat Jerman frustasi dengan perlakuan ini, sehingga radikalisme bekembang pesat pada waktu itu. Salah satu tokoh radikal saat itu adalah Adolf Hitler, Hitler berhasil memainkan perasaan rakyat Jerman hingga dia sendiri bisa memusatkan kekuasaan Jerman pada dirinya tahun 1934. Setelah Hitler memiliki kontrol total dalam masalah internal, Hitler mulai melirik masalah internal yaitu negara-negara tetangganya. Jerman melakukan beberapa ekspansi secara diplomatis dan berhati-hati sampai berhasil merebut Austria dan Republik Ceko, tetapi perang tidak dapat dihindarkan pada 1 September 1939 dimana Jerman menginvasi Polandia dan memulai Perang Dunia II. Jerman memiliki inisiatif karena negara-negara yang menentangnya seperti Inggris dan Perancis belum siap untuk perang, Jerman berhasil menguasai hampir seluruh Eropa Barat termasuk negara-negara" size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara1_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara1_1"), Show("bantuan_negara1_1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara1_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara1_1"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara1_1"), Show("negara1_2")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara1_1"), Show("negara1_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara1_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara1_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara1_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara1_2"), Show("negara1_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara1_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Jerman" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera jerman.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Nazi_Germany#World_War_\nII" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "seperti Perancis, Belanda, dan Norwegia sebelum tahun 1941. Kehancuran Jerman dimulai dengan invasinya ke Rusia pada 22 Juni 1941, walaupun awalnya memiliki inisiasi tetapi Jerman menerima kekalahan telak di Pertempuran Stalingrad yang berakhir pada 2 Februari 1943. Kekalahan di Stalingrad membuat Sekutu semakin leluasa membuka front-front baru seperti di Italia dan di Prancis, pembukaan front ini dilakukan agar tentara Jerman tersebar semakin tipis. Memasuki tahun 1945 Jerman sudah semakin terdesak, Hitler sendiri tewas pada 30 April 1945 dan Jerman menyerah pada 8 Mei 1945." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara1_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara1_2"), Show("bantuan_negara1_2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara1_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara1_2"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara1_2"), Show("negara1_1")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara1_2"), Show("negara1_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara2_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara2_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara2_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara2_1"), Show("negara2_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara2_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Jepang" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera jepang.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Empire_of_Japan#Later_\nSh%C5%8Dwa_(1931%E2%80%931941)" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Memasuki abad ke-20, Jepang merupakan satu-satunya negara Asia yang dapat dianggap negara yang maju. Keberhasilannya mengalahkan Rusia pada 1905 juga membuktikan bahwa orang Asia bisa melawan imperialisme barat, kemenangan ini juga memperkuat ideologi Pan-Asia dan Jepang secara aktif mendorong ideologi tersebut. Pada tahun 1920an ekonomi Jepang berkembang dengan pesat, namun masih bergantung dengan impor bahan mentah seperti karet, besi, dan minyak. Ketergantungan ini membuat Jepang melakukan ekspansi di Asia untuk menguasai sumber bahan-bahan mentah di Asia agar Jepang tidak perlu impor lagi, target pertama ekspansi Jepang adalah Cina. Dimulai dari invasi Jepang ke Manchuria, Jepang secara perlahan-lahan mulai merebut daerah Cina sampai perang total antar Cina-Jepang terjadi pada 1937. Invasi Jepang terhadap Cina ini membuat Amerika Serikat mulai memutus ekspor bahan mentah ke Jepang, hal ini membuat Jepang" size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara2_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara2_1"), Show("bantuan_negara2_1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara2_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara2_1"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara2_1"), Show("negara2_2")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara2_1"), Show("negara2_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara2_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara2_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara2_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara2_2"), Show("negara2_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara2_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Jepang" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera jepang.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Empire_of_Japan#Later_\nSh%C5%8Dwa_(1931%E2%80%931941)" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "mulai melirik koloni seperti Malaya dan Hindia Belanda yang kaya akan bahan mentah. Dengan serangan Jepang terhadap pelabuhan Pearl Harbor milik Amerika Serikat pada 7 Desember 1941, Jepang mulai bergerak dengan cepat melumpuhkan Malaya, Hindia Belanda, dan juga Filipina diawal tahun 1942. Dalam koloni-koloni ini Jepang menganggap dirinya sebagai pembebas mereka sekaligus menanamkan jiwa nasionalisme dan anti barat, termasuk “mendukung” pergerakan kemerdekaan seperti di Indonesia. Kemenangan Jepang tidaklah bertahan lama, Jepang mulai dipukul mundur di Pasifik setelah pertempuran Midway pada 4-7 Juni 1942. Jepang terus kehilangan pulau-pulau pasifiknya sampai Pulau Okinawa jatuh pada 22 Juni 1945, setelah itu Jepang menyerah pada 15 Agustus 1945 setelah Hiroshima di bom pada 6 Agustus diikuti dengan bom Nagasaki dan invasi Rusia pada tanggal 9 Agustus 1945." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara2_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara2_2"), Show("bantuan_negara2_2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara2_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara2_2"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara2_2"), Show("negara2_1")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara2_2"), Show("negara2_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara3_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara3_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara3_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara3_1"), Show("negara3_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara3_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Hindia Belanda" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera hindia belanda.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://id.wikipedia.org/wiki/Hindia_Belanda#Sejarah" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Lahir dari bangkrutnya VOC pada tahun 1799, Hindia Belanda hadir agar Belanda mendapatkan untung yang lebih besar daripada zaman VOC yang menguntungkan pengusaha-pengusaha dalam VOC saja. Dengan Hindia Belanda juga Belanda melakukan ekspansi besar-besaran sampai pada akhirnya seluruh kepulauan Indonesia berada dibawah Hindia Belanda pada tahun 1920, ekspansi ini dilakukan karena Belanda menganggap penduduk pribumi masih tidak beradab dan merekalah yang akan mengajarkan adab kepada mereka. Sempat terjadi beberapa kali pemberontakan daerah selama Hindia Belanda berdiri seperti Perang Padri dan Perang Diponegoro, tetapi semuanya berhasil ditumpas oleh pemerintah kolonial. Pemerintah kolonial sangatlah rasis, pribumi tanpa memiliki jabatan, harta, atau status tidak akan mendapatkan kehidupan yang layak. Pendidikan yang layak hanya tersedia bagi orang Belanda dan juga golongan pribumi elit saja, pribumi elit. Pribumi elit ini" size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara3_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara3_1"), Show("bantuan_negara3_1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara3_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara3_1"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara3_1"), Show("negara3_2")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara3_1"), Show("negara3_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara3_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara3_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara3_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara3_2"), Show("negara3_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara3_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Hindia Belanda" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera hindia belanda.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://id.wikipedia.org/wiki/Hindia_Belanda#Sejarah" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "diharapkan Belanda dapat membantu mereka mengurus Hindia Belanda, tetapi banyak juga yang mendorong lepasnya Belanda dari tanah airnya. Tokoh seperti Soekarno dan Mohammad Hatta dengan lantang menentang pemerintah kolonial, perlawanan ini jugalah yang membuat mereka diasingkan dan meredam gerakan pergerakaan kemerdekaan untuk sementara. Pemerintah Hindia Belanda akhirnya hancur pada 8 Maret 1942 karena invasi Jepang dalam Perang Dunia II, Belanda sendiri sudah jatuh pada 14 Mei 1940 karena invasi Jerman." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara3_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara3_2"), Show("bantuan_negara3_2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara3_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara3_2"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara3_2"), Show("negara3_1")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara3_2"), Show("negara3_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara4_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara4_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara4_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara4_1"), Show("negara4_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara4_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Amerika Serikat" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera amerika serikat.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/United_States#Great_\nDepression,_New_Deal,_and_World_War_II_\n(1929%E2%80%931945)" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Tahun 1930an adalah tahun-tahun yang sulit bagi Amerika Serikat, krisis ekonomi yang menimpa dunia terutama Amerika Serikat masih menyulitkan penduduk Amerika. Setelah Perang Dunia II pecah di Eropa, Amerika Serikat enggan turun tangan langsung tetapi lebih memilih memberi bantuan persenjataan pada Inggris dan Rusia. Amerika Serikat akhirnya terseret dalam Perang Dunia II ketika Jepang menyerang Pearl Harbor pada 7 Desember 1941, Amerika Serikat membangkitkan industri perangnya sehingga perekonomian Amerika Serikat segera pulih. Amerika Serikat dengan cepat menjadi pemimpin Sekutu dalam perang ini. Amerika Serikat menjadi kontributor utama di Perang Pasifik dengan operasinya di pulau-pulau pasifik, di front Eropa juga Amerika Serikat menjadi pionir pendaratan di Perancis. Selain aktif di medan tempur, Amerika Serikat juga rutin mengadakan pertemuan dengan negara-negara besar seperti Inggris dan Rusia untuk menentukan dunia" size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara4_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara4_1"), Show("bantuan_negara4_1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara4_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara4_1"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara4_1"), Show("negara4_2")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara4_1"), Show("negara4_2")]

    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara4_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara4_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara4_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara4_2"), Show("negara4_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara4_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Amerika Serikat" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera amerika serikat.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/United_States#Great_\nDepression,_New_Deal,_and_World_War_II_\n(1929%E2%80%931945)" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "pasca perang. Perang Dunia II berakhir dengan menyerahnya Jepang pada Sekutu, dan Amerika menjadi negara yang kekuatan dan pengaruhnya sulit disaingi negara manapun." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara4_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara4_2"), Show("bantuan_negara4_2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara4_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara4_2"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara4_2"), Show("negara4_1")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara4_2"), Show("negara4_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara5_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara5_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara5_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara5_1"), Show("negara5_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara5_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Rusia" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera rusia.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Soviet_Union#World_War_II" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Rusia, atau Uni Soviet adalah negara komunis yang berdiri pasca Revolusi Oktober 1917. Negara ini memiliki kontrol yang ketat pada rakyatnya dengan polisi rahasia, pembersihan-pembersihan, dan kolektivisasi massal. Rusia merupakan bagian dari negara sekutu setelah Jerman menginvasinya pada 22 Juni 1941, Rusia awalnya berhasil dipukul mundur oleh Jerman tetapi Rusia berhasil membalikkan keadaan dengan pertempuran Stalingrad yang berakhir pada 2 Februari 1943. Front Rusia atau Front Timur merupakan front terpenting dalam Perang Dunia II, karena Jerman memfokuskan banyak tentaranya di Front Timur dan memberi kesempatan bagi Sekutu untuk membuka front baru seperi di Perancis dan Italia. Di Front Timur Rusia terus memukul mundur Jerman sampai memasuki wilayah Jerman itu sendiri dan Berlin pada 2 Mei 1945, 6 hari kemudian Jerman menyerah pada Sekutu. Setelah perang di Eropa selesai, Rusia bergerak menghadapi Jepang di Asia" size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara5_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara5_1"), Show("bantuan_negara5_1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara5_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara5_1"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara5_1"), Show("negara5_2")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara5_1"), Show("negara5_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara5_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara5_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara5_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara5_2"), Show("negara5_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara5_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Rusia" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera rusia.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Soviet_Union#World_War_II" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "dengan menyerang Manchuria pada 9 Agustus 1945 dan tak lama kemudian Jepang menyerah pada Sekutu. Keterlibatan Rusia membawa Rusia menjadi negara adidaya dan juga membawa dunia dalam Perang Dingin karena perbedaan ideologi dengan bekas sekutunya yaitu Amerika Serikat." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara5_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara5_2"), Show("bantuan_negara5_2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara5_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara5_2"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara5_2"), Show("negara5_1")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara5_2"), Show("negara5_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara6_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara6_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara6_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara6_1"), Show("negara6_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara6_1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Mancuko" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera mancuko.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Manchukuo#World_War_II_\nand_aftermath" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Mancuko adalah negara boneka buatan Jepang, negara ini didirikan di daerah Manchuria yang berada di bagian timur laut Cina. Negara Mancuko didirikan tak lama setelah Jepang merebut daerah Manchuria dari Cina pada 1931, Jepang menunjuk kaisar terakhir Dinasti Qing yaitu Puyi untuk menjadi pemimpin Mancuko sebagai tanda “legitimasi”. Jepang menggunakan Mancuko sebagai basis operasi di Cina, Mancuko tidak bisa berbuat banyak karena statusnya sebagai negara boneka. Jepang berusaha menjadikan Mancuko sebagai model koloni Jepang yang sukses, Jepang melakukannya dengan cara mengirim banyak penduduk dan perusahaan-perusahaan Jepang bekerja disana. Kelemahan Mancuko adalah perbatasannya dengan Rusia yang sangat luas, Jepang dan Rusia pernah beberapa kali berbenturan dalam perbatasan sebelum keduanya berjanji tidak saling serang pada tahun 1941. Invasi Rusia pada 9 Agustus merupakan awal dari runtuhnya Mancuko, tentara" size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara6_1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara6_1"), Show("bantuan_negara6_1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara6_1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara6_1"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara6_1"), Show("negara6_2")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara6_1"), Show("negara6_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_negara6_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_negara6_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara6_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_negara6_2"), Show("negara6_2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen negara6_2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Mancuko" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bendera mancuko.png"
        vbox:
            xpos 385 ypos 355
            text "Sumber:\nhttps://en.wikipedia.org/wiki/Manchukuo#World_War_II_\nand_aftermath" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Mancuko segera menyerah tanpa perlawanan dan menyisakan Jepang yang berhadapan dengan Rusia. Pernyataan menyerah Jepang tanggal 15 Agustus masih belum dipercayai semua tentara Jepang yang berada di Mancuko, sehingga pertempuran baru berakhir pada 20 Agustus 1945." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("negara6_2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara6_2"), Show("bantuan_negara6_2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara6_2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("negara6_2"), Show("negara")]
        vbox:
            xpos 385 ypos 540
            button:
                xysize (40,40)
                style "button2_tb"
                action [Hide("negara6_2"), Show("negara6_1")]
        vbox:
            xpos 440 ypos 540
            button:
                xysize (40,40)
                style "button3_tb"
                action [Hide("negara6_2"), Show("negara6_1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_bacaan:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_bacaan"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_bacaan"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_bacaan"), Show("bacaan")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bacaan:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")    
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"    
        if unlock == 0 or unlock == 1:
            vbox:
                xpos 780 ypos 210
                spacing 15  
                text "Bacaan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "Untuk Negeriku" size 28 hover_underline True color "#000000" 
                    action [Hide("bacaan"), Show("bacaan1")]
                button:
                    text "QS. Al-Maun Ayat 1-7" size 28 hover_underline True color "#7F7F7F" 
                    action [Play("sound","audio/SFX/invalid.mp3")]
                button:
                    text "QS. Al-Humazah Ayat \n1-3" size 28 hover_underline True color "#7F7F7F"
                    action [Play("sound","audio/SFX/invalid.mp3")]
                add "images/Icon/lock.png" xpos -30 ypos -131
                add "images/Icon/lock.png" xpos -30 ypos -115
        else:
            vbox:
                xpos 780 ypos 210
                spacing 15  
                text "Bacaan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
                button:
                    text "Untuk Negeriku" size 28 hover_underline True color "#000000" 
                    action [Hide("bacaan"), Show("bacaan1")]
                button:
                    text "QS. Al-Maun Ayat 1-7" size 28 hover_underline True color "#000000" 
                    action [Hide("bacaan"), Show("bacaan2")]
                button:
                    text "QS. Al-Humazah Ayat \n1-3" size 28 hover_underline True color "#000000"
                    action [Hide("bacaan"), Show("bacaan3")]
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bacaan"), Return()]   
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bacaan"), Show("bantuan_bacaan")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bacaan"), Show("pilihanbuku")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_bacaan1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_bacaan1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_bacaan1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_bacaan1"), Show("bacaan1")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bacaan1:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "Untuk Negeriku" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bacaan untuk negeriku.png"
        vbox:
            xpos 385 ypos 535
            text "Sumber:\nSyuja Davala" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Untuk Negeriku adalah buku autobiografi tulisan Mohammad Hatta sendiri yang beliau tulis menjelang wafatnya beliau pada tahun 1980. Buku ini menceritakan kisah hidup Sang Proklamator dari beliau masih kanak-kanak sampai Perundingan Meja Bundar tahun 1949, buku ini sendiri terbagi dalam tiga jilid. Jilid pertama menceritakan masa kanak-kanaknya dan perjuangannya di Belanda, jilid kedua menceritakan perjuangannya berjuang di Hindia Belanda sampai ia dibuang kesana kemari sampai tahun 1942, jilid terakhir menceritakan tentang perjuangannya dalam memperjuangkan kemerdekaan Indonesia. Menurut beliau ada dua peristiwa yang sangat beliau banggakan selama hidupnya, yaitu ketika Proklamasi Kemerdekaan Indonesia tahun 1945 dan juga pengakuan kedaulatan Belanda atas Kemerdekaan Indonesia di Konferensi Meja Bundar pada tahun 1949. Buku ini menjadi acuan utama dalam pengembangan gim ini." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bacaan1"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bacaan1"), Show("bantuan_bacaan1")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bacaan1"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bacaan1"), Show("bacaan")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_bacaan2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_bacaan2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_bacaan2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_bacaan2"), Show("bacaan2")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bacaan2:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "QS. Al-Maun Ayat 1-7" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 145
            add "images/Konten/bacaan qs. al-maun ayat 1-7.png"
        vbox:
            xpos 385 ypos 535
            text "Sumber:\nhttps://katadata.co.id/safrezi/berita/6189cc041c00c/surat-\nal-maun-beserta-arti-dan-kandungannya" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Surah Al-Maun merupakan surah ke 107 dan termasuk surah Makiyah yang diartikan sebagai “barang-barang yang berguna”. Surah ini menjelaskan sifat-sifat orang mendustakan agamanya, pendustaan tersebut seperti tidak mendalami sholat mereka, mencela anak yatim, menolak memberi atau mengajak orang memberi bantuan pada orang miskin, melakukan kebaikan agar dipuji orang atau riya, dan terakhir adalah enggan membantu sesama yang sedang membutuhkan sedikit atau seringan apapun." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bacaan2"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bacaan2"), Show("bantuan_bacaan2")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bacaan2"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bacaan2"), Show("bacaan")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bantuan_bacaan3:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xpos 415 ypos 265
            spacing -25
            text "Jejak Perjuangan" size 30 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Hatta" size 75 font "fonts/AbrilFatface-Regular.otf" color "#C69D7B"
        vbox:
            xpos 780 ypos 225
            xsize 325
            spacing 10
            text "Bantuan" size 36 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
            text "Untuk dapat membuka konten yang terkunci pada buku, anda perlu untuk melewati beberapa dialog pada game ini!" size 24 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bantuan_bacaan3"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_bacaan3"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 460
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bantuan_bacaan3"), Show("bacaan3")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen bacaan3:
    frame:
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")     
        vbox:
            xpos 395 ypos 92
            text "QS. Al-Humazah Ayat \n1-3" size 28 font "fonts/AbrilFatface-Regular.otf" color "#2E2C2B"
        vbox:
            xpos 385 ypos 180
            add "images/Konten/bacaan qs. al-humazah ayat 1-3.png"
        vbox:
            xpos 385 ypos 390
            text "Sumber:\nhttps://tafsirweb.com/13022-surat-al-humazah-ayat-\n3.html" size 10 color "#000000" justify True
        vbox:
            xpos 770 ypos 100
            xsize 325
            text "Surah Al-Humazah merupakan surah ke 104 dan termasuk surah Makiyah yang artinya “Pengumpat”, tiga ayat surah ini berisi tentang tercelanya orang-orang yang sering mencela, selanjutnya adalah orang-orang yang hanya menimbun harta sebanyak-banyaknya. Orang-orang seperti itu menganggap harta adalah segalanya, sehingga mereka menjadi budak dari harta mereka sendiri." size 16 color "#000000" justify True
        vbox:
            xpos 65 ypos 600
            button:
                text "KELUAR" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [SetVariable("quick_menu", True), Hide("bacaan3"), Return()]
        vbox:
            xpos 65 ypos 530
            button:
                text "INFORMASI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bacaan3"), Show("bantuan_bacaan3")]
        vbox:
            xpos 65 ypos 460
            button:
                text "MENU" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bacaan3"), Show("pilihanbuku")]
        vbox:
            xpos 65 ypos 390
            button:
                text "KEMBALI" xalign 0.5 yalign 0.5
                xysize (175,55)
                style "button_tb"
                action [Hide("bacaan3"), Show("bacaan")]
    
    frame:
        xpos 55 ypos 50
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            if waktu == 0:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "09" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 1:
                vbox:
                    xalign 0.5    
                    text "Minggu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "12" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 2:
                vbox:
                    xalign 0.5    
                    text "Selasa" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "14" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 3:
                vbox:
                    xalign 0.5    
                    text "Rabu" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "15" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            elif waktu == 4:
                vbox:
                    xalign 0.5    
                    text "Kamis" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "16" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"
            else:
                vbox:
                    xalign 0.5    
                    text "Jumat" ypos 5 xalign 0.5 size 20 color "#ffffff" bold True         
                    text "17" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"              
                    text "Agustus, 1945" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"