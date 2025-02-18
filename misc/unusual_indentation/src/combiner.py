from itertools import zip_longest


main = open("./meow/src/meow.rs").readlines()
anotherone = open("unusual_indentation.ws").readlines()

result = ""
for m,a in zip_longest(main, anotherone, fillvalue=""):
    result += a[:-1]
    result += m[:-1]
    result += "\n"

result_file = open("result.rs", "x")
result_file.write(result)


