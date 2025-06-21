def pokaz_menu():
    print("\n=== MENU NAWIGACYJNE ===")
    print("1. Strona główna")
    print("2. O nas")
    print("3. Kontakt")
    print("0. Wyjście")

def strona_glowna():
    print("Witaj na stronie głównej!")

def o_nas():
    print("Jesteśmy zespołem pasjonatów Pythona :)")

def kontakt():
    print("Skontaktuj się z nami pod adresem: kontakt@example.com")

if __name__ == "__main__":
    while True:
        pokaz_menu()
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            strona_glowna()
        elif wybor == "2":
            o_nas()
        elif wybor == "3":
            kontakt()
        elif wybor == "0":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
