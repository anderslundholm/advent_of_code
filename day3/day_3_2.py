import csv


def read_input():
    with open('day_3_input.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        input_list = list(reader)
    return input_list


def manhattan_distance(crossing_points_set):
    distances = []
    for point in crossing_points_set:
        distance = abs(point[0]) + abs(point[1])
        distances.append(distance)
    return distances


def map_wire_path(wire_cordinates):
    steps = set()
    count_point_dict = {}
    x, y, counter = 0, 0, 0
    for index, step in enumerate(wire_cordinates):
        for i in range(int(wire_cordinates[index][1:])):
            if step[0] == 'U':
                y += 1
            elif step[0] == 'R':
                x += 1
            elif step[0] == 'D':
                y -= 1
            elif step[0] == 'L':
                x -= 1
            counter += 1
            steps.add((x, y))
            count_point_dict[(x, y)] = counter
    return steps, count_point_dict


def compare_wire_paths(input_list):
    wire_set_1, count_point_dict_1 = map_wire_path(input_list[0])
    wire_set_2, count_point_dict_2 = map_wire_path(input_list[1])
    crossing_points = wire_set_1.intersection(wire_set_2)
    path_counts = [y + count_point_dict_2[x]
                   for x, y in count_point_dict_1.items()
                   if x in crossing_points]
    return path_counts


if __name__ == '__main__':
    input_list = read_input()
    path_counts = compare_wire_paths(input_list)
    # distances = manhattan_distance(crossing_points)
    closest_distance = min(path_counts)
    print(closest_distance)
