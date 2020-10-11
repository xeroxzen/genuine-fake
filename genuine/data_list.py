# -*- coding: utf-8 -*-
"""
Created on Thu December  19 14:10:59 2019

@author: Andile XeroxZen
"""
common_surnames = [
    'Moyo', 'Nyathi', 'Nyati', 'Dube', 'Sibanda', 'Mdlongwa', 'Ndlovu', 'Ndhlovu', 'Mbele', 'Stinta', 'Ncube', 'Mugabe',
    'Shoko,', 'Chamisa', 'Khumalo', 'Nxumalo', 'Ncube', 'Mkhwananzi', 'Bhebhe', 'Dlodlo', 'Nkala', 'Nkomo', 'Tshuma',
    'Mvundla', 'Ndebele', 'Khuphe', 'Nkiwane', 'Sibindi', 'Nyathi', 'Mpofu',
    'Hlabangane', 'Siziba', 'Ngwenya', 'Mathuthu', 'Mangena', 'Chafa', 'Charumbira', 'Mandela', 'Mnangagwa', 'Mangwana',
    'Khuboni', 'Nyilika', 'Nyoni', 'Garanganga', 'Hatendi', 'Kachingwe', 'Mabuwa', 'Mangwende', 'Manyuchi', 'Mapfumo',
    'Mariga', 'Mupfumira', 'Musambasi', 'Ndandarika', 'Nyakasikana', 'Nyandoro', 'Tongofa', 'Nkabinde', 'Musa',
    'Dlamini', 'Makaza', 'Mafara', 'Marara', 'Sikhosana', 'Olsen', 'Coltart', 'Biti', 'Tsvangirai', 'Makoni',
    'Makonese', 'Chibvu', 'Mali', 'Dywili', 'Mlambo', 'Nxusani', 'Ntuli', 'Phiri', 'Maphosa', 'Kheswa',
    'Mutambara',
    'Magaisa',
    'Gandiwa',
    'Nzombe',
    'Tazvivinga',
    'Mangisi',
    'Makoto',
    'Mafa',
    'Mutukwa',
    'Veremu',
    'Chidembo',
    'Utete',
    'Mpande',
    'Chakauya',
    'Chiwawa',
    'Marara',
    'Ndaba',
    'Mazuru',
    'Kachidza',
    'Mushangwe',
    'Khoza',
    'Chigora',
    'Marumisa',
    'Mazarire',
    'Bhobho',
    'Nhliziyo',
    'Musoni',
    'Dhlakama',
    'Jakarasi',
    'Muchingami',
    'Magama',
    'Manatsa',
    'Mutisi',
    'Muronda',
    'Jokonya',
    'Hamadziripi',
    'Mutengwa',
    'Mudonhi',
    'Maketo',
    'Maruza',
    'Bonde',
    'Matavire',
    'Runganga',
    'Kanyongo',
    'Makawa',
    'Muringani',
    'Zivanai',
    'Nyirenda',
    'Ndemera',
    'Mukwena',
    'Mushamba',
    'Ngwarati',
    'Masukume',
    'Mungofa',
    'Chaitezvi',
    'Samuriwo',
    'Mukamba',
    'Matambanadzo',
    'Mazonde',
    'Danda',
    'Chigumira',
    'Tagara',
    'Mloyi',
    'Chasara',
    'Sixpence',
    'Magadzire',
    'Gwebu',
    'Bhunu',
    'Tinago',
    'Kumalo',
    'Marima',
    'Tagwireyi',
    'Nyamandi',
    'Van',
    'Mukuze',
    'Chiramba',
    'Kanda',
    'Zivengwa',
    'Chaparadza',
    'Chitsike',
    'Mukondo',
    'Mukombe',
    'Chitima',
    'Nota',
    'Makotore',
    'Masikati',
    'Magora',
    'Imbayago',
    'Muronzi',
    'Zireva',
    'Ganda',
    'Masanga',
    'Pamire',
    'Vurayayi',
    'Kanyoka',
    'Chitongo',
    'Nyamunda',
    'Zambezi',
    'Chiota',
    'Kamanga',
    'Chikati',
    'Chikosha',
    'Tsoka',
    'Mafusire',
    'Khosa',
    'Nzou',
    'Mabuto',
    'Masimba',
    'Mudiwa',
    'Masunga',
    'Nyaude',
    'Jere',
    'Mahembe',
    'Matekenya',
    'Dondo',
    'Chisvo',
    'Bhebe',
    'Magara',
    'Chikandiwa',
    'Chareka',
    'Mashonga',
    'Chingwaru',
    'Madzivanzira',
    'Duri',
    'Mapani',
    'Manda',
    'Nyikayaramba',
    'Chapwanya',
    'Mabwe',
    'Chibvongodze',
    'Panganai',
    'Jim',
    'Magombedze',
    'Bvunzawabaya',
    'Chipuriro',
    'Mudzinganyama',
    'Tarwireyi',
    'Nhongo',
    'Bwanya',
    'Milanzi',
    'Chihuri',
    'Chaka',
    'Murehwa',
    'Chiromo',
    'Chimusoro',
    'Matika',
    'Mhungu',
    'Kufakunesu',
    'Gonese',
    'Phtrt',
    'Chirima',
    'Dumani',
    'Majuru',
    'Benhura',
    'Marecha',
    'Moses',
    'Mashumba',
    'Peter',
    'Manyara',
    'Mabasa',
    'Muyengwa',
    'Chidziva',
    'Chanakira',
    'Paradzai',
    'Ngara',
    'Zimba',
    'Makuni',
    'Shayamano',
    'Dzingirai',
    'Jeche',
    'Joe',
    'Dumba',
    'Chishiri',
    'Ziki',
    'Sabau',
    'Gororo',
    'Tevera',
    'Msipha',
    'Mahere',
    'Mahuni',
    'Muzambi',
    'Chiringa',
    'Mapanzure',
    'Guzha',
    'Tirivanhu',
    'Mapira',
    'Tamanikwa',
    'Damba',
    'Mupunga',
    'Rangwani',
    'Chibwe',
    'Murefu',
    'Denga',
    'Matsilele',
    'Chivanga',
    'Tayengwa',
    'Seremwe',
    'Nhamburo',
    'Munyaka',
    'Chawatama',
    'Mataga',
    'Ngwaru',
    'Juru',
    'Musemwa',
    'Saizi',
    'Chiripanyanga',
    'Matashu',
    'Masiyiwa',
    'Chikumba',
    'Mabhiza',
    'Maunganidze',
    'Hanyani',
    'Murwisi',
    'Chitanda',
    'Maromo',
    'Mandishona',
    'Chingoma',
    'Mufuka',
    'Hodzi',
    'Chiware',
    'Chando',
    'Ndimande',
    'Nyahuma',
    'Chitambo',
    'Jele',
    'Chagonda',
    'Shoriwa',
    'Chingombe',
    'Lupahla',
    'Chigova',
    'Gurupira',
    'Hwata',
    'Chitauro',
    'Chigwada',
    'Zindi',
    'Hama',
    'Mpunzi',
    'Muzembe',
    'Chiduku',
    'Murungweni',
    'Mawarire',
    'Chitimbe',
    'Mutami',
    'Machisa',
    'Magomo',
    'Nyamazana',
    'Chizanga',
    'Nyanga',
    'Zishiri',
    'Mangombe',
    'Mabena',
    'Mandere',
    'Saunyama',
    'Mukumba',
    'Muroyiwa',
    'Guta',
    'Mhishi',
    'Kamudyariwa',
    'Ticharwa',
    'Kapfunde',
    'Ndava',
    'Nyangani',
    'Jubane',
    'Maregere',
    'Chitumba',
    'Nyatsanga',
    'Ndongwe',
    'Munodawafa',
    'Chigariro',
    'Tumbare',
    'Muchini',
    'Gavaza',
    'Masaiti',
    'Hofisi',
    'Dzikiti',
    'Gwata',
    'Masarakufa',
    'Smith',
    'Mombe',
    'Chiminya',
    'David',
    'Zhanda',
    'Msebele',
    'Mkwebu',
    'Tsingano',
    'Tauzeni',
    'Makovere',
    'Mangava',
    'Bande',
    'Nhemachena',
    'Machinga',
    'Chiradza',
    'Chipanga',
    'Mudarikwa',
    'Ndowa',
    'Rwafa',
    'Dewa',
    'Makwanya',
    'Marongedza',
    'Tizora',
    'Ali',
    'Hondo',
    'Mhuru',
    'Marozva',
    'Muzuva',
    'Mugoni',
    'Mashavira',
    'Chingwena',
    'Nziramasanga',
    'Muringayi',
    'Mazambani',
    'Chikaka',
    'Chipara',
    'Mawoyo',
    'Rwizi',
    'Musakwa',
    'Mbanje',
    'Mudadi',
    'Mutyambizi',
    'Ranganai',
    'Zvinavashe',
    'Kwangware',
    'Mufudza',
    'Samuel',
    'Ndlela',
    'Tore',
    'Mutete',
    'Muzondiwa',
    'Kambanje',
    'Madziya',
    'Mukozho',
    'Tagwirei',
    'Magumise',
    'Mutemeri',
    'Goremusandu',
    'Tsikira',
    'Gasura',
    'Machiridza',
    'Chigumbu',
    'Jacob',
    'Chikwanha',
    'Mungate',
    'Muchero',
    'Mushunje',
    'Makwarimba',
    'Komboni',
    'Chinhema',
    'Takura',
    'Chakawa',
    'Gwati',
    'Chirongoma',
    'Mushaninga',
    'Muchineripi',
    'Mujaji',
    'Nyatsanza',
    'Chipato',
    'Bumhira',
    'Ganya',
    'Lungu',
    'Masaka',
    'Dzomba',
    'Muranganwa',
    'Pawandiwa',
    'Chigogo',
    'Murandu',
    'Mushoriwa',
    'Nyamupfukudza',
    'Nyasha',
    'Brown',
    'Marime',
    'Danga',
    'Kativu',
    'Muzvondiwa',
    'Murombedzi',
    'Goronga',
    'Mariga',
    'Mzizi',
    'Svosve',
    'Dzenga',
    'Moyo',
    'Ncube',
    'Sibanda',
    'Dube',
    'Ndlovu',
    'Mpofu',
    'Sithole',
    'Ngwenya',
    'Phiri',
    'Tshuma',
    'Nyoni',
    'Nkomo',
    'Nyathi',
    'Ndhlovu',
    'Mhlanga',
    'Khumalo',
    'Zhou',
    'Banda',
    'Shumba',
    'Gumbo',
    'Ndebele',
    'Muleya',
    'Hove',
    'Shoko',
    'Mapfumo',
    'Siziba',
    'Ndou',
    'Mlambo',
    'Dhliwayo',
    'Simango',
    'Maposa',
    'Masuku',
    'Bhebhe',
    'Marufu',
    'Mudenda',
    'Makoni',
    'Mlilo',
    'Zulu',
    'Muyambo',
    'Nyandoro',
    'Mathe',
    'Chuma',
    'Takawira',
    'Chauke',
    'Zuze',
    'Mpala',
    'Muchenje',
    'Sigauke',
    'Munemo',
    'Lunga',
    'Nkala',
    'Mudzingwa',
    'Taruvinga',
    'Mutasa',
    'Mahachi',
    'Katsande',
    'Ndoro',
    'Mbedzi',
    'Chari',
    'Muza',
    'Munsaka',
    'Mapuranga',
    'Mutero',
    'Maseko',
    'Nyika',
    'Muchemwa',
    'Ngulube',
    'Mubaiwa',
    'Mudimba',
    'Sande',
    'Gondo',
    'Chiwara',
    'Munetsi',
    'Mushonga',
    'Munkuli',
    'Kaseke',
    'Chifamba',
    'Mumpande',
    'Mabhena',
    'Nyamadzawo',
    'Mangena',
    'Makaza',
    'Mlalazi',
    'Shava',
    'Masango',
    'Tigere',
    'Manyika',
    'Gatsi',
    'Shereni',
    'Makumbe',
    'Dlamini',
    'Shonhiwa',
    'Muzamba',
    'Mandaza',
    'Magaya',
    'Mangwiro',
    'Gwenzi',
    'Mahlangu',
    'Ruzvidzo',
    'Nyakudya',
    'Tapera',
    'Makombe',
    'Madondo',
    'Mguni',
    'Mabika',
    'Chibanda',
    'Mandizvidza',
    'Makore',
    'Nkiwane',
    'Muzenda',
    'Mwale',
    'Mugwagwa',
    'Mlotshwa',
    'Musekiwa',
    'Dhlamini',
    'Mugabe',
    'Hungwe',
    'Majoni',
    'Chibaya',
    'Matambo',
    'Masawi',
    'Machingura',
    'Gomo',
    'Rusere',
    'Mtetwa',
    'Nyamande',
    'Makuyana',
    'Mashiri',
    'Mutema',
    'Musonza',
    'Muchena',
    'Mkandla',
    'Mutandwa',
    'Chakanyuka',
    'Gumede',
    'Masunda',
    'Ndiweni',
    'Matsika',
    'Mhembere',
    'Jimu',
    'Marange',
    'Sibindi',
    'Matare',
    'Mwanza',
    'Mkwananzi',
    'Ngorima',
    'Musarurwa',
    'Mutize',
    'Muzanenhamo',
    'John',
    'Mujuru',
    'Motsi',
    'Murwira',
    'Mwembe',
    'Chinyama',
    'Mbewe',
    'Marowa',
    'Katiyo',
    'Paradza',
    'Nyikadzino',
    'Mawire',
    'Chiweshe',
    'Mamvura',
    'Munyoro',
    'Marimo',
    'Muzondo',
    'Maponga',
    'Tafirenyika',
    'James',
    'Mugadza',
    'Ngirazi',
    'Hadebe',
    'Tsuro',
    'Khupe',
    'Masiya',
    'Shoniwa',
    'Mashingaidze',
    'Mafuta',
    'Mashava',
    'Msipa',
    'Siwela',
    'Taderera',
    'Mashonganyika',
    'Mudimu',
    'Tavengwa',
    'Mhaka',
    'Nhamo',
    'Kunaka',
    'Mafukidze',
    'Mutale',
    'Chirume',
    'Madziva',
    'Nkomazana',
    'Marume',
    'Madzinga',
    'Musariri',
    'Chikomo',
    'Manjengwa',
    'Kwaramba',
    'Nyamayaro',
    'Zenda',
    'Tshabalala',
    'Chikukwa',
    'Matope',
    'Chimombe',
    'Jongwe',
    'Makina',
    'Vambe',
    'Jack',
    'Nxumalo',
    'Malunga',
    'Jonasi',
    'Mugari',
    'Rwodzi',
    'Chiyangwa',
    'Zondo',
    'Mutizwa',
    'Zimunya',
    'Mutanga',
    'Mwinde',
    'Musiiwa',
    'Chamunorwa',
    'Denhere',
    'Jani',
    'Zindoga',
    'Mavhura',
    'Munkombwe',
    'Maramba',
    'Tom',
    'Njanji',
    'Machona',
    'Masocha',
    'Sakala',
    'Madamombe',
    'Nduna',
    'Meki',
    'Chirwa',
    'Makiwa',
    'Saidi',
    'Gwatidzo',
    'Mawere',
    'Matongo',
    'Matiza',
    'Mlauzi',
    'Simbi',
    'Chinembiri',
    'Mnkandla',
    'Zimuto',
    'Charamba',
    'Mapurisa',
    'Zhakata',
    'Mazarura',
    'Mhike',
    'Gumpo',
    'Antonio',
    'Nyakabau',
    'Mavhunga',
    'Nyamukondiwa',
    'Gono',
    'Saungweme',
    'Shamu',
    'Chamboko',
    'Choto',
    'Kwenda',
    'Mashoko',
    'Mugande',
    'Mukono',
    'Chipunza',
    'Gore',
    'Mudavanhu',
    'Sango',
    'Nyama',
    'Tinarwo',
    'Dick',
    'Chikuni',
    'Ntini',
    'Kanyemba',
    'Mafu',
    'Makosa',
    'Chinyanga',
    'Ngoma',
    'Mtisi',
    'Nsingo',
    'Rusike',
    'Mhandu',
    'Makusha',
    'Shiri',
    'Zisengwe',
    'Sikhosana',
    'Munenge',
    'Nyambo',
    'Shambare',
    'Moyana',
    'Masuka',
    'Mushore',
    'Macheka',
    'Tanyanyiwa',
    'Kufa',
    'Mangezi',
    'Runesu',
    'Matanda',
    'Matema',
    'Matutu',
    'Mbano',
    'Bere',
    'Mhizha',
    'Mafunga',
    'Gurure',
    'Chimedza',
    'Tomu',
    'Mataruse',
    'Makwara',
    'Tsiga',
    'Goredema',
    'Tapfumaneyi',
    'Dlodlo',
    'Chinyoka',
    'Mangwende',
    'Chivasa',
    'Khanye',
    'Mandeya',
    'Vundla',
    'Machaya',
    'Chabata',
    'Charuma',
    'Matanhire',
    'Choga',
    'Zinyemba',
    'Khumbula',
    'Gambiza',
    'Hlabangana',
    'Machaka',
    'Tapfuma',
    'Musara',
    'Madzima',
    'Madziwa',
    'Mbofana',
    'Matenga',
    'Pedzisai',
    'Chikwanda',
    'Manyere',
    'Munyaradzi',
    'Jeke',
    'Dzapasi',
    'Mhere',
    'Gutu',
    'Ngwerume',
    'Mumba',
    'Mdlongwa',
    'Zaranyika',
    'Nyemba',
    'Dongo',
    'Musiyiwa',
    'Kazingizi',
    'Chinyani',
    'Murambiwa',
    'Makonese',
    'Thomas',
    'Chisango',
    'Makanda',
    'Luphahla',
    'Kativhu',
    'Gweshe',
    'Machingauta',
    'Gomba',
    'Magwenzi',
    'Kashiri',
    'Zinyama',
    'Masendeke',
    'Kondo',
    'Zvenyika',
    'Jonga',
    'Gwara',
    'Vheremu',
    'Nyati',
    'Manyanga',
    'Makamba',
    'Magwaza',
    'Munyanyi',
    'Chiremba',
    'Muranda',
    'Midzi',
    'Msimanga',
    'Zengeya',
    'Gava',
    'Kembo',
    'Mhondiwa',
    'Zengeni',
    'Ushe',
    'Tagarira',
    'Simon',
    'Matanga',
    'Dziva',
    'Chitiyo',
    'Mutamba',
    'Nleya',
    'William',
    'Pasipanodya',
    'Wilson',
    'Jena',
    'Mtombeni',
    'Charumbira',
    'Ngandu',
    'Chirinda',
    'Zvomuya',
    'Kanengoni',
    'Muzavazi',
    'Marisa',
    'Rupiya',
    'Gotora',
    'Jasi',
    'Mudau',
    'Mashanda',
    'Chikono',
    'Chipangura',
    'Karonga',
    'Mudzengerere',
    'Mukucha',
    'Magura',
    'Gudo',
    'Mukaro',
    'Nhidza',
    'Madzivire',
    'Gama',
    'Mavunga',
    'Chamisa',
    'Mandizha',
    'Rutsito',
    'Kwangwari',
    'Machokoto',
    'Zhuwao',
    'Musindo',
    'Donga',
    'Manyange',
    'Ndawana',
    'Mativenga',
    'Gora',
    'Makamure',
    'Jiri',
    'Chihota',
    'Tandi',
    'Tshabangu',
    'Jackson',
    'Nhema',
    'Chikanya',
    'Nyamhunga',
    'Mazhambe',
    'Mathuthu',
    'Mushayi',
    'Machipisa',
    'Kambarami',
    'Singo',
    'Chikomba',
    'Gundani',
    'Nare',
    'Musona',
    'Chirenje',
    'Mashayamombe',
    'Mapondera',
    'Mutanda',
    'Makura',
    'Chakanetsa',
    'Munyuki',
    'Matimba',
    'Muguti',
    'Tafireyi',
    'Hlongwane',
    'Nyabadza',
    'Maruta',
    'Nherera',
    'Ngoshi',
    'Mapako',
    'Mususa',
    'Mubvumbi',
    'Hamandishe',
    'Chiwanza',
    'Chimbwanda',
    'Goto',
    'Gwaze',
    'Masara',
    'Madzimure',
    'Munhenga',
    'Muchimba',
    'Mubayiwa',
    'Murove',
    'Thebe',
    'Nyashanu',
    'Kumbula',
    'Rice',
    'Nhau',
    'Chitsa',
    'Savanhu',
    'Maravanyika',
    'Samu',
    'Mudzamiri',
    'Katerere',
    'Mbambo',
    'Ngundu',
    'Shangwa',
    'Chizema',
    'Makuvaza',
    'Kahari',
    'Nyoka',
    'Takaendesa',
    'Tauro',
    'Muponda',
    'Nhira',
    'Makaya',
    'Mazorodze',
    'Mapiye',
    'Joseph',
    'Myambo',
    'Dzingai',
    'Jambaya',
    'Chikoto',
    'Mutsago',
    'Nyamukapa',
    'Nhete',
    'Baloyi',
    'Masenda',
    'Mandebvu',
    'Chikowore',
    'Samson',
    'Gonye',
    'Masamba',
    'Chikore',
    'Jaji',
    'Makondo',
    'Chidhakwa',
    'Chinoda',
    'Gonzo',
    'Madzivanyika',
    'Musengi',
    'Mudzimu',
    'Chiutsi',
    'Nyamasoka',
    'Mushambi',
    'Mazhindu',
    'Gwanzura',
    'Muchabaiwa',
    'Mapisa',
    'Tachiona',
    'Kamba',
    'Zikhali',
    'Mugova',
    'Chitate',
    'Tlou',
    'Chigodora',
    'Chimuka',
    'Khabo',
    'Chatikobo',
    'Machemedze',
    'Nyambuya',
    'Chipere',
    'Mushipe',
    'Badza',
    'Murombo',
    'Chimanga',
    'Mandava',
    'Mutare',
    'Mberi',
    'Mukombwe',
    'Kaitano',
    'Pasipamire',
    'Soko',
    'Chirara',
    'Kazembe',
    'Gutsa',
    'Chikara',
    'Maisiri',
    'Masina',
    'Mavura',
    'Zambuko',
    'Makuvire',
    'Takundwa',
    'Maturure',
    'Muvirimi',
    'Chigwida',
    'Huni',
    'Kadungure',
    'Vengesai',
    'Zvidzai',
    'Mukarati',
    'Kanyama',
    'Ruzive',
    'Mbengo',
    'Mungombe',
    'White',
    'Musasa',
    'Togara',
    'Munjoma',
    'Chidakwa',
    'Manyonga',
    'Muzira',
    'Muradzikwa',
    'Jojo',
    'Chemhere',
    'Manjoro',
    'Gunda',
    'Daka',
    'Munatsi',
    'Shamuyarira',
    'Mhako',
    'Jamu',
    'Jera',
    'Bobo',
    'Mashamba',
    'Mangoma',
    'Zvoushe',
    'Mleya',
    'Mudyiwa',
    'Chikanda',
    'Mudzviti',
    'Makota',
    'Mutetwa',
    'Nyarugwe',
    'Manomano',
    'Musa'

]

