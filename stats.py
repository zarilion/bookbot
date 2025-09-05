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