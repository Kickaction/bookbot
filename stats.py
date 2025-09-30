def get_num_words(text):
    return len(text.split())
def characters(text):
    count = {}
    for i in text.lower():
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
def sort_on_num(items):
    return items["num"]
def build_sorted_char_list(counts):
    result = []
    for c,n in counts.items():
        result.append({"char": c, "num": n})
    result.sort(reverse=True, key=sort_on_num)
    return result

 