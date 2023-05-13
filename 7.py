from pprint import pprint
# with open("sh_ip_interface2.txt", "w") as f:
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
