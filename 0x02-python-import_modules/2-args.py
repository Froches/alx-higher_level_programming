#!/usr/bin/python3
def print_args():
    args_num = len(__import__("sys").argv) - 1
    args_list = list(__import__("sys").argv)

    if args_num == 0:
        print("0 arguments.")
    elif args_num == 1:
        print("1 argument:")
        print("{}: {}".format(args_num, args_list[1]))
    elif args_num > 1:
        print("{} arguments:".format(args_num))
        for i in range(1, args_num + 1):
            print("{}: {}".format(i, args_list[i]))


if __name__ == "__main__":
    print_args()
