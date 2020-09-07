import turtle


def applyRules(ch):
    newstr = ""
    if ch == 'L':
        newstr = '+RF-LFL-FR+'  # Rule 1
    elif ch == 'R':
        newstr = '-LF+RFR+FL-'
    else:
        newstr = ch  # no rules apply so keep the character

    return newstr


def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)


# process the rules
def process(old_str):
    new_str = ""
    for ch in old_str:
        new_str = new_str + applyRules(ch)
    return new_str

# instructions
def create_Lstring(iter, axiom):
    start_str = axiom
    end_str = ""
    for i in range(iter):
        end_str = process(start_str)
        start_str = end_str
    return end_str

def main():
    inst = create_Lstring(4, "L")
    t = turtle.Turtle()
    scn = turtle.Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 90, 5)  # draw the picture
    # angle 90, segment length 5
    scn.exitonclick()


main()


