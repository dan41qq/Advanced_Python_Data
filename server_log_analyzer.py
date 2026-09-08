logs = str(input())
codes = logs.split()
udacha = int()
dlina = int(len(codes))
for i in range(dlina):
    if codes[i] == "200" or codes[i] == "301" :
        udacha = udacha+1
    elif codes[i] == "404":
        print("oshibka404")
        continue
    elif codes[i] == "500":
        print("krit sboi")
        break
print("udachno", udacha)
