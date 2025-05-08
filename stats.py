def count_words(text):
    words = text.split()
    return len(words)

def get_list_characteres(text):
    count_charact = {}
    for w in text:
        lowered = w.lower()
        if lowered in count_charact:
            count_charact[lowered] += 1
        else:
            count_charact[lowered] = 1
    return count_charact

def sort_on(dic):
    return dic["num"]

def chars_ordered_list(num_dict):
    sorted_list = []
    for ch in num_dict:
        sorted_list.append({"char": ch, "num": num_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list