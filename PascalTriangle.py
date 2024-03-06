def generate_pascal_triangle(num_rows):
    triangle = []

    for i in range(num_rows):
        row = [None] * (i + 1)
        row[0], row[-1] = 1, 1  # First and last elements of each row are always 1

        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 4))

# Example usage:
num_rows = 5
pascal_triangle = generate_pascal_triangle(num_rows)
print("Pascal's Triangle:")
print_pascal_triangle(pascal_triangle)
