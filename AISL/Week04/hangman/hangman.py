import random

def hangman():
    words = ['apple', 'tiger', 'house', 'dream']
    word = random.choice(words)  # 랜덤 단어 선택
    guessed = ['_'] * len(word)  # 현재 상태
    guessed_letters = set()
    life = 6  # 목숨: 틀릴 수 있는 횟수

    print("=== 영어 행맨 게임 ===")
    print(f"단어 길이: {len(word)} 글자")
    
    while life > 0 and '_' in guessed:
        print("\n현재 단어: ", ' '.join(guessed))
        print(f"남은 목숨: {life}")
        guess = input("알파벳을 입력하세요: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("한 글자의 알파벳만 입력해주세요.")
            continue

        if guess in guessed_letters:
            print("이미 입력한 알파벳입니다.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"'{guess}'는 정답입니다!")
            for i, ch in enumerate(word):
                if ch == guess:
                    guessed[i] = guess
        else:
            print(f"'{guess}'는 단어에 없습니다.")
            life -= 1

    if '_' not in guessed:
        print("\n축하합니다! 단어를 맞췄습니다:", word)
    else:
        print("\n실패! 정답은:", word)

if __name__ == "__main__":
    hangman()