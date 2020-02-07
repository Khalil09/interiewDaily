def longest_substring_with_k_distinct_characters(s, k):
    hash = {}
    max_length = 0
    bounds = (0, 0)

    for i, char in enumerate(s):
        hash[char] = i

        if len(hash) <= k:
            new_lower_bound = bounds[0]
        else:
            key_to_pop = min(hash, key=hash.get)
            new_lower_bound = hash.pop(key_to_pop) + 1

        bounds = (new_lower_bound, bounds[1] + 1)
        max_length = max(max_length, bounds[1] - bounds[0])

    return max_length

print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
