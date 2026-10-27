import sys
import time

if len(sys.argv) < 2:
    print("podaj argument w terminalu")
    sys.exit(1)
    
filename = sys.argv[1]
counter = 0

print("skrypt dziala")

f = open(filename, "a")
while True:
    f.write(f"Linia numer {counter}\n")
    f.flush()
    time.sleep(1)
    counter += 1
    
    #/usr/local/bin/python3 /Users/marceladamski/python/zadanie2.py testowy_plik.txt