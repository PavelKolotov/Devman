from random import sample

def s(list_, target):
    count = 0
    for i in list_:
        if i != target:
            count += 1
        else:
            break
    return count

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
            if target_index == list_len:
                print(f'Cannot find {target} in the list')
            else:
                print(f'Found {target} in index {target_index}')
    except ValueError:
        print("Invalid input")

