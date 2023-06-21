# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define H = Character("HATTA", color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = -20, ypos = -8, xsize = 150, ysize = 70))
define M = Character("MURID", xpos = 47, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = -22, ypos = -8, xsize = 140, ysize = 70))
define N = Character("NOMURA", xpos = 75, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = -9, ypos = -8, xsize = 170, ysize = 70))
define Sj = Character("SJAHRIR", xpos = 75, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = -9, ypos = -8, xsize = 170, ysize = 70))
define S = Character("SOEKARNO", xpos = 110, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = 10, ypos = -8, xsize = 205, ysize = 70))
define R = Character("RADJIMAN", xpos = 105, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = 6, ypos = -8, xsize = 205, ysize = 70))
define T = Character("TERAUCHI", xpos = 103, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = 4, ypos = -8, xsize = 205, ysize = 70))
define AS = Character("ACHMAD SOEBARDJO", xpos = 265, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = 85, ypos = -8, xsize = 365, ysize = 70))
define Ma = Character("MAEDA", xpos = 60, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = -17, ypos = -8, xsize = 150, ysize = 70))
define SS = Character("SOEBADIO SASTROSATOMO", xpos = 350, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = 127, ypos = -8, xsize = 450, ysize = 70))
define Si = Character("SOEKARNI", xpos = 95, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = 5, ypos = -8, xsize = 190, ysize = 70))
define Mi = Character("MIYOSHI", xpos = 72, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = -10, ypos = -8, xsize = 170, ysize = 70))
define Ni = Character("NISHIMURA", xpos = 113, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = 12, ypos = -8, xsize = 205, ysize = 70))
define W = Character("WIKANA", xpos = 75, color="#2E2C2B", namebox_background = Frame("gui/namebox1.png", xpos = -9, ypos = -8, xsize = 170, ysize = 70))

# The game starts here.
style button_tb:
    background Frame("images/Icon/button_idle.png")
    hover_background Frame("images/Icon/button_hover.png")

style button1_tb:
    background Frame("images/Icon/button_idle.png")
    hover_background Frame("images/Icon/button_hover.png")
    selected_idle_background Frame("images/Icon/button_selected.png")
    selected_hover_background Frame("images/Icon/button_hover.png")

style button2_tb:
    background Frame("images/Icon/back_idle.png")
    hover_background Frame("images/Icon/back_hover.png")

style button3_tb:
    background Frame("images/Icon/next_idle.png")
    hover_background Frame("images/Icon/next_hover.png")

style button4_tb:
    background Frame("images/Icon/close_idle.png")
    hover_background Frame("images/Icon/close_hover.png")

image background1 = Movie(size=(1280,720), channel="movie", play="video/epilog.ogv", loop=True)
image background2 = im.Scale("images/Screen/ended.png",1280,720)


#init:
    #untuk disable rollback
#    $config.rollback_enabled = False

label start:
    with dissolve
    play music defaultmusikbgm fadein 3.0
    scene asrama indonesia merdeka
    show screen tanggal
    show screen buku
    show hatta talk  at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Siang murid-murid semua."
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Sekarang aku sedang berada di Asrama Indonesia Merdeka, disini aku dipercaya sebagai pengajar ekonomi untuk melahirkan ekonom-ekonom saat bangsa ini merdeka nanti."
    "Sekarang sudah 9 Agustus 1945, aku sangat yakin bahwa Indonesia akan merdeka sebentar lagi."
    "Aku sedang mengajar tentang ekonomi kerakyatan dan salah satu murid ada yang bertanya padaku."
    M "Darimana Bung mempelajari hal ini semua?"
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Pertanyaan yang bagus, pemikiran saya ini berdasarkan tiga pilar, yaitu tradisi Minang, Islam, dan sosialisme Eropa. Biar saya jelaskan satu per satu."
    H "Budaya Minangkabau mengajarkan saya bahwa harta bukanlah sumber kekayaan bagi sepeser orang saja tetapi sebagai sumber kemakmuran masyarakatnya, sehingga budaya Minangkabau menentang adanya praktek memperkaya diri sendiri."
    H "Sosialisme di Eropa berkembang dengan terjadinya Revolusi Industri disana, tokoh-tokoh seperti Marx dan Engels-lah yang mematangkan teori sosialisme ini."
    $renpy.notify("Karakter Marx dan Engels telah ditambahkan ke direktori.")
    $ unlock += 1
    H "Sosialisme bisa diraih dengan dua cara, cara kekerasan disebut sosialisme revolusioner dan cara demokrasi dengan partai perwakilan buruh disebut sosialisme demokratis."
    H "Paham sosialisme ini tidak berasal dari Marx saja, bahkan Islam juga mengajarkan sosialisme. Ayat-ayat seperti QS. Al-Maun Ayat 1-7, Al-Humazah Ayat 1-3 mengajari kita tentang tercelanya orang-orang yang memperkaya diri sendiri."
    $renpy.notify("Bacaan QS. Al-Maun Ayat 1-7 dan QS. Al-Humazah Ayat 1-3 telah ditambahkan ke direktori.")
    $ unlock += 1
    H "Sehingga ekonomi yang saya dambakan dalam Indonesia nanti adalah perekonomian yang bersifat kebersamaan, kerakyatan, dan kooperasi agar rakyat bisa hidup makmur."
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Tak lama kemudian, waktu mengajarku sudah habis, saatnya aku pulang."
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Baik murid-murid sekalian, mungkin sekian dari saya untuk hari ini, Assalamualaikum."
    scene black
    with dissolve
    jump scene2

label scene2:
    play music musik2
    scene depan asrama indonesia merdeka
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Saat aku keluar asrama, ternyata sudah ada Letnan Kolonel Nomura yang menungguku, Nomura pasti ada keperluan denganku, maka dari itu aku menghampirinya."
    show nomura talk at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    show hatta silent at Position(xpos=280,ypos=120):
        zoom 0.7
    N "Selamat sore, Tuan Hatta."
    show hatta talk at Position(xpos=280,ypos=120):
        zoom 0.7
    show nomura silent at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    H "Selamat sore, ada apa Tuan Nomura?"
    show nomura talk at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    show hatta silent at Position(xpos=280,ypos=120):
        zoom 0.7
    N "Tuan diminta ke Dalat malam ini untuk bertemu atasan kami, Marsekal Terauchi untuk membahas kemerdekaan bangsa Tuan."
    show hatta talk at Position(xpos=280,ypos=120):
        zoom 0.7
    show nomura silent at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    H "Adakah wakil Indonesia yang hadir selain saya?"
    show nomura talk at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    show hatta silent at Position(xpos=280,ypos=120):
        zoom 0.7
    N "Tuan Soekarno dan Tuan Radjiman juga akan menemani Tuan dalam perjalanan ini."
    show hatta talk at Position(xpos=280,ypos=120):
        zoom 0.7
    show nomura silent at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    H "Baik saya bersedia, saya akan segera siap-siap berangkat saat pulang."
    show nomura talk at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    show hatta silent at Position(xpos=280,ypos=120):
        zoom 0.7
    N "Arigatou Tuan Hatta, nanti Tuan akan dijemput oleh utusan saya dan kita akan bertemu lagi nanti di Bandara Kemayoran."
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    hide nomura
    "Aku mengakhiri pertemuanku dengan Nomura dengan bersalaman setelah itu kami berpisah, Nomura masuk ke mobilnya dan pergi sedangkan aku pulang ke rumahku."
    scene black
    with dissolve
    jump scene3

label scene3:
    play music defaultmusikbgm fadein 3.0
    scene rumah hatta
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Sesampainya di rumah, aku langsung mempersiapkan diriku untuk berangkat nanti malam."
    "Adzhan Maghrib berkumandang tak lama aku menyelesaikan persiapanku."
    "Aku segera keluar untuk berbuka puasa."
    "Setelah berbuka puasa sholat Maghrib, Sjahrir ingin berbicara denganku."
    scene black
    with dissolve
    jump scene3a
    