common_names = [
    'Andile', 'Proud', 'Fiona', 'Natasha', 'Clifton', 'Sean', 'Tafara', 'Tofara', 'Shingirai', 'Shingai', 'Samkele',
    'Samkeliso', 'Nancy', 'Patience', 'Lennon', 'Learnmore', 'Laymore', 'Edwin', 'Edwick', 'Mzimazisi', 'Rejoice',
    'Glenda', 'Thabhelo', 'Tapelo', 'Takalani', 'Tumelo', 'Edwell', 'Rio', 'Just', 'Nozibele', 'Janine', 'Janice',
    'Pamishie', 'Buhlebenkosi', 'Ollyn', 'Ayanda', 'Anele', 'Anesu', 'Bheki', 'Beke', 'Busi', 'Donna', 'Zezu', 'Sia',
    'Simoe', 'Sarah', 'Peter', 'Melissa', 'Nobuhle', 'Nokuzola', 'Mzimkhulu', 'Amanda', 'Vuyolwenkosi', 'Romy',
    'Tinashe', 'Tanya', 'Aldrin', 'Ashley', 'Joseph', 'Tinotenda', 'kelvin', 'Kim', 'Panashe', 'Nia', 'Tatenda',
    'Kayla', 'Prayer', 'Mzingaye', 'bule', 'Ropa', 'Hearty', 'Pauline', 'Engel', 'Sophie', 'Alex', 'Nataly', 'Kida',
    'Nomanqoba', 'Eric', 'tanya', 'naty', 'Selena', 'Nkosikhona', 'Nkosiyabo', 'Mziyanda', 'Mhlanguli', 'Melithemba',
    'Menelisi', 'Evelyn', 'Ruth', 'Amy', 'Mandy', 'Penny', 'Madonna', 'Brittney', 'Juliana', 'Juliette', 'Juliet',
    'Samora', 'Samuel', 'Lindani', 'Thembelani', 'Thembeka', 'Phumzile', 'Nandipa', 'Nandipha', 'Terence', 'Jaden',
    'Jason', 'Misheck', 'Abel', 'Tom', 'Keith', 'Nigel', 'Darlington', 'Prince', 'Ben', 'Brighton', 'Thandolwenkosi',
    'Thandiwe', 'Ruramai', 'Farai', 'Tisdale', 'Chad', 'Lastborn', 'Kudakwashe', 'Mduduzi', 'Sibonisiwe', 'Sibonakele',
    'Sipho', 'Sihle', 'Cynthia', 'Celia', 'Cecilia', 'Drake', 'Dumoluhle', 'Dumisani', 'Anderson', 'Dumezweni',
    'Vikani', 'Vuyisile', 'Vuyani', 'Vumile', 'Mbangisi', 'Mbonisi', 'Mbongeni', 'Devon', 'Jasper', 'Michelle', 'Carol',
    'Sam', 'Sicelo', 'Simosethu', 'Simosenkosi', 'Mary', 'Marylene', 'Marlene', 'Vusa', 'Vusumuzi', 'Albert', 'Utile',
    'Shantelle', 'Chantel', 'Charmaine', 'Shamiso', 'Shylet', 'Nyasha', 'Wisbert', 'Obert', 'Noel', 'Noah', 'Nozipho',
    'Nokukhanya', 'Babalwa', 'Leeroy', 'Jabulani', 'Irene', 'Mangosuthu', 'Sasha', 'Nobantu', 'Gugulethu', 'Duduzile',
    'Siduduzile', 'Munyaradzi', 'Mayibongwe', 'Mongezi', 'Itai', 'Brett', 'Brandon', 'Brendon', 'Eulitha', 'Shona',
    'Doreen', 'Dorothy', 'Gabriel', 'Gabriella', 'Ndumiso', 'Nondumiso', 'Bhekumusa', 'Njabulo', 'Clifford', 'Herbert',
    'Stanley', 'Stanford', 'Sithabile', 'Sithandazile', 'Sithatshisiwe', 'Nomsa', 'Nobuntu', 'Zenande', 'Susan',
    'Susanna', 'Grace', 'Sally', 'Auxillia', 'Thokozani', 'Thokozile', 'Belinda', 'Samantha', 'Joshua', 'John', 'Peter',
    'Akim', 'Achim', 'Nick', 'Jadyn', 'Scott', 'Lionel', 'Ronald', 'Belta', 'Maurine', 'Mondli', 'Thobelikhaya',
    'Thobelumzi', 'Olwethu', 'Shanae', 'Leona', 'Princess', 'Lihle', 'Hlelile', 'Janet', 'Nolwazi', 'Melody',
    'Monwabisi', 'Humphrey', 'Leonard', 'Len', 'Charles', 'Charlie', 'Charlene', 'Gracious', 'Petra', 'Petronella',
    'Junior', 'Tiana', 'Cyril', 'Miley', 'Rihanna', 'Donna', 'Donald', 'Jeremiah', 'Andrew', 'Anders', 'Robert',
    'Emmanuel', 'Nelson', 'Emmerson', 'Jonathan', 'Velisile', 'Velile', 'Nomvula', 'Nkosentsha', 'Naomi', 'Ruth',
    'Gertrude', 'Iza', 'Yoleeswa', 'Vaida', 'Faith', 'Patience', 'Millicent', 'Tonderai', 'Tongai', 'Justin',
    'Catherine', 'Concelia', 'Ida', 'Donnel', ' Zeus', 'Queen', 'King', 'Carl', 'Charlington', 'Kudzai', 'Kudzi',
    'Zandile', 'Emmy', 'Jacqueline', 'Jessica', 'Jesse', 'Lorraine', 'Sikhanyisiwe', 'Sharon', 'Zolisile', 'Zolile',
    'Bongani', 'Zabe', 'Makanaka', 'James', 'Sean', 'Irvine', 'Evans', 'Jenny', 'Tania', 'Petrolater', 'Mal', 'Dani',
    'Daniel', 'Lynnet', 'Joyful', 'Joylene', 'Theo', 'Theodore', 'Wayne', 'Kelly', 'Takura', 'Takunda', 'Tanatswa',
    'Mercy', 'Harmony', 'Tariro', 'Chichi', 'Lisa', 'Clayt', 'Arani', 'Morgan', 'Theresa', 'Malcolm', 'Laue',
    'Simelinkosi', 'Suave', 'Marko', 'Steven', 'Stephanie', 'Lexi', 'Obriel', 'Hassan', 'Nakai', 'Cherrie', 'Tinevimbo',
    'Aaron', 'AJ', 'Ane', 'Anne', 'Tadiwanashe', 'Clement', 'Carita', 'Charity', 'Victor', 'Elsa', 'Precious',
    'Tawanda', 'Brian', 'Innocent', 'Tendai', 'Mandla', 'Mandlenkosi', 'Simba', 'Zenith', 'Angela', 'Clite', 'Clyte',
    'Aisha', 'Nesta', 'Mike', 'Jordan', 'Elizabeth', 'Tavonga', 'Lonely', 'Nicky', 'Noela', 'Sheline', 'Jordan',
    'Mukudzei', 'Jagger', 'Nesta', 'Gerald', 'Anesu', 'Godwin', 'Mitchelle', 'Petros', 'Lerato', 'Edward', 'Tammy',
    'Tiara', 'Adrain', 'Elijah', 'Tanaka', 'Godwin', 'Emma', 'Nesta', 'Kellington', 'Nikolai', 'Lindsay', 'Peace',
    'Kimberley', 'Tawonga', 'Stellar', 'Roselyn', 'Allie', 'Thabani', 'Makhosini', 'Ronny', 'Unathi', 'Admire',
    'Ntandoe', 'Vince', 'Liam', 'Hope', 'Ronald', 'Rue', 'Privilege', 'Anopa', 'Gamuchirai', 'Tengerai', 'Isabel',
    'Ali', 'Chengetai', 'Shaniqi', 'Mufaro', 'Marcia', 'Isabella', 'Wendy', 'Agatha', 'William', 'Bob', 'Bill',
    'Harvey', 'Abigirl', 'Esther', 'Adam', 'Eve', 'Siphiwe', 'Godfrey', 'Emerge', 'Sydney', 'Denver', 'Zenzo',
    'Zenzele', 'Zodwa', 'Zanele', 'Sandile', 'Mandisi', 'Bridgette', 'Dalindyebo', 'Gratuitous', 'Bradley',
    'Marymaculate', 'Andreas', 'Ryan', 'Colin', 'Collins', 'Nicole', 'Nichols', 'Nicholas', 'Stan', 'Tina', 'Miranda',
    'Sasha', 'Bridget', 'Pretty', 'Roxanne', 'Elliot', 'Mica', 'Berlin', 'Nondyebo', 'Phumuzile', 'Natalie', 'Ivy',
    'Blue-Ivy', 'Ayan', 'Matthew', 'Martin', 'Nyasha', 'Rutendo', 'Fungai', 'Mutsa', 'Tawanda', 'Kudakwashe', 'Nakai',
    'Kumbirai', 'Tinashe', 'Munashe', 'Tanatswa', 'Tumai', 'Farai', 'Tariro', 'Mufaro',
    'Vongai', 'Tendai', 'Tadiwa', 'Ruvarashe', 'Paidamoyo', 'Tatenda', 'Chido', 'Taurai', 'Mazvita', 'Rufaro',
    'Munyaradzi', 'Kundai', 'Tavonga', 'Tanaka', 'Anesu', 'Ngoni', 'Ngonidzashe', 'Tafadzwa', 'Kuda', 'Tawananyasha',
    'Batsirai', 'Rudo', 'Nyarai', 'Mudiwa', 'Gamuchirai', 'Tapiwa', 'Hama', 'Anashe', 'Tanga', 'Kudzai', 'Tarisai',
    'Tendo', 'Tamuka', 'Tinotenda', 'Sekai', 'Tafara', 'Dambudzo', 'Panashe', 'Tanyaradzwa', 'Tashinga', 'Mukai',
    'Danai', 'Takunda', 'Fadzai', 'Rukudzo'

]

