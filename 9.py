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