'''
Угадайка слов
Описание проекта: 
программа загадывает слово, а пользователь должен его угадать. 
Изначально все буквы слова неизвестны. 
Также рисуется виселица с петлей. 
Пользователь предлагает букву, которая может входить в это слово. 
Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове. 
Если такой буквы нет, к виселице добавляется круг в петле, изображающий голову. 
Пользователь продолжает отгадывать буквы до тех пор, пока не отгадает всё слово. 
За каждую неудачную попытку добавляется еще одна часть туловища висельника 
(обычно их 6: голова, туловище, 2 руки и 2 ноги).

Составляющие проекта:
    Целые числа (тип int);
    Переменные;
    Ввод / вывод данных (функции input() и print());
    Условный оператор (if/elif/else);
    Цикл while;
    Бесконечный цикл;
    Операторы break, continue;
    Создание пользовательских функций;
    Списочные выражения;
    Работа с модулем random для генерации случайных чисел.

Примечание 1. 
На английском игра называется Hangman.

Примечание 2. 
Почитать подробнее об игре можно (тут)[https://en.wikipedia.org/wiki/Hangman_(game)]. 

Заголовок программы
Подключите модуль random;
Создайте глобальный список word_list, содержащий слова, которые будут использоваться в игре.

Функция, возвращающая случайное слово
Напишите функцию get_word(), которая возвращает случайное слово из списка word_list в верхнем регистре.

Функция, возвращающая текущее состояние
Функция display_hangman() принимает один аргумент tries – количество попыток угадывания слова – 
и возвращает текущее состояние игры в графическом виде:
    значение tries = 6 соответствует начальному положению, пустая виселица;
    ...
    значение tries = 0 соответствует конечному положению, то есть проигрышу и полностью нарисованному телу повешенного.
Примечание. 
Для вывода символа бэкслеша \\ используется экранирование символа с помощью \\, то есть комбинация \\\\.

Функция play()
Напишите функцию play(), в которой будет осуществляться основная логика игры. 
Функция play() принимает в качестве аргумента слово word, сгенерированное функцией  get_word().
    def play(word):
        # тело функции
Используйте следующие локальные переменные:
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
Функция play() в самом начале должна:
    отобразить текст 'Давайте играть в угадайку слов!';
    отобразить текущее состояние игры, распечатав результат вызова функции display_hangman() 
    с начальным количеством допустимых промахов tries = 6;
    отобразить начальное слово word_completion в виде строки с символом _ на каждую букву задуманного слова;
Необходимо обрабатывать ввод букв или слова целиком. 
Предусмотрите защиту от дурака, на случай если пользователь ввел символ, не являющийся буквой;
Если пользователь вводит уже названную букву или слово, то необходимо ему об этом сообщить, 
и не засчитывать попытку;
Если пользователь угадал букву, то требуется заменить все символы _ соответствующие этой букве;
Если пользователь угадал слово целиком, 
то следует его поздравить и вывести текст 'Поздравляем, вы угадали слово! Вы победили!';
Если пользователь исчерпал все свои попытки 
и не угадал слово, следует вывести загаданное слово.
Примечание. 
Переводите все символы в верхний регистр.

Основной цикл программы
Организуйте цикл, который будет содержать: 
генерацию случайного слова с помощью функции get_word(), 
а затем последующий вызов функции play().
Организуйте повторный запуск игры, 
если пользователь пожелает играть еще раз.

Улучшения проекта
Можно отображать первую и последнюю букву слова;
Слова можно выделить в категории и давать подсказку пользователю;
Существует также вариант игры с 8 частями — добавляются ступни, 
а также самый длинный вариант, когда сначала за не отгаданную букву рисуются части самой виселицы.
'''

import random

word_list = []

def get_words():
    while True:
        try:
            count = int(input('How many words do you want to enter? '))
            break
        except ValueError:
            print('Please enter a integer!')
    
    for i in range(count):
        word = input(f'Enter word {i+1}: ').strip().upper()
        if word and word not in word_list:
            word_list.append(word)
    print(f'{len(word_list)} words have been added to the game!')

