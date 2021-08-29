#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

#格式轉換
def convert(lines):
    history = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            history.append(person + ': ' + line)
    return history


#寫入檔案
def write_file(filename, history):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for line in history:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    history = convert(lines)
    write_file('output.txt', history)

main()
