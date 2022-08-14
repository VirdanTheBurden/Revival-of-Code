def part1(file) -> int:
    floor: int = 0
    for char in file.read():
        if "(" == char:
            floor += 1
        elif ")" == char:
            floor -= 1
    
    return floor

def part2(file) -> int:
    floor: int = 0
    pos: int = 0

    for char in file.read():
        pos += 1

        if "(" == char:
            floor += 1
        elif ")" == char:
            floor -= 1
        
        if floor <= -1:
            return pos

with open("input.txt", "r") as f:
    print("Part 1:", part1(f))
    f.seek(0)
    print("Part 2:", part2(f))

