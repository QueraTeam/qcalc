def calc():
    user_input = input().split()
    nums = [int(num) for num in user_input[::2]]
    ops = [op for op in user_input[1::2]]
    ans = nums[0]
    for i, num in enumerate(nums[1:]):
        if ops[i] == '+':
            ans += num
        elif ops[i] == '-':
            ans -= num
        elif ops[i] == '*':
            ans *= num
        elif ops[i] == '/':
            ans /= num

    return ans


if __name__ == '__main__':
    print(calc())
