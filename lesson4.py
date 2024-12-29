def selection_sort(values):
    for i in range(len(values) - 1):
        min_idx = i
        for j in range(i + 1, len(values)):
            if values[min_idx] > values[j]:
                min_idx = j

        if i != min_idx:
            values[i], values[min_idx] = values[min_idx], values[i]
