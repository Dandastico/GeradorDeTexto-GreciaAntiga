'''
Gerador de texto aleatório baseado no livro dr Jekyll
Codificação escrita seguindo o passo a passo do livro Pense em Python
'''


def main():
    input_file = "dr_jekyll.txt"
    output_file = "cln_txt.txt"

    clean_file(input_file, output_file)


def is_special_line(line):
    # retira espaços em brancos, retorna None se tiver apenas espaços
    line = line.strip()
    # return só retorna o que não começar com *** ou None
    return line.strip().startswith("*** ") or not line


def clean_file(input_file, output_file):
    # abrir input como loop para ler linha por linha
    with open(input_file, encoding="utf-8") as reader:
        # abrir output como loop para escrever linha por linha
        with open(output_file, 'w', encoding="utf-8") as writer:
            for line in reader:
                if not is_special_line(line):
                    writer.write(line)


main()