data = [2, 5, 4, 6, 3, 4, 5, 6, 3, 4, 6, 2, 8, 7, 4, 4, 5, 7, 8, 4, 6, 8, 4, 5, 8, 9, 4, 6, 3, 2, 8, 7, 9, 9, 7, ]
data2 = ['hitam', ' putih', 'Hitam', ' putih']


def mode(data_value):

    # Add one value to x
    if type(data_value[0]) is str:
        inp_ = input('Case Sensitive data?? y/n ')
        if inp_.lower() == 'n':
            data_value = [data_value.strip().capitalize() for data_value in data_value]
        else:
            pass
    else:
        pass

    data_value.sort()
    x, x_freq = [], {}

    for i in data_value:
        if i not in x:
            x.append(i)
        else:
            pass

    # Count How Many X
    for o in x:
        mode_ = 0
        for i in data_value:
            if i == o:
                mode_ += 1
            else:
                pass

        x_freq[f'frequency {o}'] = f'{mode_}'

    return x_freq


print(mode(data))
