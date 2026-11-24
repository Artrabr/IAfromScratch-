def encode_word(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    inputs = [0] * 500

    for position, letter in enumerate(word.lower()):
        inputs[position] = alphabet.index(letter) + 1

    return inputs

def neuron(inputs, weights, bias=0):
    total = bias

    for value, weight in zip(inputs, weights): #pra cada valor e peso, em valores com peso
        total += value * weight  # cada conecção no diagrama

    return max(0, total)  # negativo = 0 ou vem maior

def main():
    contentInput = input()  # primeira camada de entrada
    contentInput = contentInput.lstrip()
    vetor = [0] * len(contentInput)

    for i in range(len(contentInput)):
        vetor[i] = contentInput[i]
        
    return vetor


if __name__ == "__main__":
    print(main())
