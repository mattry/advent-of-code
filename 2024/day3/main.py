import re

def add_products(filename: str):
    with open(filename) as f:
        instructions = f.read()
        
        pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

        matches = [(int(x), int(y)) for x, y in re.findall(pattern, instructions)]

        sum = 0

        for match in matches:
            sum += match[0] * match[1]
        
        print(sum)




if __name__ == "__main__":
    input = "input.txt"
    add_products(input)