label scene3a:
    scene rumah hatta
    show sjahrir talk at Position(xpos=280,ypos=95):
        zoom 0.65
    show hatta silent at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    Sj "Ada keperluan apa Bung pergi ke Dalat?"
    show hatta talk at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    show sjahrir silent at Position(xpos=280,ypos=95):
        zoom 0.65
    H "Aku akan bertemu dengan Marsekal Terauchi disana, Nomura bilang beliau memiliki hal penting yang ingin beliau bicarakan tentang kemerdekaan Indonesia."
    show sjahrir talk at Position(xpos=280,ypos=95):
        zoom 0.65
    show hatta silent at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    Sj "Saya heran dengan dirimu Bung, Nippon itu sudah semakin terjepit, lebih baik kita yang menentukan kapan Indonesia merdeka, bukan Dai Nippon."
    show hatta talk at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    show sjahrir silent at Position(xpos=280,ypos=95):
        zoom 0.65
    H "Aku paham dengan kegelisahanmu, tapi bersabarlah sedikit, kita tidak bisa melakukan hal gegabah tanpa persetujuan PPKI."
    $renpy.notify("Organisasi PPKI telah ditambahkan ke direktori.")
    $ unlock += 1
    show sjahrir talk at Position(xpos=280,ypos=95):
        zoom 0.65
    show hatta silent at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    Sj "PPKI? Bung masih yakin Dai Nippon akan menepati janjinya? Organisasi itu tetap saja organisasi buatan Nippon."
    show hatta talk at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    show sjahrir silent at Position(xpos=280,ypos=95):
        zoom 0.65
    H "Bung, jangan lupakan BPUPKI organisasi buatan Dai Nippon itu, BPUPKI membantu kita dalam mempersiapkan pondasi negara kita jika Indonesia merdeka nanti."
    $renpy.notify("Organisasi BPUPKI dan peristiwa Sidang Pertama BPUPKI telah ditambahkan ke direktori.")
    $ unlock += 1
    H "Percayalah bahwa aku bawa berita tanggal kemerdekaan saat pulang dari Dalat nanti, Bung lanjutkan saja perkerjaan Bung selama ini dan pantau terus radio sekutu."
    show sjahrir talk at Position(xpos=280,ypos=95):
        zoom 0.65
    show hatta silent at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    Sj "Sudahlah terserah Bung saja!"
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    hide sjahrir
    "Sjahrir meninggalkanku setelah tidak terlihat tidak puas dengan jawabanku."
    "Akhirnya ada mobil yang datang, pasti itu adalah utusan Nomura."
    "Aku segera memasuki mobil dan dengan ini kami pergi menuju Bandara Kemayoran."
    scene black
    with dissolve
    jump scene4

label scene4:
    scene bandara kemayoran
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Kami akhirnya sampai di Bandara Kemayoran."
    "Aku segera dituntun ke ruang tunggu bandara."
    show radjiman silent at Position(xpos=120,ypos=115) behind hatta:
        zoom 0.75
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    "Di ruang tunggu itu sudah ada Soekarno dan Radjiman."
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Selamat malam saudara-saudara."
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show radjiman talk at Position(xpos=120,ypos=115) behind hatta:
        zoom 0.75
    R "Selamat malam Bung."
    show radjiman silent at Position(xpos=120,ypos=115) behind hatta:
        zoom 0.75
    show soekarno talk at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    S "Selamat malam Bung."
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    H "Apa yang harus kita lakukan sekarang?"
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show radjiman talk at Position(xpos=120,ypos=115) behind hatta:
        zoom 0.75
    R "Untuk saat ini kita menunggu Nomura datang."
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    show radjiman silent at Position(xpos=120,ypos=115) behind hatta:
        zoom 0.75
    H "Baiklah, terima kasih Bung."
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Kami bertiga menunggu kedatangan Nomura sambil berbicara ringan."
    "Pada akhirnya Nomura datang."
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    show radjiman silent at Position(xpos=0,ypos=115) behind hatta:
        zoom 0.75
    show soekarno silent at Position(xpos=460,ypos=120) behind hatta:
        zoom 0.75
    show nomura talk at Position(xpos=670,ypos=120) behind soekarno:
        zoom 0.7
    N "Selamat malam tuan-tuan, maaf telah membuat tuan-tuan menunggu."
    N "Silahkan tuan-tuan ikut saya, kita berangkat sekarang."
    show nomura silent at Position(xpos=670,ypos=120) behind soekarno:
        zoom 0.7
    "Kami mengikuti Nomura dan kami akhirnya naik pesawat."
    hide hatta
    hide radjiman
    hide soekarno
    hide nomura
    hide screen tanggal
    with dissolve
    scene black
    "Pesawat tak lama kemudian lepas landas."
    with dissolve
    scene black
    jump scene5

label scene5:
    play music airplane_takeoff
    scene black
    "Perjalanan kami ke Dalat tidaklah lancar."
    "Perjalanan kami dipenuhi dengan kegelisahan, kecemasan, dan penundaan."
    "Selama perjalanan kami, kami menginap semalam di Singapura dan semalam di Saigon."
    "Dari sini juga aku dapat mengetahui bahwa situasi Dai Nippon semakin terpojok."
    "Setelah bermalam di Saigon, kami berangkat dari pagi untuk akhirnya ke Dalat."
    scene black
    with dissolve
    jump scene6

label scene6:
    play music musik2
    $ waktu += 1
    scene kantor terauchi
    show screen tanggal
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Pada tepat pukul 10:00 kami bertemu dengan Marsekal Terauchi."
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    show radjiman silent at Position(xpos=0,ypos=115) behind hatta:
        zoom 0.75
    show soekarno silent at Position(xpos=460,ypos=120) behind hatta:
        zoom 0.75
    show terauchi silent at Position(xpos=640,ypos=110) behind soekarno:
        zoom 0.7
    "Setelah kami semua bersalaman dengan Terauchi, beliau memberikan pidato singkat."
    "Pidato tersebut berisi tentang bagaimana besarnya peran Indonesia dalam membantu Dai Nippon sehingga akhirnya Dai Nippon memutuskan untuk memberikan Indonesia kemerdekaan dan juga secara simbolis melantik aku dan Soekarno sebagai ketua dan wakil PPKI."
    show terauchi talk at Position(xpos=640,ypos=110) behind soekarno:
        zoom 0.7
    T "Selamat!"
    show terauchi silent at Position(xpos=640,ypos=110) behind soekarno:
        zoom 0.7
    show soekarno talk at Position(xpos=460,ypos=120) behind hatta:
        zoom 0.75
    S "Atas nama bangsa Indonesia, saya ucapkan terima kasih."
    show soekarno silent at Position(xpos=460,ypos=120) behind hatta:
        zoom 0.75
    "Terauchi mengucapkan selamat kepada kami bertiga sambil bersalaman dengan kami sekali lagi."
    "Hatiku senang sekali mendengar Indonesia merdeka, hari ini sekaligus hari ulang tahunku, Aku merasa ini adalah hadiah ulang tahun yang membuktikan bahwa perjuangan aku selama ini tidak sia-sia."
    "Setelah Terauchi memberikat selamat pada kami, kami didatangkan kue-kue untuk disantap bersama sebagai perayaan."
    "Dalam jamuan ini muka Terauchi terlihat lemas, apakah itu karena sakit lumpuhnya? Atau karena kondisi perang bagi Dai Nippon? Atau keduanya?"
    "Pada jamuan ini juga Soekarno bertanya pada Terauchi."
    show soekarno talk at Position(xpos=460,ypos=120) behind hatta:
        zoom 0.75
    S "Tuan Terauchi, kapankah keputusan Dai Nippon ini dapat kami beritahu kepada rakyat Indonesia?"
    show soekarno silent at Position(xpos=460,ypos=120) behind hatta:
        zoom 0.75
    show terauchi talk at Position(xpos=640,ypos=110) behind soekarno:
        zoom 0.7
    T "Terserah kepada tuan-tuan Panitia Persiapan, kapan saja boleh, itu sudah menjadi urusan tuan."
    show terauchi silent at Position(xpos=640,ypos=110) behind soekarno:
        zoom 0.7
    "Setelah itu Terauchi menghampiriku dan bertanya."
    show terauchi talk at Position(xpos=640,ypos=110) behind soekarno:
        zoom 0.7
    T "Tuan Hatta, Indonesia sebentar lagi merdeka, apakah tuan sudah memiliki rencana untuk menikah?"
    show terauchi silent at Position(xpos=640,ypos=110) behind soekarno:
        zoom 0.7
    "Aku terkejut mendengar pertanyaan Terauchi itu, aku sama sekali belum memikirkan hal itu."
    show hatta talk at Position(xpos=260,ypos=120):
        zoom 0.7
    H "Untuk hal itu belum saya pikirkan Tuan Terauchi."
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    "Semua tertawa mendengar jawabanku itu."
    "Kami untuk terakhir kalinya bersalaman dengan Terauchi dan kembali ke Saigon sebelum pukul 12.00 dan kembali ke tempat peristirahatan kami di Saigon."
    scene black
    with dissolve
    jump scene7

