import random

def generate_character(map_list, character='P', num=1, dimension=10):
    character_counter = 0
    while True:
        x_random_index = random.randint(0, dimension)
        y_random_index = random.randint(0, dimension)
        if map_list[x_random_index][y_random_index] == ' ':
            row = list(map_list[x_random_index])
            row[y_random_index] = character
            str1 = ''.join(row)
            map_list[x_random_index] = str1
            character_counter += 1
        if character_counter == num:
            break
    return map_list, (x_random_index, y_random_index)

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
        map_list, _ = generate_character(map_list, character='L', num=num_agents_orange, dimension=dimension+7)
        map_list, _ = generate_character(map_list, character='P', num=num_agents_apples,dimension=dimension+7)
    map_list, (x_A, y_A) = generate_character(map_list, character='A', dimension=dimension+7)
    list_values = []
    for value_x in range(x_A-distance, x_A+distance+1):
      value_to_sum_y = distance-abs(value_x-x_A)
      for value_y in range(y_A-value_to_sum_y, y_A+value_to_sum_y+1):
        if (distance -2) <= abs(value_to_sum_y - abs(value_y-y_A)) <= distance:
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