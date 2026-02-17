import math
klockan = 8
hopp = 6
dygn = 0
print (f"startar klockan {klockan}:00")
for i in range(1,5):
    gammal_tid = klockan
    dygn = math.floor((klockan + hopp)/24) + dygn
    klockan = (klockan + hopp)%24
    print(f"Resa {i}: Från {gammal_tid}:00 till {klockan}:00. Det har gått {dygn} sedan start tid")