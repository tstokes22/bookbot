def get_num_words(text):
    num_words = text.split()
    value = 0
    for x in num_words:
        value += 1
    return value

def get_num_char(text):
    chardict = {
    }
    for c in text:
       c = c.lower()
       if c in chardict.keys():
            chardict[f'{c}'] += 1 
       else:
            chardict[f'{c}'] = 1

    return chardict

def sort_on(dict):
    return dict["num"]


def sort_dict(dict):
    my_list = []
    for key in dict:
        if key.isalpha():
           new_dict = {"char": key, "num": dict.get(f"{key}")}
           my_list.append(new_dict)

    my_list.sort(reverse=True, key=sort_on)
    return my_list
