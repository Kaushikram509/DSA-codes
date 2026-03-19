def char_count(txt):
    count = 0
    for char in txt:
        count += 1
    return count
def main():
    txt = input("Enter name: ")
    print("character text: ",char_count(txt))
main()
