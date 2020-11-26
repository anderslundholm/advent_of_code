def read_input():
    with open('day_6_input.txt') as f:
        input_list = [row.rstrip() for row in f]
    return input_list


def create_orbit_dict(input_list):
    orbit_dict = {x.split(")")[1]: x.split(")")[0] for x in input_list}
    return orbit_dict


def count_planet_distance(orbit_dict, planet):
    map_list = []
    while planet in orbit_dict:
        map_list.append(orbit_dict[planet])
        planet = orbit_dict[planet]
    return map_list


def calc_effective_distance(orbit_dict):
    you_map = count_planet_distance(orbit_dict, 'YOU')
    san_map = count_planet_distance(orbit_dict, 'SAN')
    remove = set(you_map) & set(san_map)
    effective_distance = len(set(you_map + san_map) - remove)
    return effective_distance


if __name__ == '__main__':
    input_list = read_input()
    orbit_dict = create_orbit_dict(input_list)
    effective_distance = calc_effective_distance(orbit_dict)
    print(effective_distance)
