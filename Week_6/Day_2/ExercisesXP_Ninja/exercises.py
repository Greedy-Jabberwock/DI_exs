border = '=======================\n'

#=========================='Exercise 3 : Outputs==========================

print(border + 'Exercise 3 : Outputs\n')

print('''3 <= 3 < 9 -------------------------- true
3 == 3 == 3 ------------------------- true
bool(0) ----------------------------- false
bool(5 == "5") ---------------------- false
bool(4 == 4) == bool("4" == "4") ---- true
bool(bool(None)) -------------------- false\n''')

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x) # true
print("y is", y) # false
print("a:", a) # 5
print("b:", b) # 10

print(border)

#=========================='Exercise 4 : How Many Characters In A Sentence==========================

print(border + 'Exercise 4 : How Many Characters In A Sentence\n')

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(len(my_text))

print(border)

#=========================='Exercise 5: Longest Word Without A Specific Character==========================

print(border + 'Exercise 5: Longest Word Without A Specific Character\n')

longest = ''

while (True):
    userWord = input('Enter the longest word without A; enter "AAA" if you want exit:\n')
    
    if (userWord == 'AAA'):
        break
    
    if ('a' in userWord.lower()):
        continue
    elif (len(longest) < len(userWord)):
        longest = userWord
        print("Congratulation! New longest word without 'A'")


