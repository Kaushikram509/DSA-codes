def count_digits(n):
    count = 0
    while n>0:
        n = n//10
        count += 1
    return count
def main():
    n = int(input("Enter the value: "))
    print(count_digits(n))
main()
