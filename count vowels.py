def count_vowels(txt):
    count = 0
    vowels = "aeiou"
    for ch in txt:
        if ch in vowels:
            count += 1
    return count
def main():
    txt = input("Enter the name: ")
    print("The vowels are: ",count_vowels(txt))
main()
