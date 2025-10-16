url = "https://www.kaggle.com/datasets"
# TODO: Find the position of the colon (:) to extract protocol
protocol = url[0:5]


# TODO: Find the positions of the dots (.) to locate the start/end of the domain
# print(len(url))
# dot1 = url.find(".")
# print(url.find(".", 12, len(url) - 1))
# print(f"this is dot 1: {dot1}")
# dot2 = ???


# TODO: Use slicing to get the protocol (before :) and the domain (between dots)
protocol = url[0:5]
domain = url[12:18]


# TODO: Find the slash after the domain and slice to get the page part
page = url.find("/", 8, 31)
page = url[22:]

print("Protocol:", protocol)
print("Domain:", domain)
print("Page:", page)
