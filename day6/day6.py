input = open("input.txt").read().strip()
input_list = input.split('\n')

time, distance = input_list
times = [int(x) for x in time.split(':')[1].split()]
distances = [int(x) for x in distance.split(':')[1].split()]


def function(_time, _distance):
    ret = 0
    for x in range(_time + 1):
        dx = x * (_time - x)
        if dx >= _distance:
            ret += 1
    return ret


answer = 1
for i in range(len(times)):
    answer *= function(times[i], distances[i])

print(answer)