label scene7:
    scene peristirahatan saigon
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Pada pukul 16:30, Nomura datang menghampiri tempat kami."
    show nomura talk at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    show hatta silent at Position(xpos=280,ypos=120):
        zoom 0.7
    N "Tuan Hatta, bisakah saya berbicara dengan Tuan Soekarno?"
    show hatta talk at Position(xpos=280,ypos=120):
        zoom 0.7
    show nomura silent at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    H "Maaf Tuan Nomura, Soekarno sedang mandi sekarang."
    H "Silahkan duduk selagi menunggunya Tuan Nomura."
    show nomura talk at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    show hatta silent at Position(xpos=280,ypos=120):
        zoom 0.7
    N "Baik Tuan, saya berbicara dengan Tuan saja."
    N "Bagaimana perjalanan anda sejauh ini Tuan?"
    show hatta talk at Position(xpos=280,ypos=120):
        zoom 0.7
    show nomura silent at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    H "Sejauh ini baik Tuan Nomura, terima kasih sudah menemani kami dalam perjalanan ini."
    show nomura talk at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    show hatta silent at Position(xpos=280,ypos=120):
        zoom 0.7
    N "Sudah menjadi janji Dai Nippon untuk memberikan kemerdekaan bangsa Tuan."
    show nomura silent at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    "Nomura akhirnya membicarakan apa yang sebenarnya ingin ia bicarakan."
    show nomura talk at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    N "Tuan Hatta, tentara Rusia sudah menyerang Mancuko, akan tetapi Tuan tenang saja, tentara Dai Nippon cukup kuat untuk menahannya."
    $renpy.notify("Peristiwa Invasi Rusia di Asia, negara Rusia, dan Mancuko telah ditambahkan ke direktori.")
    $ unlock += 1
    show nomura silent at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    "Aku tahu itu adalah sebuah kebohongan."
    show hatta talk at Position(xpos=280,ypos=120):
        zoom 0.7
    H "Bagaimana caranya Dai Nippon bisa bertahan dari serangan Rusia itu Tuan Nomura?"
    show nomura talk at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    show hatta silent at Position(xpos=280,ypos=120):
        zoom 0.7
    N "Kami sudah yakin dari awal cepat atau lambat Rusia akan menyerang Dai Nippon, maka dari itu Dai Nippon sudah membuat fortifikasi-fortifikasi yang tidak dapat mereka tembus sebesar apapun kekuatan serangan mereka di Mancuko."
    N "Tuan juga jangan melupakan semangat juang tentara Dai Nippon yang tak terpatahkan, dengan dua hal ini serangan Rusia sebesar apapun dapat kami halau."
    show nomura silent at Position(xpos=475,ypos=120) behind hatta:
        zoom 0.7
    "Lagi-lagi Nomura berbohong."
    scene black
    with dissolve
    jump scene7a

