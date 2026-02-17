def get_even(nums):
    return [num for num in nums if num % 2 == 0]


def get_odd(nums):
    return [num for num in nums if num % 2 == 1]


def compute_mean(nums):
    return sum(nums) / len(nums)


def compute_median(nums):
    # check is list is empty
    if len(nums) == 0:
        raise ValueError("List must contain numbers")

    # check for correct list type among elements
    for num in nums:
        if not isinstance(num, (int, float)):
            raise TypeError("List must contain only int's and float's")

    # sort list
    sorted_list = sorted(nums)

    # get length of list
    n = len(sorted_list)

    # odd num of items in a list
    if n % 2 == 1:
        return sorted_list[n // 2]  # return middle item
    else:
        right = sorted_list[n // 2]
        left = sorted_list[n // 2 - 1]
        return (right + left) / 2


def summarize(nums):

    if len(nums) == 0:
        raise ValueError("List must contain numbers")

    for num in nums:
        if not isinstance(num, (int, float)):
            raise TypeError("Number must be an int or float")

    summary = {
        "even": get_even(nums),
        "odd": get_odd(nums),
        "mean": compute_mean(nums),
        "median": compute_median(nums),
    }
    return summary


def main():
    # nums = [1, 2, 3, 4]
    # nums = [1.5, 2.5, 3.5]
    # nums = [1, "x", 3]
    nums = []
    summary = summarize(nums)
    print(summary)


if __name__ == "__main__":
    main()
