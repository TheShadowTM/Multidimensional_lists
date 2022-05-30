n, m = [int(x) for x in input().split()]

number_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k',
               11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u',
               21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

matrix = []

for row in range(n):
    matrix.append([])
    for column in range(m):
        secondary = row + column
        matrix[row].append(number_dict[row] + number_dict[secondary] + number_dict[row])

for row in matrix:
    print(*row, sep=' ')