'''
Gerador de texto aleatório baseado no livro dr Jekyll
Codificação escrita seguindo o passo a passo do livro Pense em Python
'''


def main():
    input_file = "dr_jekyll.txt"
    output_file = "txt.txt"

    clean_file(input_file, output_file)


def is_special_line(line):
    return line.strip().startswith('*** ')


def clean_file(input_file, output_file):
    reader = open(input_file, encoding="utf-8")
    writer = open(output_file, 'w')

    for line in reader:
        if is_special_line(line):
            break

    for line in reader:
        if is_special_line(line):
            break
        writer.write(line)

    reader.close()
    writer.close()


    if __name__ == "__main__":
        main()