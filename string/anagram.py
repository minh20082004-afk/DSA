def isAnagram(s, t):
    # Method 1: count characters (currently implemented below)
    # Another common approach is to sort both strings and compare them directly.
    # Examples:
    #   sorted_s = sorted(s)
    #   sorted_t = sorted(t)
    #   if sorted_s == sorted_t:
    #       return True
    # Sorting is O(n log n) while counting can be O(n), but sorted version is
    # simple and useful for short strings or when readability is prioritized.

    if len(s) != len(t):
        return False
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1    
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]
    return len(count) == 0   
    