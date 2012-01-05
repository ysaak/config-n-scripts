import sys, shutil

def setProgressImage(iconfile, value):
    value = float(str(value).replace("%", ""))


    ## increm : 6.25 ----> 3,125

    if value < 3.125:
        nf = "00-00"
    elif value <= 9.375:
        nf = "6-25"
    elif value <= 15.625:
        nf = "12-50"
    elif value <= 21.875:
        nf = "18-75"
    elif value <= 28.125:
        nf = "25-00"
    elif value <= 34.375:
        nf = "31-25"
    elif value <= 40.625:
        nf = "37-50"
    elif value <= 46.875:
        nf = "43-75"
    elif value <= 53.125:
        nf = "50-00"
    elif value <= 53.375:
        nf = "56-25"
    elif value <= 65.625:
        nf = "62-50"
    elif value <= 71.875:
        nf = "68-75"
    elif value <= 78.125:
        nf = "75-00"
    elif value <= 84.375:
        nf = "81-25"
    elif value <= 90.625:
        nf = "87-50"
    elif value <= 96.875:
        nf = "93-75"
    else:
        nf = "100-00"

    src = "/Users/ysaak/.geektools/circle_blue/cp_" + nf + ".png"
    dst = "/Users/ysaak/.geektools/" + iconfile + ".png"

    shutil.copyfile(src, dst)

if __name__ == '__main__':
    iconfile = sys.argv[1]
    value = sys.argv[2]

    setProgressImage(iconfile, value)