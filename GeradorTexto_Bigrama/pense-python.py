import os
import sys


'''
Gerador de texto aleatório baseado no livro dr Jekyll
Codificação escrita seguindo o passo a passo do livro Pense em Python
'''


def main():
    # variáveis com nomes dos arquivos
    input_file = "drjekyll.txt"
    output_file = "cln_txt.txt"

    # checar se arquivo existe
    if not os.path.exists(input_file):
        sys.exit(f"Arquivo {input_file} não existe")
        
    # limpa e escreve conteúdo de um arquivo para outro
    clean_file(input_file, output_file)

    # salvar os bigramas que compõe o texto limpo
    bigrams = get_bigrams(output_file)


# define se encontrou a parte de metadados do texto
def is_section_marker(line):
    '''se a linha começar com a marcação, retorna True'''
    return line.strip().startswith("*** ")


# transfere conteúdo de um arquivo para outro, ignorando a seção de metadados
def clean_file(input_file, output_file):
    '''Captura texto desejado pra análise de um arquivo .txt'''
    # verifica se está na seção desejada do texto
    targeted_section = False

    try:
        # abrir input como loop para ler linha por linha
        with open(input_file, 'r',encoding="utf-8") as reader:
            # abrir output como loop para escrever linha por linha
            with open(output_file, 'w', encoding="utf-8") as writer:
                for line in reader:
                    # se a função retornar True
                    if is_section_marker(line):
                        # inverte valor em targeted_section
                        targeted_section = not targeted_section
                        # "continue" garante que a linha com "*** " não seja escrito
                        continue
                    # se o sinalizador da posição desejada for True
                    if targeted_section:    
                        writer.write(line)
    except:
        sys.exit("Deu num ao manipular os arquivos")


# compõe bigramas
def get_bigrams(cln_file):
    '''
    Compõe bigramas usando o modelo de Markov
    Rettorna um dicionário
    Chave: string
    Valor: lista de strings que seguiram a string chave no texto avaliado
    '''
    bigrams_map = {}
    for line in open(cln_file):
        for i in range(len(line)-1):
            bigram = line[i], line[i + 1]
            print(bigram)


if __name__ == "__main__":
    main()