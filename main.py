while True:
            meme_dict = {
                        "КРИНЖ": "Что-то очень странное или стыдное",
                        "ЛОЛ": "Что-то очень смешное",
                        "РОФЛ": "шутка",
                        "ЩИЩ": "Одобрение или восторг",
                        "КИПОВЫЙ": "страшный",
                        "АГРИТЬСЯ": "злиться"
                        }
            word = input("Введите непонятное слово (большими буквами!): ")
            if word in meme_dict.keys():
                print(meme_dict.get(word))
            else:
                print("KeyError:Key not found!")
