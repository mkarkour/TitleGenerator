from art import *

def generate_3d_comment_title(title):
    border_length = 80
    if len(title) > border_length - 6:
        raise ValueError("La longueur du titre dépasse la longueur maximale autorisée")
    side_length = (border_length - len(title) - 8) // 2  
    border_top = "#" * border_length
    title_line = f"###{'-' * side_length}   {title}   {'-' * side_length}###"  
    border_bottom = "#" * border_length
    print(border_top)
    print(title_line)
    print(border_bottom)

def generate_art_single(word):
    my_art = text2art(word)
    lines = my_art.split('\n')  
    max_line_length = max(len(line) for line in lines)  
    modified_lines = ['#' + line.ljust(max_line_length) for line in lines]
    modified_art = '\n'.join(modified_lines)  
    print(modified_art)

def generate_title_art_block(word):
    my_art = text2art(word, font='block')
    lines = my_art.split('\n')  
    max_line_length = max(len(line) for line in lines)  
    modified_lines = ['#' + line.ljust(max_line_length) for line in lines]
    modified_art = '\n'.join(modified_lines)  
    print(modified_art)


def main():
    word = input("Le mot : ")
    type_title = int(input("Le type de titre : "))
    dico = {
        1: generate_3d_comment_title,
        2: generate_art_single,
        3: generate_title_art_block
    }
    funct = dico[type_title]
    print(funct(word))

if __name__ == "__main__":
    main()