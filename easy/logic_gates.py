import sys
import math

n = int(input())
m = int(input())
signal_dct = {}
 

def forward_transform(signal):
    bool_signal_lst = []
    for i in signal:
        if i == "_": bool_signal_lst.append(False)
        if i == "-": bool_signal_lst.append(True)
    return bool_signal_lst


def reverse_transform(signal):
    str_signal_lst = []
    for i in signal:
        if i: str_signal_lst.append('-')
        else: str_signal_lst.append('_')
    return ''.join(str_signal_lst)


for i in range(n):
    input_name, input_signal = input().split()
    signal_dct[input_name] = forward_transform(input_signal)



for i in range(m):
    output_name, bool_operation, input_name_1, input_name_2 = input().split()
    if bool_operation == "AND":
        result = []
        for i in range(len(signal_dct[input_name_1])):
            result.append(signal_dct[input_name_1][i] and signal_dct[input_name_2][i])
           

        print(output_name, reverse_transform(result))

    elif bool_operation == "OR":
        result = []
        for i in range(len(signal_dct[input_name_1])):
            result.append(signal_dct[input_name_1][i] or signal_dct[input_name_2][i])

        print(output_name, reverse_transform(result))

    
    elif bool_operation == "XOR":
        result = []
        for i in range(len(signal_dct[input_name_1])):
            result.append((signal_dct[input_name_1][i] or signal_dct[input_name_2][i]) and not (signal_dct[input_name_1][i] and signal_dct[input_name_2][i]))
         
        print(output_name, reverse_transform(result))

    elif bool_operation == "NAND":
        result = []
        for i in range(len(signal_dct[input_name_1])):
            result.append(not(signal_dct[input_name_1][i] and signal_dct[input_name_2][i]))

        print(output_name, reverse_transform(result))

    elif bool_operation == "NOR":
        result = []
        for i in range(len(signal_dct[input_name_1])):
            result.append(not(signal_dct[input_name_1][i] or signal_dct[input_name_2][i]))

        print(output_name, reverse_transform(result))

    elif bool_operation == "NXOR":
        result = []
        for i in range(len(signal_dct[input_name_1])):
            result.append(not((signal_dct[input_name_1][i] or signal_dct[input_name_2][i]) and not (signal_dct[input_name_1][i] and signal_dct[input_name_2][i])))
    
        print(output_name, reverse_transform(result))
