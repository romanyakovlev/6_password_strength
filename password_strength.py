import argparse
import string

def get_password_strength(password):

    with open('password_blacklist.txt', 'r') as file_pass:
        pass_black_list = file_pass.read()
    file_pass.closed
    pass_black_list = pass_black_list.split('\n')

    pass_complexity = 1

    string_pass_params = [

        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        string.punctuation,
        string.punctuation+string.digits,
        
]

    string_pass_list = [password]*4 + [password[1:-1]]

    pass_complexity += sum(any(symbol for symbol  in y if symbol  in x ) for x, y in zip(string_pass_list,string_pass_params))

    pass_complexity += password not in pass_black_list

    if len(password) < 8 and len(password) > 4:
        pass_complexity += 1
    if len(password) > 8 and len(password) < 14:
        pass_complexity += 2
    if len(password) > 14:
        pass_complexity += 3

    return pass_complexity


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('password_text')
    password_text = parser.parse_args().password_text
    print(get_password_strength(password_text))
