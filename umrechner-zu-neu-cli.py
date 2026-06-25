eingegeben = input('Alter DWZ: ')
try:
    eingegeben = eingegeben.replace(',', '.')
    dwz_alt = float(eingegeben)
except ValueError:
    print('Das ist keine Zahl du Sack')
    exit()

if dwz_alt < 1000:
    dwz_neu = dwz_alt + 400
elif 1000 <= dwz_alt < 2110:
    dwz_neu = 0.64 * dwz_alt + 760
else:
    dwz_neu = dwz_alt

print(f'Neuer DWZ: {dwz_neu} ≈ {round(dwz_neu)}')