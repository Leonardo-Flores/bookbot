with open('books/frankenstein.txt') as file:
    file_contents = file.read()


char_dict = {}
def sort_on(dict):
    return dict[1]

def count_chars(word):
    word_lower = word.lower()
    for char in word_lower:
        counter = 0 if char_dict.get(char) is None else char_dict.get(char)
        char_dict.update({char: counter + 1}) 
        

def get_numbers_of_words(text):
    words = text.split()
    for word in words:
        count_chars(word) 

    return len(words)



#print("file é: " + file)
text = file_contents
number_of_words = get_numbers_of_words(text)
dict_list = list(char_dict.items())
dict_list.sort(reverse=True, key=sort_on)
print('--- Begin Report of books/frankenstein.txt ---\n')
print(f'{number_of_words} words found in the document')
for item in dict_list:
    if item[0].isalpha():
        print(f'The \'{item[0]}\' character was found {item[1]} times')

print('\n--- End report ---')



