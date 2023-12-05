# get the first number per line
#get the last number in the line
#join those numbers together to create a two digit number
#sum all of the two digit numbers 

file_path = "day_1_input.txt"
# file_path = "test.txt"

# Part 1 Solution that identifes first and last number per line and then sums the combined numbers
def part_1():
    with open(file_path, 'r') as file:
        two_digit_numbers = []
        for line in file:
            digits = [char for char in line if char.isdigit()]
            first_digit = digits[0]
            last_digit = digits[-1]
            combined_digit=first_digit+last_digit
            two_digit_numbers.append(int(combined_digit))
        total_sum = sum(two_digit_numbers)
        return total_sum

# Part 2 Solution that also includes written numbers
def part_2():
    D = open(file_path).read().strip()
    ans = 0
    for line in D.split('\n'):
        digits=[]
        for i,c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    digits.append(str(d+1))
        score = int(digits[0]+digits[-1])
        ans += score
    return ans
print(part_2())
