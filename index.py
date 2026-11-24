def main():
    contentInput = input()  # primeira camada de entrada
    contentInput = contentInput.lstrip()
    vetor = [0] * len(contentInput)

    for i in range(len(contentInput)):
        vetor[i] = contentInput[i]
        
    return vetor


if __name__ == "__main__":
    print(main())
