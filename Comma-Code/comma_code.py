letters = ['a', 'b', 'c']
animals = ['dogs', 'cats', 'horses', 'rats']
fruits = ["apple", "banana", "cherry", "apple", "cherry"]
empty = []

def comma_concat(list):
    list_len = len(list)
    if list_len > 0:
        full_string = ''
        for i in range(list_len):
            if i == (list_len - 1):
                full_string = full_string + 'and ' + list[i]
            
            else:
                full_string = full_string + list[i] + ', '
                i =+ 1
        print(full_string)    
    else:
        print('The list is empty')

comma_concat(letters)
comma_concat(animals)
comma_concat(fruits)
comma_concat(empty)