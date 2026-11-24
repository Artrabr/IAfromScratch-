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


def network(word):
    inputs = encode_word(word)

    # o primeiro neuronio adiciona valores das primeiras dias letras
    first_weights = [1, 1] + [0] * 498

    # o segundo newu add valor de 3 e 4 
    second_weights = [0, 0, 1, 1] + [0] * 496

    first_output = neuron(inputs, first_weights)
    second_output = neuron(inputs, second_weights)

    # a saida, neuronio add o result de dois neu escondido
    output = neuron([first_output, second_output], [1, 1])

    print(f"{word} → N1 = {first_output}, N2 = {second_output}, output = {output}")


def main():
    contentInput = input()  # primeira camada de entrada
    contentInput = contentInput.lstrip()
    vetor = [0] * len(contentInput)

    for i in range(len(contentInput)):
        vetor[i] = contentInput[i]
        
    return vetor


if __name__ == "__main__":
    network("gato")