def get_word():
    if not word_list:
        return None
    word = random.choice(word_list)
    word_list.remove(word)
    return word

def display_hangman(tries, extended=False):
    if extended:
        stages = [
            """
        -----
        |   |
        |   💀
        |  /|\\
        |  / \\
        |  |_|
        =========
        """,
            """
        -----
        |   |
        |   😵‍💫
        |  /|\\
        |  / \\
        |
        =========
        """,
            """
        -----
        |   |
        |   🤯
        |  /|\\
        |  /
        |
        =========
        """,
            """
        -----
        |   |
        |   😱
        |  /|\\
        |
        |
        =========
        """,
            """
        -----
        |   |
        |   😭
        |  /|
        |
        |
        =========
        """,
            """
        -----
        |   |
        |   😵
        |   |
        |
        |
        =========
        """,
            """
        -----
        |   |
        |   😐
        |
        |
        |
        =========
        """,
            """
        -----
        |   |
        |
        |
        |
        |
        =========
        """
        ]
    else:
        stages = [
            """
        -----
        |   |
        |   💀
        |  /|\\
        |  / \\
        |
        =========
        """,
            """
        -----
        |   |
        |   🤯
        |  /|\\
        |  /
        |
        =========
        """,
            """
        -----
        |   |
        |   😱
        |  /|\\
        |
        |
        =========
        """,
            """
        -----
        |   |
        |   😭
        |  /|
        |
        |
        =========
        """,
            """
        -----
        |   |
        |   😵
        |   |
        |
        |
        =========
        """,
            """
        -----
        |   |
        |   😐
        |
        |
        |
        =========
        """,
            """
        -----
        |   |
        |
        |
        |
        |
        =========
        """
        ]
    print(stages[tries])

def play(word):
    mode = input('Choose a mode (1 - normal, 2 - with hints, 3 - advanced): ')
    
    show_hints = mode == '2'
    extended_mode = mode == '3'
    tries = 7 if extended_mode else 6
    
    if show_hints and len(word) > 2:
        word_completion = word[0] + '_' * (len(word) - 2) + word[-1]
        guessed_letters = [word[0], word[-1]]
    else:
        word_completion = '_' * len(word)
        guessed_letters = []
    
    guessed = False
    guessed_words = []
    
    print("Let's play a word guessing game!")
    display_hangman(tries, extended_mode)
    print(word_completion)
    
    while not guessed and tries > 0:
        guess = input('Enter a letter or word: ').upper()
        
        if not guess.isalpha():
            print('Please enter letters only!')
            continue
            
        if len(guess) == 1:
            if guess in guessed_letters:
                print('You have already guessed this letter!')
                continue
            guessed_letters.append(guess)
            
            if guess in word:
                word_completion = ''.join([letter if letter in guessed_letters else '_' for letter in word])
                if '_' not in word_completion:
                    guessed = True
            else:
                tries -= 1
        else:
            if guess in guessed_words:
                print('You have already guessed this word!')
                continue
            guessed_words.append(guess)
            
            if guess == word:
                guessed = True
                word_completion = word
            else:
                tries -= 1
        
        if not guessed:
            display_hangman(tries, extended_mode)
            print(word_completion)
    
    if guessed:
        print('''
        🎉 VICTORY! 🎉
        
           😄
          /|\\  
          / \\  
        =========
        ''')
        print("Congratulations, you guessed the word! You won!")
    else:
        print(f"You lost! The hidden word was: {word}")

def main():
    get_words()
    
    while True:
        word = get_word()
        print(f'\nWords left: {len(word_list)}')
        play(word)
        
        continue_game = input('\nContinue the game? (yes/no): ').lower()
        if continue_game not in ['да', 'д', 'yes', 'y']:
            break
            
        if not word_list:
            new_game = input('\nThe words have run out! Would you like to start a new game? (yes/no): ').lower()
            if new_game in ['да', 'д', 'yes', 'y']:
                get_words()
            else:
                break
    
    print('Thank you for playing!')

if __name__ == "__main__":
    main()