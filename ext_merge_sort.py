def sort():
    f1 = open("input/unsorted_1.txt", "r")
    f2 = open("input/unsorted_2.txt", "r")
    f3 = open("input/unsorted_3.txt", "r")
    f4 = open("input/unsorted_4.txt", "r")
    f5 = open("input/unsorted_5.txt", "r")
    f6 = open("input/unsorted_6.txt", "r")
    f7 = open("input/unsorted_7.txt", "r")
    f8 = open("input/unsorted_8.txt", "r")
    f9 = open("input/unsorted_9.txt", "r")
    f10 = open("input/unsorted_10.txt", "r")
    l1 = [int(line) for line in f1.readlines()]
    l2 = [int(line) for line in f2.readlines()]
    l3 = [int(line) for line in f3.readlines()]
    l4 = [int(line) for line in f4.readlines()]
    l5 = [int(line) for line in f5.readlines()]
    l6 = [int(line) for line in f6.readlines()]
    l7 = [int(line) for line in f7.readlines()]
    l8 = [int(line) for line in f8.readlines()]
    l9 = [int(line) for line in f9.readlines()]
    l10 = [int(line) for line in f10.readlines()]
    combined_list = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10
    combined_list.sort()
    out_file = open("output/out_file.txt", "w")
    for i in combined_list:
        out_file.write(str(i) + '\n')
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
    f10.close()
    out_file.close()


if __name__ == "__main__":
    sort()
