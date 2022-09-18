rodas = 4
peso = 7000
pessoas = 4

if 1 < rodas < 4:
    print('tipo A')
else:
    if rodas == 4 and pessoas <= 8 and peso < 3500:
        print('tipo B')
    elif 3500 <= peso <= 6000:
        print('tipo C')
    elif pessoas >= 8:
        print('tipo D')
    elif peso >= 6000:
        print('tipo E')

