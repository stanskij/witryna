imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")


nazwa_pliku = "dane.txt"


with open(nazwa_pliku, "w", encoding="utf-8") as plik:
    plik.write(f"Imię: {imie}\n")
    plik.write(f"Nazwisko: {nazwisko}\n")


print("\nDo pliku zapisane zostało:\n")
with open(nazwa_pliku, "r", encoding="utf-8") as plik:
    zawartosc = plik.read()
    print(zawartosc)