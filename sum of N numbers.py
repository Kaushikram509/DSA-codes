def sum_numbers(n):
    sum = 0
    for i in range(0, n+1):
        sum += i
    return sum

def main():
    n = int(input("Enter the number: "))
    res = sum_numbers(n)
    print("sum:",res)

if __name__ == "__main__":
    main()
