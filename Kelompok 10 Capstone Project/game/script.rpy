# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define H = Character("HATTA", color="#2E2C2B")
define M = Character("MURID", color="#2E2C2B")
define N = Character("NOMURA", color="#2E2C2B")
define Sj = Character("SJAHRIR", color="#2E2C2B")
define S = Character("SOEKARNO", color="#2E2C2B")
define R = Character("RADJIMAN", color="#2E2C2B")
define T = Character("TERAUCHI", color="#2E2C2B")
define AS = Character("ACHMAD SOEBARDJO", color="#2E2C2B")
define Ma = Character("MAEDA", color="#2E2C2B")
define SS = Character("SOEBADIO SASTROSATOMO", color="#2E2C2B")
define Si = Character("SOEKARNI", color="#2E2C2B")
define Mi = Character("MIYOSHI", color="#2E2C2B")
define Ni = Character("NISHIMURA", color="#2E2C2B")
define W = Character("WIKANA", color="#2E2C2B")

# The game starts here.
style screentext:
    color "#9e5f12"
    size 18

style button_tb:
    background Frame("images/Icon/button_idle.png")
    hover_background Frame("images/Icon/button_hover.png")

init python:
    from datetime import datetime
    import locale
    locale.setlocale(locale.LC_TIME, 'id_ID')
    today = datetime.today()
    d1 = today.strftime("%A")
    d2 = today.strftime("%d")
    d3 = today.strftime("%B, %Y")

init python:
    import locale
    locale.setlocale(locale.LC_TIME, 'id_ID')
    d4 = today.strftime("%A, %d %B %Y, %H:%M")

screen tanggal:
    frame:
        xalign 0.5 yalign 0.5
        xsize 170 ysize 160
        xpos 135 ypos 130
        button:
            background Frame("images/Icon/kalender.png")
            action [Play("sound","audio/SFX/klik.mp3"), Hide("tanggal"), Show("pilihanbuku")]
            vbox:    
                xpos 50 ypos 4
                text "[d1]" size 20 font "fonts/LumiosTypewriter-Old.ttf" color "#ffffff" bold True
            vbox:    
                xpos 27 ypos 15
                text "[d2]" size 80 font "fonts/AbrilFatface-Regular.otf" color "#000000" bold True
            vbox:    
                xpos 45 ypos 110
                text "[d3]" size 15 font "fonts/Trocchi.otf" color "#000000"

screen pilihanbuku:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        vbox:
            xalign 0.5 xpos 260 ypos 120
            spacing 30
            hbox:
                spacing 40
                vbox:
                    imagebutton:
                        auto "images/Icon/karakter_%s.png" 
                        action [Play("sound","audio/SFX/klik.mp3"), Hide("pilihanbuku"), Show("karakter1")]
                    text "Karakter" color "#000000"  xalign 0.5 ypos 10
                vbox:
                    imagebutton:
                        auto "images/Icon/organisasi_%s.png" 
                        action [Play("sound","audio/SFX/klik.mp3"), Hide("pilihanbuku"), Show("organisasi1")]
                    text "Organisasi" color "#000000" xalign 0.5 ypos 10
            hbox:
                spacing 40
                vbox:
                    imagebutton:
                        auto "images/Icon/peristiwa_%s.png" 
                        action [Play("sound","audio/SFX/klik.mp3"), Hide("pilihanbuku"), Show("peristiwa1")]
                    text "Peristiwa" color "#000000" xalign 0.5 ypos 10
                vbox:
                    imagebutton:
                        auto "images/Icon/negara_%s.png" 
                        action [Play("sound","audio/SFX/klik.mp3"), Hide("pilihanbuku"), Show("negara1")]
                    text "Negara" color "#000000" xalign 0.5 ypos 10
        vbox:
            xalign 0.5 xpos 600 ypos 120
            spacing 30
            hbox:
                spacing 40
                vbox:
                    imagebutton:
                        auto "images/Icon/bacaan_%s.png" 
                        action [Play("sound","audio/SFX/klik.mp3"), Hide("pilihanbuku"), Show("bacaan1")]
                    text "Bacaan" color "#000000" xalign 0.5 ypos 10
        vbox:
            xpos 860 ypos 50
            imagebutton:
                auto "images/Icon/close_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("pilihanbuku"), Show("tanggal")]

screen karakter1:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        hbox:
            xpos 860 ypos 50
            imagebutton:
                auto "images/Icon/close_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("karakter1"), Show("tanggal")]
        hbox:
            xpos 25 ypos 50
            imagebutton:
                auto "images/Icon/home_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("karakter1"), Show("pilihanbuku")]
        hbox:
            xpos 35 ypos 450
            imagebutton:
                auto "images/Icon/previous_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("karakter1"), Show("karakter2")]
        hbox:
            xpos 850 ypos 450
            imagebutton:
                auto "images/Icon/next_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("karakter1"), Show("karakter2")]
        hbox:
            text "Marx dan Engels" size 30 color "#690d1b" xpos 120 ypos 60 
        vbox:    
            xpos 50 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"   
        hbox:
            text "Douglas McArthur" size 30 color "#690d1b" xpos 550 ypos 60
        vbox:    
            xpos 490 ypos 120
            text "lorem lorem lorem" size 20 color "#690d1b"

screen karakter2:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        hbox:
            xpos 860 ypos 50
            imagebutton:
                auto "images/Icon/close_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("karakter2"), Show("tanggal")]
        hbox:
            xpos 25 ypos 50
            imagebutton:
                auto "images/Icon/home_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("karakter2"), Show("pilihanbuku")]
        hbox:
            xpos 35 ypos 450
            imagebutton:
                auto "images/Icon/previous_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("karakter2"), Show("karakter1")]
        hbox:
            xpos 850 ypos 450
            imagebutton:
                auto "images/Icon/next_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("karakter2"), Show("karakter1")]
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

