init python:
    from datetime import datetime
    import locale
    locale.setlocale(locale.LC_TIME, 'id_ID')
    today = datetime.today()
    d1 = today.strftime("%A")
    d2 = today.strftime("%d")
    d3 = today.strftime("%B, %Y")

screen tanggal:
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