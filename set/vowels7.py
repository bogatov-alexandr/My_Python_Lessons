vovels =set('aeiou')
word = input("Provide a word to search for vowels: ")
found=vovels.intersection(set(word))
for vovels in found:
    print(vovels)

