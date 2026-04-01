def rev_txt(text):
    reverse_txt = ""
    for char in text:
        reverse_txt = char + reverse_txt
    return reverse_txt
text = input("Enter the text: ")
print("Enter the reversed text: ",rev_txt(text))
