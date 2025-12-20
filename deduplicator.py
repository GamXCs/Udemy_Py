"""Take original list and print a new list without duplicates"""

test_data = [
    1,
    2,
    2,
    3,
    1,
    "a",
    "b",
    "a",
    "A",
    "b",
    " ",
    "",
    "",
    None,
    None,
    (1, 2),
    (1, 2),
    [1, 2],
    [1, 2],
    [2, 3],
    {"x": 1, "y": 2},
    {"x": 1, "y": 2},
]


# O(n^2) time complexity
# O(n) space complexity because it's a list
def deduplication(data):
    res = []

    for ele in data:
        if ele not in res:
            res.append(ele)
    return res


# print(deduplication(test_data))

# Use 2 containers
#
data = [1, 2, 2, 3, 1, "a", "a", (1, 2), (1, 2)]


def dedup_better(data):
    res = []
    seen = set()

    for ele in data:
        try:
            hash(ele)  # This will check if the object is hashable

            if ele not in seen:
                res.append(ele)
                seen.add(ele)

        except TypeError:
            if ele not in res:
                res.append(ele)
    return res


print(dedup_better(data))
