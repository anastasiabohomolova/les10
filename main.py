
def func():
    dictionary = {}
    with open('text_random.txt', 'r') as file:

        for line in file:
            words = line.split()

            for i in words:
                if i in dictionary:
                    dictionary[i] += 1
                else:
                    dictionary[i] = 1

    k = sum(dictionary.values())
    print(k)

    return dictionary


n = func()
print(n)












