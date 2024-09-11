lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")

    valinta = input("Anna valintasi (1, 2 tai 3): ")

    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()  # Muutetaan ICAO-koodi isoiksi kirjaimiksi
        nimi = input("Anna lentoaseman nimi: ")

        # Tallennetaan uusi lentoasema sanakirjaan
        lentoasemat[icao] = nimi

        print(f"Lentoasema {nimi} (ICAO: {icao}) on tallennettu.")  # Tulostetaan tallennusviesti

    elif valinta == "2":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()  # Muutetaan koodi isoiksi kirjaimiksi

        # Tarkistetaan, löytyykö ICAO-koodi sanakirjasta
        if icao in lentoasemat:
            print(f"Lentoasema ICAO-koodilla {icao} on {lentoasemat[icao]}.")
        else:
            print(f"Lentoasemaa ICAO-koodilla {icao} ei löydy.")

    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta. Yritä uudelleen.")
