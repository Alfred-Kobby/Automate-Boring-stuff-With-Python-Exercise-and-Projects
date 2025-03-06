tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table_data):
    colsWidth = [0] * len(table_data)  # Defne variable to hold a list containing all 0 of the size of the table
    row_len = [0] * len(table_data[0])  # Defne variables to a list containing all 0 of the size of the inner list
    longest_col_width = 0  # Defne variable to hold the longest word
    for i in range(len(colsWidth)):
        for j in range(len(table_data[i])):
            row_len[j] = len(table_data[i])
            if len(table_data[i][j]) > colsWidth[i]:
                colsWidth[i] = len(table_data[i][j])
    for k in range(len(colsWidth)):
        if colsWidth[k] > longest_col_width:
            longest_col_width = colsWidth[k]

    for a in range(len(row_len)):
        for b in range(len(table_data)):
            print(table_data[b][a].rjust(longest_col_width), end=" ")
        print()


printTable(tableData)
