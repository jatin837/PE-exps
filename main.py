import os

META = [
    "./meta/Title.md",
    "./meta/TOC.md",
    ]

EXP_DIR = "./exps/"

if __name__ == "__main__":

    out = ""
    for i in META:
        with open(i, 'r') as f:
            out += f.read()
        out += '\n'

    exps = os.listdir(EXP_DIR)
    exps.sort()

    for exp in exps:
        with open(EXP_DIR + exp, 'r') as f:
            out += f.read()
        out += '\n'

    with open('out.md', 'w') as f:
        f.write(out)
