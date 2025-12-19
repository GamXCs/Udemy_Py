practice_data = [
    "Login",
    "logout",
    "LOGIN",
    "FileUpload",
    "fileupload",
    "FileUpload ",
    " ",
    None,
    "Error",
    "ERROR",
    "Warning",
    "warning",
    "INFO",
    "info",
    "Info",
    "",
    404,
    404,
    500,
    500,
    500,
    "404",
    "500",
    "Timeout",
    "timeout",
    "TIMEOUT",
    " login",
]
count = {}

for ele in practice_data:
    if ele is None:
        continue

    if isinstance(ele, str):
        ele = ele.lower().strip()

    if ele == "":
        continue

    count[ele] = count.get(ele, 0) + 1

data_lst = list(count.items())

# sort data
data_lst.sort(key=lambda x: x[1], reverse=True)

k = 5
top_k = data_lst[:k]
print(top_k)
