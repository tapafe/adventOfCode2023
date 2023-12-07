input = open("input").read().strip()
input_list = input.split('\n')

answer_p1 = 0
answer_p2 = 0

for line in input_list:
    game_id, values = line.split(':')
    dict_color = {}
    for subset in values.split(';'):
        for balls_and_color in subset.split(','):
            number_of_cubes, color = balls_and_color.split()
            number_of_cubes = int(number_of_cubes)
            if color not in dict_color:
                dict_color[color] = number_of_cubes
            else:
                dict_color[color] = max(dict_color[color], number_of_cubes)

    # p1
    ok = True
    for valor in dict_color:
        if valor == "red" and dict_color[valor] > 12:
            ok = False
        elif valor == "green" and dict_color[valor] > 13:
            ok = False
        elif valor == "blue" and dict_color[valor] > 14:
            ok = False

    if ok:
        answer_p1 += int(game_id.split()[1])

    # p2
    score = 1
    for value in dict_color.values():
        score *= value
    answer_p2 += score


print(answer_p1)
print(answer_p2)
