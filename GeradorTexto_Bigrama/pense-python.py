import os
import sys


'''
Gerador de texto aleatório baseado no livro dr Jekyll
Codificação escrita seguindo o passo a passo do livro Pense em Python
'''


def main():
    input_file = "drjekyll.txt"
    output_file = "cln_txt.txt"

    # checar se arquivo existe
    if not os.path.exists(input_file):
        sys.exit(f"Arquivo {input_file} não existe")
        
    clean_file(input_file, output_file)


def is_section_marker(line):
    '''se a linha começar com a marcação, retorna True'''
    return line.strip().startswith("*** ")


def clean_file(input_file, output_file):
    '''Captura texto desejado pra análise de um arquivo .txt'''
    # verifica se está na seção desejada do texto
    targeted_section = False

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


if __name__ == "__main__":
    main()