from random import randint


def litres_time(litres):
    rand = randint(-1, 1)
    time = litres / 10
    if time % 1 != 0:
        time = int(time) + 1
    time = int(time)
    time += rand
    return time


def main():
    order = ""
    order_list = []
    time_counter = 0
    oil_litres = {'АИ-80': 0, 'АИ-92': 0, 'АИ-95': 0, 'АИ-98': 0}
    queue = {}

    with open("azs.txt", "r") as azs:
        azs = azs.readlines()
        counter = 0
        oil_type1 = ""
        dict1 = {}
        dict2 = {}
        for n in azs:
            for i in n:
                if i.isdigit() and counter == 0:
                    kolonka = int(i)
                    counter += 1
                elif i.isdigit() and counter == 1:
                    que = int(i)
                    counter += 1
                elif i == " " or i == "\n":
                    pass
            counter = 0

            dict1.update({kolonka:que})  # словарь {номер колонки : длина очереди}

            if n.count("А") == 1:
                oil_type1 = n[n.find("А"):n.find("А")+5]
                if oil_type1 in dict2:
                    list_ = list()
                    list_.append(dict2.get(oil_type1))
                    list_.append(kolonka)
                    dict2.update({oil_type1: list_})
                else:
                    dict2.update({oil_type1: kolonka})
                oil_type1 = ""
            else:
                s = n.count("А")
                for d in range(s):
                    oil_type1 = n[n.find("А"):n.find("А") + 5]
                    if oil_type1 in dict2:
                        list_ = list()
                        list_.append(dict2.get(oil_type1))
                        list_.append(kolonka)
                        dict2.update({oil_type1: list_})
                    else:
                        dict2.update({oil_type1: kolonka})
                    oil_type1 = ""
                    n = n[n.find("А") + 5:]
        print("{бензин : номер колонки} -  ", dict2)
        print("{номер колонки: длина очереди} -  ", dict1)


        with open("input.txt", "r") as cars:
            cars = cars.read()
            for i in cars:
                if i != "\n":
                    order += i
                else:
                    order_list.append(order)  # составили список заказов (автомобилей)
                    order = ""
            print("Список машин: ", order_list)

            for i in order_list:
                time = i[0:5]
                litres = int(i[6:8].strip())
                i += " "
                oil_type = i[-6:-1]
                litres_time(litres)
















if __name__ == "__main__":
    main()