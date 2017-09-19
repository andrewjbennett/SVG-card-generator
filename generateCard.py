import sys
from cardConstants import *

colorCode = {
        "RED":     "ff5555",
        "BLUE":    "0000ff",
        "GREEN":   "55aa55",
        "YELLOW":  "ffaa00",
        "PURPLE":  "800080"
}

suits = [
    "HEARTS",
    "DIAMONDS",
    "CLUBS",
    "SPADES",
    "QUESTIONS"
]

def main():
    if "IMAGES_PLS" in sys.argv:
        makeAllImages()
        return
    elif len(sys.argv) != 4:
        print "Usage: python %s number color suit" % sys.argv[0]
        print "eg python %s 5 RED HEARTS" % sys.argv[0]
        exit(1)

    number = getNumber(sys.argv[1])
    color = getColor(sys.argv[2])
    suit = getSuit(sys.argv[3])

    if color is None or number is None or suit is None:
        print "invalid input: %s, %s, %s" % (color, number, suit)
        exit(1)

    overall_image = makeImage(number, color, suit)

    with open("test.svg", "w") as outfile:
        outfile.write(overall_image)

def makeAllImages():
    for number in range(16):
        for color in colorCode.iteritems():
            for suit in suits:
                overall_image = makeImage(number, color[1], suit)

                cardname = "card-%s-%d-%s.svg" % (color[0], number, suit)
                with open(cardname, "w") as outfile:
                    outfile.write(overall_image)

def getColor(arg):
    return colorCode.get(arg)

def getNumber(arg):
    try:
        if int(arg) >= 0 and int(arg) <= 15:
            return int(arg)
    except ValueError:
        pass

def getSuit(arg):
    if arg in suits:
        return arg

def makeImage(number, color, suit):
    inner_card = makeInnerCard(number, color, suit)
    overall_image = outer_svg + outer_card + inner_card  + end_svg
    return overall_image

def makeInnerCard(number, color, suit):
    inner_card = (getColorFill(color) + card_white_center +
                  getCardCenterNum(number, color) +
                  getCardTopLeftNum(number) +
                  getCardTopLeftSuit(suit) +
                  getCardBottomRightNum(number) +
                  getCardBottomRightSuit(suit))
    return inner_card

def getColorFill(color):
    return card_color_fill % color

def getCardCenterNum(number, color):
    card_center = card_centers[number]
    if number > 9:
        card_center = newLetters3[number-10]
    return card_center_outer % (color, card_center)

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
    return suits_top[suit]

def getCardBottomRightSuit(suit):
    return suits_bottom[suit]

if __name__ == "__main__":
    main()