medical_aid = [
    'For All Medical Aid Society', 'Varichem Limited Medical Fund', 'Steward Health Medical Benefit Fund',
    'Save Life Medical Aid Fund', 'Pro Health Medical Aid Society', 'Parksmed Health Fund', 'Genfin Medical Aid Fund',
    'Corporate 24 Medical Aid', 'Calm Health International Medical Aid Society', 'Advantage Health Medical Aid Society',
    'Med Assist Medical Aid Scheme', 'Evolution Health & Life Assurance', 'Medtours Africa',
    'Zimbabwe General Medical Aid Fund (Zigma)', 'Agricultural Medical Aid Society (Agrim)', 'Eternal Peace Health',
    'Premier Service Medical Aid Society', 'Bonvie Medical Aid Scheme', 'Cellmed Health Medical Fund',
    'Blanket Mine Medical Aid Society', 'Emf Medical Aid Society', 'Fidelity Life Medical Aid Society',
    'First Mutual Medical Savings Fund', 'Fmre Life And Health (Pvt) Ltd', 'Generation Health Medical Fund',
    'Harare Municipality Medical Aid Society', 'Kwekwe City Council Medical Aid Society',
    'Liberty Health Medical Aid Society', 'Masvingo Municipal Medical Aid Society',
    'Medical Aid Society Of Central Africa', 'Municipality Of Bulawayo Medical Aid Society',
    'National Social Security Authority', 'Railmed', 'Northern Medical Aid Society', 'Sovereign Health (Pvt) Ltd'
]

