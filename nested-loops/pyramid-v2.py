def pyramid_row_logic(k, rowNum):
    ##### -> logic to print one row

    # print each row spaces
    for i in range(0, k):
        print(end=" ")
    # print each row stars
    for j in range(0, rowNum + 1):
        print(end="* ")


###################### out put -> --------*
n = 5

# k represent the number of spaces for each row
k = n * 2 - 2
for i in range(0, n):
    pyramid_row_logic(k, i)

    # decrement spaces counter and increment star counter
    k = k - 1
    print("\r")
