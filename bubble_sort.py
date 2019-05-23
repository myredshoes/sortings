import random


def bubble_sort(new_list):
    for i in range(len(new_list)-1, 0, -1):
        for j in range(i):
            if new_list[j] > new_list[j+1]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    print('\n', *new_list)


if __name__ == "__main__":
    # new_list = list(map(int,input("Enter list of integers: ").strip().split()))
    number_of_integers = int(input("Enter number of integers: "))
    new_list = []

    for i in range(number_of_integers):
        x = random.randint(-100, 100)
        new_list.append(x)
    print('\n', *new_list)

    bubble_sort(new_list)
