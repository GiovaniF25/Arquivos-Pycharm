def leiaDinheiro(msg):

    while True:
        a = input(msg).strip()
        if a.isnumeric():
            a = float(a)
            break
        elif '.' in a and a.count('.') == 1:
            b = a.replace('.', '')
            if b.isnumeric():
                a = float(a)
                break
            else:
                print(f'\033[31mERRO! "{a}" é um preço inválido!\033[m')
        elif ',' in a and a.count(',') == 1:
            b = a.replace(',', '')
            if b.isnumeric():
                a = a.replace(',', '.')
                a = float(a)
                break
            else:
                print(f'\033[31mERRO! "{a}" é um preço inválido!\033[m')
        else:
            print(f'\033[31mERRO! "{a}" é um preço inválido!\033[m')
    return a