label scene7a:
    scene peristirahatan saigon
    show soekarno talk at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    show nomura silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.7
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    S "Selamat sore Tuan Nomura."
    show nomura talk at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.7
    show soekarno silent at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    N "Ah Tuan Soekarno, selamat sore."
    show nomura silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.7
    "Nomura mengulang berita invasi Rusia tadi ke Soekarno dan kebohogannya tentang pertahanan Dai Nippon."
    hide nomura
    show hatta silent at Position(xpos=475,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    "Setelah itu Nomura pergi karena ingin bertemu beberapa petinggi Dai Nippon di Saigon."
    scene black
    with dissolve
    jump scene7b

label scene7b:
    play music defaultmusikbgm fadein 3.0
    scene peristirahatan saigon
    show hatta talk at Position(xpos=475,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    H "Aku yakin Nomura berbohong tentang kuatnya pertahanan Dai Nippon di Mancuko."
    show soekarno talk at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    show hatta silent at Position(xpos=475,ypos=120):
        zoom 0.7
    S "Bung tidak sendirian."
    show hatta talk at Position(xpos=475,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    H "Dengan gempuran MacArthur dan Nimitz dari selatan dan Rusia dari utara, aku yakin Bung Dai Nippon akan tunduk kurang dari dua minggu."
    $renpy.notify("Karakter Douglas MacArthur dan Chester W. Nimitz telah ditambahkan ke direktori.")
    $ unlock += 1
    show soekarno talk at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    show hatta silent at Position(xpos=475,ypos=120):
        zoom 0.7
    S "Kita harus dapat manfaatkan keadaan ini Bung."
    show hatta talk at Position(xpos=475,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    H "Aku setuju Bung, kita harus cepat-cepat menyelesaikan persiapan kemerdekaan Indonesia."
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    show radjiman silent at Position(xpos=530,ypos=115) behind hatta:
        zoom 0.75
    "Kami mengulangi pembicaraan kita saat dr. Radjiman masuk ke ruangan kami."
    "Beliau juga setuju bahwa dua minggu adalah waktu maksimal Dai Nippon dapat bertahan."
    "Malam ini kami bermalam di Saigon, besok kami kembali ke Singapura."
    hide screen tanggal
    scene black
    with dissolve
    jump scene8

label scene8:
    play music airplane_takeoff
    scene black
    "Paginya pukul 08:00, kami berangkat menuju Singapura"
    "Disana kami menginap lagi semalam."
    "Kami akhirnya berangkat kembali ke Jakarta dari Singapura pukul 09:00 lewat."
    "Selama perjalanan, aku selalu memikirkan apa yang akan aku lakukan jika Dai Nippon benar benar sudah bertekuk lutut pada Sekutu."
    scene black
    with dissolve
    jump scene9

label scene9:
    play music defaultmusikbgm fadein 3.0
    $ waktu += 1
    scene bandara kemayoran
    show screen tanggal
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    show radjiman silent at Position(xpos=530,ypos=115) behind hatta:
        zoom 0.75
    "Sudah banyak petinggi Jepang dan rakyat Indonesia yang menunggu kedatangan kami sesampainya kami di bandara."
    "Rakyat Indonesia meminta Soekarno berkata sesuatu."
    show soekarno talk at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    S "Apabila dulu saya katakan bahwa Indonesia akan merdeka sebelum jagung berbuah, sekarang dapat dikatakan Indonesia akan merdeka sebelum jagung berBunga."
    show soekarno silent at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    "Seperti biasa, suara Soekarno lantang dan menggelegar."
    play music crowd_cheer
    "Respon rakyat juga tidak kalah menggelegar."
    "“Hidup Indonesia!”, “Merdeka!”, “Indonesia Merdeka!”, dan masih banyak lagi."
    "Sebenarnya kami ingin pulang, tetapi petinggi Dai Nippon menyuruh kami ke Istana Gunseireikan terlebih dahulu."
    scene black
    with dissolve
    jump scene10

label scene10:
    play music defaultmusikbgm fadein 3.0
    scene istana gunseireikan
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    show radjiman silent at Position(xpos=530,ypos=115) behind hatta:
        zoom 0.75
    "Sesampainya kami disana, kami mendapat sambutan dan juga selamat dari petinggi-petinggi disana sekaligus makan siang."
    "Mereka juga mengulang lagi bahwa apa yang disampaikan Terauchi merupakan keputusan Tokyo dan PPKI diperbolehkan bekerja sampai memerdekakan Indonesia."
    "Pidato itu dapat sambutan meriah dari sesama petinggi Dai Nippon."
    "Setelah makan siang kami diizinkan pulang."
    scene black
    with dissolve
    jump scene11

label scene11:
    scene rumah hatta
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Aku sampai rumah pukul 14:00, disana sudah ada Sjahrir menungguku."
    show hatta silent at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    show sjahrir silent at Position(xpos=280,ypos=95):
        zoom 0.65
    "Aku bersalaman dengannya kemudian duduk berhadapan dengannya."
    show sjahrir talk at Position(xpos=280,ypos=95):
        zoom 0.65
    show hatta silent at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    Sj "Jadi, bagaimana soal kemerdekaan kita?"
    show hatta talk at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    show sjahrir silent at Position(xpos=280,ypos=95):
        zoom 0.65
    H "Kemerdekaan sudah ada di tangan kita, untuk penyelenggaraannya serahkan saja ke PPKI."
    show sjahrir talk at Position(xpos=280,ypos=95):
        zoom 0.65
    show hatta silent at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    Sj "Bung, aku sudah dengar di radio bahwa Nippon sudah meminta damai pada Sekutu."
    Sj "Sebaiknya kemerdekaan tidak diselenggarakan oleh PPKI, karena itu adalah organisasi buatan Nippon."
    Sj "Jika PPKI yang memerdekakan Indonesia, Sekutu akan melihat bahwa Indonesia adalah negara bentukan Nippon."
    Sj "Setelah itu Sekutu akan mendaratkan pasukannya di Indonesia dengan tujuan mengembalikannya ke Belanda."
    Sj "Sebaiknya Soekarno-lah yang menyatakan kemerdekaan sebagai pemimpin rakyat dan atas nama rakyat dan diberitakan kemana-mana melalui radio."
    Sj "Jangan sampai usaha kita selama ini sia-sia Bung."
    show hatta talk at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    show sjahrir silent at Position(xpos=280,ypos=95):
        zoom 0.65
    H "Aku setuju denganmu kalau kemerdekaan harus dilakukan segera."
    H "Tetapi aku tidak yakin Soekarno akan setuju dengan rencanamu."
    H "Sebagai ketua PPKI, Soekarno tidak dapat meninggalkan organisasi yang dia ketuai meskipun membawa nama rakyat Indonesia sekalipun."
    H "Soekarno nanti hanya akan merampas hak PPKI, aku yakin Soekarno tidak akan bersedia melakukan itu."
    show sjahrir talk at Position(xpos=280,ypos=95):
        zoom 0.65
    show hatta silent at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    Sj "Maka disitulah peran Bung meyakinkan Bung Karno."
    show hatta talk at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    show sjahrir silent at Position(xpos=280,ypos=95):
        zoom 0.65
    play sound calling_1
    H "Baiklah, aku telepon Bung Karno dulu."
    play sound pickupcall
    H "Assalamualaikum Bung."
    show hatta silent at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    S "Waalaikumsalam Bung Hatta, ada apa?"
    show hatta talk at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    H "Bolehkah aku dan Sjahrir ke rumah Bung? Kami ada masalah genting yang membutuhkan Bung."
    show hatta silent at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    S "Baiklah, silahkan jika Bung dan Sjahrir ingin ke rumahku."
    show hatta talk at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    H "Baik terima kasih Bung, kami berangkat sekarang."
    H "Bung Karno mengizinkan kita ke rumahnya, mari kita kesana sekarang."
    show sjahrir talk at Position(xpos=280,ypos=95):
        zoom 0.65
    show hatta silent at Position(xpos=475,ypos=120) behind sjahrir:
        zoom 0.7
    Sj "Baik, aku mengikutimu Bung."
    scene black
    with dissolve
    jump scene12

label scene12:
    scene depan rumah soekarno 1
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show sjahrir silent at Position(xpos=170,ypos=95) behind hatta:
        zoom 0.65
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    "Setelah bersalaman dan duduk, Soekarno membuka pembicaraan"
    show soekarno talk at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    S "Soal apa yang saudara-saudara bawa kemari?"
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    "Sjahrir mengulangi apa yang dia katakan tadi saat berada di rumahku."
    show soekarno talk at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    S "Memang di Saigon kami menduga, setelah Letnan Kolonel Nomura melapor ke kita kalau Rusia sudah menyerbu Mancuko, Jepang pasti akan bertekuk lutut."
    S "Akan tetapi begitu lekasnya terjadi aku belum percaya sekalipun Saudara Sjahrir mendengarkan berita luar negeri yang kebanyakan dikuasai oleh Sekutu."
    S "Oleh karena itu, aku ingin mengecek terlebih dahulu dari Gunseikanbu."
    S "Besok kami berdua, Bung Hatta dan aku, akan pergi ke sana."
    S "Aku juga tidak setuju dengan pendapat saudara tentang memerdekakan Indonesia atas nama rakyat Indonesia dan melangkahi PPKI."
    S "Aku tidak berhak bertindak sendiri, hak itu adalah hak PPKI yang kuketuai."
    S "Alangkah janggalnya di mata orang, setelah kesempatan terbuka untuk mengucapkan kemerdekaan Indonesia, aku bertindak sendiri melangkahi PPKI yang kuketuai."
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    "Sjahrir terlihat pasrah pasca mendengarkan perkataan Soekarno karena cita-cita proklamasi yang menyimpang ini tidak dapat dilaksanakan."
    "Karena tidak ada yang dibicarakan lagi, aku dan Sjahrir pulang ke rumah."
    scene black
    with dissolve
    jump scene13

label scene13:
    play music musik2
    $ waktu += 1
    scene istana gunseireikan
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    show soebardjo silent at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    "Sesampainya kami di Istana Gunseikanbu, kami terkejut mendapati tidak ada pejabat sama sekali disini."
    "Kami bertanya pada penjaga kantor dan mereka bilang semua pejabat sedang dipanggil ke Gunseireibu."
    "Hal ini hanya memperkuat fakta yang disampaikan Sjahrir itu benar."
    "Kami bertiga berdiskusi untuk memutuskan tujuan kita selanjutnya."
    show soekarno talk at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    S "Bagaimana ini Bung, kita tidak dapat apa-apa dari Gunseikanbu ini."
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    H "Menurutku kita masih harus mencari kebenaran yang dari orang Nippon sendiri."
    show soebardjo talk at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    AS "Saya ada usul, bagaimana kalau kita ke rumah Laksamada Maeda?"
    show soekarno talk at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    show soebardjo silent at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    S "Aku setuju, mari kita kesana sekarang juga."
    scene black
    with dissolve
    jump scene14

label scene14:
    scene rumah maeda 1
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=40,ypos=120) behind hatta:
        zoom 0.75
    show soebardjo silent at Position(xpos=460,ypos=100) behind hatta:
        zoom 0.75
    show maeda silent at Position(xpos=640,ypos=60) behind soebardjo:
        zoom 0.8
    "Kedatangan kami disambut dengan lagi-lagi ucapan selamat atas apa yang kami dapatkan di Dalat."
    "Soekarno membuka percakapan dengan terus terang."
    show soekarno talk at Position(xpos=40,ypos=120) behind hatta:
        zoom 0.75
    S "Apakah benar berita yang beredar diluar sana bahwa Dai Nippon sudah meminta damai dengan Sekutu Tuan Maeda?"
    show soekarno silent at Position(xpos=40,ypos=120) behind hatta:
        zoom 0.75
    "Mendengar pertanyaan itu Maeda terdiam, cukup lama."
    "Aku memberi isyarat kepada Soekarno bahwa berita yang dibawa Sjahrir itu benar, Soekarno membalas dengan menganggukan kepalanya."
    "Dengan berat hati dan muka yang sedih, Maeda akhirnya angkat suara."
    show maeda talk at Position(xpos=640,ypos=60) behind soebardjo:
        zoom 0.8
    Ma "Memang benar berita itu disiarkan oleh sekutu."
    Ma "Akan tetapi kami disini belum mendapatkan kabar dari Tokyo. Sebab itu, berita tersebut belum bisa kami anggap benar."
    Ma "Hanya instruksi dari Tokyo yang menjadi pegangan kami."
    show maeda silent at Position(xpos=640,ypos=60) behind soebardjo:
        zoom 0.8
    "Setelah mendapatkan informasi itu, kami berterima kasih kepada Laksamada Maeda."
    scene black
    with dissolve
    jump scene15

label scene15:
    play music defaultmusikbgm fadein 3.0
    scene depan rumah maeda
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    show soebardjo silent at Position(xpos=140,ypos=100) behind hatta:
        zoom 0.75
    "Kami meninggalkan rumah Laksamada Maeda dengan keyakinan bahwa Dai Nippon benar-benar menyerah."
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Bung, menurutku kita besok mengadakan rapat PPKI, selagi seluruh anggota PPKI sedang berada di Jakarta."
    show soekarno talk at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    S "Aku setuju Bung, besok 16 Agustus PPKI akan rapat."
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    H "Baik Bung, Bung Subardjo tolong besok undang semua anggota PPKI yang terkumpul di Hotel des Indes untuk pukul 10:00 bertemu di Kantor Dewan Sanyo Kaigi di Pejambon."
    show soebardjo talk at Position(xpos=140,ypos=100) behind hatta:
        zoom 0.75
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    AS "Siap Bung."
    show soebardjo silent at Position(xpos=140,ypos=100) behind hatta:
        zoom 0.75
    "Setelah itu kami berpisah dan pulang ke rumah masing-masing."
    scene black
    with dissolve
    jump scene16

label scene16:
    play music its_coming
    scene rumah hatta
    show soebadio silent at Position(xpos=250,ypos=115):
        zoom 0.75
    show hatta silent at Position(xpos=475,ypos=120) behind soebadio:
        zoom 0.7
    "Di sore harinya ada pemuda yang menunjungiku, yaitu Soebadio Sastrosatomo dan rekannya."
    show soebadio talk at Position(xpos=250,ypos=115):
        zoom 0.75
    SS "Sore Bung, kami dapat kabar bahwa Nippon sudah menyerah pada Sekutu!"
    SS "Bung harus segera meyakinkan Bung Karno bahwa kemerdekaan Indonesia janganlah dinyatakan oleh PPKI, nantinya kita hanya akan dianggap antek Nippon oleh Sekutu."
    SS "Tetapi Bung Karnolah yang memerdekakan Indonesia sebagai pemimpin rakyat, atas nama rakyat, dan disebarkan ke seluruh dunia dengan radio!"
    show soebadio silent at Position(xpos=250,ypos=115):
        zoom 0.75
    show hatta talk at Position(xpos=475,ypos=120) behind soebadio:
        zoom 0.7
    H "Aku tidak setuju dengan rencana kalian."
    H "Dai Nippon dengan perantaranya Marsekal Terauchi di Dalat telah mengakui kemerdekaan Indonesia yang pelaksanaannya akan diselenggarakan oleh PPKI besok pagi pukul 10:00 di Pejambon."
    show hatta silent at Position(xpos=475,ypos=120) behind soebadio:
        zoom 0.7
    show soebadio talk at Position(xpos=250,ypos=115):
        zoom 0.75
    SS "Hal itu dihalangi dan tidak boleh terjadi!"
    SS "Bung Karno sendiri yang harus mengucapkannya di radio atas nama rakyat Indonesia!"
    show soebadio silent at Position(xpos=250,ypos=115):
        zoom 0.75
    show hatta talk at Position(xpos=475,ypos=120) behind soebadio:
        zoom 0.7
    H "Bung Karno tidak akan mau melakukan apa yang kalian tuntut, Bung Karno tidak mau dan tidak bisa merampas hak PPKI."
    H "Dan juga maupun Bung Karno menyatakan kemerdekaan sebagai wakil rakyat maupun PPKI hasilnya akan tetap saja sama, Bung Karno telah dicap pengkhianat oleh Belanda semenjak kita bekerja sama dengan Dai Nippon."
    show soebadio silent at Position(xpos=250,ypos=115):
        zoom 0.75
    show hatta silent at Position(xpos=475,ypos=120) behind soebadio:
        zoom 0.7
    "Kami bertengkar lebih dari setengah jam, kami sama-sama gagal meyakinkan satu sama lain."
    "Pemuda menyebut pendirian mereka revolusioner, sedangkan aku dengan pendirianku yang rasional dan tidak buang-buang tenaga."
    "Akhirnya mereka menyerah dan berusaha meninggalkanku selagi berkata."
    show soebadio talk at Position(xpos=250,ypos=115):
        zoom 0.75
    SS "Di saat revolusi kami rupanya tidak dapat membawa Bung serta, Bung tidak revolusioner."
    show soebadio silent at Position(xpos=250,ypos=115):
        zoom 0.75
    show hatta talk at Position(xpos=475,ypos=120) behind soebadio:
        zoom 0.7
    H "Aku juga sebenarnya ingin mengadakan revolusi, tapi agar suatu revolusi berhasil, kita perlu organisasi yang matang terlebih dahulu."
    H "Tindakan yang akan engkau lakukan itu bukanlah sebuah revolusi, tetapi putsch, seperti yang Hitler lakukan di Munchen 1923 tetapi gagal."
    $renpy.notify("Peristiwa Beer Hall Putsch telah ditambahkan ke direktori.")
    $ unlock += 1
    show hatta silent at Position(xpos=475,ypos=120) behind soebadio:
        zoom 0.7
    show soebadio talk at Position(xpos=250,ypos=115):
        zoom 0.75
    SS "Bung Hatta tidak bisa diharapkan untuk revolusi!"
    show soebadio silent at Position(xpos=250,ypos=115):
        zoom 0.75
    "Mereka keluar setelah kubuat emosi mereka semakin naik."
    scene black
    with dissolve
    jump scene17

label scene17:
    scene rumah hatta
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Pada malam hari kira-kira pukul 09:30, aku yang sedang mengetik naskah awal proklamasi untuk anggota PPKI tiba-tiba kedatangan Achmad Soebardjo."
    scene black
    with dissolve
    jump scene17a

label scene17a:
    scene rumah hatta
    show soebardjo talk at Position(xpos=240,ypos=100):
        zoom 0.75
    show hatta silent at Position(xpos=475,ypos=120) behind soebardjo:
        zoom 0.7
    AS "Bung, mari kita ke rumah Bung Karno sekarang juga!"
    show hatta talk at Position(xpos=475,ypos=120) behind soebardjo:
        zoom 0.7
    show soebardjo silent at Position(xpos=240,ypos=100):
        zoom 0.75
    H "Apa yang terjadi disana Bung?"
    show soebardjo talk at Position(xpos=240,ypos=100):
        zoom 0.75
    show hatta silent at Position(xpos=475,ypos=120) behind soebardjo:
        zoom 0.7
    AS "Bung Karno sedang didesak oleh para pemuda yang menuntut proklamasi dilakukan malam ini juga depan radio."
    show hatta talk at Position(xpos=475,ypos=120) behind soebardjo:
        zoom 0.7
    show soebardjo silent at Position(xpos=240,ypos=100):
        zoom 0.75
    H "Baik Bung mari kita kesana."
    scene black
    with dissolve
    jump scene18

label scene18:
    scene depan rumah soekarno 1
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=40,ypos=120) behind hatta:
        zoom 0.75
    show soebardjo silent at Position(xpos=460,ypos=100) behind hatta:
        zoom 0.75
    show wikana silent at Position(xpos=780,ypos=150) behind soebardjo:
        zoom 0.57
    "Sesampainya disana benarlah ada Soekarno yang sedang didesak oleh para pemuda."
    "Sejauh ini Soekarno menolak keras semua desakan para pemuda dengan alasan Dai Nippon sudah memutuskan untuk memerdekakan Indonesia pada 16 Agustus dan PPKI akan bersidang melaksanakan kemerdekaan itu."
    "Setelah itu PPKI akan mengesahkan undang-undang yang disiapkan sebelumnya oleh BPUPKI, memilih kepala daerah, dan akhirnya kembali ke daerah masing-masing untuk mendirikan pemerintahan lokal serta strukturnya disana."
    "Pemuda menilai semua itu tidaklah perlu, mereka menganggap nantinya Indonesia hanyalah antek Dai Nippon, mereka kembali menuntut Soekarno memproklamasikan kemerdekaan atas nama rakyat sebelum pukul 24:00."
    "Soekarno dengan logikanya tetap menolak tuntutan pemuda dengan alasan aksi seperti itu nantinya tidak dapat dipertanggungjawabkan dengan jelas."
    "Dalam ketegangan itu, salah satu pemuda, Wikana menggertak Soekarno."
    show wikana talk at Position(xpos=780,ypos=150) behind soebardjo:
        zoom 0.57
    W "Apabila Bung Karno tidak mau mengucapkan pengumuman kemerdekaan itu malam ini juga, besok pagi akan terjadi pertumpahan darah."
    show wikana silent at Position(xpos=780,ypos=150) behind soebardjo:
        zoom 0.57
    "Soekarno emosi dan berdiri menantang balik Wikana setelah mendengar itu."
    show soekarno talk at Position(xpos=40,ypos=120) behind hatta:
        zoom 0.75
    S "Ini leherku, seretlah aku ke pojok sana, dan habisilah aku disana, tidak usah menunggu besok."
    show soekarno silent at Position(xpos=40,ypos=120) behind hatta:
        zoom 0.75
    "Wikana langsung tunduk setelah Soekarno bilang begitu."
    show wikana talk at Position(xpos=780,ypos=150) behind soebardjo:
        zoom 0.57
    W "Maksud kami bukan membunuh Bung, tetapi kami akan memperingatkan jika proklamasi tidak dilakukan hari ini, besok akan ada kekerasan yang dituju pada orang-orang yang diduga pro-Belanda."
    show wikana silent at Position(xpos=780,ypos=150) behind soebardjo:
        zoom 0.57
    "Karena kondisi yang tegang dan tidak berujung ini, kami setuju untuk mengadakan istirahat terlebih dahulu."
    scene black
    with dissolve
    jump scene18a

label scene18a:
    play music defaultmusikbgm
    scene rumah soekarno
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    show soebardjo silent at Position(xpos=560,ypos=100) behind hatta:
        zoom 0.75
    "Dalam istirahat itu kami berdiskusi tanpa para pemuda."
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Bagaimana menurutmu Bung tentang para pemuda diluar sana?"
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno talk at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    S "Entahlah Bung, mereka mempunyai semangat, aku akui itu."
    show soekarno silent at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Tapi semangat tanpa strategi dan perencanaan hanya akan berakhir tragis."
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno talk at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    S "Benar Bung, tapi mereka sama sekali tidak mau mendengarkan kita."
    show soekarno silent at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    show soebardjo talk at Position(xpos=560,ypos=100) behind hatta:
        zoom 0.75
    AS "Bagaimana kalau kita buat kesepakatan begini, jika mereka ingin proklamasi dilaksanakan malam ini juga, silahkan para pemuda itu cari tokoh yang bersedia."
    show soebardjo silent at Position(xpos=560,ypos=100) behind hatta:
        zoom 0.75
    show soekarno talk at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    S "Idemu bagus Bung, bagaimana? Ada ide lain?"
    show soekarno silent at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Menurutku itu sudah bagus, silahkan mereka cari pemimpin revolusi dengan cara mereka sendiri."
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Kami kembali menghadap para pemuda."
    show soekarno talk at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    S "Ini keputusan final kami, jika kalian tetap memaksa kemerdekaan dilaksanakan malam ini juga, silahkan cari pemimpin revolusi baru kalian."
    show soekarno silent at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    "Para pemuda tampak tidak setuju, tetapi mereka juga tidak ada usulan."
    "Karena pertemuan ini hanya buang-buang waktu saja, pertemuan akhirnya dibubarkan."
    "Aku sendiri jadi gagal menyelesaikan naskah proklamasi yang sedang ku ketik tadi, biarlah, aku selesaikan besok pagi sebelum rapat PPKI."
    scene black
    with dissolve
    jump scene19

label scene19:
    play music its_coming
    $ waktu += 1
    scene rumah hatta
    show soekarni silent at Position(xpos=230,ypos=100):
        zoom 0.75
    show hatta silent at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    "Aku bangun dengan niatan sahur, ternyata sudah ada Soekarni dan teman-temannya menungguku."
    show hatta talk at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    H "Ada keperluan apa kalian kesini sekarang?"
    show hatta silent at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    show soekarni talk at Position(xpos=230,ypos=100):
        zoom 0.75
    Si "Karena Bung Karno menolak memproklamasikan kemerdekaan semalam, kami para pemuda memutuskan untuk bergerak sendiri."
    Si "Nanti menjelang pukul 12:00, 15.000 rakyat akan menyerbu kota diiringi dengan mahasiswa dan juga Peta melucuti Nippon."
    Si "Bung Karno dan Bung Hatta kami bawa ke Rengasdengklok untuk meneruskan pimpinan Pemerintah Republik Indonesia dari sana."
    show soekarni silent at Position(xpos=230,ypos=100):
        zoom 0.75
    show hatta talk at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    H "Dengan menyerang kekuatan Dai Nippon di Jakarta, Saudara-saudara bukan melaksanakan revolusi, tetapi melakukan putsch yang akan membunuh revolusi."
    show hatta silent at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    show soekarni talk at Position(xpos=230,ypos=100):
        zoom 0.75
    Si "Ini sudah keputusan kami semua dan tidak dapat dipersoalkan lagi, Bung ikut saja bersama Bung Karno bersama kami ke Rengasdengklok."
    show soekarni silent at Position(xpos=230,ypos=100):
        zoom 0.75
    "Firasatku sangatlah buruk, aku membayangkan kehancurannya cita-cita kemerdekaan yang kami perjuangkan sejauh ini."
    "Bagaimana dengan PPKI yang akan rapat pukul 10:00 nanti? Jelas mereka tidak akan rapat tanpa pimpinan."
    "Aku akhirnya dibawa oleh Soekarni dalam mobil dan kami akhirnya berangkat."
    hide screen tanggal
    scene black
    with dissolve
    jump scene20

label scene20:
    play music mobil
    scene black
    "Kami singgah dulu ke rumah Soekarno dan tak lama kemudian Soekarno, Fatmawati, dan Guntur ikut bersama kami ke Rengasdengklok."
    "Kami sempat dihentikan di Karawang untuk berpindah mobil, ternyata ini adalah siasat dari Soekarni dan temannya agar supir ini tidak tahu kami dibawa kemana."
    scene black
    with dissolve
    jump scene21

label scene21:
    play music defaultmusikbgm
    scene rumah rengasdengklok
    show screen tanggal
    show soekarni silent at Position(xpos=230,ypos=100):
        zoom 0.75
    show hatta silent at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    "Tidak ada yang kami lakukan selama di Rengasdengklok ini, sekarang sudah pukul 12:30 seharusnya revolusi pemuda sudah terjadi."
    "Aku berinisiasi meminta penjaga untuk mendatangkan Soekarni."
    show soekarni talk at Position(xpos=230,ypos=100):
        zoom 0.75
    Si "Ada apa Bung?"
    show soekarni silent at Position(xpos=230,ypos=100):
        zoom 0.75
    show hatta talk at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    H "Apakah revolusi yang saudara-saudara rencanakan pada pukul 12:00 sudah dimulai?"
    H "Apakah 15.000 rakyat sudah menyerbu posisi Dai Nippon dengan mahasiswa dan Peta sudah masuk ke kota?"
    show hatta silent at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    show soekarni talk at Position(xpos=230,ypos=100):
        zoom 0.75
    Si "Saya tidak tahu Bung, saya belum dapat kabar."
    show soekarni silent at Position(xpos=230,ypos=100):
        zoom 0.75
    show hatta talk at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    H "Kalau begitu segera cari tahu."
    show hatta silent at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    show soekarni talk at Position(xpos=230,ypos=100):
        zoom 0.75
    Si "Baiklah."
    show soekarni silent at Position(xpos=230,ypos=100):
        zoom 0.75
    "Soekarni pergi dan hampir sejam ia kembali lagi."
    scene black
    with dissolve
    scene rumah rengasdengklok
    show hatta silent at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    show soekarni talk at Position(xpos=230,ypos=100):
        zoom 0.75
    Si "Saya sejauh ini tidak memperoleh kontak dari Jakarta dan Jakarta tidak memberi berita."
    show soekarni silent at Position(xpos=230,ypos=100):
        zoom 0.75
    show hatta talk at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    H "Kalau begitu revolusimu sudah gagal, buat apa kami beristirahat disini apabila di Jakarta tidak terjadi apa-apa?"
    show hatta silent at Position(xpos=485,ypos=120) behind soekarni:
        zoom 0.7
    show soekarni talk at Position(xpos=230,ypos=100):
        zoom 0.75
    Si "Saya belum yakin revolusi itu gagal Bung."
    show soekarni silent at Position(xpos=230,ypos=100):
        zoom 0.75
    "Soekarni berkata begitu, meskipun dalam dirinya aku yakin ada bayak keraguan."
    "Tak lama kemudian ia pergi."
    scene black
    with dissolve
    jump scene21a

label scene21a:
    scene rumah rengasdengklok
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarni silent at Position(xpos=550,ypos=100) behind hatta:
        zoom 0.75
    show soebardjo silent at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    "Pada pukul 18:00, Soekarni datang dengan Achmad Soebardjo."
    show soebardjo talk at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    AS "Bung, saya kesini untuk membawa kalian semua pulang ke Jakarta."
    show soebardjo silent at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Bagaimana keadaan di Jakarta Bung?"
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soebardjo talk at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    AS "Di Jakarta biasa saja, tidak terjadi apa-apa."
    AS "Buat apa pemimpin-pemimpin kita berada disini, sedangkan banyak hal yang harus dibereskan selekas-lekasnya di Jakarta."
    show soebardjo silent at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Apakah PPKI tadi jadi rapat tadi pagi Bung?"
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soebardjo talk at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    AS "Apa yang akan dikerjakan mereka? Saudara-saudara yang mengundang mereka rapat tidak ada, berada disini."
    show soebardjo silent at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Kalau untuk aku, aku lebih senang beristirahat disini sampai besok pagi, besok pagi saja kita pulang."
    H "Semuanya sudah terlambat, kerja yang seharusnya selesai tadi pagi tidak jadi dikerjakan."
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Walaupun aku bilang begitu hanya untuk menertawai kondisi sekarang, ucapanku banyak diprotes sehingga malam itu juga kita pulang kembali ke Jakarta."
    scene black
    with dissolve
    jump scene22

label scene22:
    scene rumah hatta
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=50,ypos=120) behind hatta:
        zoom 0.75
    show soebardjo silent at Position(xpos=460,ypos=100) behind hatta:
        zoom 0.75
    show soekarni silent at Position(xpos=670,ypos=100) behind soebardjo:
        zoom 0.75
    "Kami sampai di rumahku bersama Achmad Soebardjo, Soekarno, dan Soekarni."
    "Soebardjo mengurus perjanjian rapat dengan anggota PPKI, akhirnya rapat PPKI akan dilaksanakan di rumah Laksamada Maeda pada pukul 24:00."
    "Soebardjo akan menelepon anggota PPKI di rumahnya, sehingga kami semua setuju untuk pulang ke rumah masing-masing."
    show soekarni talk at Position(xpos=670,ypos=100) behind soebardjo:
        zoom 0.75
    Si "Bagaimana denganku Bung?"
    show soekarni silent at Position(xpos=670,ypos=100) behind soebardjo:
        zoom 0.75
    "Soekarni bertanya dengan penuh bingung."
    show hatta talk at Position(xpos=260,ypos=120):
        zoom 0.7
    H "Ya pulang juga."
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    show soekarni talk at Position(xpos=670,ypos=100) behind soebardjo:
        zoom 0.75
    Si "Kalau begitu aku minta Bung pinjami satu setel pakaian karena dengan baju Peta yang aku kenakan sekarang aku dapat ditangkap oleh Kempeitai."
    $renpy.notify("Organisasi Kempeitai telah ditambahkan ke direktori.")
    $ unlock += 1
    show soekarni silent at Position(xpos=670,ypos=100) behind soebardjo:
        zoom 0.75
    "Kami semua tertawa mendengar permintaan Soekarni itu."
    show hatta talk at Position(xpos=260,ypos=120):
        zoom 0.7
    H "Saudara berani mengadakan revolusi menggempur Dai Nippon. Tetapi sekarang saudara takut akan ditangkap Kempeitai karena memakai pakaian Peta."
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    show soekarni talk at Position(xpos=670,ypos=100) behind soebardjo:
        zoom 0.75
    Si "Itu lain halnya Bung, menggempur Nippon dalam suatu revolusi aku berani. Tetapi akan ditangkap Nippon begitu saja karena pakaian Peta apa gunanya."
    show soekarni silent at Position(xpos=670,ypos=100) behind soebardjo:
        zoom 0.75
    "Sambil tertawa, aku meminjamkannya salah satu setelan pakaianku."
    scene black
    with dissolve
    jump scene22a

label scene22a:
    play music musik2
    scene rumah hatta
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=50,ypos=120) behind hatta:
        zoom 0.75
    show soebardjo silent at Position(xpos=460,ypos=100) behind hatta:
        zoom 0.75
    show soekarni silent at Position(xpos=670,ypos=100) behind soebardjo:
        zoom 0.75
    play sound calling_2
    "Saat mereka ingin pulang, telepon rumahku berdering."
    play sound pickupcall
    "Aku segera mengangkat telepon tersebut."
    Mi "Selamat malam Tuan Hatta, ini Miyoshi."
    show hatta talk at Position(xpos=260,ypos=120):
        zoom 0.7
    H "Selamat malam Tuan Miyoshi, ada apa malam-malam ini telepon?"
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    Mi "Ternyata Tuan sudah kembali dari Rengasdengklok, selamat datang kembali."
    Mi "Begini Tuan Hatta, Mayor Jenderal Nishimura ingin bertemu Tuan dan Tuan Soekarno malam ini juga."
    show hatta talk at Position(xpos=260,ypos=120):
        zoom 0.7
    H "Mayor Jenderal Nishimura dari Sumobuco ingin bertemuku saat ini?"
    H "Baik Tuan Miyoshi, bagaimana kalau kita bertemu di rumah Laksamada Maeda pukul 22:00 nanti?"
    H "Setelah itu kita bersama-sama ke rumah Nishimura bersama-sama."
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    Mi "Baik tuan, saya akan menemui tuan nanti di rumah Laksamada Maeda."
    "Aku memberi tahu hal ini kepada Soekarno sebelum dia pulang, dan dia akan ke rumahku sebelum pukul 22:00 kemudian kami berangkat bersama."
    scene black
    with dissolve
    jump scene23

