dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2 = {i:val for i,val in dict1.items() if val>2000}

print(dict2)
    