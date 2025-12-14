import sys

def readlinia(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for linia in f:
            yield linia.strip()

def filterlogs(gen, poziom):
    for linia in gen:
        if poziom in linia:
            yield linia

def licz_stat(gen):
    stat = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for linia in gen:
        for key in stat:
            if key in linia:
                stat[key] += 1
    yield stat

def main():
    print("czytam")
    gen = readlinia("test.txt")
    for i in range(15):
        print(next(gen))

    print("\nfiltruję")
    gen = readlinia("test.txt")
    gen_err = filterlogs(gen, "ERROR")
    for linia in gen_err:
        print(linia)

    print("\nstatystyka: ")
    gen = readlinia("test.txt")
    stat = next(licz_stat(gen))
    print(stat)

    linie = [linia.strip() for linia in open("test.txt")]
    print("\nlista: ", sys.getsizeof(linie))

    gen = readlinia("test.txt")
    print("generator: ", sys.getsizeof(gen))

if __name__ == "__main__":
    main()