def has_digit(password):
    return any(letter.isdigit() for letter in password)


def is_very_long(password):
    password_length = len(password)
    return password_length > 12


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isalnum() for letter in password)


def calculate_password_score(password):
    score = 0
    secondary_functions = [
        has_digit,
        is_very_long,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    for second in secondary_functions:
        if second(password):
            score += 2
    return score


def main():
    password = input('Введите пароль: ')
    score = calculate_password_score(password)
    print(f'Рейтинг пароля: {score}')


if __name__ == '__main__':
    main()