allergens = [
    'Balsam of Peru', 'Egg', 'Fish', 'Fruit' 'Garlic', 'Hot pepper', 'Oats', 'Maize', 'Milk', 'Poultry Meat',
    'Red Meat', 'Rice', 'Sesame', 'Shellfish', 'Soy', 'Sulfites', 'Tartrazine', 'Tree Nut', 'Wheat', 'Tetracycline',
    'Dilantin', 'Tegretol', 'Penicillin', 'Cephalosporins', 'Sulfonamides', 'anti-inflammatories',
    'intravenous contrast dye', 'local anaesthetics', 'Pollen', 'cat', 'dog', 'insect sting', 'perfume', 'mold',
    'cosmetics', 'semen', 'latex', 'water', 'house dust mite', 'Nickel', 'Gold', 'Chromium', 'cobalt', 'formaldehyde',
    'Photographic developers', 'Fungicide'
]

places = [
    'New Luveve, Bulawayo', 'Pumula', 'Mahatshula', 'Nkulumane', 'Sunninghill', 'Hillside', 'Hillcrest', 'Burnside',
    'Douglasdale', 'Entumbane', 'Northend', 'Harrisvale', 'Mbundane', 'Masasa', 'Borrowdale Brook', 'Mbare',
    'Mt Pleasant', 'Makokoba', 'Mzilikazi', 'Lobengula', 'Malindela', 'Tshabalala', 'Old Luveve', 'Gwabalanda',
    'Emganwini', 'Nketa', 'Trenance', 'Emakhandeni', 'Cowdray Park', 'Matshe-umhlophe', 'Njube', 'Magwegwe', 'Msasa'
]