label scene23:
    scene rumah maeda 1
    show hatta silent at Position(xpos=260,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=50,ypos=120) behind hatta:
        zoom 0.75
    show miyoshi silent at Position(xpos=440,ypos=100) behind hatta:
        zoom 0.8
    show maeda silent at Position(xpos=640,ypos=60) behind miyoshi:
        zoom 0.8
    "Soekarno datang ke rumahku sebelum pukul 22:00 dan kami langsung berangkat ke rumah Maeda."
    "Sesampainya kami di rumah Maeda, Maeda sudah menunggu kami bersama Miyoshi dan beberapa petinggi Dai Nippon."
    show maeda talk at Position(xpos=640,ypos=60) behind miyoshi:
        zoom 0.8
    Ma "Selamat datang tuan-tuan."
    show maeda silent at Position(xpos=640,ypos=60) behind miyoshi:
        zoom 0.8
    show soekarno talk at Position(xpos=50,ypos=120) behind hatta:
        zoom 0.75
    S "Selamat malam Tuan Maeda dan tuan-tuan semua."
    S "Terima kasih Tuan Maeda telah mengizinkan kami mengadakan rapat PPKI di rumah tuan."
    show soekarno silent at Position(xpos=50,ypos=120) behind hatta:
        zoom 0.75
    show maeda talk at Position(xpos=640,ypos=60) behind miyoshi:
        zoom 0.8
    Ma "Itu kewajiban saya yang mencintai Indonesia merdeka."
    show maeda silent at Position(xpos=640,ypos=60) behind miyoshi:
        zoom 0.8
    "Setelah setengah jam, kami ke rumah Nishimura dengan Miyoshi sebagai juru bahasa dan Maeda."
    scene black
    with dissolve
    jump scene24

