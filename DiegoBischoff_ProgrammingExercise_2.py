SPAM_WORDS = 30

def genScamList() -> list[str]:

    words: list[str] = [" "] * SPAM_WORDS

    with open('email/scam-words.txt', 'r') as f:
        for i, line in enumerate(f):

            words[i] = line.strip()

    return words

#I keep confusing scam and spam
def scanEmail(words: list[str]) -> None:

    scamScore: int = 0
    foundWords: list[str] = []

    with open('email/email.txt', 'r') as f:
        for line in f:
            for word in words:
                if word.lower() in line.lower():
                    scamScore += 1
                    foundWords.append(word)

    print(f"Your spam score is: {scamScore}")
    print(f"Your email contained: {len(foundWords)} common spam words")
    print(*foundWords, sep=', ')

    print()

    #typecast in python
    print(f"the spam likeliness of this email is {int((scamScore / SPAM_WORDS)*100)}%")

def main():
    scamWords: list[str] = genScamList()
    scanEmail(scamWords)

if __name__ == "__main__":
    main()