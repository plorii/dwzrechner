eingegeben = input('Neuer DWZ: ')
try:
    eingegeben = eingegeben.replace(',', '.')
    dwz_neu = float(eingegeben)
except ValueError:
    print('Das ist keine Zahl.')
    exit()

if dwz_neu >= 2110:
    dwz_alt = dwz_neu
elif dwz_neu >= 1400:
    dwz_alt = (dwz_neu - 760) / 0.64
else:
    dwz_alt = dwz_neu - 400

print(f'Alter DWZ: {dwz_alt} ≈ {round(dwz_alt)}')