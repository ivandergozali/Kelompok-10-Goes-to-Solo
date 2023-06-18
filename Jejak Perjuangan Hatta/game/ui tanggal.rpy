define waktu = 0 

screen tanggal:
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