#Assignment 3 
# Function to add two matrices
def add_matrices():
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    matrix1 = []
    matrix2 = []

    print("Enter elements of the first matrix:")
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix1.append(row)

    print("Enter elements of the second matrix:")
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix2.append(row)

    result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(columns)] for i in range(rows)]

    print("Resulting matrix:")
    for row in result_matrix:
        print(row)


# Function to check if one matrix is the rotation of the other
def check_rotation():
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    matrix1 = []
    matrix2 = []

    print("Enter elements of the first matrix:")
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix1.append(row)

    print("Enter elements of the second matrix:")
    for _ in range(columns):
        row = list(map(int, input().split()))
        matrix2.append(row)

    is_rotation = matrix1 == [list(col) for col in zip(*matrix2)]

    if is_rotation:
        print("Matrix 1 is a rotation of Matrix 2.")
    else:
        print("Matrix 1 is not a rotation of Matrix 2.")


# Function to invert a dictionary
def invert_dictionary():
    items = input("Enter key-value pairs in the dictionary (separate each pair with a space): ").split()

    dictionary = {}
    for i in range(0, len(items), 2):
        key = items[i]
        value = items[i + 1]
        dictionary[value] = dictionary.get(value, []) + [key]

    print("Before inverting:")
    print(dictionary)
    print("After inverting:")
    print({value: keys for keys, value in dictionary.items()})


# Function to convert matrix to dictionary
def convert_matrix_to_dictionary():
    print("Enter user data as [First Name, Last Name, ID, Job Title, Company], separated by commas.")
    print("Enter 'exit' to stop entering data.")

    matrix = []
    while True:
        data = input("Enter user data: ")
        if data.lower() == 'exit':
            break
        user_data = data.strip().split(',')
        matrix.append(user_data)

    dictionary = {user_data[2]: user_data[:2] + user_data[3:] for user_data in matrix}

    print("Output:")
    print(dictionary)


# Recursive function to check palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


# Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


# Function to search for an element and sort the list if found
def search_and_sort():
    arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    element = int(input("Enter the element to search for: "))

    index = arr.index(element) if element in arr else -1

    if index == -1:
        print("Element not found.")
    else:
        sorted_list = merge_sort(arr)
        print("Element found at index:", index)
        print("Sorted list:", sorted_list)


def main():
    user_name = input("Enter your name: ")
    print("Welcome, " + user_name + "!")

    while True:
        print("\nMENU:")
        print("1. Add Matrices")
        print("2. Check Rotation")
        print("3. Invert Dictionary")
        print("4. Convert Matrix to Dictionary")
        print("5. Check Palindrome")
        print("6. Search for an Element (BONUS: Search, if element found then sort using merge sort algorithm)")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_matrices()
        elif choice == '2':
            check_rotation()
        elif choice == '3':
            invert_dictionary()
        elif choice == '4':
            convert_matrix_to_dictionary()
        elif choice == '5':
            s = input("Enter a string: ")
            if is_palindrome(s):
                print("It is a palindrome.")
            else:
                print("It is not a palindrome.")
        elif choice == '6':
            search_and_sort()
        elif choice == '7':
            print("Exiting the program. Goodbye, " + user_name + "!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-7).")


if __name__ == "__main__":
    main()