streets = [
    'Pine Road', 'Graham Road', 'L-Street Road', 'Alexander Road', 'Casper Road', 'President Road', 'State House Ave',
    'Jason Moyo Ave', 'Joshua Nkomo Road', 'Prinsloo Road', 'Game Free Road', 'Brentwood Road', 'Ellison Road',
    'University Road', 'Norwark Road', 'Mbare Road'
]

hospital = [
    'Arcadia Medical Centre',
    'The Avenues Clinic',
    'Baines Avenue Clinic',
    'Baines Intercare Medical Centre, 15 Baines Avenue',
    'Beatrice Road Infectious Diseases',
    'Belvedere Maternity',
    'Belvedere Medical Centre',
    'BMC Hospital',
    'Central Harare Hospital',
    'Citimed Chitungwiza Hospital',
    'Corporate 24 Medical Centre',
    'Dandaro Clinic',
    'Diagnostic Heart Center',
    'Harare Hospital',
    'Harare Maternity',
    'Highfield Poly Clinic',
    'Marlborough Medical Centre',
    'Mbuya Dorcas Hospital',
    'Med24 Medical Centre',
    'Metropolitan Clinic',
    'The Michael Gelfand Clinic',
    'The Montague Clinic',
    'New Cranborne Maternity Clinic',
    'Oncocare',
    'Parirenyatwa Hospital',
    'Queen of Peace Clinic',
    'Rock Foundation Medical Center',
    'Sekuru Kaguvi Hospital',
    "St. Anne's Hospital",
    'Suburban Medical Center',
    'Trauma Centre & Hospital',
    'West End Clinic',
    'West End Hospital',
    'Wilkins Hospital',

    'Mpilo Central Hospital',
    'Mater Dei  Hospital',
    'United Bulawayo Hospitals',
    'Inyathi Hospital',
    'Ingutsheni Psychiatric Hospital',

    'Avila Mission Hospital',
    'Bonda Mission Hospital',
    'Chikore Hospital',
    'Chipinge District Hospital',
    'Elim Mission Hospital',
    'Hauna Hospital',
    'Mount Melleray Mission Hospital',
    'Mount Selinda Hospital',
    "Murambi Hospital",
    "Murambinda Mission Hospital",
    "Mutambara Mission Hospital",
    "Mutare Provincial Hospital",
    "Nyanga District hospital",
    "Regina Coeli Mission Hospital",
    "Rusape General Hospital",
    "Rusitu Mission Hospital",
    "St Peter's Hospital",
    "Clay Bank Group of Hospitals",

    "Gokwe District Hospital",
    "Gweru Provincial General Hospital",
    "Kwekwe General Hospital",
    "Mnene Hospital",
    "St Gerald Chaya General Hospital",
    "Shurugwi District Hospital",
    "Zvishavane District Hospital",

    "Beitbridge District Hospital",
    "Brunapeg st annes Mission Hospital",
    "Esigodini District Hospital",
    "Filabusi District Hospital",
    "Gwanda Provincial Hospital",
    "Kezi rural Hospital",
    "Manama Mission Hospital",
    "Maphisa District Hospital",
    "Mtshabezi Mission Hospital",
    "Plumtree District Hospital",
    "Tshelanyemba Mission Hospital",

    "All Souls Mission Hospital",
    "Borrowdale Trust Hospital",
    "Chivhu General Hospital",
    "Kotwa Hospital",
    "Mahusekwa Hospital",
    "Makumbi Hospital",
    "Marondera Provincial Hospital",
    "Mutawatawa General Hospital",
    "Mutoko Hospital",
    "Nhowe Mission Hospital",
    "Nyadire Mission Hospital",
    "Sadza General Hospital",

    "Binga District Hospital",
    "Dakamela Rural District Hospital",
    "Lukosi Hospital",
    "Hwange Colliery Hospital",
    "Hwange Medical Centre (Baobab Hill)",
    "Mbuma Mission Hospital",
    "Nkayi Rural District Hospital",
    "St Luke's Hospital",
    "St Mary's Hospital",
    "St Patrick's Hospital",
    "Tsholotsho District Hospital",
    "Victoria Falls Hospital",

    "Alheit Hospital (Gutu)",
    "Bondolfi Hospital (Masvingo)",
    "Chiredzi Hospital (Chiredzi)",
    "Chivi Hospital (Chivi)",
    "Dewure Clinic (Gutu)",
    "Driefontein Hospital (Chartsworth)",
    "Gutu District Hospital (Mpandawana)",
    "Gutu Mission Hospital (Gutu)",
    "Mashoko Hospital (Bikita)",
    "Masvingo General Hospital",
    "Morgenster Mission Hospital (Masvingo)",
    "Mutero Mission Clinic (Gutu)",
    "Mwenezi Hospital (Mwenezi)",
    "Ndanga Hospital (Zaka)",
    "Nemanwa Clinic (Masvingo)",
    "Ngoma Huru Hospital",
    "Silveira Mission (Bikita)",
    "St Antony's Musiso Hospital (Zaka)",

    "Banket District Hospital",
    "Chegutu District Hospital",
    "Chidamoyo Mission Hospital",
    "Chinhoyi Provincial Hospital",
    "Darwendale Rural Hospital",
    "Father 'O' Hea Memorial Mission Hospital",
    "Kadoma General Hospital",
    "Kariba District Hospital",
    "Karoi District Hospital",
    "Magunje Rural Hospital",
    "Mutorashanga Rural Hospital",
    "Raffingora Rural Hospital",
    "Sanyati Baptist Hospital",
    "St Michael's Hospital",
    "Zvimba Rural Hospital",

    "Bindura Provincial Hospital - Bindura District",
    "Chimhanda District Hospital",
    "Chitsungo Mission Hospital - Mbire District",
    "Concession District Hospital",
    "Guruve Hospital - District",
    "Howard Hospital",
    "Karanda Mission Hospital - Mount Darwin District",
    "Madziwa Hospital - Shamva District",
    "Mary Mount Mission Hospital - Rushinga District",
    "Mt Darwin District Hospital",
    "Mvurwi Hospital - Mazowe District",
    "Nhowe Hospital",
    "PSMI Medical Clinic - Bindura",
    "Shamva Hospital - Shamva District",
    "Shashi Private Hospital - Bindura",
    "St Alberts Mission Hospital"
]

