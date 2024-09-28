
def fizzbuzz(n):
    for i in range(n):
        if i != 0:
            if i % 3 == 0:
                print(f"Fizz {i}")
            if i % 5 == 0:
                print(f"Buzz {i}")
            if i % 3 == 0 and i % 5 == 0:
                print(f"Fizz Buzz {i}")


fizzbuzz(6)

