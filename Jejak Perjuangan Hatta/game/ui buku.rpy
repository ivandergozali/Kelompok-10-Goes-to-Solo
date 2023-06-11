define blink = 0  

image notifikasi:
    "notif 1"
    pause 0.6
    "notif 2"
    pause 0.6
    repeat

screen buku:
    frame:
        xalign 0.5 yalign 0.5
        xpos 1190 ypos 90
        vbox:
            imagebutton:
                if blink == 0:
                    idle "buku 1"
                elif blink == 1:
                    idle "notifikasi"
                action [SetVariable("blink", 0), SetVariable("quick_menu", False), Hide("buku"), Show("pilihanbuku")]

screen pilihanbuku:
    frame:
        xalign 0.5 yalign 0.5
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")
        vbox:
            xalign 0.5 xpos 870 ypos 170
            spacing 15  
            button:
                text "Karakter" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xalign 0.5
                action [Hide("pilihanbuku"), Show("karakter1")]   
            button:
                text "Peristiwa" size 28 hover_underline True color "#000000" xalign 0.5
                action [Hide("pilihanbuku"), Show("peristiwa1")]
            button:
                text "Organisasi" size 28 hover_underline True color "#000000" xalign 0.5
                action [Hide("pilihanbuku"), Show("organisasi1")]
            button:
                text "Negara" size 28 hover_underline True color "#000000" xalign 0.5
                action [Hide("pilihanbuku"), Show("negara1")]
            button:
                text "Bacaan" size 28 hover_underline True color "#000000" xalign 0.5
                action [Hide("pilihanbuku"), Show("bacaan1")]
        vbox:
            xpos 350 ypos 560
            imagebutton:
                idle "close"
                action [SetVariable("quick_menu", True), Hide("pilihanbuku"), Show("buku")]
    frame:
        xalign 0.5 yalign 0.5
        xpos 135 ypos 130
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            vbox:
                xalign 0.5    
                text "[d1]" ypos 5 xalign 0.5 size 20 font "fonts/LumiosTypewriter-Old.ttf" color "#ffffff" bold True                  
                text "[d2]" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"             
                text "[d3]" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen karakter1:
    frame:
        xalign 0.5 yalign 0.5
        xsize 1280 ysize 720
        background Frame("images/Icon/buku 2.png")        
        vbox:
            xalign 0.5 xpos 930 ypos 170
            spacing 15  
            text "Karakter" size 36 font "fonts/AbrilFatface-Regular.otf" color "#000000" xpos 5
            button:
                text "Marx dan Engels" size 28 hover_underline True color "#000000" xalign 0.5
                action [Hide("karakter1"), Show("peristiwa1")]
            button:
                text "Adolf Hitler" size 28 hover_underline True color "#000000" xalign 0.5
                action [Hide("karakter1"), Show("adolfhitler")]
            button:
                text "Douglas MacArthur" size 28 hover_underline True color "#000000" xalign 0.5
                action [Hide("karakter1"), Show("negara1")]
            button:
                text "Chester W. Nimitz" size 28 hover_underline True color "#000000" xalign 0.5
                action [Hide("karakter1"), Show("bacaan1")]
        vbox:
            xpos 350 ypos 560
            imagebutton:
                idle "close"
                action [SetVariable("quick_menu", True), Hide("karakter1"), Show("buku")]
        vbox:
            xpos 410 ypos 560
            imagebutton:
                idle "home"
                action [Hide("karakter1"), Show("pilihanbuku")]
    frame:
        xalign 0.5 yalign 0.5
        xpos 135 ypos 130
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            vbox:
                xalign 0.5    
                text "[d1]" ypos 5 xalign 0.5 size 20 font "fonts/LumiosTypewriter-Old.ttf" color "#ffffff" bold True      
                text "[d2]" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000" 
                text "[d3]" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen adolfhitler:
    frame:
        xalign 0.5 yalign 0.5
        xsize 1280 ysize 720
        background Frame("images/Icon/adolf hitler.png")        
        vbox:
            xpos 350 ypos 560
            imagebutton:
                idle "close"
                action [SetVariable("quick_menu", True), Hide("adolfhitler"), Show("buku")]
        vbox:
            xpos 410 ypos 560
            imagebutton:
                idle "home"
                action [Hide("adolfhitler"), Show("pilihanbuku")]
        vbox:
            xpos 470 ypos 560
            imagebutton:
                idle "back"
                action [Hide("adolfhitler"), Show("karakter1")]
    frame:
        xalign 0.5 yalign 0.5
        xpos 135 ypos 130
        button:
            xsize 150 ysize 150
            background Frame("images/Icon/kalender.png")
            vbox:
                xalign 0.5    
                text "[d1]" ypos 5 xalign 0.5 size 20 font "fonts/LumiosTypewriter-Old.ttf" color "#ffffff" bold True    
                text "[d2]" ypos -10 xalign 0.5 size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000"            
                text "[d3]" ypos -25 xalign 0.5 size 15 font "fonts/Trocchi.otf" color "#000000"

