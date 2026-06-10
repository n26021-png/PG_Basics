a = ["テニス","バスケ","バレー","サッカー","野球"]
b =  ["テニス","バスケ","バレー","ゴルフ","野球"]
diff = []

for item in a:
    if item not in b:
        diff.append(item)
print(a,b)
print(diff)
