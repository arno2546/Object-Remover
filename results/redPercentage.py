from scipy import misc


def picture_to_arr(image):
    arr = misc.imread(image)
    arr_list = arr.tolist()
    r = g = b = 0
    for row in arr_list:
        for item in row:
            r = r+item[0]
            g = g+item[1]
            b = b+item[2]
    total = r+g+b
    red = r/total*100
    green = g/total*100
    blue = b/total*100
    print(total)
    print(r)
    print("the percentage of red content=", red, "%")
    print("the percentage of green content=", green, "%")
    print("the percentage of blue content=", blue, "%")


picture_to_arr('diff.png')
