vowels = ['a', 'e', 'i', 'o', 'u']
maybe_vowel = ['y']
point = 0
choice = input('Would you like to count duplicate vowels? Y/N: ').upper().strip()

if choice == 'Y':
    x = input('please write a sentence: ').lower().strip()
    for stri in vowels:
        point += x.count(stri)
    if point == 0:
        for char in x:
            if char in maybe_vowel:
                print('This sentence/word uses \'y\' as it\'s vowel')
                break
    else:
        point = str(point)
        print ('\n' + point)
        
        
elif choice == 'N':
    x = input('Please enter your sentence: ').lower()
    for stri in vowels:
        if stri in x:
            point += 1
    if point == 0:
        for char in x:
            if char == 'y':
                print('This sentence/word uses \'y\' as it\'s vowel')
    else:
        point = str(point)
        print ('\n' + point)

else:
    print('Please input valid entry')








