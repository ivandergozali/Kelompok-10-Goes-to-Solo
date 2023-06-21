default skor = False

image background3 = im.Scale("gui/namebox1.png", 150, 70)
image background4 = im.Scale("gui/namebox1.png", 190, 70)

screen tampilsoal1:
    frame:
        xsize 1280 ysize 720
        xfill True
        background Frame("images/Kuis/kuis 1.png")
        add "background3" xpos 350 ypos 470
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
                text "A). Kami Soekarno dan Hatta dengan ini menyatakan Kemerdekaan Indonesia." size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal1"), Jump("cekjawab1")]
            button:
                text "B). Kami Rakyat Indonesia dengan ini menyatakan Kemerdekaan Indonesia." size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal1"), Jump("cekjawab1")]
            button:
                text "C). Kami Bangsa Indonesia dengan ini menyatakan Kemerdekaan Indonesia." size 24 hover_underline True
                action [SetVariable("skor",True), Hide("tampilsoal1"), Jump("cekjawab1")]
            button:
                text "D). Kami Bangsa Indonesia berterimakasih atas Kemerdekaan Indonesia yang diberikan oleh Dai Nippon." size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal1"), Jump("cekjawab1")]
        
        hbox:
            xpos 375
            ypos 480
            text "HATTA" size 30 font "fonts/AbrilFatface-Regular.otf"

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Kalimat pertama diambil dari alinea ketiga rencana Pembukaan UUD tentang proklamasi agar terlihat bahwa Indonesia merdeka atas kemauannya sendiri." size 22

label cekjawab1:
    if skor == False:
        call screen salah1
    else:
        call screen tampilsoal2

screen salah1:
    frame:
        xsize 1280 ysize 720 
        xfill True
        background Frame("images/Kuis/kuis 1.png")
        add "background3" xpos 350 ypos 470
        button:
            background Frame("images/Kuis/empty.png")
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
            text "A). Kami Soekarno dan Hatta dengan ini menyatakan Kemerdekaan Indonesia." size 24 
            text "B). Kami Rakyat Indonesia dengan ini menyatakan Kemerdekaan Indonesia." size 24 
            text "C). Kami Bangsa Indonesia dengan ini menyatakan Kemerdekaan Indonesia." size 24 
            text "D). Kami Bangsa Indonesia berterimakasih atas Kemerdekaan Indonesia yang diberikan oleh Dai Nippon." size 24 

        hbox:
            xpos 375
            ypos 480
            text "HATTA" size 30 font "fonts/AbrilFatface-Regular.otf"

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Maaf Bung, tapi menurutku itu bukanlah kalimat yang tepat." size 22

screen tampilsoal2:
    frame:
        xsize 1280 ysize 720
        xfill True
        background Frame("images/Kuis/kuis 1.png")
        add "background3" xpos 350 ypos 470
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
                text "A). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan tjara seksama dan dalam tempo jang sesingkat-singkatnya." size 24 hover_underline True
                action [SetVariable("skor",True), Hide("tampilsoal2"), Jump("cekjawab2")]
            button:
                text "B). Hal-hal mengenai pemindahan kekoeasaan d.l.l., kami serahkan pada pihak Dai Nippon." size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal2"), Jump("cekjawab2")]
            button:
                text "C). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan persetoejoean Dai Nippon." size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal2"), Jump("cekjawab2")]
            button:
                text "D). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan bantoean pihak Sekoetoe." size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal2"), Jump("cekjawab2")]

        hbox:
            xpos 375
            ypos 480
            text "HATTA" size 30 font "fonts/AbrilFatface-Regular.otf"

        hbox:
            xpos 350
            ypos 590
            xsize 870
            text "Harus ada komplemen yang menyatakan bagaimana caranya menyelenggarakan revolusi nasional." size 22

label cekjawab2:
    if skor == False:
        call screen salah2
    else:
        call screen tampilsoal3

screen salah2:
    frame:
        xsize 1280 ysize 720 
        xfill True
        background Frame("images/Kuis/kuis 1.png")
        add "background3" xpos 350 ypos 470
        button:
            background Frame("images/Kuis/empty.png")
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
            text "A). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan tjara seksama dan dalam tempo jang sesingkat-singkatnya." size 24 
            text "B). Hal-hal mengenai pemindahan kekoeasaan d.l.l., kami serahkan pada pihak Dai Nippon." size 24 
            text "C). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan persetoejoean Dai Nippon." size 24 
            text "D). Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan bantoean pihak Sekoetoe." size 24 

        hbox:
            xpos 375
            ypos 480
            text "HATTA" size 30 font "fonts/AbrilFatface-Regular.otf"

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Maaf Bung, tapi menurutku itu bukanlah kalimat yang tepat." size 22