company = [
    'Datlabs', 'National Social Security Authority', 'Innscor', 'Econet Wireless', 'TelOne', 'Bakers Inn', 'Lobels',
    'Zimplats', 'CBZ Holdings', 'CABS', 'Delta Beverages', 'Stanbic Bank', 'FBC Holdings', 'Standard Chartered Bank',
    'OLD Mutual (ZW)', 'ZB Financial Holdings', 'AICO', 'NMBZ', 'Hippo Valley Estates', 'Meikles', 'Barclays Bank',
    'Hwange Coal', 'Mwana Africa', 'MBCA', 'SeedCo', 'Zimre Property', 'Masawara', 'First Mutual Holdings', 'Dairibord',
    'RioZim', 'OK Zimbabwe', 'Natfoods', 'CFI Holdings', 'Padenga', 'Cassava Smartech', 'Telecel ZW', 'NetOne'
]

career = [
    'Medical Doctor', 'Computer Programmer', 'School Teacher', 'Policy Maker', 'Metarlugical Engineer', 'Chemist',
    'Lawyer', 'Bank Teller', 'Till Operator', 'Janitor', 'General Hand', 'Security Guard', 'Physician',
    'Software Developer', 'Statistician', 'Technician', 'Physiotherapist', 'Nurse Practitioner', 'Labourer', 'Teacher',
    'Lecturer', 'Researcher', 'Pharmacist', 'Nurse', 'Nurse anaesthetist', 'Surgeon', 'Physician Assistant',
    'Police Officer', 'Mathematician', 'Gynaecologist', 'Bio Engineer', 'Chemist', 'Technologist', 'Physicist'
]

