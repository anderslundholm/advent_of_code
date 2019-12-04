import csv


def read_input():
    with open('day_3_input.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        input_list = list(reader)
    return input_list


def manhattan_distance(crossing_points):
    pass


def map_wire_path(wire_cordinates):
    steps = set()
    x, y = 0, 0
    for index, step in enumerate(wire_cordinates):
        #print(step, index)
        # wire_cordinates[index][1:]
        for i in range(int(wire_cordinates[index][1:])):
            # print(i)
            if step[:1] == 'U':
                
                # y += int(step[1:])
            elif step[:1] == 'R':
                
                # x += int(step[1:])
            elif step[:1] == 'D':
                
                # y -= int(step[1:])
            elif step[:1] == 'L':
                
                # x -= int(i[1:])
            steps.add((x, y))
    print(steps)
    return steps


def compare_wire_paths(input_list):
    wire_set_1 = map_wire_path(input_list[0])
    wire_set_2 = map_wire_path(input_list[1])
    return wire_set_1.intersection(wire_set_2)


if __name__ == '__main__':
    input_list = read_input()
    crossing_points = compare_wire_paths(input_list)
    print(crossing_points)
    manhattan_distance(crossing_points)
