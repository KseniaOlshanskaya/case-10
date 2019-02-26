from random import randint


def azs_def1(azs):
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

        dict1.update({kolonka: que})  # словарь {номер колонки : длина очереди}

        if n.count("А") == 1:
            oil_type1 = n[n.find("А"):n.find("А") + 5]
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
    return dict1, dict2



def litres_time(litres):
    rand = randint(-1, 1)
    time = litres / 10
    if time % 1 != 0:
        time = int(time) + 1
    time = int(time)
    time += rand
    return time


def car_def(cars):
    cars = cars.read()
    order_list = []
    order = ""
    for i in cars:
        if i != "\n":
            order += i
        else:
            order_list.append(order)  # составили список заказов (автомобилей)
            order = ""
    return order_list


def queue(dict2, oil_type, dict1):
    if type(dict2[oil_type]) == int:
        if dict1[dict2[oil_type]] >= 1:
            dict1[dict2[oil_type]] -= 1
            print(dict1)
        else:
            print('зашквар')
    else:
        srt1 = ''
        for i in dict2[oil_type]:
            srt1 += str(i)
        s = len(srt1) - 1
        l = 0
        d = dict1[(int(srt1[0]))]
        while l < s:
            if dict1[(int(srt1[l]))] <= 0 or dict1[(int(srt1[l]))] <= 0:
                print('пeс')
            elif d > dict1[(int(srt1[l]))] and dict1[(int(srt1[l]))] > 0:
                dict1[(int(srt1[l]))] -= 1
                d = dict1[(int(srt1[l]))]
                print(dict1)
            elif d < dict1[(int(srt1[l]))] and dict1[(int(srt1[l]))] > 0:
                dict1[(int(srt1[l]))] -= 1
                d = dict1[(int(srt1[l]))]
                print(dict1)
            elif d == dict1[(int(srt1[l]))] and dict1[(int(srt1[l]))] > 0:
                dict1[(int(srt1[l]))] -= 1
                d = dict1[(int(srt1[l]))]
                print(dict1)
            elif dict1[(int(srt1[l]))] <= 0 or dict1[(int(srt1[l]))] <= 0:
                print(dict1)
            l += 1


def bistro(time, t):


def main():
    order = ""
    order_list = []
    time_counter = 0
    oil_litres = {'АИ-80': 0, 'АИ-92': 0, 'АИ-95': 0, 'АИ-98': 0}

    with open("azs.txt", "r") as azs:
        s = azs_def1(azs)
        dict1 = s[0]
        dict2 = s[1]
        print("{бензин : номер колонки} -  ", dict2)
        print("{номер колонки: длина очереди} -  ", dict1)

        with open("input.txt", "r") as cars:
            order_list = car_def(cars)
            print("Список машин: ", order_list)
            for i in order_list:
                time = i[0:5]
                litres = int(i[6:8].strip())
                i += " "
                oil_type = i[-6:-1]
                t = litres_time(litres)
                queue(dict2, oil_type, dict1)
                bistro(time, t)




if __name__ == "__main__":
    main()