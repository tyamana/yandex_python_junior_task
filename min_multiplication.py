def compute_min_multiplication_of_list_elements(l):
    if len(l) == 0:
        raise ValueError('Empty list!')

    if len(l) == 1:
        return l[0]

    if len(l) == 2:
        return l[0] * l[1]

    first_max = max(l)   # O(n)
    l.remove(first_max)  # O(n)
    second_max = max(l)  # O(n)

    first_min = min(l)   # O(n)
    l.remove(first_min)  # O(n)
    second_min = min(l)  # O(n)

    # O(1)
    if first_min >= 0:
        return first_min * second_min
    elif first_max <= 0:
        return first_max * second_max
    else:
        return first_max * first_min
