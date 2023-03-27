#4.1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
res = nat.replace("Fast", "Gigabit")
print(res)

#4.2
mac = "AAAA:BBBB:CCCC"
res = mac.replace(":", ".")
print(res)

#4.3
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result = config.replace("switchport trunk allowed vlan ", "")
result = result.split(",")
print(result, type(result))

#4.4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = []
for i in vlans:
    if i not in result:
        result.append(i)
result.sort()
print(result)

#4.5
result = []
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1 = command1.replace("switchport trunk allowed vlan ","").split(",")
command2 = command2.replace("switchport trunk allowed vlan ","").split(",")
for i in command1:
    if i in command2:
        result.append(i)
print(result)
