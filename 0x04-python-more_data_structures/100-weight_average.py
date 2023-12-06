def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    total_weight = 0
    for score, weight in my_list:
        sum += score * weight
        total_weight += weight

    weighted_average = sum / total_weight
    return weighted_average