screen organisasi1:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        hbox:
            text "BPUPKI" size 30 color "#690d1b" xpos 190 ypos 60 
        vbox:    
            xpos 50 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"   
        hbox:
            text "Kempeitai" size 30 color "#690d1b" xpos 600 ypos 60
        vbox:    
            xpos 490 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"

screen organisasi2:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        hbox:
            text "Lorem" size 30 color "#690d1b" xpos 200 ypos 60 
        vbox:    
            xpos 50 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"   
        hbox:
            text "Lorem" size 30 color "#690d1b" xpos 650 ypos 60
        vbox:    
            xpos 490 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"

screen peristiwa1:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        hbox:
            text "Bom Atom Hiroshima" size 25 color "#690d1b" xpos 125 ypos 60 
        vbox:    
            xpos 50 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"   
        hbox:
            text "Invasi Rusia ke Mancuko" size 25 color "#690d1b" xpos 530 ypos 60
        vbox:    
            xpos 490 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"

screen peristiwa2:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        hbox:
            text "Bom Atom Nagasaki" size 25 color "#690d1b" xpos 125 ypos 60 
        vbox:    
            xpos 50 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"   
        hbox:
            text "Lorem" size 25 color "#690d1b" xpos 650 ypos 60
        vbox:    
            xpos 490 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"

screen negara1:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        hbox:
            text "Jepang" size 30 color "#690d1b" xpos 200 ypos 60 
        vbox:    
            xpos 50 ypos 120
            text "Selama Perang Dunia II, Jepang belum" size 20 color "#690d1b" 
            text "menjadi negara anime yang dipenuhi" size 20 color "#690d1b" 
            text "dengan maid dan catgirl. Jepang selama" size 20 color "#690d1b" 
            text "Perang Dunia II belum mengenal hentai" size 20 color "#690d1b" 
            text "karena Jepang sedang sibuk berusaha" size 20 color "#690d1b" 
            text "mendominasi Asia termasuk Indonesia" size 20 color "#690d1b" 
            text "yang waktu itu namanya masih Hindia" size 20 color "#690d1b" 
            text "Belanda. Kedatangan Jepang pada saat" size 20 color "#690d1b" 
            text "itu bukan membawa budaya wibu pada" size 20 color "#690d1b" 
            text "rakyat, melainkan memanfaatkan keada-" size 20 color "#690d1b" 
            text "an untuk memenangkan Perang Pasifik" size 20 color "#690d1b" 
            text "melawan Amerika Serikat dan kronco-" size 20 color "#690d1b" 
            text "kronconya." size 20 color "#690d1b" 
        hbox:
            text "Rusia" size 30 color "#690d1b" xpos 650 ypos 60 
        vbox:    
            xpos 490 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"

screen negara2:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        hbox:
            text "Belanda" size 30 color "#690d1b" xpos 185 ypos 60 
        vbox:    
            xpos 50 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"   
        hbox:
            text "Lorem" size 30 color "#690d1b" xpos 650 ypos 60
        vbox:    
            xpos 490 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"

screen bacaan1:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        hbox:
            text "QS. Al-Maun 1-7" size 30 color "#690d1b" xpos 130 ypos 60 
        vbox:    
            xpos 50 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"   
        hbox:
            text "QS. Al-Humazah 1-3" size 30 color "#690d1b" xpos 525 ypos 60
        vbox:    
            xpos 490 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"

screen bacaan2:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        hbox:
            text "Lorem" size 30 color "#690d1b" xpos 200 ypos 60 
        vbox:    
            xpos 50 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"   
        hbox:
            text "Lorem" size 30 color "#690d1b" xpos 650 ypos 60
        vbox:    
            xpos 490 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"