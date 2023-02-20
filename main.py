vowels = ['a', 'e', 'i', 'o', 'u']
point = 0
y = input('Would you like to count duplicate vowels? Y/N: ').upper().strip()

if y == 'Y':
    x = input('please write a sentence:').lower().strip()
    for vowel in vowels:
        point += x.count(vowel)

    print(point)

elif y == 'N':
    
    x = input('Please enter your sentence: ').lower()
    for vowel in vowels:
        if vowel in x:
            point += 1 


    print(point)
    
else: 
    print('Please input valid entry')
    
