import random


def insertion_sort(new_list):
    for i in range(1, len(new_list)):
        current_number = new_list[i]
        for j in range(i-1, -1, -1):
            if new_list[j] > current_number:
                new_list[j+1] = new_list[j]
                new_list[j] = current_number
    print('\n', *new_list)


if __name__ == "__main__":
    # new_list = list(map(int,input("Enter list of integers: ").strip().split()))
    number_of_integers = int(input("Enter number of integers: "))
    new_list = []

    for i in range(number_of_integers):
        x = random.randint(-100, 100)
        new_list.append(x)
    print('\n', *new_list)

    insertion_sort(new_list)
