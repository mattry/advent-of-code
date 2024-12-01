def make_lists(filename: str):

    with open(filename) as f:
        left = []
        right = []
        lines = f.readlines()

        #total = 0

        for line in lines:
            line = line.strip()
            left_num = []
            right_num = []
            l = 0
            r = len(line) - 1
            while line[l].isnumeric():
                left_num.append(line[l])
                l += 1
            while line[r].isnumeric():
                right_num.append(line[r])
                r -= 1
            
            left.append(int("".join(left_num)))
            right_num = right_num[::-1]
            right.append(int("".join(right_num)))

        '''
        left.sort()
        right.sort()

        for i in range(len(left)):
            total += abs(left[i] - right[i])

        return total
        '''

        sim_score = 0

        for num in left:
            sim_score += num * right.count(num)
        
        return sim_score




if __name__ == "__main__":
    input = "input.txt"
    print(make_lists(input))