
def isPalindrome(x: int) -> bool:

        t = []

        i = 1
        counter = 0
        while True:
            val = x // i % 10
            if i > x:
                break
            t.append((val))
            i = i * 10

        rev = []

        # for i, _ in enumerate(t):
        #     rev.append(t[-(i+1)])

        for i in range(1, len(t) + 1):
            rev.append(t[-i])

        import pdb;pdb.set_trace()

        if rev == t:
            return True
        return False


print(isPalindrome(10))




