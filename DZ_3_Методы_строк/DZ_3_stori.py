story_band = """
Пивет! Меня зовут {name}, и я учусь в группе {group} в Академии "ТОП".\n
Совсем недавно мы завершили JavaScript. Болльше всего мне запомнилась тема {favorite_past_topic}
Сейчас с группой {group} мы переходим к другому стилю разработки.\n\n
От Python я жду прежде всего системности. Хочу {exepetation}.
И однажды с гордостью сказать, что этот проэкт я собрал сам от начала до конца!
"""
name = "Евгений"
group = "Python621"
favorite_past_topic = "работа с DOM, функции"
exepetation = "научиться строить бэкенд на FastAPI и парсеры"

final_story_band = story_band.format(name=name, group=group, 
favorite_past_topic=favorite_past_topic, exepetation=exepetation)
print(final_story_band)