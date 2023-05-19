# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define H = Character("Hatta", color="#CD6247", who_bold=True, who_outlines=[(1, "#000")])
define M = Character("Murid", color="#EE8A79", who_bold=True, who_outlines=[(1, "#000")])
define N = Character("Nomura", color="#B6AAA6", who_bold=True, who_outlines=[(1, "#000")])
define Sj = Character("Sjahrir", color="#F8DC71", who_bold=True, who_outlines=[(1, "#000")])
define D = Character("Driver", color="#99DAEC", who_bold=True, who_outlines=[(1, "#000")])
define S = Character("Soekarno", color="#F18E76", who_bold=True, who_outlines=[(1, "#000")])
define R = Character("Radjiman", color="#af2c40", who_bold=True, who_outlines=[(1, "#000")])
define T = Character("Terauchi", color="#5fb9c9", who_bold=True, who_outlines=[(1, "#000")])
define RnS = Character("Radjiman & Soekarno", color="#55c023", who_bold=True, who_outlines=[(1, "#000")])

# The game starts here.
style screentext:
    color "#9e5f12"
    size 18

style buku_tb:
    background Frame("images/Icon/buku 1_idle.png")
    hover_background Frame("images/Icon/buku 1_hover.png")

init python:
    from datetime import date
    import locale
    locale.setlocale(locale.LC_TIME, 'id_ID')
    today = date.today()
    d1 = today.strftime("%A, %d/%B/%Y")

screen buku:
    vbox:
        xpos 1225
        ypos 10
        button:
            style "buku_tb" xysize (45,156)
            action [Play("sound","audio/SFX/klik.mp3"), Hide("buku"), Show("pilihanbuku")]

screen pilihanbuku:
    frame:
        xalign 0.5 yalign 0.5
        xsize 942 ysize 638
        xpos 630
        background Frame("images/Icon/buku 2.png")
        vbox:    
            xpos 570 ypos 65
            text "[d1]" size 20 color "#ff1212" bold True
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
                action [Play("sound","audio/SFX/klik.mp3"), Hide("pilihanbuku"), Show("buku")]

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
                action [Play("sound","audio/SFX/klik.mp3"), Hide("karakter1"), Show("buku")]
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
                action [Play("sound","audio/SFX/klik.mp3"), Hide("karakter2"), Show("buku")]
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
                action [Play("sound","audio/SFX/klik.mp3"), Hide("organisasi1"), Show("buku")]
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
                action [Play("sound","audio/SFX/klik.mp3"), Hide("organisasi2"), Show("buku")]
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
                action [Play("sound","audio/SFX/klik.mp3"), Hide("peristiwa1"), Show("buku")]
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
                action [Play("sound","audio/SFX/klik.mp3"), Hide("peristiwa2"), Show("buku")]
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
                action [Play("sound","audio/SFX/klik.mp3"), Hide("negara1"), Show("buku")]
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
                action [Play("sound","audio/SFX/klik.mp3"), Hide("negara2"), Show("buku")]
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
                action [Play("sound","audio/SFX/klik.mp3"), Hide("bacaan1"), Show("buku")]
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
                action [Play("sound","audio/SFX/klik.mp3"), Hide("bacaan2"), Show("buku")]
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
    scene bg 1
    show screen buku
    H "Siang murid-murid semua."
    "Sekarang aku sedang berada di Asrama Indonesia Merdeka, disini aku dipercaya sebagai pengajar ekonomi untuk melahirkan ekonom-ekonom saat bangsa ini merdeka nanti."
    "Sekarang sudah 9 Agustus 1945, aku sangat yakin bahwa Indonesia akan merdeka sebentar lagi."
    "Aku sedang mengajar tentang ekonomi kerakyatan dan salah satu murid ada yang bertanya padaku"
    M "Darimana bung mempelajari hal ini semua?"
    H "Pertanyaan yang bagus, pemikiran saya ini berdasarkan tiga pilar, yaitu tradisi Minang, Islam, dan sosialisme Eropa." 
    extend " Biar saya jelaskan satu per satu."
    H "Budaya Minangkabau mengajarkan saya bahwa harta bukanlah sumber kekayaan bagi sepeser orang saja tetapi sebagai sumber kemakmuran masyarakatnya," 
    extend " sehingga budaya Minangkabau menentang adanya praktek memperkaya diri sendiri."
    H "Sosialisme di Eropa berkembang dengan terjadinya Revolusi Industri disana, tokoh-tokoh seperti Marx dan Engels-lah yang mematangkan teori sosialisme ini."
    H "Sosialisme bisa diraih dengan dua cara, cara kekerasan disebut sosialisme revolusioner dan cara demokrasi dengan partai perwakilan buruh disebut sosialisme demokratis."
    H "Paham sosialisme ini tidak berasal dari Marx saja, bahkan Islam juga mengajarkan sosialisme." 
    extend " Ayat-ayat seperti QS. Al-Maun Ayat 1-7, Al-Humazah Ayat 1-3 mengajari kita tentang tercelanya orang-orang yang memperkaya diri sendiri."
    H "Sehingga ekonomi yang saya dambakan dalam Indonesia nanti adalah perekonomian yang bersifat kebersamaan, kerakyatan, dan kooperasi agar rakyat bisa hidup makmur."
    "Tak lama kemudian, waktu mengajarku sudah habis, saatnya aku pulang."
    H "Baik murid-murid sekalian, mungkin sekian dari saya untuk hari ini, Assalamualaikum."
    scene bg 2
    "Hatta meninggalkan ruang kelas"
    scene black
    with dissolve
    jump scene2