screen organisasi1:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        hbox:
            xpos 860 ypos 50
            imagebutton:
                auto "images/Icon/close_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("organisasi1"), Show("tanggal")]
        hbox:
            xpos 25 ypos 50
            imagebutton:
                auto "images/Icon/home_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("organisasi1"), Show("pilihanbuku")]
        hbox:
            xpos 35 ypos 450
            imagebutton:
                auto "images/Icon/previous_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("organisasi1"), Show("organisasi2")]
        hbox:
            xpos 850 ypos 450
            imagebutton:
                auto "images/Icon/next_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("organisasi1"), Show("organisasi2")]
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
            xpos 860 ypos 50
            imagebutton:
                auto "images/Icon/close_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("organisasi2"), Show("tanggal")]
        hbox:
            xpos 25 ypos 50
            imagebutton:
                auto "images/Icon/home_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("organisasi2"), Show("pilihanbuku")]
        hbox:
            xpos 35 ypos 450
            imagebutton:
                auto "images/Icon/previous_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("organisasi2"), Show("organisasi1")]
        hbox:
            xpos 850 ypos 450
            imagebutton:
                auto "images/Icon/next_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("organisasi2"), Show("organisasi1")]
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
            xpos 860 ypos 50
            imagebutton:
                auto "images/Icon/close_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("peristiwa1"), Show("tanggal")]
        hbox:
            xpos 25 ypos 50
            imagebutton:
                auto "images/Icon/home_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("peristiwa1"), Show("pilihanbuku")]
        hbox:
            xpos 35 ypos 450
            imagebutton:
                auto "images/Icon/previous_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("peristiwa1"), Show("peristiwa2")]
        hbox:
            xpos 850 ypos 450
            imagebutton:
                auto "images/Icon/next_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("peristiwa1"), Show("peristiwa2")]
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
            xpos 860 ypos 50
            imagebutton:
                auto "images/Icon/close_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("peristiwa2"), Show("tanggal")]
        hbox:
            xpos 25 ypos 50
            imagebutton:
                auto "images/Icon/home_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("peristiwa2"), Show("pilihanbuku")]
        hbox:
            xpos 35 ypos 450
            imagebutton:
                auto "images/Icon/previous_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("peristiwa2"), Show("peristiwa1")]
        hbox:
            xpos 850 ypos 450
            imagebutton:
                auto "images/Icon/next_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("peristiwa2"), Show("peristiwa1")]
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
            xpos 860 ypos 50
            imagebutton:
                auto "images/Icon/close_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("negara1"), Show("tanggal")]
        hbox:
            xpos 25 ypos 50
            imagebutton:
                auto "images/Icon/home_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("negara1"), Show("pilihanbuku")]
        hbox:
            xpos 35 ypos 450
            imagebutton:
                auto "images/Icon/previous_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("negara1"), Show("negara2")]
        hbox:
            xpos 850 ypos 450
            imagebutton:
                auto "images/Icon/next_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("negara1"), Show("negara2")]
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
            xpos 860 ypos 50
            imagebutton:
                auto "images/Icon/close_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("negara2"), Show("tanggal")]
        hbox:
            xpos 25 ypos 50
            imagebutton:
                auto "images/Icon/home_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("negara2"), Show("pilihanbuku")]
        hbox:
            xpos 35 ypos 450
            imagebutton:
                auto "images/Icon/previous_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("negara2"), Show("negara1")]
        hbox:
            xpos 850 ypos 450
            imagebutton:
                auto "images/Icon/next_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("negara2"), Show("negara1")]
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
            xpos 860 ypos 50
            imagebutton:
                auto "images/Icon/close_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("bacaan1"), Show("tanggal")]
        hbox:
            xpos 25 ypos 50
            imagebutton:
                auto "images/Icon/home_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("bacaan1"), Show("pilihanbuku")]
        hbox:
            xpos 35 ypos 450
            imagebutton:
                auto "images/Icon/previous_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("bacaan1"), Show("bacaan2")]
        hbox:
            xpos 850 ypos 450
            imagebutton:
                auto "images/Icon/next_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("bacaan1"), Show("bacaan2")]
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
            xpos 860 ypos 50
            imagebutton:
                auto "images/Icon/close_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("bacaan2"), Show("tanggal")]
        hbox:
            xpos 25 ypos 50
            imagebutton:
                auto "images/Icon/home_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("bacaan2"), Show("pilihanbuku")]
        hbox:
            xpos 35 ypos 450
            imagebutton:
                auto "images/Icon/previous_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("bacaan2"), Show("bacaan1")]
        hbox:
            xpos 850 ypos 450
            imagebutton:
                auto "images/Icon/next_%s.png" 
                action [Play("sound","audio/SFX/klik.mp3"), Hide("bacaan2"), Show("bacaan1")]
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

label start:
    with dissolve
    show screen tanggal
    H "Siang murid-murid semua."
    "Sekarang aku sedang berada di Asrama Indonesia Merdeka, disini aku dipercaya sebagai pengajar ekonomi untuk melahirkan ekonom-ekonom saat bangsa ini merdeka nanti."
    "Sekarang sudah 9 Agustus 1945, aku sangat yakin bahwa Indonesia akan merdeka sebentar lagi."
    "Aku sedang mengajar tentang ekonomi kerakyatan dan salah satu murid ada yang bertanya padaku."
    M "Darimana Bung mempelajari hal ini semua?"
    H "Pertanyaan yang bagus, pemikiran saya ini berdasarkan tiga pilar, yaitu tradisi Minang, Islam, dan sosialisme Eropa. Biar saya jelaskan satu per satu."
    H "Budaya Minangkabau mengajarkan saya bahwa harta bukanlah sumber kekayaan bagi sepeser orang saja tetapi sebagai sumber kemakmuran masyarakatnya, sehingga budaya Minangkabau menentang adanya praktek memperkaya diri sendiri."
    H "Sosialisme di Eropa berkembang dengan terjadinya Revolusi Industri disana, tokoh-tokoh seperti Marx dan Engels-lah yang mematangkan teori sosialisme ini."
    $renpy.notify("Karakter Marx dan Engels telah ditambahkan ke direktori. Silahkan tekan logo tanggal untuk melihat")
    H "Sosialisme bisa diraih dengan dua cara, cara kekerasan disebut sosialisme revolusioner dan cara demokrasi dengan partai perwakilan buruh disebut sosialisme demokratis."
    H "Paham sosialisme ini tidak berasal dari Marx saja, bahkan Islam juga mengajarkan sosialisme. Ayat-ayat seperti QS. Al-Maun Ayat 1-7, Al-Humazah Ayat 1-3 mengajari kita tentang tercelanya orang-orang yang memperkaya diri sendiri."
    $renpy.notify("Bacaan QS. Al-Maun Ayat 1-7, Al-Humazah Ayat 1-3 telah ditambahkan ke direktori. Silahkan tekan logo tanggal untuk melihat")
    H "Sehingga ekonomi yang saya dambakan dalam Indonesia nanti adalah perekonomian yang bersifat kebersamaan, kerakyatan, dan kooperasi agar rakyat bisa hidup makmur."
    "Tak lama kemudian, waktu mengajarku sudah habis, saatnya aku pulang."
    H "Baik murid-murid sekalian, mungkin sekian dari saya untuk hari ini, Assalamualaikum."
    scene black
    with dissolve
    jump scene2

label scene2:
    "Saat aku keluar asrama, ternyata sudah ada Letnan Kolonel Nomura yang menungguku, Nomura pasti ada keperluan denganku, maka dari itu aku menghampirinya."
    N "Selamat sore, Tuan Hatta."
    H "Selamat sore, ada apa Tuan Nomura?"
    N "Tuan diminta ke Dalat malam ini untuk bertemu atasan kami, Marsekal Terauchi untuk membahas kemerdekaan bangsa Tuan."
    H "Adakah wakil Indonesia yang hadir selain saya?"
    N "Tuan Soekarno dan Tuan Radjiman juga akan menemani Tuan dalam perjalanan ini."
    H "Baik saya bersedia, saya akan segera siap-siap berangkat saat pulang."
    N "Arigatou Tuan Hatta, nanti Tuan akan dijemput oleh utusan saya dan kita akan bertemu lagi nanti di Bandara Kemayoran."
    "Aku mengakhiri pertemuanku dengan Nomura dengan bersalaman setelah itu kami berpisah, Nomura masuk ke mobilnya dan pergi sedangkan aku pulang ke rumahku."
    scene black
    with dissolve
    jump scene3

