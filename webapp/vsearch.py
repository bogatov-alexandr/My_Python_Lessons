def search4vowels(phrase: str) -> set:
    """Возвращает булевое значение в зависимости от присутствия любых гласных."""
    vowels = set('aeiou')
    return print(vowels.intersection(set(phrase)))

def search4letters(phrase: str, letters:str='aeiou') -> set:
    """"Возвращает множество букв из "letters", найденных в указанной фразе."""
    return print(set(letters).intersection(set(phrase)))




