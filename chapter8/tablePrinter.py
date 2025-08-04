tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]



def printTable(table):
    colWidths = [0] * len(table)
    

    for sublist in (tableData):
        max_length= len(sublist[0])
        i =1 
        for i in range(len(sublist)):
            if len(sublist[i]) > max_length:
                max_length = len(sublist[i])
        
        index = tableData.index(sublist)
        colWidths[index] = max_length

    for i in range(len(tableData[1])):
        for sublist in tableData:
            index = tableData.index(sublist)
            print(sublist[i].rjust(colWidths[index]),end= ' ')
        print() 
    
        
    
    


printTable(tableData)


