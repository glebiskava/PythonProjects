
move = int(input("Please input your key (1-13): "))

word = str(input("Please enter the word you want to be encrypted (only lowercase letters): "))

alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

encrypted = ""

for letter in word:
    index_letter = alph.index(letter)
    if move > index_letter:
        encrypted += alph[index_letter + move]
    else: 
        encrypted += alph[index_letter + move]
        
print(encrypted)


