import sys

# n, m, and p are the unknown digits of y (= *7*0*), from most to least significant
# 1 <= n, m, p <= 9

# 9*111 < 1000, start at 112
for x in range(112, 1000):
  for n in range(1, 10):
    # n*x must be 4 digits
    if n*x < 1000:
      continue

    for m in range(1, 10):
      # m*x must be 3 digits
      if m*x >= 1000:
        continue

      for p in range(1, 10):
        # p*x must be 4 digits
        if p*x < 1000:
          continue

        y = p + 10*0 + 100*m + 1000*7 + 10000*n
        z = x*y

        # z must be 8 digits
        if z >= 10000000 and z < 100000000:
          # the second stage remainder must be 3 digits
          # i.e., the 5 most significant digits of z, minus x times the two most significant digits of y, must be 3 digits
          # so: reduce z from 8 digits to 5, reduce y from 5 digits to 2, and do the above
          if z//1000 - x*(y//1000) >= 100:
            # first stage remainder must be 2 digits (out of order here because i wrote the above first, so sue me)
            if z//10000 - x*(y//10000) < 100:
              # third stage must be 2 digits
              if z//100 - x*(y//10) < 100:
                print z, '/', x, '=', y

