#4.1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
res = nat.replace("Fast", "Gigabit")
print(res, "4.1")

#4.2
mac = "AAAA:BBBB:CCCC"
res = mac.replace(":", ".")
print(res, "4.2")

#4.3
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result = config.replace("switchport trunk allowed vlan ", "")
result = result.split(",")
print(result, type(result), "4.3")

#4.4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = []
for i in vlans:
    if i not in result:
        result.append(i)
result.sort()
print(result, "4.4")

#4.5
result = []
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1 = command1.replace("switchport trunk allowed vlan ","").split(",")
command2 = command2.replace("switchport trunk allowed vlan ","").split(",")
for i in command1:
    if i in command2:
        result.append(i)
print(result, "4.5")

#4.6
l = ["Prefix", "AD/Metric", "Next-Hop", "Last update", "Outbound Interface"]
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
result = ospf_route.replace("       ", "")
res = result.split(" ")
res_final = f'{l[0]:20}\t{res[0]:20}\n{l[1]:20}\t{res[1].strip("[]"):10}\n{l[2]:20}\t{res[3].replace(",","")}\n{l[3]:20}\t{res[4].replace(",","")}\n{l[4]:20}\t{res[5]:20}'
print(res_final, "\n4.6")

#4.7

mac = "AAAA:BBBB:CCCC"
res = ""
for i in mac:
    step1 = ord(i)
    step2 = format(step1, "08b")
    res = res + step2
print(res)

#4.8
ip = "192.168.3.1"
ip_split = ip.split(".")
teamplate = """
IP address:
{0:10}  {1:10}  {2:10}  {3:10}
{0:010b}  {1:010b}  {2:010b}  {3:010b}
"""
print(type(ip_split[0]))
print(teamplate.format(int(ip_split[0]), int(ip_split[1]), int(ip_split[2]), int(ip_split[3])))

