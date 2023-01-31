vowels = ['a', 'e', 'i', 'o', 'u', 'y']

x = input('please write a sentence:').lower().strip()
score = 0


for vowels in vowels:
    score += x.count(vowels)


print(score)
