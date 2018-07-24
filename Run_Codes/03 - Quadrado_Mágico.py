entrada = input().split(" ")
dimension = int(entrada[0])
elements = map(lambda x: int(x),entrada[1:])
elements = list(elements)
cubo = []
ind = 0
for row in range(dimension):
    row1 = []
    for col in range(dimension):
        row1.append(elements[ind])
        ind+=1
    cubo.append(row1)
diag_p = 0
diag_s = 0
for row in range(dimension):
    diag_p += cubo[row][row] 
    diag_s += cubo[-row][-row]
end_row = []
for row in range(dimension):
    var = 0
    for col in range(dimension):
        var += cubo[row][col]
    end_row.append(var)
c = 0
end_col = []
for row in range(dimension):
    l = 0
    var = 0
    for j in range(dimension):
        var+=cubo[l][c]
        l+=1
    c+=1
    end_col.append(var)
if end_col == end_row:
    if end_row[0] == diag_p == diag_s:
        print(diag_p)
    else:
        print(-1)
else:
    print(-1)
