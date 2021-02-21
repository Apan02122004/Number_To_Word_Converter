# Advanced program which convert the number into its word form with using some maths .
def number_handler(n, suffix):
    # Function which sorts the number and its name zero - ninety nine
    if n == 0:
        return EMPTY
    if n > 19:
        return TENS[n // 10] + DIGIT[n % 10] + suffix
    else:
        return DIGIT[n] + suffix


""" Example Calculation :- 
                        n = 51234565 
                        n // 10000000 => 51234565 // 10000000 = 5                  
                        5 % 100 = 5                                                      

                        return value = 5(Five), crore                                     


                        if number is less than a crore value                        10000000 | 2 5 4 5 3 8 7 | 0.254387
                                                                                               2 5 4 5 3 8 7 0 
                                                                                             - 2 0 0 0 0 0 0 0           
                        return value = 5(Five), crore                                            5 4 5 3 8 7 0 
                                                                                                 5 0 0 0 0 0 0
                             n = 2545387                                                       -- This goes on till end
                                n // 10000000 => 2545387 // 10000000 = 0                       and due to flour division
                                0 % 100 = 0                                                    only returns value before                  
                                                                                               decimal place 
                        returns value o,''                                                     return value = 0 
                        if number is greater than One crore                                            
                        We will get two digits from % as remainder                             
    """


# Function which give the number their Unit place value Hundred, Thousand, Crore etc
def converter(n):
    result = number_handler((n // 10000000) % 100, "Crore ")
    result += number_handler(((n // 100000) % 100), "Lakh ")
    result += number_handler(((n // 1000) % 100), "Thousand ")
    result += number_handler(((n // 100) % 10), "Hundred ")
    if n > 100 and n % 100:
        result += "and "
    result += number_handler((n % 100), "")
    return result


while True:
    if __name__ == '__main__':
        # These are the list which are used in the program to assign name to the numbers
        EMPTY = ""

        DIGIT = [EMPTY, "One ", "Two ", "Three ", "Four ", "Five ", "Six ",
                 "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
                 "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
                 "Seventeen ", "Eighteen ", "Nineteen "]

        TENS = [EMPTY, EMPTY, "Twenty ", "Thirty ", "Forty ", "Fifty ",
                "Sixty ", "Seventy ", "Eighty ", "Ninety "]

        try:
            # Taking input values here
            value = int(input(' Enter number to convert : '))
            print(f'NUMBER : {converter(value)}')
        except Exception as E:
            print(E)
