def search4letters(phrase: str, letters:str='aeiou') -> set:
    """"Возвращает множество букв из "letters", найденных в указанной фразе."""
    return print(set(letters).intersection(set(phrase)))

search4letters(letters='fdc',phrase='cfrankfurt')