# Program to convert any number to its word form

DIGITS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eighth', 'Nine', '']
DUAL_DIGITS = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'seventeen', 'Eighteen', 'Nineteen',
               '']
TENS = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', '']
UNITS = ['Hundred', 'Thousand', 'Lakh', 'Crore', '']


# TODO : Remove a bug { The unit places remains even after there is no values before it  }
def word_converter():
    value = list(input('Enter the number you want to calculate : '))
    length = len(value)
    # For ones place
    if length == 1:
        if int(value[0]) == 0:
            print('Zero ')

        else:
            print(DIGITS[int(value[0]) - 1])
    # FOR tens place
    elif length == 2:
        a1 = value[0] + value[1]
        a1 = int(a1)
        if 11 <= a1 <= 19:
            print(DUAL_DIGITS[int(value[1]) - 1])
        else:
            l1 = TENS[int(value[0]) - 1]
            l2 = DIGITS[int(value[1]) - 1]
            print(l1, l2)
    # Hundred place
    elif length == 3:
        a1 = int(value[1] + value[2])
        if a1 == 00:
            l1 = UNITS[0]
            l2 = DIGITS[int(value[0]) - 1]
            print(l2, l1)
        elif 11 <= a1 <= 19:
            l1 = UNITS[0]
            l2 = DIGITS[int(value[0]) - 1]
            l3 = DUAL_DIGITS[int(value[2]) - 1]
            print(l2, l1, l3)
        else:
            l1 = UNITS[0]
            l2 = DIGITS[int(value[0]) - 1]
            l3 = TENS[int(value[1]) - 1]
            l4 = DIGITS[int(value[2]) - 1]
            print(l2, l1, l3, l4)
    # Thousand place
    elif length == 4 or length == 5:
        if length == 4:  # 1411
            a1 = int(value[1] + value[2] + value[3])
            if a1 == 000:
                l1 = UNITS[1]
                l2 = DIGITS[int(value[0]) - 1]
                print(l2, l1)
            elif 11 <= (int(value[2] + value[3])) <= 19:  # 9418
                l1 = UNITS[1]
                l2 = UNITS[0]
                l3 = DIGITS[int(value[0]) - 1]
                l4 = DIGITS[int(value[1]) - 1]
                l5 = DUAL_DIGITS[int(value[3]) - 1]
                print(l3, l1, l4, l2, l5)
            else:  # 1489
                l1 = UNITS[1]
                l2 = DIGITS[int(value[0]) - 1]
                l3 = TENS[int(value[2]) - 1]
                l4 = DIGITS[int(value[3]) - 1]
                l5 = DIGITS[int(value[1]) - 1]
                l6 = UNITS[0]
                print(l2, l1, l5, l6, l3, l4)
        else:
            a1 = int(value[2] + value[3] + value[4])  # 94567
            if a1 == 000:
                if int(value[0]) == 1 and int(value[1]) == 0:
                    l1 = UNITS[1]
                    l2 = TENS[int(value[0]) - 1]
                    print(l2, l1)
                elif 11 <= int(value[0] + value[1]) <= 19:
                    l1 = UNITS[1]
                    l2 = DUAL_DIGITS[int(value[1]) - 1]
                    print(l2, l1)
                elif 19 < int(value[0] + value[1]) <= 99:
                    l1 = TENS[int(value[0]) - 1]
                    l2 = DIGITS[int(value[1]) - 1]
                    l3 = UNITS[1]
                    print(l1, l2, l3)
            elif 11 <= int(value[3] + value[4]) <= 19:  # 94118
                if value[0] == '1' and value[1] == '0':  # 10415
                    l1 = 'Ten'
                    l2 = UNITS[1]
                    l3 = DIGITS[int(value[2]) - 1]
                    l4 = UNITS[0]
                    l5 = DUAL_DIGITS[int(value[4]) - 1]
                    print(l1, l2, l3, l4, l5)
                else:
                    l1 = DUAL_DIGITS[int(value[1]) - 1]
                    l2 = UNITS[1]
                    l3 = DIGITS[int(value[2]) - 1]
                    l4 = UNITS[0]
                    l5 = DUAL_DIGITS[int(value[4]) - 1]
                    print(l1, l2, l3, l4, l5)
            else:
                if value[0] == '1' and value[1] == '0':  # 10455
                    l1 = 'Ten'
                    l2 = UNITS[1]
                    l3 = DIGITS[int(value[2]) - 1]
                    l4 = UNITS[0]
                    l5 = TENS[int(value[3]) - 1]
                    l6 = DIGITS[int(value[4]) - 1]
                    print(l1, l2, l3, l4, l5, l6)
                elif 11 <= int(value[0] + value[1]) >= 19:  # 11455
                    l1 = DUAL_DIGITS[int(value[1]) - 1]
                    l2 = UNITS[1]
                    l3 = DIGITS[int(value[2]) - 1]
                    l4 = UNITS[0]
                    l5 = TENS[int(value[3]) - 1]
                    l6 = DIGITS[int(value[4]) - 1]
                    print(l1, l2, l3, l4, l5, l6)
                else:
                    if int(value[1]) == 0 and int(value[0]) >= 20:
                        l1 = DUAL_DIGITS[int(value[1]) - 1]
                    elif int(value[0] + value[1]) <= 9:
                        l1 = DIGITS[int(value[0])]
                    l2 = UNITS[1]
                    l3 = DIGITS[int(value[2]) - 1]
                    l4 = UNITS[0]
                    l5 = TENS[int(value[3]) - 1]
                    l6 = DIGITS[int(value[4]) - 1]
                    print(l1, l2, l3, l4, l5, l6)
    # Lakh place
    elif length == 6 or length == 7:
        if length == 6:
            a1 = int(value[3] + value[4] + value[5])
            if a1 == 000:  # 100000
                l1 = UNITS[2]
                l2 = DIGITS[int(value[0]) - 1]
                print(l2, l1)
            elif 11 <= (int(value[4] + value[5])) <= 19:  # 109418
                l1 = DIGITS[int(value[3]) - 1]
                l2 = UNITS[1]
                l3 = DUAL_DIGITS[int(value[2]) - 1]
                l4 = UNITS[0]
                l5 = DUAL_DIGITS[int(value[4]) - 1]
                l7 = UNITS[2]
                l8 = DIGITS[int(value[0]) - 1]
                print(l8, l7, l3, l2, l1, l4, l5)
            else:
                l1 = DIGITS[int(value[3]) - 1]
                l2 = UNITS[1]
                l3 = DUAL_DIGITS[int(value[2]) - 1]
                l4 = UNITS[0]
                l5 = TENS[int(value[4]) - 1]
                l6 = DIGITS[int(value[5]) - 1]
                l7 = UNITS[2]
                l8 = DIGITS[int(value[0]) - 1]
                print(l8, l7, l3, l2, l1, l4, l5, l6)
        else:
            a1 = int(value[3] + value[4] + value[5] + value[6])  # 1000000
            if a1 == 00000:
                if int(value[0]) == 1 and int(value[1]) == 0:
                    l1 = UNITS[2]
                    l2 = TENS[int(value[0]) - 1]
                    print(l2, l1)
                elif 11 <= int(value[0] + value[1]) <= 19:
                    l1 = UNITS[2]
                    l2 = DUAL_DIGITS[int(value[1]) - 1]
                    print(l2, l1)
                elif 19 < int(value[0] + value[1]) <= 99:
                    l1 = TENS[int(value[0]) - 1]
                    l2 = DIGITS[int(value[1]) - 1]
                    l3 = UNITS[2]
                    print(l1, l2, l3)
            elif 11 <= int(value[5] + value[6]) <= 19:  # 1000000
                if value[0] == '1' and value[1] == '0':  # 10415
                    l1 = 'Ten'
                    l2 = UNITS[2]
                    l3 = DIGITS[int(value[3]) - 1]
                    l4 = UNITS[1]
                    l6 = TENS[int(value[2]) - 1]
                    l5 = DIGITS[int(value[4]) - 1]
                    l7 = UNITS[0]
                    l8 = DUAL_DIGITS[int(value[6]) - 1]
                    print(l1, l2, l6, l3, l4, l5, l7, l8)
                elif value[0] == '1' and int(value[1]) <= 9:
                    l1 = DUAL_DIGITS[int(value[1]) - 1]
                    l2 = UNITS[2]
                    l3 = DIGITS[int(value[3]) - 1]
                    l4 = UNITS[1]
                    l6 = TENS[int(value[2]) - 1]
                    l5 = DIGITS[int(value[4]) - 1]
                    l7 = UNITS[1]
                    l8 = DUAL_DIGITS[int(value[5]) - 1]
                    print(l1, l2, l6, l3, l4, l5, l7, l8)
                else:
                    l1 = TENS[int(value[0]) - 1]
                    l0 = DIGITS[int(value[1]) - 1]
                    l2 = UNITS[2]
                    l3 = DIGITS[int(value[3]) - 1]
                    l4 = UNITS[1]
                    l6 = TENS[int(value[2]) - 1]
                    l5 = DIGITS[int(value[4]) - 1]
                    l7 = UNITS[1]
                    l8 = DUAL_DIGITS[int(value[6]) - 1]
                    print(l1, l0, l2, l6, l3, l4, l5, l7, l8)
            else:
                if value[0] == '1' and value[1] == '0':  # 10455
                    l1 = 'Ten'
                elif value[0] == '1' and int(value[1]) <= 9:
                    l1 = DUAL_DIGITS[int(value[1]) - 1]
                else:  # 10455
                    l1 = TENS[int(value[0]) - 1]
                    l0 = DIGITS[int(value[1]) - 1]
                l2 = UNITS[2]
                l3 = DIGITS[int(value[3]) - 1]
                l4 = UNITS[1]
                l6 = TENS[int(value[2]) - 1]
                l5 = DIGITS[int(value[4]) - 1]
                l7 = UNITS[1]
                l8 = TENS[int(value[5]) - 1]
                l9 = DIGITS[int(value[6]) - 1]
                try:
                    print(l1, l0, l2, l6, l3, l4, l5, l7, l8, l9)
                except:
                    pass
                    print(l1, l2, l6, l3, l4, l5, l7, l8, l9)
    # Crore
    elif length == 8 or length == 9:
        if length == 8:
            a1 = int(value[5] + value[6] + value[7])
            if a1 == 000:  # 100000
                l1 = UNITS[3]
                l2 = DIGITS[int(value[0]) - 1]
                print(l2, l1)
            elif 11 <= (int(value[6] + value[7])) <= 19:  # 109418
                l1 = DIGITS[int(value[0]) - 1]
                l2 = UNITS[1]
                if int(value[4]) == 0 and int(value[3]) >= 0:
                    l3 = TENS[int(value[3]) - 1]
                elif 0 <= int(value[3] + value[4]) <= 9:
                    l3 = DIGITS[int(value[4]) - 1]
                elif 11 <= int(value[3] + value[4]) <= 19:
                    l3 = DUAL_DIGITS[int(value[4]) - 1]
                elif 20 <= int(value[3] + value[4]) <= 99:
                    l3 = str(TENS[int(value[3]) - 1] + ' ' + DIGITS[int(value[4]) - 1])
                l4 = UNITS[0]
                l5 = DUAL_DIGITS[int(value[7]) - 1]
                l7 = UNITS[2]
                if int(value[1]) == 0 and int(value[2]) >= 0:
                    l8 = TENS[int(value[1]) - 1]
                elif 0 <= int(value[1] + value[2]) >= 9:
                    l8 = DIGITS[int(value[2]) - 1]
                elif 11 <= int(value[1] + value[2]) <= 19:
                    l8 = DUAL_DIGITS[int(value[2]) - 1]
                elif 20 <= int(value[1] + value[2]) <= 99:
                    l8 = str(TENS[int(value[1]) - 1] + ' ' + DIGITS[int(value[2]) - 1])
                l9 = DIGITS[int(value[0]) - 1]
                l10 = UNITS[3]
                print(l9, l10, l8, l7, l3, l2, l1, l4, l5)
            else:
                l1 = DIGITS[int(value[5]) - 1]
                l2 = UNITS[1]
                if int(value[4]) == 0 and int(value[3]) >= 0:
                    l3 = TENS[int(value[3]) - 1]
                elif 0 <= int(value[3] + value[4]) <= 9:
                    l3 = DIGITS[int(value[4]) - 1]
                elif 11 <= int(value[3] + value[4]) <= 19:
                    l3 = DUAL_DIGITS[int(value[4]) - 1]
                elif 20 <= int(value[3] + value[4]) <= 99:
                    l3 = str(TENS[int(value[3]) - 1] + ' ' + DIGITS[int(value[4]) - 1])
                l4 = UNITS[0]
                if int(value[6]) == 0:
                    l5 = DIGITS[int(value[7]) - 1]
                else:
                    l5 = str(DUAL_DIGITS[int(value[6]) - 1] + ' ' + DIGITS[int(value[7]) - 1])
                l7 = UNITS[2]
                if int(value[1]) == 0 and int(value[2]) <= 9:
                    l8 = TENS[int(value[1]) - 1]
                elif 0 <= int(value[1] + value[2]) <= 9:
                    l8 = DIGITS[int(value[2]) - 1]
                elif 11 <= int(value[1] + value[2]) <= 19:
                    l8 = DUAL_DIGITS[int(value[2]) - 1]
                elif 20 <= int(value[1] + value[2]) <= 99:
                    l8 = str(TENS[int(value[1]) - 1] + ' ' + DIGITS[int(value[2]) - 1])
                l9 = DIGITS[int(value[0]) - 1]
                l10 = UNITS[3]
                print(l9, l10, l8, l7, l3, l2, l1, l4, l5)
        else:
            a1 = int(value[3] + value[4] + value[5] + value[6] + value[7])  # 1000000
            if a1 == 00000:
                if int(value[0]) == 1 and int(value[1]) == 0:
                    l1 = UNITS[3]
                    l2 = TENS[int(value[0]) - 1]
                    print(l2, l1)
                elif 11 <= int(value[0] + value[1]) <= 19:
                    l1 = UNITS[3]
                    l2 = DUAL_DIGITS[int(value[1]) - 1]
                    print(l2, l1)
                elif 19 < int(value[0] + value[1]) <= 99:
                    l1 = TENS[int(value[0]) - 1]
                    l2 = DIGITS[int(value[1]) - 1]
                    l3 = UNITS[3]
                    print(l1, l2, l3)
            elif 11 <= int(value[7] + value[8]) <= 19:  # 1000000
                if value[0] == '1' and value[1] == '0':  # 10415
                    l9 = 'Ten'
                elif value[0] == '1' and int(value[1]) <= 9:
                    l9 = DUAL_DIGITS[int(value[1]) - 1]
                else:
                    l9 = TENS[int(value[0]) - 1]
                    l0 = DIGITS[int(value[1]) - 1]
                l1 = DIGITS[int(value[0]) - 1]
                l2 = UNITS[1]
                if int(value[4]) == 0 and int(value[3]) >= 0:
                    l3 = TENS[int(value[3]) - 1]
                elif 0 <= int(value[3] + value[4]) <= 9:
                    l3 = DIGITS[int(value[4]) - 1]
                elif 11 <= int(value[3] + value[4]) <= 19:
                    l3 = DUAL_DIGITS[int(value[4]) - 1]
                elif 20 <= int(value[3] + value[4]) <= 99:
                    l3 = str(TENS[int(value[3]) - 1] + ' ' + DIGITS[int(value[4]) - 1])
                l4 = UNITS[0]
                l5 = DUAL_DIGITS[int(value[7]) - 1]
                l7 = UNITS[2]
                if int(value[1]) == 0 and int(value[2]) >= 0:
                    l8 = TENS[int(value[1]) - 1]
                elif 0 <= int(value[1] + value[2]) >= 9:
                    l8 = DIGITS[int(value[2]) - 1]
                elif 11 <= int(value[1] + value[2]) <= 19:
                    l8 = DUAL_DIGITS[int(value[2]) - 1]
                elif 20 <= int(value[1] + value[2]) <= 99:
                    l8 = str(TENS[int(value[1]) - 1] + ' ' + DIGITS[int(value[2]) - 1])
                l10 = UNITS[3]
                print(l9, l0, l10, l8, l7, l3, l2, l1, l4, l5)
            else:
                if value[0] == '1' and value[1] == '0':  # 10415
                    l9 = 'Ten'
                elif value[0] == '1' and int(value[1]) <= 9:
                    l9 = DUAL_DIGITS[int(value[1]) - 1]
                else:
                    l9 = TENS[int(value[0]) - 1]
                    l0 = DIGITS[int(value[1]) - 1]
                l1 = DIGITS[int(value[0]) - 1]
                l2 = UNITS[1]
                if int(value[4]) == 0 and int(value[3]) >= 0:
                    l3 = TENS[int(value[3]) - 1]
                elif 0 <= int(value[3] + value[4]) <= 9:
                    l3 = DIGITS[int(value[4]) - 1]
                elif 11 <= int(value[3] + value[4]) <= 19:
                    l3 = DUAL_DIGITS[int(value[4]) - 1]
                elif 20 <= int(value[3] + value[4]) <= 99:
                    l3 = str(TENS[int(value[3]) - 1] + ' ' + DIGITS[int(value[4]) - 1])
                l4 = UNITS[0]
                if value[0] == '1' and value[1] == '0':  # 10415
                    l5 = 'Ten'
                elif value[0] == '1' and int(value[1]) <= 9:
                    l5 = DUAL_DIGITS[int(value[1]) - 1]
                else:
                    l5 = TENS[int(value[0]) - 1]
                    l10 = DIGITS[int(value[1]) - 1]
                l7 = UNITS[2]
                if int(value[1]) == 0 and int(value[2]) >= 0:
                    l8 = TENS[int(value[1]) - 1]
                elif 0 <= int(value[1] + value[2]) >= 9:
                    l8 = DIGITS[int(value[2]) - 1]
                elif 11 <= int(value[1] + value[2]) <= 19:
                    l8 = DUAL_DIGITS[int(value[2]) - 1]
                elif 20 <= int(value[1] + value[2]) <= 99:
                    l8 = str(TENS[int(value[1]) - 1] + ' ' + DIGITS[int(value[2]) - 1])
                try:
                    print(l9, l0, l10, l8, l7, l3, l2, l1, l4, l5)
                except:
                    pass
                    print(l9, l10, l8, l7, l3, l2, l1, l4, l5)


if __name__ == '__main__':
    try:
        while True:
            word_converter()
    except Exception as E:
        print(E)

    '''
    Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        print_hi('PyCharm')

    '''
