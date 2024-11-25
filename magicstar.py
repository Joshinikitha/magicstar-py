from collections import defaultdict

def calculate_intensity(n, lines, k):
    def cells_touched(line):
        x1, y1, x2, y2 = line
        cells = []
        if x1 == x2:  # Vertical line
            for y in range(min(y1, y2), max(y1, y2) + 1):
                cells.append((x1, y))
        elif y1 == y2:  # Horizontal line
            for x in range(min(x1, x2), max(x1, x2) + 1):
                cells.append((x, y1))
        else:  # Diagonal line
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            for i in range(abs(x2 - x1) + 1):
                cells.append((x1 + i * dx, y1 + i * dy))
        return cells

    def find_intersection(cells):
        counter = defaultdict(list)
        for i, line_cells in enumerate(cells):
            for cell in line_cells:
                counter[cell].append(i)
        return counter

    def calculate_star_intensity(intersection, lines):
        total_intensity = 0
        for point, line_indices in intersection.items():
            if len(line_indices) == k:
                intensities = []
                for idx in line_indices:
                    line = lines[idx]
                    line_cells = cells_touched(line)
                    if point == line_cells[0] or point == line_cells[-1]:
                        intensities.append(1)
                    else:
                        left = line_cells.index(point)
                        right = len(line_cells) - left - 1
                        intensities.append(min(left + 1, right + 1))
                total_intensity += min(intensities)
        return total_intensity

    # Convert all lines to cells they touch
    all_cells = [cells_touched(line) for line in lines]
    intersections = find_intersection(all_cells)
    return calculate_star_intensity(intersections, lines)

# Input reading
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
k = int(input())

# Calculate and output result
print(calculate_intensity(n, lines, k))
