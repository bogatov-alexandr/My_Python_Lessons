def search4vowels(phrase: str) -> set:
    """Возвращает булевое значение в зависимости от присутствия любых гласных."""
    vowels = set('aeiou')
    return print(vowels.intersection(set(phrase)))


search4vowels('hitch-hiker')
search4vowels('galaxy')
search4vowels('sky')