label scene24:
    play music its_coming
    scene rumah nishimura
    show hatta silent at Position(xpos=190,ypos=120) behind nishimura:
        zoom 0.7
    show soekarno silent at Position(xpos=-10,ypos=120) behind hatta:
        zoom 0.75
    show miyoshi silent at Position(xpos=530,ypos=100) behind nishimura:
        zoom 0.8
    show maeda silent at Position(xpos=680,ypos=60) behind miyoshi:
        zoom 0.8
    show nishimura silent at Position(xpos=320,ypos=105):
        zoom 0.85
    "Sesampainya di rumah Nishimura, kami bersalaman dengan beliau dan berbicara sebentar tentang perjalanan kami dari Rengasdengklok."
    "Setelah itu kami membahas tentang kelanjutan rapat PPKI yang harusnya dilaksanakan tadi pagi."
    show nishimura talk at Position(xpos=320,ypos=105):
        zoom 0.85
    Ni "Maaf tuan-tuan, sayang rapat itu sudah tidak boleh dilaksanakan."
    show nishimura silent at Position(xpos=320,ypos=105):
        zoom 0.85
    show hatta talk at Position(xpos=190,ypos=120) behind nishimura:
        zoom 0.7
    H "Mengapa begitu? Dai Nippon telah menyetujui kemerdekaan kita."
    show hatta silent at Position(xpos=190,ypos=120) behind nishimura:
        zoom 0.7
    show nishimura talk at Position(xpos=320,ypos=105):
        zoom 0.85
    Ni "Kalau tadi pagi masih dapat dilangsungkan, pukul 13:00 tadi tentara Dai Nippon yang berada di Jawa mendapat perintah dari Tokyo tidak boleh lagi mengubah status quo."
    show nishimura silent at Position(xpos=320,ypos=105):
        zoom 0.85
    show soekarno talk at Position(xpos=-10,ypos=120) behind hatta:
        zoom 0.75
    S "Tuan tidak bisa bertindak seperti itu, Dai Nippon dan Tokyo sudah mengakui kemerdekaan Indonesia dengan Marsekal Terauchi sebagai perantaranya."
    S "Dan pelaksanaannya diserahkan pada PPKI."
    show soekarno silent at Position(xpos=-10,ypos=120) behind hatta:
        zoom 0.75
    show nishimura talk at Position(xpos=320,ypos=105):
        zoom 0.85
    Ni "Apabila rapatnya dilaksanakan tadi pagi, akan kami bantu. Akan tetapi pada tengah hari tadi kami harus tunduk pada Sekutu dan mempertahankan status quo."
    Ni "Perubahan pada status quo itu tidak diperbolehkan, jadi sekarang rapat PPKI terpaksa kami larang."
    hide maeda
    show hatta talk at Position(xpos=280,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=80,ypos=120) behind hatta:
        zoom 0.75
    show nishimura silent at Position(xpos=410,ypos=105) behind hatta:
        zoom 0.85
    show miyoshi silent at Position(xpos=620,ypos=100) behind nishimura:
        zoom 0.8
    H "Sekarang seluruh rakyat Indonesia tahu bahwa Dai Nippon sudah menyerah pada Sekutu dan mereka juga tidak lupa akan janji Dai Nippon tentang kemerdekaan Indonesia."
    H "Kalau Dai Nippon tidak mampu menepati janjinya, rakyat Indonesia akan memerdekakan dirinya sendiri."
    show hatta silent at Position(xpos=280,ypos=120):
        zoom 0.7
    show soekarno talk at Position(xpos=80,ypos=120) behind hatta:
        zoom 0.75
    S "Semangat rakyat yang bergelora sekarang akan diperhatikan oleh Sekutu, kecuali Belanda. Sebab itu Dai Nippon sudah tidak perlu menolong kami lagi."
    S "Kami minta setidaknya jangan halangi kami, rakyat Indonesia dan pemudanya siap mati untuk melaksanakan cita-cita Indonesia Merdeka."
    show soekarno silent at Position(xpos=80,ypos=120) behind hatta:
        zoom 0.75
    show nishimura talk at Position(xpos=410,ypos=105) behind hatta:
        zoom 0.85
    Ni "Saya benar-benar paham perasaan tuan-tuan dan cita-cita rakyat Indonesia."
    Ni "Aku menangis dalam hatiku, akan tetapi apa boleh buat."
    Ni "Kami sebagai alat telah menerima perintah untuk menghalangi segala upaya perubahan status quo, termasuk gerakan rakyat Indonesia dan pemuda."
    show nishimura silent at Position(xpos=410,ypos=105) behind hatta:
        zoom 0.85
    show soekarno talk at Position(xpos=80,ypos=120) behind hatta:
        zoom 0.75
    S "Apakah itu termasuk tuan dan tentara Dai Nippon akan menembak pemuda Indonesia sebagai Bunga bangsa jika mereka bergerak melaksanankan janji Dai Nippon?"
    S "Janji tentang kemerdekaan yang Dai Nippon sendiri tidak sanggup menepatinya."
    show soekarno silent at Position(xpos=80,ypos=120) behind hatta:
        zoom 0.75
    show nishimura talk at Position(xpos=410,ypos=105) behind hatta:
        zoom 0.85
    Ni "Apa boleh buat, dengan hati yang luka kami terpaksa melakukannya."
    Ni "Saya yakin, jika tuan-tuan bersabar sedikit lagi, Sekutu akan memperhatikan keinginan bangsa Indonesia."
    Ni "Betapa sakitnya terasa dalam jiwa, kami Dai Nippon terpaksa tunduk dan menjilat Sekutu agar mendapatkan nasib yang tidak terlalu buruk setelah kami kalah."
    show nishimura silent at Position(xpos=410,ypos=105) behind hatta:
        zoom 0.85
    "Mendengar itu, aku tidak dapat lagi menahan amarahku."
    show hatta talk at Position(xpos=280,ypos=120):
        zoom 0.7
    H "Apakah itu janji dan perbuatan seorang Samurai!?"
    H "Dapatkah seorang Samurai menjilat musuhnya yang menang untuk memperoleh nasib yang kurang jelek!?"
    H "Apakah Samurai hanya hebat terhadap orang yang lemah di masa jayanya tetapi hilang semangatnya saat kalah?"
    H "Baiklah, kami akan jalan terus apapun yang terjadi."
    H "Mungkin kami akan menunjukkan kepada Tuan bagaimana jiwa Samurai semestinya menghadapi suasana yang berubah."
    show hatta silent at Position(xpos=280,ypos=120):
        zoom 0.7
    "Mendengar perkataanku itu, Miyoshi sebagai penerjemah gugup ingin meneruskan pesannya pada Nishimura."
    "Aku yakin Miyoshi berusaha memperhalus perkataanku tadi."
    "Aku dan Soekarno meninggalkan rumah Nishimura setelah sepakat kembali ke rumah Maeda setelah berdebat disana tidak membuahkan hasil."
    "Maeda sendiri sudah meninggalkan rapat dari tadi tanpa sepengetahuan kami semua."
    scene black
    with dissolve
    jump scene25

