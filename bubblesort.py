correctlist = [1, 2, 8, 12, 12, 15, 17, 20, 21, 24, 36, 48, 56, 69, 95, 120, 250]

def main():
    liste = [
        17,
        2,
        24,
        12,
        1,
        69,
        20,
        250,
        12,
        8,
        56,
        120,
        15,
        21,
        36,
        95,
        48,
    ]

    while (liste != correctlist):
        bsort(liste)
        print(liste)


def bsort(list):
    a = len(list)
    for b in range(a - 1):
        if list[b] > list[b + 1]:
            c = list[b]
            list[b] = list[b + 1]
            list[b + 1] = c

    return list


if __name__ == "__main__":
    main()