label scene2:
    scene bg 3
    "Saat aku keluar asrama, ternyata sudah ada Letnan Kolonel Nomura yang menungguku, Nomura pasti ada keperluan denganku, maka dari itu aku menghampirinya."
    scene bg 4
    N "Selamat sore, Hatta-san."
    H "Selamat sore, ada apa Nomura-san?"
    N "Tuan diminta ke Dalat malam ini untuk bertemu atasan kami, Marsekal Terauchi untuk membahas kemerdekaan bangsa Tuan."
    H "Adakah wakil Indonesia yang hadir selain saya?"
    N "Soekarno-san dan Radjiman-san juga akan menemani Tuan dalam perjalanan ini."
    H "Baik saya bersedia, saya akan segera siap-siap berangkat saat pulang."
    N "Arigatou Hatta-san, nanti Tuan akan dijemput oleh utusan saya dan kita akan bertemu lagi nanti di Bandara Kemayoran."
    "Aku mengakhiri pertemuanku dengan Nomura dengan bersalaman setelah itu kami berpisah."
    scene bg 3
    "Nomura masuk ke mobilnya dan pergi sedangkan aku pulang ke rumahku."
    scene black
    with dissolve
    jump scene3

label scene3:
    scene bg 5
    "Sesampainya di rumah, aku langsung mempersiapkan diriku untuk berangkat nanti malam."
    "Adzhan Maghrib berkumandang tak lama aku menyelesaikan persiapanku."
    "Aku segera keluar untuk berbuka puasa."
    "Setelah berbuka puasa sholat Maghrib, Sjahrir ingin berbicara denganku."
    scene bg 6
    Sj "Ada keperluan apa bung pergi ke Dalat?"
    H "Saya akan bertemu dengan Marsekal Terauchi disana, Nomura bilang beliau memiliki hal penting yang ingin beliau bicarakan tentang kemerdekaan Indonesia."
    Sj "Saya heran dengan dirimu bung, Nippon itu sudah semakin terjepit, lebih baik kita yang menentukan kapan Indonesia merdeka, bukan Dai Nippon."
    H "Saya paham dengan kegelisahan bung, tapi bersabarlah sedikit, kita tidak bisa melakukan hal gegabah tanpa persetujuan PPKI."
    Sj "PPKI? Bung masih yakin Dai Nippon akan menepati janjinya? Organisasi itu tetap saja organisasi buatan Nippon."
    H "Bung, jangan lupakan BPUPKI organisasi buatan Dai Nippon itu, BPUPKI membantu kita dalam mempersiapkan pondasi negara kita jika Indonesia merdeka nanti."
    H "Percayalah bahwa saya bawa berita tanggal kemerdekaan saat pulang dari Dalat nanti, bung lanjutkan saja perkerjaan bung selama ini dan pantau terus radio sekutu."
    Sj "Sudahlah terserah bung saja!"
    scene bg 5
    "Sjahrir meninggalkanku setelah tidak terlihat tidak puas dengan jawabanku."
    "Akhirnya ada mobil yang datang, pasti itu adalah utusan Nomura."
    scene bg 7
    D "Selamat malam Hatta-san, apakah tuan siap berangkat sekarang?"
    H "Selamat malam, saya sudah siap."
    D "Baik, tuan dipersilahkan masuk mobil, kita berangkat segera."
    "Aku segera memasuki mobil dan dengan ini kami pergi menuju Bandara Kemayoran."
    scene black
    with dissolve
    jump scene4

