from random import sample


def s(list_, target):
    left, right = 0, len(list_) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_[middle] < target:
            left = middle + 1
        elif list_[middle] > target:
            right = middle - 1
        else:
            return middle
    return


if __name__ == "__main__":
    list_len = 10
    rand_list = sorted(sample(range(0, 101, 2), list_len))

    try:
        target = int(input('Pick a even number between 0-100: '))
        target_index = s(rand_list, target)
        if target < 0 or target > 100 or target % 2 != 0:
            print("Invalid input")
        else:
            print(f'List: {rand_list}')
            if target_index is None:
                print(f'Cannot find {target} in the list')
            else:
                print(f'Found {target} in index {target_index}')
    except ValueError:
        print("Invalid input")