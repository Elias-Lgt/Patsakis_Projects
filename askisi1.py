import random
dimension=int(input("Give dimension for the square(greater than 3):"))
'''square=[]
for i in range(dimension):
    square.append([])
for column in square:
    for j in range(dimension):
        column.append(0)'''
sum=0
for k in range(100):
    square=[]
    for i in range(dimension):
        square.append([])
    for column in square:
        for j in range(dimension):
            column.append(0)                  #square creation
    l=0
    while l<(round(dimension*dimension/2)):
        p=random.randint(0,dimension-1)
        o=random.randint(0,dimension-1)
        if square[p][o]==0:
            square[p].insert(o,1)
            del square[p][o+1]
            l=l+1                              #putting 1s
    '''for d in range(dimension):
        try:
            if d==0 :
                if square[d].index(1)==0:
                    square[d].index(1)
                elif square[d].index(1)>0 and square[d].index(1)<dimension-1:

                elif square[d].index(1)==dimension-1:

        except:
            continue'''
    '''thesis=[];
    for a in range(dimension):
        if square[a].count(1)>0:
            ArxikosArithmosAson=square[a].count(1)
            for q in range(ArxikosArithmosAson):
                thesis.append(str(a) + str(square[a].index(1)))
                square[a].insert(square[a].index(1),0)
                square[a].remove(1)
        else:
            continue                            #filling thesis with 1s position and deleting 1s from square'''
    No4=0
    for column in range(dimension):
        for elem in range(dimension):
                if square[column][elem]==1:
                        if column<=dimension-4 and square[column+1][elem]==1 and square[column+2][elem]==1 and square[column+3][elem]==1:
                                No4=No4+1
                                #print(str(column)+','+str(elem)+ 'orizontia' +'\n' )
                        if column<=dimension-4 and elem<=dimension-4 and  square[column+1][elem+1]==1 and square[column+2][elem+2]==1 and square[column+3][elem+3]==1:
                                No4=No4+1
                                #print(str(column)+','+str(elem)+ 'diagonia katw dexia' + '\n' )
                        if elem<=dimension-4 and square[column][elem+1]==1 and square[column][elem+2]==1 and square[column][elem+3]==1:
                                No4=No4+1
                                #print(str(column)+','+str(elem)+ 'katheta' +'\n' )
                        if column<=dimension-4 and elem>=dimension-4 and  square[column+1][elem-1]==1 and square[column+2][elem-2]==1 and square[column+3][elem-3]==1:
                                No4=No4+1
                                #print(str(column)+','+str(elem)+ 'diagonia panw dexia' +'\n' )
                else:
                        continue                                                  #metraei poses 4ades exei o pinakas square

    sum=sum+No4
print('o mesos oros twn tetradwn einai: '+ str(sum/100))
