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

suits = {
        "HEARTS":0,
        "DIAMONDS":1,
        "CLUBS":2,
        "SPADES":3,
        "QUESTIONS":4
}


def main():
    makeAllImages()
    if len(sys.argv) != 4:
        print "Usage: python %s number color suit" % sys.argv[0]
        print "eg python %s 5 RED HEARTS" % sys.argv[0]
        exit(1)

    number = getNumber(sys.argv[1])
    color = getColor(sys.argv[2])
    suit = getSuit(sys.argv[3])

    if color is None or number is None or suit is None:
        print color
        print number
        print suit
        print "invalid input"
        exit(1)


    overall_image = makeImage(number, color, suit)

    with open("test.svg", "w") as outfile:
        outfile.write(overall_image)

def makeAllImages():
    for number in range(0,16):
        for color in colors:
            for suit in suits.iterkeys():
                overall_image = makeImage(number, color, suit)

                cardname = "card-%s-%d-%s.svg" % (color, number, suit)
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
    except:
        pass
    return None

def getSuit(arg):
    if arg in suits.iterkeys():
        return arg
    else:
        return None


def makeImage(number, color, suit):
    inner_card = makeInnerCard(number, color, suit)

    overall_image = outer_svg + outer_card + inner_card  + end_svg

    return overall_image

def makeInnerCard(number, color, suit):
    inner_card = getColorFill(color) + card_white_center + \
            getCardCenterNum(number, color) + \
            getCardTopLeftNum(number) + \
            getCardTopLeftSuit(suit) + \
            getCardBottomRightNum(number) + \
            getCardBottomRightSuit(suit)

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

def getCardTopLeftSuit(suit):
    return suits_top[suits[suit]]

def getCardBottomRightSuit(suit):
    return suits_bottom[suits[suit]]

if __name__ == "__main__":
    main()

