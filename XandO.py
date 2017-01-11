loop=1
line=(['','',''],['','',''],['','',''])
while loop<10:
    print"Player 1 will have X and player 2 will have 'O'."
    row=input("Please enter the row number:")
    column=input("Please enter column number:")
    if loop%2==0:
        line[row-1][column-1]="O"
    else:
        line[row-1][column-1]="X"
    for rows in line:
        print rows,'\n' 
    loop=loop+1