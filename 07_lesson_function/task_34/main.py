#
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
#  если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке


def count_vowel_letters(phrase: str) -> int:
    alpha_count = 0
    for ch in phrase.lower():
        if ch in 'аеёиоуыэюя':
            alpha_count += 1

    return alpha_count


if __name__ == '__main__':
    pux_say = input("Pux say: ")
    pux_say_phrase = pux_say.split()
    
    if len(set(map(count_vowel_letters, pux_say_phrase))) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")
