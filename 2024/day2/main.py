from typing import List


def check_levels(filename: str):

    with open(filename) as f:
        reports = f.readlines()

        safe = 0

        for report in reports:
            report = list(map(int, report.strip().split()))
            
            if is_increasing(report) or is_decreasing(report):
                # we only want to check if a report is safe if the report is monotonic 
                if is_safe(report):
                    safe += 1
        
        return safe


def is_increasing(nums: List[int]) -> bool:
    N = len(nums)
    for i in range(1, N):
        if not nums[i] > nums[i-1]:
            return False
    return True



def is_decreasing(nums: List[int]) -> bool:
    N = len(nums)
    for i in range(1, N):
        if not nums[i] < nums[i-1]:
            return False
    return True

def is_safe(nums: List[int]) -> bool:
    N = len(nums)
    for i in range(1, N):
        difference = abs(nums[i] - nums[i-1])
        if not 1 <= difference <= 3:
            return False
    return True
    



if __name__ == "__main__":
    input = "input.txt"
    print(check_levels(input))