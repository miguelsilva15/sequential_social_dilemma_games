import random

from social_dilemmas.maps import APPLE_AGENT_POSITON, APPLE_RESOURCE_POSITION, ORANGE_AGENT_POSITON

def generate_character(map_list, character='P', num=1, dimension=10, padding=4, possible_positions=None):
    indexes = []
    temp_map_list = map_list.copy()
    if possible_positions:
        for i in range(num):
            x_random_index, y_random_index = random.choice(possible_positions)
            row = list(temp_map_list[x_random_index])
            row[y_random_index] = character
            str1 = ''.join(row)
            temp_map_list[x_random_index] = str1
            indexes.append((x_random_index, y_random_index))
    else:
        character_counter = 0
        while True:
            x_random_index = random.randint(0+padding, dimension+padding+1)
            y_random_index = random.randint(0+padding, dimension+padding+1)
            if temp_map_list[x_random_index][y_random_index] == ' ':
                row = list(temp_map_list[x_random_index])
                row[y_random_index] = character
                str1 = ''.join(row)
                temp_map_list[x_random_index] = str1
                character_counter += 1
                indexes.append((x_random_index, y_random_index))
            if character_counter == num:
                break
    return temp_map_list, indexes

def reverse_map_to_list(e_map):
    final_map = []
    for row in e_map.tolist():
        row_list = []
        for charac in row:
            row_list.append(charac.decode("utf-8"))
        final_map.append(''.join(row_list))
    return final_map

def create_map(num_agents_orange=1, num_agents_apples=1, dimension = 10, distance=2, seed=None, existing_map=None):
    # TODO: add existing map funcionality
    if seed:
      random.seed(666)
    if existing_map is not None: 
        map_list = reverse_map_to_list(existing_map)
    else:
        map_list = []
        map_list.append('@'*(dimension+8))
        map_list.append('@'*(dimension+8))
        map_list.append('@'*(dimension+8))
        map_list.append('@'*(dimension+8))
        for i in range(dimension):
            map_list.append('@@@@'+' '*(dimension)+'@@@@')
        map_list.append('@'*(dimension+8))
        map_list.append('@'*(dimension+8))
        map_list.append('@'*(dimension+8))
        map_list.append('@'*(dimension+8))
        map_list, _ = generate_character(map_list, character='L', num=num_agents_orange, dimension=dimension, possible_positions= ORANGE_AGENT_POSITON)
        map_list, _ = generate_character(map_list, character='P', num=num_agents_apples,dimension=dimension, possible_positions= APPLE_AGENT_POSITON)
    map_list, list_appls = generate_character(map_list, character='A', dimension=dimension, possible_positions= APPLE_RESOURCE_POSITION)
    # replace this in the case of more apples
    (x_A, y_A) = list_appls[0]
    list_values = []
    for value_x in range(x_A-distance, x_A+distance+1):
      value_to_sum_y = distance-abs(value_x-x_A)
      # print(value_to_sum_y)
      for value_y in range(y_A-value_to_sum_y, y_A+value_to_sum_y+1):
        if ((abs(value_x-x_A) + abs(value_y-y_A)) == distance) and (4 <= value_x <= (dimension+4)) and (4 <= value_y <= (dimension+4)):
            list_values.append((value_x, value_y))
    list_values = list(set(list_values))
    if (x_A, y_A) in list_values:
        list_values.remove((x_A, y_A))
    orange_flag = True
    while orange_flag:
        x_random_index, y_random_index = random.choice(list_values)
        if map_list[x_random_index][y_random_index] == ' ':
            row = list(map_list[x_random_index])
            row[y_random_index] = 'O'
            str1 = ''.join(row)
            map_list[x_random_index] = str1
            orange_flag = False
    return map_list 