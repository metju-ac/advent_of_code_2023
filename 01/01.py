def load_data():
    data = []
    with open("01.txt", "r") as f:
        for line in f:
            data.append(line.strip())
    return data


def first_digit(line, reverse):
    if reverse:
        line = line[::-1]
    for char in line:
        if char.isdigit():
            return int(char)


def first(data):
    res = 0
    for line in data:
        res += first_digit(line, False) * 10 + first_digit(line, True)
    return res


def second(data):
    res = 0
    for line in data:
        line = line.replace("one", "o1e")
        line = line.replace("two", "t2o")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")

        res += first_digit(line, False) * 10 + first_digit(line, True)
    return res


if __name__ == '__main__':
    loaded_data = load_data()
    print(first(loaded_data))
    print(second(loaded_data))
