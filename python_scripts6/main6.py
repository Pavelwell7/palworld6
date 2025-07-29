password = input('Введите пароль: ')


def calculate_password_score(password):
    score = 0
    password_length = len(password)
    if any(letter.isdigit() for letter in password):
        score += 2
    if password_length > 12:
        score += 2
    if any(letter.islower() for letter in password):
        score += 2
    if any(letter.isupper() for letter in password):
        score += 2
    if any(not letter.isalnum() for letter in password):
        score += 2
    return score


score = calculate_password_score(password)
print(f'Рейтинг пароля: {score}')


if __name__ == '__calculate_password_score(password)__':
    calculate_password_score(password)
    