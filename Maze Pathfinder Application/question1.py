def cachedfibonacci(number, dictionary):

    if(number == 1):
        dictionary[number] = 1

    if(number == 2):
        dictionary[number] = 1

    if number in dictionary:
        return(dictionary[number])

    if number not in dictionary:
        value = cachedfibonacci(number-1, dictionary) + cachedfibonacci(number-2, dictionary)
        dictionary[number] = value

    return dictionary[number]

def main():
    dict = {}

    print(cachedfibonacci(100, dict))
    print(cachedfibonacci(10, dict))


if __name__ == "__main__":
    main()