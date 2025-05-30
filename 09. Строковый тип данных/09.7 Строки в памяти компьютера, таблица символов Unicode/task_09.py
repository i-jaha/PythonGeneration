'''
Самое тяжёлое слово
Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode 
всех символов этого слова. 
Напишите программу, которая принимает 4 слова и 
находит среди них самое тяжёлое слово. 
Если самых тяжёлых слов будет несколько, 
то программа должна вывести первое из них.
'''

# option 1
s1 = input()
s2 = input()
s3 = input()
s4 = input()

count1 = 0
for i in s1:    
    count1 += ord(i)

count2 = 0
for i in s2:    
    count2 += ord(i)

count3 = 0
for i in s3:    
    count3 += ord(i)

count4 = 0
for i in s4:    
    count4 += ord(i)

if count1 >= count2 and count1 >= count3 and count1 >= count4:
    print(s1)
elif count2 >= count1 and count2 >= count3 and count2 >= count4:
    print(s2)
elif count3 >= count1 and count3 >= count2 and count3 >= count4:
    print(s3)
else:
    print(s4)

#option 2
heaviest_word = ''
max_heaviness = 0

for _ in range(4):
    cur_word = input()
    cur_heaviness = 0
    for c in cur_word:
        cur_heaviness += ord(c)
    
    if cur_heaviness > max_heaviness:
        heaviest_word = cur_word
        max_heaviness = cur_heaviness

print(heaviest_word)