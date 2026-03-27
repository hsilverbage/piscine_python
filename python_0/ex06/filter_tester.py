from ft_filter import ft_filter

def even_or_odd(n: any)-> bool:
    return (n % 2 == 0)

def main():
    numbers = [1,2,3,4,5]
    words = ["test", "ok", "soleil", "a", "nul"]

    print("TEST 1:")
    result = ft_filter(even_or_odd, numbers)
    for res in result:
        print(res)

    print("TEST 2:")
    greater_than_5 = list(ft_filter(lambda x: x > 3, numbers))
    print(greater_than_5)

    print("TEST 3:")
    words_greater_than_2_char = list(ft_filter(lambda x: len(x) > 2, words))
    print(words_greater_than_2_char)

if __name__ == "__main__":
    main()

