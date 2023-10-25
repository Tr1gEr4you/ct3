import random

word_list = [
    {"word": "олень", "description": "Животное с рогами, обитающее в лесах и степях"},
    {"word": "слон", "description": "Крупное животное с длинным хоботом"},
    {"word": "жираф", "description": "Высокое животное с длинной шеей"},
    {"word": "кенгуру", "description": "Животное, которое прыгает на двух ногах"},
    {"word": "тигр", "description": "Хищное животное с полосатой шерстью"},
    {"word": "леопард", "description": "Хищное животное с пятнистой шерстью"},
    {"word": "зебра", "description": "Животное с черно-белой полосатой шерстью"}
]

def get_word_and_description():
    word_info = random.choice(word_list)
    return word_info["word"], word_info["description"]

def create_table(word):
    return ["\u25A0" for _ in word]

def get_lives(word):
    return len(word)

def is_alive(lives):
    return lives > 0

def show_table(table, description):
    display = " ".join(table)
    print(display)
    print(description)

def get_player_input():
    return input("Угадайте букву или введите слово целиком: ").lower()

def is_word_correct(word, answer):
    return word == answer

def is_letter_correct(word, letter):
    return letter in word

def update_table(word, table, letter):
    for i, char in enumerate(word):
        if char == letter:
            table[i] = letter

def play_hangman():
    while word_list:
        word, description = get_word_and_description()
        table = create_table(word)
        lives = get_lives(word)
        
        print("Добро пожаловать в игру 'Виселица на поле чудес'!")
        print("У вас есть", lives, "жизней.")
        
        while is_alive(lives):
            show_table(table, description)
            answer = get_player_input()
            
            if len(answer) == 1:
                if is_letter_correct(word, answer):
                    print("Правильно! Буква", answer, "находится в слове.")
                    update_table(word, table, answer)
                    if "".join(table) == word:
                        print("Поздравляем! Вы угадали слово:", word)
                        break
                else:
                    print("Неправильно! Буквы", answer, "нет в слове.")
                    lives -= 1
            elif is_word_correct(word, answer):
                print("Поздравляем! Вы угадали слово:", word)
                break
            else:
                print("Неправильный ввод. Пожалуйста, введите одну букву или слово целиком.")
        
        if lives == 0:
            print("Игра окончена. Загаданное слово было:", word)
        
        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != "да":
            break
        
        word_list.remove({"word": word, "description": description})
    
    print("Спасибо за игру!")