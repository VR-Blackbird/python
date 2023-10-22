import numpy as np


def get_average(days):
    lst = []
    sum_lst = 0
    for day in range(days):
        temp = int(input(f"Enter Day {day+1}'s temperature\n"))
        sum_lst += temp
        lst.append(temp)
    all_temps = np.array(lst)
    avg = sum_lst / len(lst)
    print("Average = ", avg)
    print(f"{len(all_temps[all_temps > avg])} day(s) is above average")



def main():
    days = int(input("Enter number of days: \n"))
    get_average(days)


if __name__ == "__main__":
    main()