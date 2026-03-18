def count_even(n):
    count = 0
    for i in range(0,n+1):
        if(i%2==0):
            count += 1
    return count
def main():
    n = int(input("Enter number: "))
    print(count_even(n))
main()
