def encode_word(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    inputs = [0] * 500

    for position, letter in enumerate(word.lower()):
        inputs[position] = alphabet.index(letter) + 1

    return inputs

def main():
    contentInput = input()  # primeira camada de entrada
    contentInput = contentInput.lstrip()
    vetor = [0] * len(contentInput)

    for i in range(len(contentInput)):
        vetor[i] = contentInput[i]
        
    return vetor


if __name__ == "__main__":
    print(main())
