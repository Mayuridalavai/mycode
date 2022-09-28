#!/usr/bin/env python3
""" MayuriDalavai """

proto = ["ssh", "http", "https"]
print(proto)
print(proto[1])
proto.extend("dns") # this line will add dns to proto list
print(proto)
