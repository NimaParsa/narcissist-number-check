def narcissistic(value):
    mvalue = value
    new_value = 0
    chars_no = len(str(mvalue))
    no = chars_no

    while chars_no > 0 :
        h = (10 ** (chars_no-1))
        f = int(mvalue / h)
        new_value += f ** no
        mvalue = mvalue - h * f
        chars_no -= 1

    if new_value == value:
        print("True")
    else:
        print("False")


narcissistic(int(input("Enter a number to ch12eck if its Narcissistic number or not: ")))