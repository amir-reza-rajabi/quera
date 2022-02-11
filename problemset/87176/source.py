# def game(number):
#     number = list(str(number))

#     number[0] = int(number[0])
#     number[1] = int(number[1])

#     if number[1] > number[0] :
#         tafazol = number[1] - number[0]
#     else :
#         tafazol = number[0] - number[1]
    
#     return tafazol

def game(number):
    # number = list(str(number))
    # for i in range(len(number)):
    #     number[i] = int(number[i])

    number = [int(i) for i in str(number)]

    return number[1] - number[0] if number[1] > number[0] else number[0] - number[1]
    
    

