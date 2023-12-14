def find_mirror_index(grid):
    for i in range(1, len(grid)):
        top_half = grid[:i][::-1]
        bottom_half = grid[i:]

        top_half = top_half[:len(bottom_half)]
        bottom_half = bottom_half[:len(top_half)]

        if top_half == bottom_half:
            return i

    return 0


with open("./day 13/file.txt", "r") as file:
    blocks = file.read().split("\n\n")
hor_ans = 0
ver_ans = 0
ans = 0
for block in blocks:
    grid = block.splitlines()

    row_index = find_mirror_index(grid)
    hor_ans += row_index * 100

    transposed_grid = list(zip(*grid))
    column_index = find_mirror_index(transposed_grid)
    ver_ans += column_index

    ans += hor_ans + ver_ans

print(hor_ans, ver_ans, ans)