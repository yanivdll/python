tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidth = [0] * len(table)

    #This for loop defines the width of each column
    for i in range(len(table[0])):
        for x in range(len(table)):
            if len(table[x][i]) > colWidth[x]:
                colWidth[x] = len(table[x][i]) + 2

    for i in range(len(table[0])):
        for x in range(len(table)):
            try:
                print(table[x][i].rjust(colWidth[x]), end='')
            except IndexError: #catch an exception in case not all sub-lists have the same size
                break;
        print()

printTable(tableData)
