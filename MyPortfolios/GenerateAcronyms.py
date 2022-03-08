# Generate acronyms the phrase which entering

user_input = str(input("Please enter a phrase= "))  # Entering a phrase
text = user_input.split()
a = " "

for i in text:
    a = a + str(i[0]).upper()
print(a)
