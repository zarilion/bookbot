def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    characters = {}
    for char in text:
        lowered = char.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def sort_on(items):
    return items["num"]

def sort_dict(num_characters):
    result = []
    for char, num in num_characters:
        result.append({"char": char, "num": num_characters[char]})
        result.sort(key=sort_on, reverse=True)
    return result