label scene4:
    scene bg 8
    "Kami akhirnya sampai di Bandara Kemayoran."
    "Aku segera dituntun ke ruang tunggu bandara."
    scene bg 9
    "Di ruang tunggu itu sudah ada Soekarno dan Radjiman."
    H "Selamat malam saudara-saudara."
    RnS "Selamat malam bung."
    H "Apa yang harus kita lakukan sekarang?"
    R "Untuk saat ini kita menunggu Nomura datang."
    H "Baiklah, terima kasih bung."
    "Selagi menunggu Nomura, aku membaca buku dan sekali-kali bicara dengan mereka."
    "Pada akhirnya Nomura datang."
    scene bg 10
    N "Selamat malam tuan-tuan, maaf telah membuat tuan-tuan menunggu."
    N "Silahkan tuan-tuan ikut saya, kita berangkat sekarang."
    "Kami mengikuti Nomura dan kami akhirnya naik pesawat."
    scene black
    with dissolve
    "Pesawat tak lama kemudian lepas landas."
    jump scene5

label scene5:
    "Perjalanan kami ke Dalat tidaklah lancar."
    "Perjalanan kami dipenuhi dengan kegelisahan, kecemasan, dan penundaan."
    "Selama perjalanan kami, kami menginap semalam di Singapura dan semalam di Saigon."
    "Dari sini juga aku dapat mengetahui bahwa situasi Dai Nippon semakin terpojok."
    "Setelah bermalam di Saigon, kami berangkat dari pagi untuk akhirnya ke Dalat."
    jump scene6

label scene6:
    "Pada tepat pukul 10:00 kami bertemu dengan Marsekal Terauchi."
    "Setelah kami semua bersalaman dengan Terauchi, beliau memberikan pidato singkat."
    "Pidato tersebut berisi tentang bagaimana besarnya peran Indonesia dalam membantu Dai Nippon sehingga akhirnya Dai Nippon memutuskan untuk memberikan Indonesia kemerdekaan dan juga secara simbolis melantik aku dan Soekarno sebagai ketua dan wakil PPKI."
    T "Selamat!"
    S "Atas nama bangsa Indonesia, saya ucapkan terima kasih."
    "Terauchi mengucapkan selamat kepada kami bertiga sambil bersalaman dengan kami sekali lagi."
    "Hatiku senang sekali mendengar Indonesia merdeka, hari ini sekaligus hari ulang tahunku,"
    "Aku merasa ini adalah hadiah ulang tahun yang membuktikan bahwa perjuangan aku selama ini tidak sia-sia."
    "Setelah Terauchi memberikat selamat pada kami, kami didatangkan kue-kue untuk disantap bersama sebagai perayaan."
    "Dalam jamuan ini muka Terauchi terlihat lemas, apakah itu karena sakit lumpuhnya? Atau karena kondisi perang bagi Dai Nippon? Atau keduanya?"
    "Pada jamuan ini juga Soekarno bertanya pada Terauchi."
    S "Terauchi-san, kapankah keputusan Dai Nippon ini dapat kami beritahu kepada rakyat Indonesia?"
    T "Terserah kepada Tuan-tuan Panitia Persiapan, kapan saja boleh, itu sudah menjadi urusan Tuan.
    Setelah itu Terauchi menghampiriku dan bertanya."
    T "Hatta-san, Indonesia sebentar lagi merdeka, apakah Hatta-san sudah memiliki rencana untuk menikah?"
    "Aku terkejut mendengar pertanyaan Terauchi itu, aku sama sekali belum memikirkan hal itu."
    H "Untuk hal itu belum saya pikirkan Terauchi-san."
    "Semua tertawa mendengar jawabanku itu."
    "Kami untuk terakhir kalinya bersalaman dengan Terauchi dan kembali ke Saigon sebelum pukul 12.00 dan kembali ke tempat peristirahatan kami di Saigon."
    jump scene7

