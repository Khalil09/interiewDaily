def isSorted(words, order):
    dict_order = {}

    for i, c in enumerate(order): # O(k) where k is the order size
        dict_order[c] = i

    sum_order = []
    for word in words: # O(len(words)*biggest(Word))
        word_sum = 0
        for c in word:
            word_sum += dict_order[c]

        sum_order.append([word_sum])

    for i in range(len(sum_order)-1): # O(len(words))
        if sum_order[i] > sum_order[i+1]:
            return False

    return True


print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True