label scene3:
    scene bg
    "Sesampainya di rumah, aku langsung mempersiapkan diriku untuk berangkat nanti malam."
    "Adzhan Maghrib berkumandang tak lama aku menyelesaikan persiapanku."
    "Aku segera keluar untuk berbuka puasa."
    "Setelah berbuka puasa sholat Maghrib, Sjahrir ingin berbicara denganku."
    scene black
    with dissolve
    scene bg
    Sj "Ada keperluan apa Bung pergi ke Dalat?"
    H "Aku akan bertemu dengan Marsekal Terauchi disana, Nomura bilang beliau memiliki hal penting yang ingin beliau bicarakan tentang kemerdekaan Indonesia."
    Sj "Saya heran dengan dirimu Bung, Nippon itu sudah semakin terjepit, lebih baik kita yang menentukan kapan Indonesia merdeka, bukan Dai Nippon."
    H "Aku paham dengan kegelisahanmu, tapi bersabarlah sedikit, kita tidak bisa melakukan hal gegabah tanpa persetujuan PPKI."
    Sj "PPKI? Bung masih yakin Dai Nippon akan menepati janjinya? Organisasi itu tetap saja organisasi buatan Nippon."
    H "Bung, jangan lupakan BPUPKI organisasi buatan Dai Nippon itu, BPUPKI membantu kita dalam mempersiapkan pondasi negara kita jika Indonesia merdeka nanti."
    H "Percayalah bahwa aku bawa berita tanggal kemerdekaan saat pulang dari Dalat nanti, Bung lanjutkan saja perkerjaan Bung selama ini dan pantau terus radio sekutu."
    Sj "Sudahlah terserah Bung saja!"
    "Sjahrir meninggalkanku setelah tidak terlihat tidak puas dengan jawabanku."
    "Akhirnya ada mobil yang datang, pasti itu adalah utusan Nomura."
    "Aku segera memasuki mobil dan dengan ini kami pergi menuju Bandara Kemayoran."
    scene black
    with dissolve
    jump scene4

label scene4:
    "Kami akhirnya sampai di Bandara Kemayoran."
    "Aku segera dituntun ke ruang tunggu bandara."
    "Di ruang tunggu itu sudah ada Soekarno dan Radjiman."
    H "Selamat malam saudara-saudara."
    R "Selamat malam Bung."
    S "Selamat malam Bung."
    H "Apa yang harus kita lakukan sekarang?"
    R "Untuk saat ini kita menunggu Nomura datang."
    H "Baiklah, terima kasih Bung."
    "Kami bertiga menunggu kedatangan Nomura sambil berbicara ringan."
    "Pada akhirnya Nomura datang."
    N "Selamat malam tuan-tuan, maaf telah membuat tuan-tuan menunggu."
    N "Silahkan tuan-tuan ikut saya, kita berangkat sekarang."
    "Kami mengikuti Nomura dan kami akhirnya naik pesawat."
    scene black
    "Pesawat tak lama kemudian lepas landas."
    with dissolve
    jump scene5

label scene5:
    "Perjalanan kami ke Dalat tidaklah lancar."
    "Perjalanan kami dipenuhi dengan kegelisahan, kecemasan, dan penundaan."
    "Selama perjalanan kami, kami menginap semalam di Singapura dan semalam di Saigon."
    "Dari sini juga aku dapat mengetahui bahwa situasi Dai Nippon semakin terpojok."
    "Setelah bermalam di Saigon, kami berangkat dari pagi untuk akhirnya ke Dalat."
    scene black
    with dissolve
    jump scene6

label scene6:
    "Pada tepat pukul 10:00 kami bertemu dengan Marsekal Terauchi."
    "Setelah kami semua bersalaman dengan Terauchi, beliau memberikan pidato singkat."
    "Pidato tersebut berisi tentang bagaimana besarnya peran Indonesia dalam membantu Dai Nippon sehingga akhirnya Dai Nippon memutuskan untuk memberikan Indonesia kemerdekaan dan juga secara simbolis melantik aku dan Soekarno sebagai ketua dan wakil PPKI."
    T "Selamat!"
    S "Atas nama bangsa Indonesia, saya ucapkan terima kasih."
    "Terauchi mengucapkan selamat kepada kami bertiga sambil bersalaman dengan kami sekali lagi."
    "Hatiku senang sekali mendengar Indonesia merdeka, hari ini sekaligus hari ulang tahunku, Aku merasa ini adalah hadiah ulang tahun yang membuktikan bahwa perjuangan aku selama ini tidak sia-sia."
    "Setelah Terauchi memberikat selamat pada kami, kami didatangkan kue-kue untuk disantap bersama sebagai perayaan."
    "Dalam jamuan ini muka Terauchi terlihat lemas, apakah itu karena sakit lumpuhnya? Atau karena kondisi perang bagi Dai Nippon? Atau keduanya?"
    "Pada jamuan ini juga Soekarno bertanya pada Terauchi."
    S "Tuan Terauchi, kapankah keputusan Dai Nippon ini dapat kami beritahu kepada rakyat Indonesia?"
    T "Terserah kepada tuan-tuan Panitia Persiapan, kapan saja boleh, itu sudah menjadi urusan tuan.
    Setelah itu Terauchi menghampiriku dan bertanya."
    T "Tuan Hatta, Indonesia sebentar lagi merdeka, apakah tuan sudah memiliki rencana untuk menikah?"
    "Aku terkejut mendengar pertanyaan Terauchi itu, aku sama sekali belum memikirkan hal itu."
    H "Untuk hal itu belum saya pikirkan Tuan Terauchi."
    "Semua tertawa mendengar jawabanku itu."
    "Kami untuk terakhir kalinya bersalaman dengan Terauchi dan kembali ke Saigon sebelum pukul 12.00 dan kembali ke tempat peristirahatan kami di Saigon."
    scene black
    with dissolve
    jump scene7

