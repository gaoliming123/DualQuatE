if __name__ == '__main__':
    knowledge = set()
    with open('entities.dict', 'r') as fin:
        for line in fin.readlines():
            knowledge.add(line)
    fout = open('entities.dict', 'w')
    for e in knowledge:
        fout.write(e)
    fout.close()
