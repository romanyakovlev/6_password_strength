import argparse
import string

def get_password_strength(password, black_list):

    with open(black_list, 'r') as file_pass:
        pass_black_string = file_pass.read()

    pass_black_list = pass_black_string.split('\n')

    pass_complexity = 1

    string_pass_params = [
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        string.punctuation,
    ]

    complexity_counter = list(any(symbol for symbol  in password if symbol  in check_values)
    for check_values in string_pass_params)

    pass_complexity += sum(complexity_counter)
    pass_complexity += password not in pass_black_list

    len_pass = len(password)

    if len_pass >= 4 and len_pass < 8 :
        pass_complexity += 1
    if len_pass >= 8 and len_pass < 14:
        pass_complexity += 2
    if len_pass >= 14 and len_pass < 20 :
        pass_complexity += 3
    if len_pass >= 20:
        pass_complexity += 4

    return pass_complexity


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('password_text')
    parser.add_argument('black_list')
    args =  vars(parser.parse_args())
    password_text, black_list = args['password_text'], args['black_list']

    print('Сложность вашего пароля {}/10'.format(get_password_strength(password_text, black_list)))
