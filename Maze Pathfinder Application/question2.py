import math

def get_distance(tuple, tuple2):

    x_1 = tuple[0]
    y_1 = tuple[1]

    x_2 = tuple2[0]
    y_2 = tuple2[1]

    distance = math.sqrt(math.pow((x_2-x_1), 2) + math.pow((y_2-y_1), 2))

    return(distance)


def closest_enemies(hero_position, enemy_positions):

    swapped = True

    while(swapped == True):

        swapped = False

        for i in range(0, len(enemy_positions)-1):

            if(get_distance(hero_position, enemy_positions[i]) > get_distance(hero_position, enemy_positions[i+1])):

                enemy_positions[i], enemy_positions[i+1] = enemy_positions[i+1], enemy_positions[i]
                swapped = True

        swapped = False

        for i in range(len(enemy_positions)-2, 0, -1):

            if (get_distance(hero_position, enemy_positions[i]) > get_distance(hero_position, enemy_positions[i + 1])):

                enemy_positions[i], enemy_positions[i + 1] = enemy_positions[i + 1], enemy_positions[i]
                swapped = True

    return enemy_positions


def main():

    hero_position = (11, 11)
    enemy_positions = [(10, 20), (1000, 1000), (55, 10), (23, -5), (0, 0), (0, 200)]

    listo = closest_enemies(hero_position, enemy_positions)

    print(listo)

    for i in range(len(listo)):
        print(get_distance(hero_position, listo[i]))


if __name__ == "__main__":
    main()