label scene25:
    play music suara_gemuruh
    $ waktu += 1
    scene rumah maeda 2
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soebardjo silent at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    "Sesampainya di rumah Laksamada Maeda, sudah banyak orang menunggu, kira-kira antara 40-50, semuanya tokoh-tokoh pergerakan dan juga anggota PPKI."
    "Belum lagi diluar banyak pemuda yang ikut menyaksikan."
    "Karena terlalu ramai, kami melanjutkan diskusi di ruang tamu kecil bersama Soekarno dan Achmad Soebardjo."
    scene black
    with dissolve
    jump scene25a

label scene25a:
    play music defaultmusikbgm
    scene rumah maeda 3
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soebardjo silent at Position(xpos=130,ypos=100) behind hatta:
        zoom 0.75
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    "Di ruangan ini kami mendiskusikan naskah teks Proklamasi."
    show soekarno talk at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    S "Aku persilahkan Bung Hatta menyusun teks ringkas itu sebab bahasanya kuanggap yang terbaik, sesudah itu kita persoalkan bersama-sama."
    S "Setelah kita memperoleh persetujuan, nantinya kita bawa ke sidang lengkap yang sudah hadir di ruang tengah."
    show soekarno silent at Position(xpos=570,ypos=120) behind hatta:
        zoom 0.75
    show hatta talk at Position(xpos=370,ypos=120):
        zoom 0.7
    H "Apabila aku mesti memikirkannya, lebih baik Bung menuliskan, aku mendiktekannya."
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Semuanya setuju dan penulisanpun dimulai."
    scene black
    with dissolve
    hide screen tanggal
    hide screen buku
    $ quick_menu = False
    scene proklamasi 1
    "Pembuatan Naskah Teks Proklamasi Dimulai."
    "Mari bantu untuk menyusun teks proklamasi!"
    scene black
    with dissolve
    call screen tampilsoal1

