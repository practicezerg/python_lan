"""Функция"""
#9.1
print("9.1","="*100)
"""Создать функцию generate_access_config, которая генерирует конфигурацию
для access-портов."""

def generate_access_config(slov, access_mode_template, psecurity = None):
    l = []
    for port, vlan in slov.items():
        l.append(f"interface {port}")
        for command in access_mode_template:
            if "switchport access vlan" in command:
                l.append(f'{command} {vlan}')
            else:
                l.append(command)
        if psecurity:
            l.extend(psecurity)
    return l

slov = {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/16': 17}

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

l = generate_access_config(slov, access_mode_template)
print(*l, sep="\n")


#9.1a
print("9.1a","="*100)
"""Создать функцию generate_access_config, которая генерирует конфигурацию
для access-портов."""

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]

l = generate_access_config(slov, access_mode_template, port_security_template)
print(*l, sep="\n")

#9.2
print("9.2","="*100)
"""Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов."""

intf_vlan_mapping = {
    "FastEthernet0/1": [10, 20],
     "FastEthernet0/2": [11, 30],
     "FastEthernet0/4": [17]}
trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"]

def swich_trunk(intf_vlan_mapping, trunk_mode_template):
    res = []
    for port, vlan in intf_vlan_mapping.items():
        res.append(f'interface {port}')
        for command in trunk_mode_template:
            if "switchport trunk allowed vlan" in command:
                vlan = ",".join([str(x) for x in vlan])
                res.append(f'{command} {vlan}')
            else:
                res.append(command)
    return res



res = swich_trunk(intf_vlan_mapping, trunk_mode_template)
print(res)

#9.2a
print("9.2a","="*100)
"""Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов. Финальный результат
Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида «FastEthernet0/1»
- значения: список команд, который надо выполнить на этом интерфейсе"""

def swich_trunk(intf_vlan_mapping, trunk_mode_template):
    res = {}
    for port, vlan in intf_vlan_mapping.items():
        res[f'interface {port}'] = []
        for command in trunk_mode_template:
            if "switchport trunk allowed vlan" in command:
                vlan = ",".join([str(x) for x in vlan])
                res[f'interface {port}'].append(f'{command} {vlan}')
            else:
                res[f'interface {port}'].append(command)
    return res


res = swich_trunk(intf_vlan_mapping, trunk_mode_template)
print(res)

#9.3
print("9.3","="*100)
"""Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла."""

def get_int_vlan_map(config_filename):
    res = ()
    trunk, access = {}, {}
    with open(config_filename, "r") as f:
        for line in f:
            if "interface FastEthernet" in line:
                intf = line.split()[1]
            if "switchport access" in line:
                access[intf] = int(line.split()[-1])
            elif "switchport trunk allowed" in line:
                trunk[intf] = [int(num) for num in line.split()[-1].split(",")]
    return  (trunk, access)
config_filename = "config_sw1.txt"
res = get_int_vlan_map(config_filename)
print(res)

#9.3a
print("9.3a","="*100)
"""Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла."""
def get_int_vlan_map2(config_filename):
    res = ()
    trunk, access = {}, {}
    with open(config_filename, "r") as f:
        for line in f:
            if "interface FastEthernet" in line:
                intf = line.split()[1]
            if "switchport mode access" in line:
                access[intf] = 1
            elif "switchport access" in line:
                access[intf] = int(line.split()[-1])

            elif "switchport trunk allowed" in line:
                trunk[intf] = [int(num) for num in line.split()[-1].split(",")]
    return (trunk, access)


config_filename = "config_sw2.txt"
res = get_int_vlan_map2(config_filename)
print(res)

#9.4
print("9.4","="*100)
"""Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении
  у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command."""
def ignore_command(line):
    ignore = ["duplex", "alias", "configuration"]
    for word in ignore:
        if word in line:
            return False
    return True

def convert_config_to_dict(config_filename):
    res = {}
    with open(config_filename, "r") as f:
        for line in f:
            if not line[0] == "!":
                if ignore_command(line):
                    if line[0].isalpha():
                        kly4 = line.rstrip()
                        res[kly4] = []
                    if line[0] == " ":
                        res[kly4].append(line.rstrip())
    return res

config_filename = "config_sw1.txt"
res = convert_config_to_dict(config_filename)
print(res)