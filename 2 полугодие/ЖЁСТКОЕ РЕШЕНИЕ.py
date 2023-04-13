#with open ('27_A.txt') as f:
#    n=[x for x in f]
 #   n.pop(0)
  #  sp=[]
  #  for i in n:
    #    sp.append(list(map(int, i.split())))
    #print(sp)
    #for i in sp:
      #  if sp[i][1]%36==0:
        #    sp[i][1]= sp[i][1]//36
        #else: sp[i][1]=(sp[i][1]//36)+1
    #stoim=[]
        

with open('27_B.txt') as f:
            n=[x for x in f]
            n.pop(0)
            sp=[]
            for i in n:
                sp.append(list(map(int, i.split())))
            
            for i in range (len(sp)):
                if sp[i][1]%36==0:
                    sp[i][1] = sp[i][1]//36
                else: sp[i][1]=(sp[i][1]//36)+1
cost_punkt=[]
for i in range (10):
        position0=int(sp[i][0])
        cost=0
        for y in range (len(sp)):
            if round(int(sp[y][1])/36) < int(sp[y][1])/36:
                cost+=abs(int(sp[y][0])-position0) * sp[y][1]
       # print(f'cost={cost}  kont={konteiners}-{int(data[y][1])/36} разница пути пункта={abs(int(data[y][0])-position0)}')
        cost_punkt.append(cost)    
        print(i, cost)
print(f"{min(cost_punkt)} - минимальная стоимость доставки")



#sp='012345678'
#f=int('55055', 9)
#print(f+1) #ура

    



