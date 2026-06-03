PASSWORD_GOOD_LENGTH = 12

def is_very_long(password):
	password_length = len(password)
	is_password_long = password_length > PASSWORD_GOOD_LENGTH
	return is_password_long


def has_digit(password):
	return any(letter.isdigit() for letter in password)


def has_upper_letters(password):
	return any(letter.isupper() for letter in password)


def has_lower_letters(password):
	return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isdigit() and not letter.isalpha() for letter in password)


def count_score(password_checks, password):
	current_score = 0
	for password_check in password_checks:
		if password_check(password):
			current_score = current_score + 2
	return current_score


def main():
    password = input("Введите пароль: ")
    password_checks = [
    is_very_long,
    has_digit,
    has_upper_letters, has_lower_letters,
    has_symbols,
    ]
    score = count_score(password_checks, password)
    print("Рейтинг пароля:", score)


if __name__ == "__main__":
    main()


