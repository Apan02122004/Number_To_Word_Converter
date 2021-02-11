def number_handler(n, suffix):
    if n == 0:
        return EMPTY
    if n > 19:
        return TENS[n // 10] + DIGIT[n % 10] + suffix
    else:
        return DIGIT[n] + suffix


def converter(n):
    result = number_handler((n // 10000000) % 100, "Crore ")
    result += number_handler(((n // 100000) % 100), "Lakh ")
    result += number_handler(((n // 1000) % 100), "Thousand ")
    result += number_handler(((n // 100) % 10), "Hundred ")
    if n > 100 and n % 100:
        result += "and "
    result += number_handler((n % 100), "")
    return result


if __name__ == '__main__':
    EMPTY = ""

    DIGIT = [EMPTY, "One ", "Two ", "Three ", "Four ", "Five ", "Six ",
             "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
             "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
             "Seventeen ", "Eighteen ", "Nineteen "]

    TENS = [EMPTY, EMPTY, "Twenty ", "Thirty ", "Forty ", "Fifty ",
            "Sixty ", "Seventy ", "Eighty ", "Ninety "]
    
    try:
        while True:
            value = int(input(' Enter number to convert : '))
            print(converter(value))
    except Exception as E:
        print(E)