import re

def get_paragraph() -> str:
    print("Please enter a paragraph: ")
    print()
    paragraph: str = input()
    return paragraph

def split_sentences(paragraph: str) -> list[str]:

    sentences: list[str] = re.split(r'(?<=[.!?])\s+', paragraph.strip())
    
    cleaned: list[str] = []
    for s in sentences:
        if s.strip():
            cleaned.append(s.strip())
    sentences = cleaned
    return sentences

def display_sentences(sentences: list[str]) -> None:
    print()
    for i, sentence in enumerate(sentences, 1):
        print(f"Sentence {i}: {sentence}")
    
    print(f"\nTotal number of sentences: {len(sentences)}")

def main() -> None:
    paragraph: str = get_paragraph()
    sentences: list[str] = split_sentences(paragraph)
    display_sentences(sentences)

main()