label scene7:
    "Pada pukul 16:30, Nomura datang menghampiri tempat kami."
    N "Tuan Hatta, bisakah saya berbicara dengan Tuan Soekarno?"
    H "Maaf Tuan Nomura, Soekarno sedang mandi sekarang."
    H "Silahkan duduk selagi menunggunya Tuan Nomura."
    N "Baik Tuan, saya berbicara dengan Tuan saja."
    N "Bagaimana perjalanan anda sejauh ini Tuan?"
    H "Sejauh ini baik Tuan Nomura, terima kasih sudah menemani kami dalam perjalanan ini."
    N "Sudah menjadi janji Dai Nippon untuk memberikan kemerdekaan bangsa Tuan."
    "Nomura akhirnya membicarakan apa yang sebenarnya ingin ia bicarakan."
    N "Tuan Hatta, tentara Rusia sudah menyerang Mancuko, akan tetapi Tuan tenang saja, tentara Dai Nippon cukup kuat untuk menahannya."
    "Aku tahu itu adalah sebuah kebohongan."
    H "Bagaimana caranya Dai Nippon bisa bertahan dari serangan Rusia itu Tuan Nomura?"
    N "Kami sudah yakin dari awal cepat atau lambat Rusia akan menyerang Dai Nippon, maka dari itu Dai Nippon sudah membuat fortifikasi-fortifikasi yang tidak dapat mereka tembus sebesar apapun kekuatan serangan mereka di Mancuko."
    N "Tuan juga jangan melupakan semangat juang tentara Dai Nippon yang tak terpatahkan, dengan dua hal ini serangan Rusia sebesar apapun dapat kami halau."
    "Lagi-lagi Nomura berbohong."
    scene black
    with dissolve
    S "Selamat sore Tuan Nomura."
    N "Ah Tuan Soekarno, selamat sore."
    "Nomura mengulang berita invasi Rusia tadi ke Soekarno dan kebohogannya tentang pertahanan Dai Nippon."
    "Setelah itu Nomura pergi karena ingin bertemu beberapa petinggi Dai Nippon di Saigon."
    scene black
    with dissolve
    H "Aku yakin Nomura berbohong tentang kuatnya pertahanan Dai Nippon di Mancuko."
    S "Bung tidak sendirian."
    H "Dengan gempuran McArthur dan Nimitz dari selatan dan Rusia dari utara, aku yakin Bung Dai Nippon akan tunduk kurang dari dua minggu."
    S "Kita harus dapat manfaatkan keadaan ini Bung."
    H "Aku setuju Bung, kita harus cepat-cepat menyelesaikan persiapan kemerdekaan Indonesia."
    "Kami mengulangi pembicaraan kita saat dr. Radjiman masuk ke ruangan kami."
    "Beliau juga setuju bahwa dua minggu adalah waktu maksimal Dai Nippon dapat bertahan."
    "Malam ini kami bermalam di Saigon, besok kami kembali ke Singapura."
    scene black
    with dissolve
    jump scene8

label scene8:
    "Paginya pukul 08:00, kami berangkat menuju Singapura"
    "Disana kami menginap lagi semalam."
    "Kami akhirnya berangkat kembali ke Jakarta dari Singapura pukul 09:00 lewat."
    "Selama perjalanan, aku selalu memikirkan apa yang akan aku lakukan jika Dai Nippon benar benar sudah bertekuk lutut pada Sekutu."
    scene black
    with dissolve
    jump scene9

label scene9:
    "Sudah banyak petinggi Jepang dan rakyat Indonesia yang menunggu kedatangan kami sesampainya kami di bandara."
    "Rakyat Indonesia meminta Soekarno berkata sesuatu."
    S "Apabila dulu saya katakan bahwa Indonesia akan merdeka sebelum jagung berbuah, sekarang dapat dikatakan Indonesia akan merdeka sebelum jagung berBunga."
    "Seperti biasa, suara Soekarno lantang dan menggelegar."
    "Respon rakyat juga tidak kalah menggelegar."
    "“Hidup Indonesia!”, “Merdeka!”, “Indonesia Merdeka!”, dan masih banyak lagi."
    "Sebenarnya kami ingin pulang, tetapi petinggi Dai Nippon menyuruh kami ke Istana Gunseireikan terlebih dahulu."
    scene black
    with dissolve
    jump scene10

label scene10:
    "Sesampainya kami disana, kami mendapat sambutan dan juga selamat dari petinggi-petinggi disana sekaligus makan siang."
    "Mereka juga mengulang lagi bahwa apa yang disampaikan Terauchi merupakan keputusan Tokyo dan PPKI diperbolehkan bekerja sampai memerdekakan Indonesia."
    "Pidato itu dapat sambutan meriah dari sesama petinggi Dai Nippon."
    "Setelah makan siang kami diizinkan pulang."
    scene black
    with dissolve
    jump scene11

label scene11:
    "Aku sampai rumah pukul 14:00, disana sudah ada Sjahrir menungguku."
    "Aku bersalaman dengannya kemudian duduk berhadapan dengannya."
    Sj "Jadi, bagaimana soal kemerdekaan kita?"
    H "Kemerdekaan sudah ada di tangan kita, untuk penyelenggaraannya serahkan saja ke PPKI."
    Sj "Bung, aku sudah dengar di radio bahwa Nippon sudah meminta damai pada Sekutu."
    Sj "Sebaiknya kemerdekaan tidak diselenggarakan oleh PPKI, karena itu adalah organisasi buatan Nippon."
    Sj "Jika PPKI yang memerdekakan Indonesia, Sekutu akan melihat bahwa Indonesia adalah negara bentukan Nippon."
    Sj "Setelah itu Sekutu akan mendaratkan pasukannya di Indonesia dengan tujuan mengembalikannya ke Belanda."
    Sj "Sebaiknya Soekarno-lah yang menyatakan kemerdekaan sebagai pemimpin rakyat dan atas nama rakyat dan diberitakan kemana-mana melalui radio."
    Sj "Jangan sampai usaha kita selama ini sia-sia Bung."
    H "Aku setuju denganmu kalau kemerdekaan harus dilakukan segera."
    H "Tetapi aku tidak yakin Soekarno akan setuju dengan rencanamu."
    H "Sebagai ketua PPKI, Soekarno tidak dapat meninggalkan organisasi yang dia ketuai meskipun membawa nama rakyat Indonesia sekalipun."
    H "Soekarno nanti hanya akan merampas hak PPKI, aku yakin Soekarno tidak akan bersedia melakukan itu."
    Sj "Maka disitulah peran Bung meyakinkan Bung Karno."
    H "Baiklah, aku telepon Bung Karno dulu."
    H "Assalamualaikum Bung."
    S "Waalaikumsalam Bung Hatta, ada apa?"
    H "Bolehkah aku dan Sjahrir ke rumah Bung? Kami ada masalah genting yang membutuhkan Bung."
    S "Baiklah, silahkan jika Bung dan Sjahrir ingin ke rumahku."
    H "Baik terima kasih Bung, kami berangkat sekarang."
    H "Bung Karno mengizinkan kita ke rumahnya, mari kita kesana sekarang."
    Sj "Baik, aku mengikutimu Bung."
    scene black
    with dissolve
    jump scene12

label scene12:
    "Setelah bersalaman dan duduk, Soekarno membuka pembicaraan"
    S "Soal apa yang saudara-saudara bawa kemari?"
    "Sjahrir mengulangi apa yang dia katakan tadi saat berada di rumahku."
    S "Memang di Saigon kami menduga, setelah Letnan Kolonel Nomura melapor ke kita kalau Rusia sudah menyerbu Mancuko, Jepang pasti akan bertekuk lutut."
    S "Akan tetapi begitu lekasnya terjadi aku belum percaya sekalipun Saudara Sjahrir mendengarkan berita luar negeri yang kebanyakan dikuasai oleh Sekutu."
    S "Oleh karena itu, aku ingin mengecek terlebih dahulu dari Gunseikanbu."
    S "Besok kami berdua, Bung Hatta dan aku, akan pergi ke sana."
    S "Aku juga tidak setuju dengan pendapat saudara tentang memerdekakan Indonesia atas nama rakyat Indonesia dan melangkahi PPKI."
    S "Aku tidak berhak bertindak sendiri, hak itu adalah hak PPKI yang kuketuai."
    S "Alangkah janggalnya di mata orang, setelah kesempatan terbuka untuk mengucapkan kemerdekaan Indonesia, aku bertindak sendiri melangkahi PPKI yang kuketuai."
    "Sjahrir terlihat pasrah pasca mendengarkan perkataan Soekarno karena cita-cita proklamasi yang menyimpang ini tidak dapat dilaksanakan."
    "Karena tidak ada yang dibicarakan lagi, aku dan Sjahrir pulang ke rumah."
    scene black
    with dissolve
    jump scene14