screen tampilsoal3:
    frame:
        xsize 1280 ysize 720
        xfill True
        background Frame("images/Kuis/kuis 1.png")
        add "background3" xpos 350 ypos 470
        hbox:
            xpos 275
            ypos 130
            text "Tanggal berapa proklamasi kemerdekaan dilaksanakan?" size 24

        vbox:
            xpos 273
            ypos 170
            spacing 10
            xsize 720
            button:
                text "A). Batavia, 17 Agoestoes 1945" size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal3"), Jump("cekjawab3")]
            button:
                text "B). Djakarta, hari 17 boelan 8 tahoen 05" size 24 hover_underline True
                action [SetVariable("skor",True), Hide("tampilsoal3"), Jump("cekjawab3")]
            button:
                text "C). Jakarta, hari 17 boelan 8 tahoen 45" size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal3"), Jump("cekjawab3")]
            button:
                text "D). Djakarta, hari 17 boelan 8 tahoen 1945" size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal3"), Jump("cekjawab3")]
        
        hbox:
            xpos 375
            ypos 480
            text "HATTA" size 30 font "fonts/AbrilFatface-Regular.otf"

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Untuk mengakhiri naskah ini, Bung silahkan tulis tanggal hari ini." size 22

label cekjawab3:
    if skor == False:
        call screen salah3
    else:
        call screen proklamasi

screen salah3:
    frame:
        xsize 1280 ysize 720 
        xfill True
        background Frame("images/Kuis/kuis 1.png")
        add "background3" xpos 350 ypos 470
        button:
            background Frame("images/Kuis/empty.png")
            action [Hide("salah3"), Show("tampilsoal3")]
        hbox:
            xpos 275
            ypos 130
            text "Tanggal berapa proklamasi kemerdekaan dilaksanakan?" size 24

        vbox:
            xpos 277
            ypos 174
            spacing 18
            xsize 720
            text "A). Batavia, 17 Agoestoes 1945" size 24 
            text "B). Djakarta, hari 17 boelan 8 tahoen 05" size 24 
            text "C). Jakarta, hari 17 boelan 8 tahoen 45" size 24 
            text "D). Djakarta, hari 17 boelan 8 tahoen 1945" size 24 

        hbox:
            xpos 375
            ypos 480
            text "HATTA" size 30 font "fonts/AbrilFatface-Regular.otf"

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Maaf Bung, tapi menurutku itu bukanlah kalimat yang tepat." size 22

screen tampilsoal4:
    frame:
        xsize 1280 ysize 720
        xfill True
        background Frame("images/Kuis/kuis 1.png")
        add "background3" xpos 350 ypos 470
        hbox:
            xpos 275
            ypos 130
            text "Apa kalimat terakhir naskah proklamasi?" size 24

        vbox:
            xpos 273
            ypos 170
            spacing 10
            xsize 720
            button:
                text "A). Atas nama bangsa Indonesia, Soekarno/Hatta." size 24 hover_underline True
                action [SetVariable("skor",True), Hide("tampilsoal4"), Jump("cekjawab4")]
            button:
                text "B). Kami semua disini mewakili bangsa Indonesia." size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal4"), Jump("cekjawab4")]
            button:
                text "C). Kami semua sebagai wakil Indonesia." size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal4"), Jump("cekjawab4")]
            button:
                text "D). Atas nama perwakilan bangsa Indonesia, Soekarno/Hatta." size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal4"), Jump("cekjawab4")]
        
        hbox:
            xpos 375
            ypos 480
            text "HATTA" size 30 font "fonts/AbrilFatface-Regular.otf"

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Mari kita semuanya yang hadir disini menandatangani naskah Proklamasi Indonesia Merdeka ini sebagai suatu dokumen yang bersejarah." size 22

label cekjawab4:
    if skor == False:
        call screen salah4
    else:
        call screen tampilsoal5

screen salah4:
    frame:
        xsize 1280 ysize 720 
        xfill True
        background Frame("images/Kuis/kuis 2.png")
        add "background4" xpos 350 ypos 470
        button:
            background Frame("images/Kuis/empty.png")
            action [Hide("salah4"), Show("tampilsoal4")]
        hbox:
            xpos 275
            ypos 130
            text "Apa kalimat terakhir naskah proklamasi?" size 24

        vbox:
            xpos 277
            ypos 174
            spacing 18
            xsize 720
            text "A). Atas nama bangsa Indonesia, Soekarno/Hatta." size 24 
            text "B). Kami semua disini mewakili bangsa Indonesia." size 24 
            text "C). Kami semua sebagai wakil Indonesia." size 24 
            text "D). Atas nama perwakilan bangsa Indonesia, Soekarno/Hatta." size 24 

        hbox:
            xpos 370
            ypos 480
            text "SOEKARNI" size 30 font "fonts/AbrilFatface-Regular.otf"

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Bukan kita semua yang hadir disini harus menandatangani naskah itu, cukuplah Bung Karno dan Bung Hatta saja yang menandatanganinya atas nama rakyat Indonesia." size 22

