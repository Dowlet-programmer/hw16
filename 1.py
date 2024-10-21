harytlar = {
"alma" : {
    "bahasy" : 15,
    "mukdary" : 30
    },
"mandarin" : {
    "bahasy" : 30,
    "mukdary" : 10
    },
"banan" : {
    "bahasy" : 27,
    "mukdary" : 20
    },
"hyyar" : {
    "bahasy" : 5,
    "mukdary" : 25
    },
"pomidor" : {
    "bahasy" : 7,
    "mukdary" : 35
    },
"un" : {
    "bahasy" : 50,
    "mukdary" : 100
    },
"cigit" : {
    "bahasy" : 61,
    "mukdary" : 10
    }
}
while True:
    kassa = 0
    print("""
    *** DUKAN DOLANDYRYSY ***
    1.Haryt gorkezijilerini gor
    2.Haryt satyn al
    3.Harytlary gos
    4.Harytlaryn bahasyny uytget
    5.Harytlary ayyr
    6.Mukdary artdyr
    Cykys ucin 'quit' yazyn
    """)
    isleg = input("Name etmeli (san girizin): ")
    if isleg == "1":
        for haryt, maglumat in harytlar.items():
            print(f"Haryt: {haryt}, Bahasy: {maglumat['bahasy']} manat, Mukdary: {maglumat['mukdary']} kg")
    elif isleg == "2":
        haryt = input("Nama satyn aljak? ")
        mukdar = float(input("Nache kg almak isleyan? "))
        if harytlar[haryt]["mukdary"] == 0 or harytlar[haryt]["mukdary"] < mukdar:
            print("bizde galmady")
        else:
            harytlar[haryt]["mukdary"] = harytlar[haryt]["mukdary"] - mukdar
            kassa += harytlar[haryt]["bahasy"] * mukdar
            print(f"{haryt} - y (i) satyn aldynyz! {kassa} mnt tolediniz.")
    elif isleg == "3":
        haryt_ady = input("Harytyň adyny giriziň: ")
        bahasy = int(input("Harytyň bahasyny giriziň: "))
        mukdary = int(input("Harytyň mukdaryny giriziň: "))
        harytlar[haryt_ady] = {
            "bahasy": bahasy,
            "mukdary": mukdary
        }
        print("Täze haryt goşuldy")
    elif isleg == "4":
        haryt_ady = input("Harydyň adyny giriziň: ")
        if haryt_ady in harytlar:
            täze_bahasy = int(input("Täze bahasyny giriziň: "))
            harytlar[haryt_ady]["bahasy"] = täze_bahasy
            print(f"{haryt_ady} harydynyň täze bahasy: {harytlar[haryt_ady]['bahasy']}")
        else:
            print("Haryt tapylmady.")
    elif isleg == "5":
        haryt_ady = input("Harydyň adyny giriziň: ")
        if haryt_ady in harytlar:
            del harytlar[haryt_ady]
            print(f"{haryt_ady} harydy dukandan-dan aýryldy.")
        else:
            print("Haryt tapylmady.")
    elif isleg == "6":
        haryt_ady = input("Harydyň adyny giriziň: ")
        if haryt_ady in harytlar:
            goşuljak_mukdar = int(input("Goşuljak mukdaryny giriziň: "))
            harytlar[haryt_ady]["mukdary"] += goşuljak_mukdar
            print(f"{haryt_ady} harydynyň täze mukdary: {harytlar[haryt_ady]['mukdary']}")
        else:
            print("Haryt tapylmady.")
    elif isleg == "quit":
        break
    else:
        print("Bizde olar yaly hyzmat yok!")



