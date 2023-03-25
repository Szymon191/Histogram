import matplotlib.pyplot as plt

alfabet = {}
for i in 'aąbcćdeęfghijklłmnńoóprsśtuwyźż':
    alfabet[i] = 0

#path = input("podaj sciezke pliku: ")


def plik(fpath):
    global file
    try:
        file = open(fpath, 'r', encoding="utf-8")
    except FileNotFoundError as e:
        print("bledna sciezka pliku", e)
    else:
        print(count(file))
        graph()
    finally:
        file.close()


def count(file):
    for l in file.read():
        for i in alfabet:
            if i == l:
                alfabet[i] += 1

    return alfabet


def graph():
    plt.style.use('bmh')
    group_data = list(count(file).values())
    group_names = list(count(file).keys())

    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)

    plt.show()


plik('list.txt')
