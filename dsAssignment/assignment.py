def get_data(inp_file_num):
    """
    this function returns the data of the selected input file in desired format.
    """
    f = open(f"{inp_file_num}.in", "r")
    num_of_shifts = int(f.readline().strip())
    lines = list(
        line for line in (list(map(int, l.strip().split(" "))) for l in f) if line
    )
    max_num = max(max(i) for i in lines)
    return lines, num_of_shifts, max_num + 1


def pool_coverage(inp_file_num):
    """
    this function is used to calculate the maximum time units that can be covered after firing one life guard.
    """
    interval_list, total_shifts, max_num = get_data(inp_file_num)
    total_coverage = 0
    max_coverage = 0
    tu_diff = 0
    time_unit = calc_time_occurance(interval_list, total_shifts, max_num)
    un_frequency = calc_unique_number_frequency(time_unit, max_num)
    # print(time_unit,un_frequency)
    for i in range(max_num):
        if time_unit[i]:
            total_coverage = total_coverage + 1
    for shift in range(total_shifts):
        l = interval_list[shift][0]
        r = interval_list[shift][1]
        if l != 0:
            tu_diff = un_frequency[r] - un_frequency[l]
        else:
            tu_diff = un_frequency[r]
        if total_coverage - tu_diff >= max_coverage:
            max_coverage = total_coverage - tu_diff
    print("Maximum pool time coverage after firing one life guard is", max_coverage)
    write_output(inp_file_num, max_coverage)


def calc_time_occurance(interval_list, total_shifts, max_num):
    """
    this function is used to create and return a list of the number of times a time unit occurs.
    """
    time_unit = [0 for i in range(max_num)]
    for shift in range(total_shifts):
        l = interval_list[shift][0]
        r = interval_list[shift][1]
        for j in range(l + 1, r + 1):
            time_unit[j] = time_unit[j] + 1
    return time_unit


def calc_unique_number_frequency(time_unit, max_num):
    """
    this function is used to create and return a list of elements that denote the number of unique time units at any given position 'i'.
    """
    un_frequency = [0 for i in range(max_num)]
    if time_unit[0] == 1:
        un_frequency[0] = 1
    for i in range(1, max_num):
        if time_unit[i] == 1:
            un_frequency[i] = un_frequency[i - 1] + 1
        else:
            un_frequency[i] = un_frequency[i - 1]
    return un_frequency


def write_output(op_file_num, cov):
    """
    this function is used to write the output to the desired file.
    """
    f = open(f"{op_file_num}.out", "w")
    f.write(str(cov))
    f.close()
