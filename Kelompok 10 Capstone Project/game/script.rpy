# The script of the game goes in this file.
# Test
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define H = Character("Hatta", color="#CD6247", who_bold=True, who_outlines=[(1, "#000")])
define M = Character("Murid", color="#EE8A79", who_bold=True, who_outlines=[(1, "#000")])
define N = Character("Nomura", color="#B6AAA6", who_bold=True, who_outlines=[(1, "#000")])
define Sj = Character("Sjahrir", color="#F8DC71", who_bold=True, who_outlines=[(1, "#000")])
define D = Character("Driver", color="#99DAEC", who_bold=True, who_outlines=[(1, "#000")])
define S = Character("Soekarno", color="#F18E76", who_bold=True, who_outlines=[(1, "#000")])
define R = Character("Radjiman", color="#af2c40", who_bold=True, who_outlines=[(1, "#000")])
define RnS = Character("Radjiman & Soekarno", color="#55c023", who_bold=True, who_outlines=[(1, "#000")])
define T = Character("Terauchi", color="#5fb9c9", who_bold=True, who_outlines=[(1, "#000")])

# The game starts here.
style screentext:
    color "#9e5f12"
    size 18

label start:
    with dissolve
    scene bg 1
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
    jump scene2

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
    jump scene3

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

label end:
    return
