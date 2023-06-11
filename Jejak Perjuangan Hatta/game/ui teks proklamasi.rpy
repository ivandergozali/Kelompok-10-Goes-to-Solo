default skor1 = False
default skor2 = False

screen tampilsoal1:
    frame:
        xsize 1280 ysize 720
        xfill True
        background Frame("images/kuis.png")
        hbox:
            xpos 275
            ypos 130
            text "Apa isi kalimat pertama teks proklamasi?" size 24

        vbox:
            xpos 273
            ypos 170
            spacing 10
            xsize 720
            button:
                text "1). Kami Bangsa Indonesia dengan ini menyatakan Kemerdekaan Indonesia" size 24 hover_underline True
                action [SetVariable("skor1",True), Hide("tampilsoal1"), Jump("cekjawab1")]
            button:
                text "2). Kami Rakyat Indonesia dengan ini menyatakan Kemerdekaan Indonesia" size 24 hover_underline True
                action [SetVariable("skor1",False), Hide("tampilsoal1"), Jump("cekjawab1")]
            button:
                text "3). Kami Soekarno dan Hatta dengan ini menyatakan Kemerdekaan Indonesia" size 24 hover_underline True
                action [SetVariable("skor1",False), Hide("tampilsoal1"), Jump("cekjawab1")]
            button:
                text "4). Kami Bangsa Indonesia berterimakasih atas Kemerdekaan Indonesia yang diberikan oleh Dai Nippon" size 24 hover_underline True
                action [SetVariable("skor1",False), Hide("tampilsoal1"), Jump("cekjawab1")]
        
        hbox:
            xpos 330
            ypos 620
            xsize 850
            text "Kalimat pertama diambil dari alinea ketiga rencana Pembukaan UUD tentang proklamasi agar terlihat bahwa Indonesia merdeka atas kemauannya sendiri." size 18

screen tampilsoal2:
    frame:
        xsize 1280 ysize 720
        xfill True
        background Frame("images/kuis.png")
        hbox:
            xpos 275
            ypos 130
            text "Apa isi kalimat kedua teks proklamasi?" size 24
        
        vbox:
            xpos 273
            ypos 170
            spacing 10
            xsize 740
            button:
                text "1). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan tjara seksama dan dalam tempo jang sesingkat-singkatnya." size 24 hover_underline True
                action [SetVariable("skor2",True), Hide("tampilsoal2"), Jump("cekjawab2")]
            button:
                text "2). Hal-hal mengenai pemindahan kekoeasaan d.l.l., kami serahkan pada pihak Dai Nippon." size 24 hover_underline True
                action [SetVariable("skor2",False), Hide("tampilsoal2"), Jump("cekjawab2")]
            button:
                text "3). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan persetoejoean Dai Nippon." size 24 hover_underline True
                action [SetVariable("skor2",False), Hide("tampilsoal2"), Jump("cekjawab2")]
            button:
                text "4). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan bantoean pihak Sekoetoe." size 24 hover_underline True
                action [SetVariable("skor2",False), Hide("tampilsoal2"), Jump("cekjawab2")]

        hbox:
            xpos 330
            ypos 620
            xsize 870
            text "Harus ada komplemen yang menyatakan bagaimana caranya menyelenggarakan revolusi nasional." size 18

label cekjawab1:
    if skor1 == False:
        call screen salah1
    else:
        call screen tampilsoal2

screen salah1:
    frame:
        xsize 1280 ysize 720 
        xfill True
        background Frame("images/kuis.png")
        button:
            background Frame("images/empty.png")
            action [Hide("salah1"), Show("tampilsoal1")]
        hbox:
            xpos 275
            ypos 130
            text "Apa isi kalimat pertama teks proklamasi?" size 24

        vbox:
            xpos 277
            ypos 174
            spacing 18
            xsize 720
            text "1). Kami Bangsa Indonesia dengan ini menyatakan Kemerdekaan Indonesia" size 24 
            text "2). Kami Rakyat Indonesia dengan ini menyatakan Kemerdekaan Indonesia" size 24 
            text "3). Kami Soekarno dan Hatta dengan ini menyatakan Kemerdekaan Indonesia" size 24 
            text "4). Kami Bangsa Indonesia berterimakasih atas Kemerdekaan Indonesia yang diberikan oleh Dai Nippon" size 24 

        hbox:
            xpos 330
            ypos 620
            xsize 850
            text "Maaf Bung, tapi menurutku itu bukanlah kalimat yang tepat." size 18

label cekjawab2:
    if skor2 == False:
        call screen salah2
    else:
        call screen proklamasi1

screen salah2:
    frame:
        xsize 1280 ysize 720 
        xfill True
        background Frame("images/kuis.png")
        button:
            background Frame("images/empty.png")
            action [Hide("salah2"), Show("tampilsoal2")]
        hbox:
            xpos 275
            ypos 130
            text "Apa isi kalimat kedua teks proklamasi?" size 24

        vbox:
            xpos 277
            ypos 174
            spacing 18
            xsize 740
            text "1). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan tjara seksama dan dalam tempo jang sesingkat-singkatnya." size 24 
            text "2). Hal-hal mengenai pemindahan kekoeasaan d.l.l., kami serahkan pada pihak Dai Nippon." size 24 
            text "3). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan persetoejoean Dai Nippon." size 24 
            text "4). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan bantoean pihak Sekoetoe." size 24 

        hbox:
            xpos 330
            ypos 620
            xsize 850
            text "Maaf Bung, tapi menurutku itu bukanlah kalimat yang tepat." size 18

screen proklamasi1:
    frame:
        xsize 1280 ysize 720 
        xfill True
        background Frame("images/proklamasi 2.png")
        button:
            background Frame("images/empty.png")
            action [Hide("proklamasi1"), Show("proklamasi2")]

        hbox:
            xpos 230
            ypos 620
            xsize 860
            text "Setelah sedikit berbincang tentang naskah tersebut, naskah tersebut diketik oleh Sayuti Melik sebelum dibawa rapat." size 22

screen proklamasi2:
    frame:
        xsize 1280 ysize 720 
        xfill True
        background Frame("images/proklamasi 3.png")
        button:
            background Frame("images/empty.png")
            action [Hide("proklamasi2"), Jump("scene27")]
        hbox:
            xpos 465
            ypos 100
            text "PROKLAMASI" size 48

        vbox:
            xpos 255
            ypos 174
            spacing 40
            xsize 765
            text "Kami bangsa Indonesia  dengan ini  menyatakan Kemerdekaan Indonesia" size 23 
            text "Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan tjara seksama dan dalam tempo jang sesingkat-singkatnya." size 23 

        vbox:
            xpos 600
            ypos 400
            spacing 20
            xsize 440
            text "Djakarta, hari 17 boelan 8 tahoen 05 Atas nama bangsa Indonesia." size 23 
            text "Soekarno/Hatta." size 23 

        hbox:
            xpos 300
            ypos 610
            xsize 700
            text "Setelah diketik oleh Sayuti Melik, beginilah naskah teks proklamasi yang kami buat." size 26