label scene14:
    "Sesampainya kami di Istana Gunseikanbu, kami terkejut mendapati tidak ada pejabat sama sekali disini."
    "Kami bertanya pada penjaga kantor dan mereka bilang semua pejabat sedang dipanggil ke Gunseireibu."
    "Hal ini hanya memperkuat fakta yang disampaikan Sjahrir itu benar."
    "Kami bertiga berdiskusi untuk memutuskan tujuan kita selanjutnya."
    S "Bagaimana ini Bung, kita tidak dapat apa-apa dari Gunseikanbu ini."
    H "Menurutku kita masih harus mencari kebenaran yang dari orang Nippon sendiri."
    AS "Saya ada usul, bagaimana kalau kita ke rumah Laksamada Maeda?"
    S "Aku setuju, mari kita kesana sekarang juga."
    scene black
    with dissolve
    jump scene15

label scene15:
    "Kedatangan kami disambut dengan lagi-lagi ucapan selamat atas apa yang kami dapatkan di Dalat."
    "Soekarno membuka percakapan dengan terus terang."
    S "Apakah benar berita yang beredar diluar sana bahwa Dai Nippon sudah meminta damai dengan Sekutu Tuan Maeda?"
    "Mendengar pertanyaan itu Maeda terdiam, cukup lama."
    "Aku memberi isyarat kepada Soekarno bahwa berita yang dibawa Sjahrir itu benar, Soekarno membalas dengan menganggukan kepalanya."
    "Dengan berat hati dan muka yang sedih, Maeda akhirnya angkat suara."
    Ma "Memang benar berita itu disiarkan oleh sekutu."
    Ma "Akan tetapi kami disini belum mendapatkan kabar dari Tokyo. Sebab itu, berita tersebut belum bisa kami anggap benar."
    Ma "Hanya instruksi dari Tokyo yang menjadi pegangan kami."
    "Setelah mendapatkan informasi itu, kami berterima kasih kepada Laksamada Maeda."
    scene black
    with dissolve
    jump scene16

label scene16:
    "Kami meninggalkan rumah Laksamada Maeda dengan keyakinan bahwa Dai Nippon benar-benar menyerah."
    H "Bung, menurutku kita besok mengadakan rapat PPKI, selagi seluruh anggota PPKI sedang berada di Jakarta."
    S "Aku setuju Bung, besok 16 Agustus PPKI akan rapat."
    H "Baik Bung, Bung Subardjo tolong besok undang semua anggota PPKI yang terkumpul di Hotel des Indes untuk pukul 10:00 bertemu di Kantor Dewan Sanyo Kaigi di Pejambon."
    AS "Siap Bung."
    "Setelah itu kami berpisah dan pulang ke rumah masing-masing."
    scene black
    with dissolve
    jump scene17

label scene17:
    "Di sore harinya ada pemuda yang menunjungiku, yaitu Soebadio Sastrosatomo dan rekannya."
    SS "Sore Bung, kami dapat kabar bahwa Nippon sudah menyerah pada Sekutu!"
    SS "Bung harus segera meyakinkan Bung Karno bahwa kemerdekaan Indonesia janganlah dinyatakan oleh PPKI, nantinya kita hanya akan dianggap antek Nippon oleh Sekutu."
    SS "Tetapi Bung Karnolah yang memerdekakan Indonesia sebagai pemimpin rakyat, atas nama rakyat, dan disebarkan ke seluruh dunia dengan radio!"
    H "Aku tidak setuju dengan rencana kalian."
    H "Dai Nippon dengan perantaranya Marsekal Terauchi di Dalat telah mengakui kemerdekaan Indonesia yang pelaksanaannya akan diselenggarakan oleh PPKI besok pagi pukul 10:00 di Pejambon."
    SS "Hal itu dihalangi dan tidak boleh terjadi!"
    SS "Bung Karno sendiri yang harus mengucapkannya di radio atas nama rakyat Indonesia!"
    H "Bung Karno tidak akan mau melakukan apa yang kalian tuntut, Bung Karno tidak mau dan tidak bisa merampas hak PPKI."
    H "Dan juga maupun Bung Karno menyatakan kemerdekaan sebagai wakil rakyat maupun PPKI hasilnya akan tetap saja sama, Bung Karno telah dicap pengkhianat oleh Belanda semenjak kita bekerja sama dengan Dai Nippon."
    "Kami bertengkar lebih dari setengah jam, kami sama-sama gagal meyakinkan satu sama lain."
    "Pemuda menyebut pendirian mereka revolusioner, sedangkan aku dengan pendirianku yang rasional dan tidak buang-buang tenaga."
    "Akhirnya mereka menyerah dan berusaha meninggalkanku selagi berkata."
    SS "Di saat revolusi kami rupanya tidak dapat membawa Bung serta, Bung tidak revolusioner."
    H "Aku juga sebenarnya ingin mengadakan revolusi, tapi agar suatu revolusi berhasil, kita perlu organisasi yang matang terlebih dahulu."
    H "Tindakan yang akan engkau lakukan itu bukanlah sebuah revolusi, tetapi putsch, seperti yang Hitler lakukan di Munchen 1923 tetapi gagal."
    SS "Bung Hatta tidak bisa diharapkan untuk revolusi!"
    "Mereka keluar setelah kubuat emosi mereka semakin naik."
    scene black
    with dissolve
    jump scene18

label scene18:
    "Pada malam hari kira-kira pukul 09:30, aku yang sedang mengetik naskah awal proklamasi untuk anggota PPKI tiba-tiba kedatangan Achmad Soebardjo."
    scene black
    with dissolve
    AS "Bung, mari kita ke rumah Bung Karno sekarang juga!"
    H "Apa yang terjadi disana Bung?"
    AS "Bung Karno sedang didesak oleh para pemuda yang menuntut proklamasi dilakukan malam ini juga depan radio."
    H "Baik Bung mari kita kesana."
    scene black
    with dissolve
    jump scene19

