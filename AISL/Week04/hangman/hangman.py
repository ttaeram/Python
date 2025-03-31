import random

words = ['python', 'programming', 'line', 'hangman']


def get_guess(guessed_letters):
    while True:
        guess = input("알파벳을 입력하세요: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("한 글자의 알파벳만 입력해주세요.")
        elif guess in guessed_letters:
            print("이미 입력한 알파벳입니다.")
        else:
            return guess


def update_guessed(word, guess, guessed):
    hit = False
    for i, ch in enumerate(word):
        if ch == guess:
            guessed[i] = guess
            hit = True
    return hit


def print_status(guessed, life):
    print("\n현재 단어: ", ' '.join(guessed))
    print(f"남은 목숨: {life}")


def is_word_guessed(guessed):
    return '_' not in guessed


def hangman():
    word = random.choice(words)
    guessed = ['_'] * len(word)
    guessed_letters = set()
    life = 6

    print("----- 행맨 게임 -----")
    
    while life > 0 and not is_word_guessed(guessed):
        print_status(guessed, life)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if update_guessed(word, guess, guessed):
            print(f"'{guess}'는 정답입니다!")
        else:
            print(f"'{guess}'는 단어에 없습니다.")
            life -= 1

    if is_word_guessed(guessed):
        print("\n축하합니다! 단어를 맞췄습니다:", word)
    else:
        print("\n실패! 정답은:", word)


hangman()