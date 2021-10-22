# List comprehensions

# %% md
# We want to create a list of powers of two: $2^n$, $n = 0, 1, 2, ...$ <br />
# $1, 2, 4, 8, 32, 64, 128, ...$

# %% codecell

powers_two = []
for n in range(12):
    if (2**n >= 100) and (2**n < 1000):
        powers_two.append(2**n)


print(powers_two)

powers_two_lc = [2**n for n in range(12) if (2**n >= 100) and (2**n < 1000)]

print(powers_two_lc)
