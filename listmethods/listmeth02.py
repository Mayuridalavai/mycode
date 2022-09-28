#!/usr/bin/env python3
""" Alta3 Research | MayuriDalavai
list Methods"""

proto = ["ssh", "http", "https"]
protoa =["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [22, 80, 443, 53] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

proto.reverse()
print(proto
        )
proto2.sort()
print(proto2
        )
protoa.pop(0)
print(protoa)

proto.remove("http")
print(proto)
