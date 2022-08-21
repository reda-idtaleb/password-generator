import string
import random
import sys

lower_case = string.ascii_lowercase;
upper_case = string.ascii_uppercase
numbers = string.digits;
special_chars = string.punctuation;

list_chars = [lower_case, upper_case, numbers, special_chars]

MIN_LENGTH = 8

def generate_powerful_pwd(length=MIN_LENGTH):
    assert(type(length) == int)
    if length < MIN_LENGTH:
        raise ValueError("The length of your password must be greater than 8.")
    
    n_char = length // len(list_chars)
    
    diff = length - (n_char * len(list_chars))
    rest = 0
    
    if  diff > 0:
        rest = diff
        
    password = ""
    
    while (len(password) < length): 
        for char_group in list_chars:
            for _ in range(n_char):
                random_char = random.randint(0, len(char_group)-1)
                password += char_group[random_char]
        if rest:
           password += __generate_rest_pwd(rest)
    
    randomized = list(password)
    random.shuffle(randomized)
    return "".join(randomized)
        
    
def __generate_rest_pwd(length):
    password = ""
    for _ in range(0, length):
        random_group = random.randint(0, len(list_chars)-1)
        random_char = random.randint(0, len(list_chars[random_group])-1)
        password += list_chars[random_group][random_char] 
    return password    


def usage():
    return "The programm takes one argument, please enter a length of your password."\
           "\nIf no argument is given then the default length of the generated password is 8."
    
if __name__ == "__main__":
    args = sys.argv[1:]
    
    if len(args) < 1:
        print(generate_powerful_pwd())
    elif len(args) == 1:
        assert(int(args[0]))
        length = int(args[0])
        try:
            print(generate_powerful_pwd(length))
        except ValueError as e:
            print(str(e))
    else:
        print(usage())
        
    