label scene19:
    "Sesampainya disana benarlah ada Soekarno yang sedang didesak oleh para pemuda."
    "Sejauh ini Soekarno menolak keras semua desakan para pemuda dengan alasan Dai Nippon sudah memutuskan untuk memerdekakan Indonesia pada 16 Agustus dan PPKI akan bersidang melaksanakan kemerdekaan itu."
    "Setelah itu PPKI akan mengesahkan undang-undang yang disiapkan sebelumnya oleh BPUPKI, memilih kepala daerah, dan akhirnya kembali ke daerah masing-masing untuk mendirikan pemerintahan lokal serta strukturnya disana."
    "Pemuda menilai semua itu tidaklah perlu, mereka menganggap nantinya Indonesia hanyalah antek Dai Nippon, mereka kembali menuntut Soekarno memproklamasikan kemerdekaan atas nama rakyat sebelum pukul 24:00."
    "Soekarno dengan logikanya tetap menolak tuntutan pemuda dengan alasan aksi seperti itu nantinya tidak dapat dipertanggungjawabkan dengan jelas."
    "Dalam ketegangan itu, salah satu pemuda, Wikana menggertak Soekarno."
    W "Apabila Bung Karno tidak mau mengucapkan pengumuman kemerdekaan itu malam ini juga, besok pagi akan terjadi pertumpahan darah."
    "Soekarno emosi dan berdiri menantang balik Wikana setelah mendengar itu."
    S "Ini leherku, seretlah aku ke pojok sana, dan habisilah aku disana, tidak usah menunggu besok."
    "Wikana langsung tunduk setelah Soekarno bilang begitu."
    W "Maksud kami bukan membunuh Bung, tetapi kami akan memperingatkan jika proklamasi tidak dilakukan hari ini, besok akan ada kekerasan yang dituju pada orang-orang yang diduga pro-Belanda."
    "Karena kondisi yang tegang dan tidak berujung ini, kami setuju untuk mengadakan istirahat terlebih dahulu."
    "Dalam istirahat itu kami berdiskusi tanpa para pemuda."
    H "Bagaimana menurutmu Bung tentang para pemuda diluar sana?"
    S "Entahlah Bung, mereka mempunyai semangat, aku akui itu."
    H "Tapi semangat tanpa strategi dan perencanaan hanya akan berakhir tragis."
    S "Benar Bung, tapi mereka sama sekali tidak mau mendengarkan kita."
    AS "Bagaimana kalau kita buat kesepakatan begini, jika mereka ingin proklamasi dilaksanakan malam ini juga, silahkan para pemuda itu cari tokoh yang bersedia."
    S "Idemu bagus Bung, bagaimana? Ada ide lain?"
    H "Menurutku itu sudah bagus, silahkan mereka cari pemimpin revolusi dengan cara mereka sendiri."
    "Kami kembali menghadap para pemuda."
    S "Ini keputusan final kami, jika kalian tetap memaksa kemerdekaan dilaksanakan malam ini juga, silahkan cari pemimpin revolusi baru kalian."
    "Para pemuda tampak tidak setuju, tetapi mereka juga tidak ada usulan."
    "Karena pertemuan ini hanya buang-buang waktu saja, pertemuan akhirnya dibubarkan."
    "Aku sendiri jadi gagal menyelesaikan naskah proklamasi yang sedang ku ketik tadi, biarlah, aku selesaikan besok pagi sebelum rapat PPKI."
    scene black
    with dissolve
    jump scene20

label scene20:
    "Aku bangun dengan niatan sahur, ternyata sudah ada Soekarni dan teman-temannya menungguku."
    H "Ada keperluan apa kalian kesini sekarang?"
    Si "Karena Bung Karno menolak memproklamasikan kemerdekaan semalam, kami para pemuda memutuskan untuk bergerak sendiri."
    Si "Nanti menjelang pukul 12:00, 15.000 rakyat akan menyerbu kota diiringi dengan mahasiswa dan juga Peta melucuti Nippon."
    Si "Bung Karno dan Bung Hatta kami bawa ke Rengasdengklok untuk meneruskan pimpinan Pemerintah Republik Indonesia dari sana."
    H "Dengan menyerang kekuatan Dai Nippon di Jakarta, Saudara-saudara bukan melaksanakan revolusi, tetapi melakukan putsch yang akan membunuh revolusi."
    Si "Ini sudah keputusan kami semua dan tidak dapat dipersoalkan lagi, Bung ikut saja bersama Bung Karno bersama kami ke Rengasdengklok."
    "Firasatku sangatlah buruk, aku membayangkan kehancurannya cita-cita kemerdekaan yang kami perjuangkan sejauh ini."
    "Bagaimana dengan PPKI yang akan rapat pukul 10:00 nanti? Jelas mereka tidak akan rapat tanpa pimpinan."
    "Aku akhirnya dibawa oleh Soekarni dalam mobil dan kami akhirnya berangkat."
    scene black
    with dissolve
    jump scene21

label scene21:
    "Kami singgah dulu ke rumah Soekarno dan tak lama kemudian Soekarno, Fatmawati, dan Guntur ikut bersama kami ke Rengasdengklok."
    "Kami sempat dihentikan di Karawang untuk berpindah mobil, ternyata ini adalah siasat dari Soekarni dan temannya agar supir ini tidak tahu kami dibawa kemana."
    scene black
    with dissolve
    jump scene22

label scene22:
    "Tidak ada yang kami lakukan selama di Rengasdengklok ini, sekarang sudah pukul 12:30 seharusnya revolusi pemuda sudah terjadi."
    "Aku berinisiasi meminta penjaga untuk mendatangkan Soekarni."
    Si "Ada apa Bung?"
    H "Apakah revolusi yang saudara-saudara rencanakan pada pukul 12:00 sudah dimulai?"
    H "Apakah 15.000 rakyat sudah menyerbu posisi Dai Nippon dengan mahasiswa dan Peta sudah masuk ke kota?"
    Si "Saya tidak tahu Bung, saya belum dapat kabar."
    H "Kalau begitu segera cari tahu."
    Si "Baiklah."
    "Soekarni pergi dan hampir sejam ia kembali lagi."
    Si "Saya sejauh ini tidak memperoleh kontak dari Jakarta dan Jakarta tidak memberi berita."
    H "Kalau begitu revolusimu sudah gagal, buat apa kami beristirahat disini apabila di Jakarta tidak terjadi apa-apa?"
    Si "Saya belum yakin revolusi itu gagal Bung."
    "Soekarni berkata begitu, meskipun dalam dirinya aku yakin ada bayak keraguan."
    "Tak lama kemudian ia pergi."
    scene black
    with dissolve
    "Pada pukul 18:00, Soekarni datang dengan Achmad Soebardjo."
    AS "Bung, saya kesini untuk membawa kalian semua pulang ke Jakarta."
    H "Bagaimana keadaan di Jakarta Bung?"
    AS "Di Jakarta biasa saja, tidak terjadi apa-apa."
    AS "Buat apa pemimpin-pemimpin kita berada disini, sedangkan banyak hal yang harus dibereskan selekas-lekasnya di Jakarta."
    H "Apakah PPKI tadi jadi rapat tadi pagi Bung?"
    AS "Apa yang akan dikerjakan mereka? Saudara-saudara yang mengundang mereka rapat tidak ada, berada disini."
    H "Kalau untuk aku, aku lebih senang beristirahat disini sampai besok pagi, besok pagi saja kita pulang."
    H "Semuanya sudah terlambat, kerja yang seharusnya selesai tadi pagi tidak jadi dikerjakan."
    "Walaupun aku bilang begitu hanya untuk menertawai kondisi sekarang, ucapanku banyak diprotes sehingga malam itu juga kita pulang kembali ke Jakarta."
    scene black
    with dissolve
    jump scene23

