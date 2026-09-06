# After receiving a number, the program prints the number's table.

n=int(input("Enter the number to print the table for:"))
for i in range(1,11):
    print(n,"x" ,i,"=" ,n*i)
    