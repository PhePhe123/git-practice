def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    largest_number = max(numbers)
    return largest_number


    for val in numbers:
        if val > highest_value:
            highest_value = val
        

if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
