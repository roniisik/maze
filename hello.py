def main():
    list = [[False], []]
    print(any(cell for col in list for cell in col))

    print(len(list))
main()