label scene26:
    play music suara_gemuruh
    scene rumah maeda 2
    show hatta silent at Position(xpos=475,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    "Kami kembali ke ruang tengah untuk mendiskusikan Teks Proklamasi, rapat ini bukan lagi rapat PPKI dengan banyaknya tokoh-tokoh lain yang ikut terlibat dalam rapat ini."
    "Soekarno membuka rapat dengan membacakan Teks Proklamasi."
    show soekarno talk at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    S "Dapatkah saudara-saudara setuju dengan ini?"
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    "Suara gemuruh dan tak teratur menjawab “Setuju”."
    show soekarno talk at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    S "Benar-benar saudara semuanya setuju?"
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    "Baru kali ini serentak mengucapkan “Setuju”."
    hide screen tanggal
    hide screen buku
    $ quick_menu = False
    play music defaultmusikbgm
    scene black    
    with dissolve
    call screen tampilsoal4

label scene27:
    stop music
    scene rumah maeda 2
    show hatta silent at Position(xpos=475,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    "Sebelum rapat ditutup, Soekarno mengingatkan bahwa proklamasi akan dibacakan di rumah Soekarno jalan Pegangsaan Timur no. 56 pukul 10:00."
    "Dengan itu rapat berakhir kira-kira pukul 03:00 pagi."
    scene black
    with dissolve
    jump scene27a

label scene27a:
    scene rumah maeda 2
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=160,ypos=120) behind hatta:
        zoom 0.75
    show maeda silent at Position(xpos=520,ypos=60) behind hatta:
        zoom 0.8
    "Maeda sempat keluar dari kamar tidurnya untuk memberikan kami selamat atas apa yang kami capai saat ini."
    "Sebelum pulang aku berkata pada pemuda-pemuda golongan pers yang ada disana untuk siap memperbanyak teks proklamasi untuk disebar keseluruh Indonesia dan kalau bisa seluruh dunia."
    "Sebelum pulang juga aku sempatkan untuk sahur dan tidak lupa berterima kasih pada Laksamada Maeda atas jasanya selama ini."
    scene black
    with dissolve
    jump scene28

label scene28:
    scene rumah hatta
    show hatta silent at Position(xpos=370,ypos=120):
        zoom 0.7
    "Setelah sampai di rumah, aku sholat subuh terlebih dahulu baru tidur."
    "Aku bangun pukul 08:30 dan segera siap-siap ke rumah Soekarno."
    "Pada pukul 09:50 aku berangkat menuju rumah Soekarno."
    scene black
    with dissolve
    jump scene29

label scene29:
    scene rumah soekarno
    show hatta silent at Position(xpos=475,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    "Aku sampai di rumah Soekarno pukul 09:55, disana sudah banyak rakyat menunggu."
    "Aku menyempatkan diri menghampiri Soekarno."
    show hatta talk at Position(xpos=475,ypos=120):
        zoom 0.7
    H "Bagaimana Bung, sudah siap?"
    show hatta silent at Position(xpos=475,ypos=120):
        zoom 0.7
    show soekarno talk at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    S "Siap."
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    "Kami bersama ke depan rumah Soekarno."
    scene black
    with dissolve
    jump scene29a

label scene29a:
    scene depan rumah soekarno 2
    show hatta silent at Position(xpos=475,ypos=120):
        zoom 0.7
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    "Aku dan Soekarno menghadapi ribuan rakyat Indonesia."
    "Soekarno membuka dengan pidato pembukaan."
    show soekarno talk at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    play sound proklamasi
    "Proklamasi dibacakan."
    show soekarno silent at Position(xpos=280,ypos=120) behind hatta:
        zoom 0.75
    play sound indonesia_raya
    "Setelah dibacakan, kami semua melakukan upacara penaikan bendera Merah Putih yang dijahit oleh Fatmawati dengan bahan seadanya dan diiringi lagu Indonesia Raya."
    stop sound
    play music crowd_cheer
    "Setelah itu rakyat bergemuruh kesenangan dan aku juga sadar, Indonesia sudah merdeka."
    hide screen tanggal
    hide screen buku
    $ quick_menu = False
    play music ins_tanah_airku
    scene black
    with dissolve
    call screen epilog1

screen epilog1:
    frame:
        xfill True
        add "background1"
        add "background2"
        button:
            background Frame("images/Kuis/empty.png")
            action [Hide("epilog1"), Show("epilog2")]

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Dengan ini Indonesia sudah merdeka, dan aku tahu ini bukanlah akhir dari perjuangan kami." size 22

screen epilog2:
    frame:
        add "background1"
        add "background2"
        button:
            background Frame("images/Kuis/empty.png")
            action [Hide("epilog2"), Show("epilog3")]

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Masih banyak pekerjaan yang harus kami lakukan, kemerdekaan hanyalah sebuah awalan baru bagi kami." size 22

screen epilog3:
    frame:
        xsize 1280 ysize 720 
        xfill True
        add "background1"
        add "background2"
        button:
            background Frame("images/Kuis/empty.png")
            action [Hide("epilog3"), Show("epilog4")]

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Aku juga tidak akan selamanya mengurus negeri ini, ada saatnya pekerjaan itu dilanjutkan oleh penerus-penerusku." size 22

screen epilog4:
    frame:
        xsize 1280 ysize 720 
        xfill True
        add "background1"
        add "background2"
        button:
            background Frame("images/Kuis/empty.png")
            action [Hide("epilog4"), Show("epilog5")]

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Aku berharap generasi-generasi penerusku tidak akan lupa apa yang aku perjuangkan selama ini dan menjaga hasil perjuanganku ini." size 22

screen epilog5:
    frame:
        xsize 1280 ysize 720 
        xfill True
        add "background1"
        add "background2"
        button:
            background Frame("images/Kuis/empty.png")
            action [Hide("epilog5"), Show("epilog6")]

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Aku mungkin tidak akan hidup saat negeri ini makmur, tapi setidaknya aku tahu suatu saat itu akan terjadi di tangan generasi-generasi penerusku." size 22

screen epilog6:
    frame:
        xsize 1280 ysize 720 
        xfill True
        add "background1"
        add "background2"
        button:
            background Frame("images/Kuis/empty.png")
            action [Hide("epilog6"), Jump("end")]

        hbox:
            xpos 350
            ypos 590
            xsize 850
            text "Indonesia merdeka tidak ada gunanya bagi kita, apabila kita tidak sanggup untuk mempergunakannya memenuhi cita-cita rakyat kita: hidup bahagia dan makmur dalam pengertian jasmani maupun rohani." size 22

label end:
    return