screen tampilsoal5:
    frame:
        xsize 1280 ysize 720
        xfill True
        background Frame("images/Kuis/kuis 1.png")
        add "background3" xpos 350 ypos 470
        hbox:
            xpos 275
            ypos 130
            text "Siapa yang mengetik naskah proklamasi?" size 24

        vbox:
            xpos 273
            ypos 170
            spacing 10
            xsize 720
            button:
                text "A). Soekarni" size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal5"), Jump("cekjawab5")]
            button:
                text "B). Radjiman" size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal5"), Jump("cekjawab5")]
            button:
                text "C). Sutan Sjahrir" size 24 hover_underline True
                action [SetVariable("skor",False), Hide("tampilsoal5"), Jump("cekjawab5")]
            button:
                text "D). Sayuti Melik" size 24 hover_underline True
                action [SetVariable("skor",True), Hide("tampilsoal5"), Jump("cekjawab5")]
        
        hbox:
            xpos 375
            ypos 480
            text "HATTA" size 30 font "fonts/AbrilFatface-Regular.otf"

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Baiklah, jika tidak ada permasalan lagi teks ini hanya perlu diketik." size 22

label cekjawab5:
    if skor == False:
        call screen salah5
    else:
        call screen proklamasi2

screen salah5:
    frame:
        xsize 1280 ysize 720 
        xfill True
        background Frame("images/Kuis/kuis 1.png")
        add "background3" xpos 350 ypos 470
        button:
            background Frame("images/Kuis/empty.png")
            action [Hide("salah5"), Show("tampilsoal5")]
        hbox:
            xpos 275
            ypos 130
            text "Siapa yang mengetik naskah proklamasi?" size 24

        vbox:
            xpos 277
            ypos 174
            spacing 18
            xsize 720
            text "A). Soekarni" size 24 
            text "B). Radjiman" size 24 
            text "C). Sutan Sjahrir" size 24 
            text "D). Sayuti Melik" size 24 

        hbox:
            xpos 375
            ypos 480
            text "HATTA" size 30 font "fonts/AbrilFatface-Regular.otf"

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Maaf Bung, tapi menurutku itu bukanlah jawaban yang tepat." size 22

screen proklamasi:
    frame:
        xsize 1280 ysize 720 
        xfill True
        background Frame("images/Kuis/proklamasi 2.png")
        button:
            background Frame("images/Kuis/empty.png")
            action [SetVariable("quick_menu", True), Hide("proklamasi"), Show("tanggal"), Show("buku"), Jump("scene26")]
        hbox:
            xpos 465
            ypos 100
            text "PROKLAMASI" size 48

        vbox:
            xpos 255
            ypos 174
            spacing 40
            xsize 765
            text "Kami bangsa Indonesia  dengan ini  menyatakan Kemerdekaan Indonesia." size 23 
            text "Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan tjara seksama dan dalam tempo jang sesingkat-singkatnya." size 23 

        vbox:
            xpos 600
            ypos 400
            spacing 20
            text "Djakarta, hari 17 boelan 8 tahoen 05" size 23 
        hbox:
            xpos 240
            ypos 580
            xsize 850
            text "Menurutku segini sudah cukup, mari kita bawa ke ruang rapat terlebih dahulu." size 26

screen proklamasi2:
    frame:
        xsize 1280 ysize 720 
        xfill True
        background Frame("images/Kuis/proklamasi 2.png")
        button:
            background Frame("images/Kuis/empty.png")
            action [SetVariable("quick_menu", True), Hide("proklamasi2"), Show("tanggal"), Show("buku"), Jump("scene27")]
        hbox:
            xpos 465
            ypos 100
            text "PROKLAMASI" size 48

        vbox:
            xpos 255
            ypos 174
            spacing 40
            xsize 765
            text "Kami bangsa Indonesia  dengan ini  menyatakan Kemerdekaan Indonesia." size 23 
            text "Hal-hal jang mengenai pemindahan kekoeasaan d.l.l., diselenggarakan dengan tjara seksama dan dalam tempo jang sesingkat-singkatnya." size 23 

        vbox:
            xpos 600
            ypos 365
            spacing 20
            xsize 440
            text "Djakarta, hari 17 boelan 8 tahoen 05 Atas nama bangsa Indonesia." size 23 
            text "Soekarno/Hatta." size 23

        hbox:
            xpos 250
            ypos 580
            xsize 850
            text "Setelah diketik oleh Sayuti Melik, beginilah naskah teks proklamasi yang kami buat." size 26