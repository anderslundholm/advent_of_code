def read_input():
    with open('day_6_input.txt') as f:
        input_list = [row.rstrip() for row in f]
    return input_list


def create_orbit_dict(input_list):
    orbit_dict = {x.split(")")[1]: x.split(")")[0] for x in input_list}
    return orbit_dict


def count_planet_distance(orbit_dict):
    distance_count = 0
    for planet in orbit_dict:
        while planet in orbit_dict:
            planet = orbit_dict[planet]
            distance_count += 1
    return distance_count


if __name__ == '__main__':
    input_list = read_input()
    orbit_dict = create_orbit_dict(input_list)
    distance_count = count_planet_distance(orbit_dict)   
    print("total:", distance_count)
