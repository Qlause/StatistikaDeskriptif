import math

data = [2, 5, 4, 6, 3, 4, 5, 6, 3, 4, 6, 2, 8, 7, 4, 4, 5, 7, 8, 4, 6, 8, 4, 5, 8, 9, 4, 6, 3, 2, 8, 7, 9, 9, 7]
data2 = ['hitam', ' putih', 'Hitam', 'putih']


def mode(data_value):

    # Add one value to x
    if type(data_value[0]) is str:
        inp_ = input('Case Sensitive data?? y/n ')
        if inp_.lower() == 'n':
            data_value = [data_value.strip().capitalize() for data_value in data_value]
        else:
            data_value = [data_value.strip() for data_value in data_value]

    data_value.sort()
    x, x_freq = [], {}

    for i in data_value:
        if i not in x:
            x.append(i)

    # Count How Many X
    for o in x:
        mode_ = 0
        for i in data_value:
            if i == o:
                mode_ += 1

        x_freq[f'frequency {o}'] = f'{mode_}'

    return x_freq


def mean(data_value):

    mean_ = 0
    for i in data_value:
        if type(i) != int:
            return print('Data Type Is not Integer!')
        else:
            mean_ += int(i)

    return mean_ / len(data_value)


def median(data_value):

    data_value.sort()
    if len(data_value) % 2 == 0:
        return data_value[len(data_value)//2]
    else:
        return data_value[len(data_value)//2], data_value[len(data_value)//2 - 1]


def standard_deviation(data_value):
    test = mode(data_value)
    sig_value = float(0)
    for i in test:
        sig_value += ((float(i.split()[-1]) - mean(data_value)) ** 2) * float(test[i])

    data_value.sort()
    return math.sqrt(sig_value / len(data_value))


def quatile(data_value):
    data_value.sort()
    return data_value[int(1/4 * (len(data_value) + 1))], data_value[int(1/2 * (len(data_value) + 1))], data_value[int(3/4 * (len(data_value) + 1))]

print(quatile(data))