career_position = [
    'Programs Manager', 'Chief Executive Officer', 'Head Teller', 'Vice President of Engineering',
    'VP of Product Development', 'Book Keeper', 'Accountant', 'Senior Engineer', 'Head Master', 'Head Mistress',
    'Head of Department', 'Chairman', 'President', 'Co-CEO', 'Co-Chairman', 'Secretary', 'Secretary General',
    'Data Entry Clerk', 'Manager', 'Personal Assistant', 'Chauffeur', 'Book Keeper', 'Librarian', 'Chief Librarian',
    'Till Operator'
]

medical_roles = [
    "Ambulatory Nurse",
    "Anesthesiologist",
    "Audiologist",
    "Behavioral Health Charge Nurse",
    "Bereavement Counselor",
    "Cardiac Catholic Lab Nurse",
    "Cardiovascular Operating Room Nurse",
    "Cardiovascular Technologist",
    "Charge Nurse",
    "Chiropractor",
    "Counselor",
    "Dentist",
    "Dermatology Nurse",
    "Dialysis Nurse",
    "Doctor",
    "Emergency Room Nurse",
    "Endoscopy Nurse",
    "Family Nurse Practitioner",
    "Flight Nurse",
    "Genetic Counselor",
    "Home Health Nurse",
    "Hospice Counselor",
    "Hospice Nurse",
    "House Supervisor Nurse",
    "Intensive Care Nurse",
    "Interventional Radiology Nurse",
    "Labor and Delivery Nurse",
    "Lead Registered Nurse",
    "Legal Nurse Consultant",
    "Licensed Practical Nurse",
    "Licensed Vocational Nurse",
    "Medical Surgery Nurse",
    "Microbiologist",
    "Neonatal Intensive Care Nurse",
    "Nurse",
    "Nurse Anesthetist",
    "Nurse Midwife",
    "Nurse Practitioner",
    "Nursing Assistant",
    "Occupational Health Nurse",
    "Occupational Health and Safety Specialist",
    "Occupational Therapist",
    "Office Nurse",
    "Oncology Nurse",
    "Operating Room Nurse",
    "Optician",
    "Optometrist",
    "Orthodontist",
    "Orthotist",
    "Outreach RN",
    "Paramedic",
    "Pediatrician",
    "Pediatric Endocrinology Nurse",
    "Pediatric Intensive Care Nurse",
    "Pediatric Nurse",
    "Pediatric Nurse Practitioner",
    "Perioperative Nurse",
    "Pharmacist",
    "Prosthetist",
    "Physician",
    "Podiatrist",
    "Post Anesthesia Nurse",
    "Postpartum Nurse",
    "Progressive Care Nurse"
    "Psychiatric Nurse",
    "Psychiatric Nurse Practitioner"
    "Public Health Nurse",
    "Registered Nurse (RN)",
    "Registered Nurse (RN) Case Manager",
    "Registered Nurse(RN) Data Coordinator",
    "Registered Nurse (RN) First Assistant",
    "Registered Nurse (RN) Geriatric Care",
    "Registered Nurse (RN) Medical Inpatient Services",
    "Registered Nurse (RN) Patient Call Center",
    "Registered Nurse (RN) Student Health Services",
    "Registered Nurse (RN) Telephone Triage",
    "Registered Nurse (RN) Urgent Care",
    "Registered Nurse (RN) Women's Services",
    "Restorative Nurse",
    "Registered Medical Assistant",
    "Respiration (Inhalation) Therapist",
    "School Nurse",
    "Speech-Language Pathologist",
    "Surgeon",
    "Telemetry Nurse",
    "Therapist",
    "Veterinarian",
    "Veterinary Assistant",
    "Veterinary Technologist",
    "Wellness Nurse"
]
