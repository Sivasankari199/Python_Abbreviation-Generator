letter_scores = {}
remaining = {}

def generate_index(words):
    word_indexes = []
    for word in words:
        for i in range(len(word)):
            word_indexes.append([word[i], i])
    return word_indexes

def read_values():
    with open('values.txt', 'r') as f:
        letter = [line.rstrip().split(' ') for line in f.readlines()]
        for score in letter:
            letter_scores[score[0].upper()] = int(score[2]) if score[1] == '' else int(score[1])

def split_name(name):
    words = []
    word = ''
    for i in range(len(name)):
        if name[i] == "'":
            i += 1
        elif name[i].isalpha():
            word += name[i]
        else:
            if word:
                words.append(word.upper())
            word = ''
    if word:
        words.append(word.upper())
        return words

def generate_abbreviations(names):
    for name in names:
        words = split_name(name)
        indexed_names = generate_index(words)
        for i in range(1, len(indexed_names) - 1):
            second_letter_total = 0
            third_letter_total = 0
            for j in range(i + 1, len(indexed_names)):
                abbreviation = indexed_names[0][0] + indexed_names[i][0] + indexed_names[j][0]
                if indexed_names[i][1] == 0:
                    second_letter_total = 0
                elif i == len(indexed_names) - 1 or (i + 1 < len(indexed_names) and indexed_names[i + 1][1] == 0):
                    if indexed_names[i][0] == "E":
                        second_letter_total = 20
                    else:
                        second_letter_total = 5
                else:
                    second_letter_total = indexed_names[i][1] + letter_scores[indexed_names[i][0]]
                if indexed_names[j][1] == 0:
                    third_letter_total = 0
                elif j == len(indexed_names) - 1 or (j + 1 < len(indexed_names) and indexed_names[j + 1][1] == 0):
                    if indexed_names[j][0] == "E":
                        third_letter_total = 20
                    else:
                        third_letter_total = 5
                else:
                    third_letter_total = indexed_names[j][1] + letter_scores[indexed_names[j][0]]
                if abbreviation not in remaining:
                    remaining[abbreviation] = [name, second_letter_total + third_letter_total, 1]
                elif remaining[abbreviation][1] >= second_letter_total + third_letter_total and \
                        remaining[abbreviation][0] == name:
                    remaining[abbreviation][1] = second_letter_total + third_letter_total
                    remaining[abbreviation][2] += 1
                elif remaining[abbreviation][1] != second_letter_total + third_letter_total and \
                        remaining[abbreviation][0] != name:
                    remaining[abbreviation][2] += 1

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            names = [line.rstrip() for line in file.readlines()]
            return names
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

def write_to_file(file_name, names, sorted_items):
    try:
        with open(file_name, 'w') as file:
            for i in names:
                for j in sorted_items:
                    if i == j[1][0]:
                        file.write(f"{i}\n{j[0]}\n")
                        break
        print(f"Results written to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error writing to file '{file_name}': {e}")

if __name__ == "__main__":
    names = read_file('trees.txt')
    read_values()
    generate_abbreviations(names)
    remaining = {key: value for key, value in remaining.items() if value[2] <= 1}
    sorted_items = sorted(remaining.items(), key=lambda x: x[1][1])
    write_to_file('output.txt', names, sorted_items)
