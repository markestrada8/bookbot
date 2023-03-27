with open('./books/frankenstein.txt') as file:
    book = file.read()
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{len(book.split())} words found in the document\n')
    
    char_data = {}
    char_list = []
    for char in book:
        if char.lower() in char_data and char.isalpha():
            char_data[char.lower()] += 1
        elif char.isalpha():
            char_data[char.lower()] = 1
    for k, v in char_data.items():
        char_list.append([k, v])
    char_list.sort(key=lambda x: x[1], reverse=True)
    for item in char_list:
        print(f'The {item[0]} character was found {item[1]} times')
    print('--- End report ---')