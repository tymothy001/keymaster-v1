
#pip3 install progress progressbar2 alive-progress tqdm

from bitcoinlib.keys import Key
from progress.bar import Bar
import sys




print("                                                                                           ")
print("                                                                                           ")
print("\033[0;32m       ██████╗░███████╗░█████╗░  ████████╗░█████╗░  ██████╗░██╗████████╗░█████╗░░█████╗░██╗███╗░░██╗\033[00m")
print("\033[0;32m       ██╔══██╗██╔════╝██╔══██╗  ╚══██╔══╝██╔══██╗  ██╔══██╗██║╚══██╔══╝██╔══██╗██╔══██╗██║████╗░██║\033[00m")
print("\033[0;32m       ██║░░██║█████╗░░██║░░╚═╝  ░░░██║░░░██║░░██║  ██████╦╝██║░░░██║░░░██║░░╚═╝██║░░██║██║██╔██╗██║\033[00m")
print("\033[0;32m       ██║░░██║██╔══╝░░██║░░██╗  ░░░██║░░░██║░░██║  ██╔══██╗██║░░░██║░░░██║░░██╗██║░░██║██║██║╚████║\033[00m")
print("\033[0;32m       ██████╔╝███████╗╚█████╔╝  ░░░██║░░░╚█████╔╝  ██████╦╝██║░░░██║░░░╚█████╔╝╚█████╔╝██║██║░╚███║\033[00m")
print("\033[0;32m       ╚═════╝░╚══════╝░╚════╝░  ░░░╚═╝░░░░╚════╝░  ╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░░╚════╝░╚═╝╚═╝░░╚══╝\033[00m")
print("                                                  ")
print("                                  wersja testowa v0.1 23.04.2023                                                      ")
print("                                                                                           ")
print("                                                                                           ")
print("                                                                                           ")
print("                                                                                           ")





# Otwieranie pliku cyfry.txt w trybie odczytu
#with open('keys.txt', 'r') as file:
with open('output3.txt', 'r') as file:
    lines = file.readlines()

keys = []
total_lines = len(lines)
current_line = 0

with Bar('Postęp', fill='▒', suffix='%(percent).1f%% - %(eta)ds') as bar:
    for line in lines:
        # Konwertowanie liczby z pliku na klucz adresu Bitcoin
        number = int(line.strip())
        key = Key(number)
        keys.append(key)

        # Aktualizowanie postępu ładowania danych
        current_line += 1
        progress = (current_line / total_lines) * 100
        bar.goto(progress)

# Otwieranie pliku keya.txt w trybie zapisu
with open('adress.txt', 'w') as file:
    for key in keys:
        # Zapisywanie klucza adresu Bitcoin do pliku
        file.write(key.address() + '\n')

print('Konwersja zakończona. Klucze zapisane w pliku keya.txt.')