label scene7:
    "Pada pukul 16:30, Nomura datang menghampiri tempat kami."
    N "Hatta-san, bisakah saya berbicara dengan Soekarno-san?"
    H "Maaf Nomura-san, Soekarno sedang mandi sekarang."
    H "Silahkan duduk selagi menunggunya Nomura-san."
    N "Baik Hatta-san, saya berbicara dengan Hatta-san saja."
    N "Bagaimana perjalanan anda sejauh ini Hatta-san?"
    H "Sejauh ini baik Nomura-san, terima kasih sudah menemani kami dalam perjalanan ini."
    N "Sudah menjadi janji Dai Nippon untuk memberikan kemerdekaan bangsa Tuan."
    "Nomura akhirnya membicarakan apa yang sebenarnya ingin ia bicarakan."
    N "Hatta-san, tentara Rusia sudah menyerang Manchuko, akan tetapi Tuan tenang saja, tentara Dai Nippon cukup kuat untuk menahannya."
    "Aku tahu itu adalah sebuah kebohongan."
    H "Bagaimana caranya Dai Nippon bisa bertahan dari serangan Rusia itu Nomura-san?"
    N "Kami sudah yakin dari awal cepat atau lambat Rusia akan menyerang Dai Nippon, maka dari itu Dai Nippon sudah membuat fortifikasi-fortifikasi yang tidak dapat mereka tembus sebesar apapun kekuatan serangan mereka di Manchuko."
    N "Tuan juga jangan melupakan semangat juang tentara Dai Nippon yang tak terpatahkan, dengan dua hal ini serangan Rusia sebesar apapun dapat kami halau."
    "Lagi-lagi Nomura berbohong."
    S "Selamat sore Nomura-san."
    scene bg 11
    N "Ah Soekarno-san, selamat sore."
    "Nomura mengulang berita invasi Rusia tadi ke Soekarno dan kebohogannya tentang pertahanan Dai Nippon."
    "Setelah itu Nomura pergi karena ingin bertemu beberapa petinggi Dai Nippon di Saigon,"
    scene bg 12
    H "Saya yakin Nomura berbohong tentang kuatnya pertahanan Dai Nippon di Mancuko."
    S "Bung tidak sendirian."
    H "Dengan gempuran McArthur dan Nimitz dari selatan dan Rusia dari utara, saya yakin bung Dai Nippon akan tunduk kurang dari dua minggu."
    S "Kita harus dapat manfaatkan keadaan ini bung."
    H "Saya setuju bung, kita harus cepat-cepat menyelesaikan persiapan kemerdekaan Indonesia."
    "Kami mengulangi pembicaraan kita saat dr. Radjiman masuk ke ruangan kami."
    "Beliau juga setuju bahwa dua minggu adalah waktu maksimal Dai Nippon dapat bertahan."
    "Malam ini kami bermalam di Saigon, besok kami kembali ke Singapura."
    jump scene8

label scene8:
    scene black
    with dissolve
    "Paginya pukul 08:00, kami berangkat menuju Singapura"
    "Disana kami menginap lagi semalam."
    "Kami akhirnya berangkat kembali ke Jakarta dari Singapura pukul 09:00 lewat."
    jump scene9

label scene9:
    "Sudah banyak petinggi Jepang dan rakyat Indonesia yang menunggu kedatangan kami sesampainya kami di bandara."
    "Rakyat Indonesia meminta Soekarno berkata sesuatu."
    S "Apabila dulu saya katakan bahwa Indonesia akan merdeka sebelum jagung berbuah, sekarang dapat dikatakan Indonesia akan merdeka sebelum jagung berbunga,"
    "Seperti biasa, suara Soekarno lantang dan menggelegar."
    "Respon rakyat juga tidak kalah menggelegar."
    "“Hidup Indonesia!”, “Merdeka!”, “Indonesia Merdeka!”, dan masih banyak lagi."
    "Sebenarnya kami ingin pulang, tetapi petinggi Dai Nippon menyuruh kami ke Istana Gunseireikan terlebih dahulu."
    jump scene10

label scene10:
    "Sesampainya kami disana, kami mendapat sambutan dan juga selamat dari petinggi-petinggi disana sekaligus makan siang."
    "Mereka juga mengulang lagi bahwa apa yang disampaikan Terauchi merupakan keputusan Tokyo dan PPKI diperbolehkan bekerja sampai memerdekakan Indonesia."
    "Pidato itu dapat sambutan meriah dari sesama petinggi Dai Nippon."
    "Setelah makan siang kami diizinkan pulang."
    jump end

label end:
    return
