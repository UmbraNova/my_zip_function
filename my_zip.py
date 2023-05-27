def archive(data_1, data_2):
    data_1, data_2 = tuple(data_1), tuple(data_2)
    min_num = data_1
    if len(data_1) > len(data_2):
        min_num = len(data_2)
    return ((data_1[i], data_2[i]) for i in range(len(min_num)))


def print_info(archived):
    print('Result:')
    print(f'Type: {archived}')
    for item in archived:
        print(item)


# input_1 = 'abcd'
input_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# input_2 = (10, 20, 30, 40)
# input_2 = ('01110000', '01111001', '01110100', '01101000', '01101111', '01101110')
input_2 = [987, 567, 23.3556, 111.9]


archived_data = archive(input_1, input_2)
# comparison vs zip function
zipped_data = zip(input_1, input_2)


print_info(zipped_data)
print('=='*40, '\n')
print_info(archived_data)
