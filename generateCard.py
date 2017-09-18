import sys
from cardConstants import *

colors = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE"]
colorCode = {
        "RED":     "ff5555",
        "BLUE":    "0000ff",
        "GREEN":   "55aa55",
        "YELLOW":  "ffaa00",
        "PURPLE":  "800080"
}


def main():
    makeAllImages()
    if len(sys.argv) != 3:
        print "Usage: python %s number color" % sys.argv[0]
        print "eg python %s 5 RED" % sys.argv[0]
        exit(1)

    number = getNumber(sys.argv[1])
    color = getColor(sys.argv[2])

    if color is None or number is None:
        print "invalid input"
        exit(1)


    overall_image = makeImage(number, color)

    with open("test.svg", "w") as outfile:
        outfile.write(overall_image)

def makeAllImages():
    for number in range(0,16):
        for color in colors:
            overall_image = makeImage(number, color)

            cardname = "card-%s-%d.svg" % (color, number)
            with open(cardname, "w") as outfile:
                outfile.write(overall_image)



def getColor(arg):
    if arg in colors:
        return arg
    else:
        return None

def getNumber(arg):
    try:
        if int(arg) >= 0 and int(arg) <= 15:
            return int(arg)
        else:
            return None
    except:
        return None


def makeImage(number, color):
    inner_card = makeInnerCard(number, color)

    overall_image = outer_svg + outer_card + inner_card  + end_svg

    return overall_image

def makeInnerCard(number, color):
    inner_card = getColorFill(color) + card_white_center + \
            getCardCenterNum(number, color) + getCardTopLeftNum(number) + \
            getCardBottomRightNum(number)

    return inner_card

def getColorFill(color):
    return card_color_fill % colorCode[color]

def getCardCenterNum(number, color):
    card_center = card_centers[number]
    if number > 9:
        card_center = newLetters3[number-10]
    return card_center_outer % (colorCode[color], card_center)

def getCardTopLeftNum(number):
    thing = card_topleft_outer % topleft[number]
    if number > 9:
        return matrix_transform_upper + card_topleft_outer % \
        newLetters3[number-10] + matrix_close_group
    else:
        return thing

def getCardBottomRightNum(number):
    if number > 9:
        return matrix_transform_lower + card_bottomright_outer % \
        newLetters3[number-10] + matrix_close_group
    return card_bottomright_outer % bottomright[number]

if __name__ == "__main__":
    main()

