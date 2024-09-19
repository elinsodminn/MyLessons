
def all_variants(text):
    n = len(text)

    for start in range(n):

        for length in range(1, n - start + 1):
            
            yield text[start:start + length]

a = all_variants('abc')
for i in a:
    print(i)
