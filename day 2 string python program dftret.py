print("Enter String: ", end="")
text = input()
print("Enter a Word to Delete: ", end="")
word = input()

wordlist = text.split()
newtext = [x for x in wordlist if x not in word]

print("\nNew String is:")
for x in newtext:
    print(x, end=" ")
print()
