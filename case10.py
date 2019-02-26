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
    time += rand
    if time % 1 != 0:
        time = int(time) + 1
    time = int(time)
    if time == 0:
        time += 1
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


def queue(dict2, oil_type, dict1, m, dict3, j):
    if type(dict2[oil_type]) == int:
        if dict1[dict2[oil_type]] >= 1:
            dict1[dict2[oil_type]] -= 1
            p = dict2[oil_type]
            print(dict1)
        else:
            print('зашквар')
            p = 0
    else:
        srt1 = ''
        for i in dict2[oil_type]:
            srt1 += str(i)
        s = len(srt1) - 1
        l = 0
        d = dict1[(int(srt1[0]))]
        while l < s:
            if dict1[(int(srt1[l]))] <= 0:
                p = 0
                print('пeс')
            elif d > dict1[(int(srt1[l]))] and dict1[(int(srt1[l]))] > 0:
                dict1[(int(srt1[l]))] -= 1
                d = dict1[(int(srt1[l]))]
                p = int(srt1[l])
                print(dict1)
            elif d < dict1[(int(srt1[l]))] and dict1[(int(srt1[l]))] > 0:
                dict1[(int(srt1[l]))] -= 1
                d = dict1[(int(srt1[l]))]
                p = int(srt1[l])
                print(dict1)
            elif d == dict1[(int(srt1[l]))] and dict1[(int(srt1[l]))] > 0:
                dict1[(int(srt1[l]))] -= 1
                d = dict1[(int(srt1[l]))]
                p = int(srt1[l])
                print(dict1)
            l += 1
    if p != 0:
        dict3.update({p: m})
        print('jgbhjn', dict3)



def hours(time, t):
    if time[:1] == '0':
        h = int(time[1:2])
    else:
        h = int(time[:2])
    if time[3:4] == '0':
        m = int(time[4:])
    else:
        m = int(time[3:])
    m += t
    if m >= 60:
        m -= 60
        h += 1
    h = str(h)
    m = str(m)
    if len(h) == 1:
        h += '0'
        h = h[::-1]
    else:
        pass
    if len(m) == 1:
        m += '0'
        m = m[::-1]
    else:
        pass
    g = ''
    g += h
    g += ':'
    g+= m
    return g
def minutes(time, t):
    if time[:1] == '0':
        h = int(time[1:2])
    else:
        h = int(time[:2])
    if time[3:4] == '0':
        m = int(time[4:])
    else:
        m = int(time[3:])
    m += t
    h *= 60
    m += h
    return m


def gigi(time, t):
    if time[:1] == '0':
        h = int(time[1:2])
    else:
        h = int(time[:2])
    if time[3:4] == '0':
        m = int(time[4:])
    else:
        m = int(time[3:])
    l = h * 60 + m
    return l

def main():
    order = ""
    order_list = []
    time_counter = 0
    oil_litres = {'АИ-80': 0, 'АИ-92': 0, 'АИ-95': 0, 'АИ-98': 0}
    dict3 = {}

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
                h = hours(time, t)
                m = minutes(time, t)
                j = gigi(time, t)
                queue(dict2, oil_type, dict1, m, dict3, j)
                oil_litres[oil_type] += litres





if __name__ == "__main__":
    main()