'''
                                    Початок
                                        |
                                        | 
                                    Запитати:
                            "Якою мовою програмуємо?"
                                        |
                                        |
                    -False------Відповіть == "Python"------TRUE-
                    |                                           |
            Друкувати: "Так?"                           Друкувати: "Звичайно"
                    |                                           |
    Друкувати: "Введена відповідь" +"?"             Друкувати: "Давайте ще програмувати на Python!"
                    |                                           |
    Друкувати: "Я такого не розумію..."                 Друкувати: "Вам подобається?"


'''

lang = input("Якою мовою ми програмуємо? ")
if lang == "Python":
    print("Звичайно!")
    print("Давай ще програмувати на Python!")
    print("Тобі подобається?")
else:
    print("Так?")
    print(lang + "?")
    print("Я такого не розумію...")

