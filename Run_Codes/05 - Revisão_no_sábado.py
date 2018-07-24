entrada = input().split(" ")
meses = {"JAN":31,"FEV":28,"MAR":31,"ABR":30,"MAI":31,"JUN":30,"JUL":31,"AGO":31,"SET":30,"OUT":31,"NOV":30,"DEZ":31}
nome_mes = {1:"JAN",2:"FEV",3:"MAR",4:"ABR",5:"MAI",6:"JUN",7:"JUL",8:"AGO",9:"SET",10:"OUT",11:"NOV",12:"DEZ"}
num_mes = {"JAN":1,"FEV":2,"MAR":3,"ABR":4,"MAI":5,"JUN":6,"JUL":7,"AGO":8,"SET":9,"OUT":10,"NOV":11,"DEZ":12}
dic = {1:"SEG",2:"TER",3:"QUA",4:"QUI",5:"SEX",6:"SAB",7:"DOM"}
dic1 = {"SEG":1,"TER":2,"QUA":3,"QUI":4,"SEX":5,"SAB":6,"DOM":7}
ind1,ind2,x = 0,3,0
saida = ''
while x < len(entrada)/3:
    qtd_sab = 0
    caso = entrada[ind1:ind2]
    var = dic1[caso[1]]
    lista = []
    mes_num = num_mes[caso[0]]
    mes = meses[nome_mes[mes_num]]
    for i in range(int(caso[-1])):
        lista = []
        if mes_num == 13:
            mes_num = 1
        mes = meses[nome_mes[mes_num]]            
        for j in range(mes):
            lista.append(dic[var])
            var+=1
            if var == 8:
                var = 1
        mes_num+=1
        qtd_sab += lista.count("SAB")
    numero_mes = num_mes[caso[0]]
    y = 1
    lista1 = []
    saida+=str(qtd_sab)+' '
    ind1+=3
    ind2+=3
    x+=1
saida = " ".join(saida.split())
print(saida)