label scene23:
    "Kami sampai di rumahku bersama Achmad Soebardjo, Soekarno, dan Soekarni."
    "Soebarjo mengurus perjanjian rapat dengan anggota PPKI, akhirnya rapat PPKI akan dilaksanakan di rumah Laksamada Maeda pada pukul 24:00."
    "Soebarjo akan menelepon anggota PPKI di rumahnya, sehingga kami semua setuju untuk pulang ke rumah masing-masing."
    Si "Bagaimana denganku Bung?"
    "Soekarni bertanya dengan penuh bingung."
    H "Ya pulang juga."
    Si "Kalau begitu aku minta Bung pinjami satu setel pakaian karena dengan baju Peta yang aku kenakan sekarang aku dapat ditangkap oleh Kempeitai."
    "Kami semua tertawa mendengar permintaan Soekarni itu."
    H "Saudara berani mengadakan revolusi menggempur Dai Nippon. Tetapi sekarang saudara takut akan ditangkap Kempeitai karena memakai pakaian Peta."
    Si "Itu lain halnya Bung, menggempur Nippon dalam suatu revolusi aku berani. Tetapi akan ditangkap Nippon begitu saja karena pakaian Peta apa gunanya."
    "Sambil tertawa, aku memimjamkannya salah satu setelan pakaianku."
    scene black
    with dissolve
    "Saat mereka ingin pulang, telepon rumahku berdering."
    "Aku segera mengangkat telepon tersebut."
    Mi "Selamat malam Tuan Hatta, ini Miyoshi."
    H "Selamat malam Tuan Miyoshi, ada apa malam-malam ini telepon?"
    Mi "Ternyata Tuan sudah kembali dari Rengasdengklok, selamat datang kembali."
    Mi "Begini Tuan Hatta, Mayor Jenderal Nishimura ingin bertemu Tuan dan Tuan Soekarno malam ini juga."
    "Mayor Jenderal Nishimura dari Sumobuco ingin bertemuku saat ini?"
    H "Baik Tuan Miyoshi, bagaimana kalau kita bertemu di rumah Laksamada Maeda pukul 22:00 nanti?"
    H "Setelah itu kita bersama-sama ke rumah Nishimura bersama-sama."
    Mi "Baik tuan, saya akan menemui tuan nanti di rumah Laksamada Maeda."
    "Aku memberi tahu hal ini kepada Soekarno sebelum dia pulang, dan dia akan ke rumahku sebelum pukul 22:00 kemudian kami berangkat bersama."
    "Soekarno datang ke rumahku sebelum pukul 22:00 dan kami langsung berangkat ke rumah Maeda."
    scene black
    with dissolve
    jump scene24

label scene24:
    "Soekarno datang ke rumahku sebelum pukul 22:00 dan kami langsung berangkat ke rumah Maeda."
    "Sesampainya kami di rumah Maeda, Maeda sudah menunggu kami bersama Miyoshi dan beberapa petinggi Dai Nippon."
    Ma "Selamat datang tuan-tuan."
    S "Selamat malam Tuan Maeda dan tuan-tuan semua."
    S "Terima kasih Tuan Maeda telah mengizinkan kami mengadakan rapat PPKI di rumah tuan."
    Ma "Itu kewajiban saya yang mencintai Indonesia merdeka."
    "Setelah setengah jam, kami ke rumah Nishimura dengan Miyoshi sebagai juru bahasa dan Maeda."
    scene black
    with dissolve
    jump scene25

label scene25:
    "Sesampainya di rumah Nishimura, kami bersalaman dengan beliau dan berbicara sebentar tentang perjalanan kami dari Rengasdengklok."
    "Setelah itu kami membahas tentang kelanjutan rapat PPKI yang harusnya dilaksanakan tadi pagi."
    Ni "Maaf tuan-tuan, sayang rapat itu sudah tidak boleh dilaksanakan."
    H "Mengapa begitu? Dai Nippon telah menyetujui kemerdekaan kita."
    Ni "Kalau tadi pagi masih dapat dilangsungkan, pukul 13:00 tadi tentara Dai Nippon yang berada di Jawa mendapat perintah dari Tokyo tidak boleh lagi mengubah status quo."
    S "Tuan tidak bisa bertindak seperti itu, Dai Nippon dan Tokyo sudah mengakui kemerdekaan Indonesia dengan Marsekal Terauchi sebagai perantaranya."
    S "Dan pelaksanaannya diserahkan pada PPKI."
    Ni "Apabila rapatnya dilaksanakan tadi pagi, akan kami bantu. Akan tetapi pada tengah hari tadi kami harus tunduk pada Sekutu dan mempertahankan status quo."
    Ni "Perubahan pada status quo itu tidak diperbolehkan, jadi sekarang rapat PPKI terpaksa kami larang."
    H "Sekarang seluruh rakyat Indonesia tahu bahwa Dai Nippon sudah menyerah pada Sekutu dan mereka juga tidak lupa akan janji Dai Nippon tentang kemerdekaan Indonesia."
    H "Kalau Dai Nippon tidak mampu menepati janjinya, rakyat Indonesia akan memerdekakan dirinya sendiri."
    S "Semangat rakyat yang bergelora sekarang akan diperhatikan oleh Sekutu, kecuali Belanda. Sebab itu Dai Nippon sudah tidak perlu menolong kami lagi."
    S "Kami minta setidaknya jangan halangi kami, rakyat Indonesia dan pemudanya siap mati untuk melaksanakan cita-cita Indonesia Merdeka."
    Ni "Saya benar-benar paham perasaan tuan-tuan dan cita-cita rakyat Indonesia."
    Ni "Aku menangis dalam hatiku, akan tetapi apa boleh buat."
    Ni "Kami sebagai alat telah menerima perintah untuk menghalangi segala upaya perubahan status quo, termasuk gerakan rakyat Indonesia dan pemuda."
    S "Apakah itu termasuk tuan dan tentara Dai Nippon akan menembak pemuda Indonesia sebagai Bunga bangsa jika mereka bergerak melaksanankan janji Dai Nippon?"
    S "Janji tentang kemerdekaan yang Dai Nippon sendiri tidak sanggup menepatinya."
    Ni "Apa boleh buat, dengan hati yang luka kami terpaksa melakukannya."
    Ni "Saya yakin, jika tuan-tuan bersabar sedikit lagi, Sekutu akan memperhatikan keinginan bangsa Indonesia."
    Ni "Betapa sakitnya terasa dalam jiwa, kami Dai Nippon terpaksa tunduk dan menjilat Sekutu agar mendapatkan nasib yang tidak terlalu buruk setelah kami kalah."
    "Mendengar itu, aku tidak dapat lagi menahan amarahku."
    H "Apakah itu janji dan perbuatan seorang Samurai!?"
    H "Dapatkah seorang Samurai menjilat musuhnya yang menang untuk memperoleh nasib yang kurang jelek!?"
    H "Apakah Samurai hanya hebat terhadap orang yang lemah di masa jayanya tetapi hilang semangatnya saat kalah?"
    H "Baiklah, kami akan jalan terus apapun yang terjadi."
    H "Mungkin kami akan menunjukkan kepada Tuan bagaimana jiwa Samurai semestinya menghadapi suasana yang berubah."
    "Mendengar perkataanku itu, Miyoshi sebagai penerjemah gugup ingin meneruskan pesannya pada Nishimura."
    "Aku yakin Miyoshi berusaha memperhalus perkataanku tadi."
    "Aku dan Soekarno meninggalkan rumah Nishimura setelah sepakat kembali ke rumah Maeda setelah berdebat disana tidak membuahkan hasil."
    "Maeda sendiri sudah meninggalkan rapat dari tadi tanpa sepengetahuan kami semua."
    scene black
    with dissolve
    jump scene26

