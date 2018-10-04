WEIGHT = 1
VALUE = 0


def read_file_into_list(file_path="knapsack_small.txt"):
    l = []
    knapsack_size = None
    number_of_items = None
    with open(file_path) as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                knapsack_size = int(line.split(" ")[0])
                number_of_items = int(line.split(" ")[1])
                continue
            l.append([int(line.split(" ")[0]), int(line.split(" ")[1])])
    return l, knapsack_size, number_of_items


def solve():
    A = {}
    l, knapsack_size, number_of_items = read_file_into_list()
    i = 0
    for item in range(number_of_items):
        for knapsack_capacity in range(knapsack_size + 1):
            if (item-1, knapsack_capacity) not in A:
                first_term = 0
            else:
                first_term = A[(item-1, knapsack_capacity)]
            if (item-1, knapsack_capacity - l[item][WEIGHT]) not in A:
                if knapsack_capacity - l[item][WEIGHT] < 0:
                    second_term = 0
                else:
                    second_term = l[item][VALUE]
            else:
                second_term = A[(item-1, knapsack_capacity - l[item][WEIGHT])] + l[item][VALUE]
            solution = max(first_term, second_term)
            if solution > 0:
                A[(item, knapsack_capacity)] = solution
        i += 1
        print item, len(A)
        if i == 2:
            B = {}
            for knapsack_capacity in range(knapsack_size + 1):
                if (item, knapsack_capacity) in A:
                    B[(item, knapsack_capacity)] = A[(item, knapsack_capacity)]
            # del A
            A = B
            i = 0

    print A[(number_of_items - 1, knapsack_size)]


if __name__ == '__main__':
    solve()
