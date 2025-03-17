def get_book_text(filepath):
     with open(filepath) as f:
          return f.read()
def count_words(text):
     words = text.split()
     return len(words)
def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def sort_characters(char_count):
    filtered_chars = {}
    for char, count in char_count.items():
        if char.isalpha():
            filtered_chars[char] = count
    sorted_list = []
    for char, count in filtered_chars.items():
        sorted_list.append({"char": char, "count": count})
    def get_count(dictionary):
        return dictionary["count"]
    sorted_list.sort(reverse=True, key=get_count)
    return sorted_list