label scene26:
    "Sesampainya di rumah Laksamada Maeda, sudah banyak orang menunggu, kira-kira antara 40-50, semuanya tokoh-tokoh pergerakan dan juga anggota PPKI."
    "Belum lagi diluar banyak pemuda yang ikut menyaksikan."
    "Karena terlalu ramai, kami melanjutkan diskusi di ruang tamu kecil bersama Soekarni, Achmad Soebardjo, dan Sayuti Melik."
    "Di ruangan ini kami mendiskusikan naskah teks Proklamasi."
    S "Aku persilahkan Bung Hatta menyusun teks ringkas itu sebab bahasanya kuanggap yang terbaik, sesudah itu kita persoalkan bersama-sama."
    S "Setelah kita memperoleh persetujuan, nantinya kita bawa ke sidang lengkap yang sudah hadir di ruang tengah."
    H "Apabila aku mesti memikirkannya, lebih baik Bung menuliskan, aku mendiktekannya."
    "Semuanya setuju dan penulisanpun dimulai."
    "Kalimat pertama diambil dari alinea ketiga rencana Pembukaan UUD tentang proklamasi menjadi “Kami bangsa Indonesia dengan ini menyatakan kemerdekaan Indonesia”, dengan ini akan terlihat bahwa Indonesia merdeka atas kemauannya sendiri."
    "Selanjutnya harus ada komplemen yang menyatakan bagaimana caranya menyelenggarakan revolusi nasional sehingga aku mengucapkan"
    "“Hal-hal yang mengenai pemindahan kekuasaan dan lain-lain diselenggarakan dengan cara seksama dan dalam tempo yang sesingkat-singkatnya.”"
    "Setelah sedikit berbincang tentang naskah tersebut, naskah tersebut diketik oleh Sayuti Melik sebelum dibawa rapat."
    scene black
    with dissolve
    jump scene27

label scene27:
    "Kami kembali ke ruang tengah untuk mendiskusikan Teks Proklamasi, rapat ini bukan lagi rapat PPKI dengan banyaknya tokoh-tokoh lain yang ikut terlibat dalam rapat ini."
    "Soekarno membuka rapat dengan membacakan Teks Proklamasi."
    S "Dapatkah saudara-saudara setuju dengan ini?"
    "Suara gemuruh dan tak teratur menjawab “Setuju”."
    S "Benar-benar saudara semuanya setuju?"
    "Baru kali ini serentak mengucapkan “Setuju”."
    H "Kalau saudara semuanya setuju, baiklah kita semuanya yang hadir disini menandatangani naskah Proklamasi Indonesia Merdeka ini sebagai suatu dokumen yang bersejarah."
    H "Ini penting bagi anak cucu kita, mereka harus tahu siapa yang ikut memproklamasikan Indonesia merdeka."
    H "Ambillah contoh kepada naskah proklamasi kemerdekaan Amerika Serikat dahulu, semuanya memutuskan untuk menandatangani keputusan mereka bersama."
    "Setelah aku berkata, rapat menjadi diam dan tidak ada yang berkomentar apapun tentang usulanku itu."
    "Kemudian Soekarni maju dan mengutarakan pendapatnya."
    scene black
    with dissolve
    Si "Bukan kita semua yang hadir disini harus menandatangani naskah itu, cukuplah Bung Karno dan Bung Hatta saja yang menandatanganinya atas nama rakyat Indonesia."
    "Ucapan itu didukung oleh peserta rapat dengan tepuk tangan yang riuh menunjukkan mereka semua setuju."
    "Aku merasa sedikit kecewa dengan keputusan tersebut, tetapi aku juga tidak bisa berbuat apa apa."
    scene black
    with dissolve
    jump scene28

label scene28:
    "Sebelum rapat ditutup, Soekarno mengingatkan bahwa proklamasi akan dibacakan di rumah Soekarno jalan Pegangsaan Timur no. 56 pukul 10:00."
    "Dengan itu rapat berakhir kira-kira pukul 03:00 pagi."
    "Maeda sempat keluar dari kamar tidurnya untuk memberikan kami selamat atas apa yang kami capai saat ini."
    "Sebelum pulang aku berkata pada pemuda-pemuda golongan pers yang ada disana untuk siap memperbanyak teks proklamasi untuk disebar keseluruh Indonesia dan kalau bisa seluruh dunia."
    "Sebelum pulang juga aku sempatkan untuk sahur dan tidak lupa berterima kasih pada Laksamada Maeda atas jasanya selama ini."
    scene black
    with dissolve
    jump scene29

label scene29:
    "Setelah sampai di rumah, aku sholat subuh terlebih dahulu baru tidur."
    "Aku bangun pukul 08:30 dan segera siap-siap ke rumah Soekarno."
    "Pada pukul 09:50 aku berangkat menuju rumah Soekarno."
    scene black
    with dissolve
    jump scene30

label scene30:
    "Aku sampai di rumah Soekarno pukul 09:55, disana sudah banyak rakyat menunggu."
    "Aku menyempatkan diri menghampiri Soekarno."
    H "Bagaimana Bung, sudah siap?"
    S "Siap."
    "Kami bersama ke depan rumah Soekarno."
    "Aku dan Soekarno menghadapi ribuan rakyat Indonesia."
    "Soekarno membuka dengan pidato pembukaan."
    "Proklamasi dibacakan."
    "Setelah dibacakan, kami semua melakukan upacara penaikan bendera Merah Putih yang dijahit oleh Fatmawati dengan bahan seadanya dan diiringi lagu Indonesia Raya."
    "Setelah itu rakyat bergemuruh kesenangan dan aku juga sadar, Indonesia sudah merdeka."
    scene black
    with dissolve
    jump epilog

label epilog:
    "Dengan ini Indonesia sudah merdeka, dan aku tahu ini bukanlah akhir dari perjuangan kami."
    "Masih banyak pekerjaan yang harus kami lakukan, kemerdekaan hanyalah sebuah awalan baru bagi kami."
    "Aku juga tidak akan selamanya mengurus negeri ini, ada saatnya pekerjaan itu dilanjutkan oleh penerus-penerusku."
    "Aku berharap generasi-generasi penerusku tidak akan lupa apa yang aku perjuangkan selama ini dan menjaga hasil perjuanganku ini."
    "Aku mungkin tidak akan hidup saat negeri ini makmur, tapi setidaknya aku tahu suatu saat itu akan terjadi di tangan generasi-generasi penerusku."
    scene black
    with dissolve
    jump end

label end:
    return
