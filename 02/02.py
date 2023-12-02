from collections import defaultdict


def load_data():
    data = []
    with open("02.txt", "r") as f:
        for line in f:
            line = line.strip().split(":")[1].split(";")
            cur_game = []
            for cubes in line:
                cur_set = defaultdict(lambda: 0)
                for pair in cubes.strip().split(", "):
                    count, color = pair.split(" ")
                    cur_set[color] = int(count)
                cur_game.append(cur_set)
            data.append(cur_game)
    return data


def first(data):
    res = 0
    for i, game in enumerate(data):
        possible = True
        for cur_set in game:
            red, green, blue = cur_set["red"], cur_set["green"], cur_set["blue"]
            if red > 12 or green > 13 or blue > 14:
                possible = False
        if possible:
            res += i + 1
    return res


def second(data):
    res = 0
    for game in data:
        r_min, g_min, b_min = 0, 0, 0
        for cur_set in game:
            red, green, blue = cur_set["red"], cur_set["green"], cur_set["blue"]
            r_min = max(r_min, red)
            g_min = max(g_min, green)
            b_min = max(b_min, blue)
        res += r_min * g_min * b_min
    return res


if __name__ == '__main__':
    loaded_data = load_data()
    print(first(loaded_data))
    print(second(loaded_data))
