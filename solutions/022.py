"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def main():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    file = "source/022.txt"
    names = sorted(parse_input(file))
    
    total_score = 0
    for name in names:
        score = 0
        for letter in name:
            score += (letters.index(letter) + 1)

        score *= (names.index(name) + 1)
        
        total_score += score

    print(total_score)    


def parse_input(file):
    with open(file, "r") as f:
        names = f.readlines()[0].split(',')
        names = list(map(lambda name: name.replace('"', ""), names))
    
    return names
    
    
main()