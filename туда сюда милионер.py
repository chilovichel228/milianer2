user_name = input("Как тебя звать нагетс?")
print(f"""Добро пожаловать, {user_name}!
Тебе будут заданы 10 вопросов. Каждый вопрос имеет 4 варианта ответа, но только один правильный. Как только ты дашь неправильный ответ, игра закончится. Но есть и приятные бонусы - несгораемые суммы.

После 3 вопроса твой несгораемый выигрыш составит 300000.
После 7 вопроса он увеличится до 700000.
Если же ты ответишь на все вопросы правильно, ты получишь 1000000!!! Желаю удачи!""")

questions = ["""
Тигр это кто
1. Большой дикий котик
2. Зверь типа медведя
3. кин конг проголодался!
4. Кирпич с завода
Ваш ответ: """, 
"""
Солнце это планета?
1. Да
2. Нет
3. Это спутник
4. Джастин Бобик
Ваш ответ: """, 
"""
А марс?
1. Да
2. Нет
3. Это спутник
4. Христос Воскрес
Ваш ответ: """, 
"""
Кто придумал теслу?
1. Никола Тесла
2. Альберт Эйнштейн
3. Илон Маск
4. Артур Пирожков
Ваш ответ: """, 
"""
Сколько лет Путину?
1. 54
2. 68
3. 71
4. 46
Ваш ответ: """, 
"""
Во сколько лет умер Пушкин?
1. 36
2. 28
3. 34
4. 21
Ваш ответ: """, 
"""
Здесь все нормально?
1. Да 
2. Нет
3. Наверное
4. ЫААААААА
Ваш ответ: """, 
"""
Какой это вопрос?
1. 9-ый
2. 6-ой
3. 8-ой
4. 7-ой
Ваш ответ: """, 
"""
Дать подсказку на следующий вопрос?
1. Да
2. Только если будет нужно
3. Нет, это читерство
4. Пэлмэн!
Ваш ответ: """, 
"""
Кто такой кит
1. Человек у которого темература +90.00
2. Млекопетающее синего цвета
3. вода из Англии
4. лайкер
Ваш ответ: """
]

true_answers = ["1", "2", "1", "3", "3", "1", "2", "3", "3", "2"]
your_answers = []

for question in questions:
    answer = input(question)
    your_answers.append(answer)

score = 0
for index in range(10):
    if true_answers[index] == your_answers[index]:
        score += 1
    else:
        print(f"Ты не молодец. Ты ошибся на {index + 1} вопросе")
        break
if score == 10:
    print("Вам дали Million Рублей!")
elif score <10 and score >=7:
    print("Вам дали 700.000  Рублей")
elif score >=3 and score <7:
    print("Вам дали 300.000 Рублей")
else:
    print("вам дали нул рублей")


    
