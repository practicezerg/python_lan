from pprint import pprint
# with open("CAM_table.txt", "w") as f:
#     print("done")

"""В этом примере будет разбираться вывод команды sh ip int br. Из вывода команды нам надо получить соответствия имя
интерфейса - IP-адрес. То есть имя интерфейса - это ключ словаря, а IP-адрес - значение. При этом, соответствие надо
делать только для тех интерфейсов, у которых назначен IP-адрес."""

slov = {}
with open("sh_ip_int_br.txt", "r") as f:
    for line in f:
        line_new = line.split()
        if line_new[0] and line_new[1][0].isdigit():
            slov[line_new[0]] = line_new[1]
pprint(slov)


"""
Очень часто вывод команд выглядит таким образом, что ключ и значение находятся в разных строках. И надо придумать каким 
образом обрабатывать вывод, чтобы получить нужное соответствие.
Например, из вывода команды sh ip interface надо получить соответствие имя интерфейса - MTU
(файл sh_ip_interface.txt):
"""
slov = {}
with open("sh_ip_interface.txt", "r") as f:
    for line in f:
        if line.startswith("Ethernet"):
            new_line = line.split()
            slov[new_line[0]] = None
        if line.startswith("  MTU"):
            res = ""
            for i in line:
                if i.isdigit():
                    res+=i
            slov[new_line[0]] = res

pprint(slov)


"""
Если из вывода команды надо получить несколько параметров, очень удобно использовать словарь с вложенным словарем.
Например, из вывода `sh ip interface` надо получить два параметра: IP-адрес и MTU. Для начала, вывод информации:
example 
{'Ethernet0/0': {'ip': '192.168.100.1/24', 'mtu': '1500'}}
"""

slov = {}
with open("sh_ip_interface.txt", "r") as f:
    for line in f:
        if "line protocol" in line:
            interface = line.split()[0]
        elif "Internet address is" in line:
            ip = line.split()[3]
        elif "MTU" in line:
            mtu = line.split()[2]
            slov[interface] = {"ip": ip, "mtu": mtu}
print(slov)


"""Вывод с пустыми значениями
Иногда, в выводе будут попадаться секции с пустыми значениями. Например, в случае с выводом `sh ip interface`, могут 
попадаться интерфейсы, которые выглядят так:
{'Ethernet0/0': {'ip': '192.168.100.2/24', 'mtu': '1500'},
 'Ethernet0/1': {},
 'Ethernet0/2': {},
 'Ethernet0/3': {},
 'Loopback0': {'ip': '2.2.2.2/32', 'mtu': '1514'}}
"""

slov = {}
with open("sh_ip_interface2.txt", "r") as f:
    # for line in f:
    #
    #     if "line protocol" in line:
    #         interface = line.split()[0]
    #     elif "Internet address is" in line:
    #         ip = line.split()[3]
    #     elif "MTU" in line:
    #         mtu = line.split()[2]
    #     elif "Internet protocol processing disabled" in line:
    #         ip, mtu = None,None
    #     if ip and mtu == None:
    #         slov[interface] = {}
    #     else:
    #         slov[interface] = {"ip": ip, "mtu": mtu}
    # print(slov)
    result = {}
    for line in f:
        if 'line protocol' in line:
            interface = line.split()[0]
            result[interface] = {}
        elif 'Internet address' in line:
            ip_address = line.split()[-1]
            result[interface]['ip'] = ip_address
        elif 'MTU' in line:
            mtu = line.split()[-2]
            result[interface]['mtu'] = mtu
print(result)
print("*"*100)

#7.1
#Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде на стандартный поток вывода:
# Prefix                10.0.24.0/24
# AD/Metric             110/41
# Next-Hop              10.0.13.3
# Last update           3d18h
# Outbound Interface    FastEthernet0/0
shablon = f'Prefix '
with open("ospf.txt", "r") as f:
    for line in f:
        new_lines = line.split()
        prefix = new_lines[1]
        metric = new_lines[2].replace("[","").replace("]","")
        next_hop = new_lines[4].replace(",","")
        last_update = new_lines[5].replace(",","")
        interface = new_lines[6]
        print(f'{"Prefix":20} {prefix:15}\n'
              f'{"AD / Metric":20} {metric:15}\n'
              f'{"Next - Hop":20} {next_hop:15}\n'
              f'{"Last update":20} {last_update:15}\n'
              f'{"Outbound Interface":20} {interface:15}\n')
        print("="*100)

#7.3
"""Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка, где есть MAC-адрес, должна быть обработана 
таким образом, чтобы на стандартный поток вывода была выведена таблица вида:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9"""

with open("CAM_table.txt", "r") as f:
    for line in f:
        if "DYNAMIC" in line:
            new_line = line.split()
            vlan = new_line[0]
            mac = new_line[1]
            port = new_line[3]
            print(f'{vlan:10}{mac:20}{port:20}')

print("=" * 100)
print("7.3a")

#7.3a
"Переделать скрипт 7.3: Отсортировать вывод по номеру VLAN В результате должен получиться такой"



res = []
with open("CAM_table.txt", "r") as f:
    for line in f:
        if "DYNAMIC" in line:
            new_line = line.split()
            vlan = new_line[0]
            mac = new_line[1]
            port = new_line[3]
            res.append([int(vlan), port, mac])  # можно через лист - проще сортировать
            slov[port] = [vlan, mac]           # можно через словарь
# res.sort()
# for i in res:
#     print(f'{str(i[0]):10}{i[2]:20}{i[1]:20}')
def for_sort(s):
    # print(s[1][0])
    return int(s[1][0])

# print(slov)
zz = sorted(slov.items(), key=for_sort)
print(zz)
for i in zz:
    print(f'{(i[1][0]):10}{i[1][1]:20}{i[0]:20}')


print("=" * 100)
print("Задание 7.3b")
"""Задание 7.3b
Сделать копию скрипта задания 7.3a.
Переделать скрипт:
Запросить у пользователя ввод номера VLAN.
Выводить информацию только по указанному VLAN.
"""
need_vlan = input("Введите vlan = ")

res = []
with open("CAM_table.txt", "r") as f:
    for line in f:
        if "DYNAMIC" in line:
            new_line = line.split()
            vlan = new_line[0]
            mac = new_line[1]
            port = new_line[3]
            res.append([int(vlan), port, mac])  # можно через лист - проще сортировать
            slov[port] = [vlan, mac]           # можно через словарь
# res.sort()
# for i in res:
#     print(f'{str(i[0]):10}{i[2]:20}{i[1]:20}')
def for_sort(s):
    # print(s[1][0])
    return int(s[1][0])

zz = sorted(slov.items(), key=for_sort)
for i in zz:
    if i[1][0] in need_vlan:
        print(f'{(i[1][0]):10}{i[1][1]:20}{i[0]:20}')

print("=" * 100)
