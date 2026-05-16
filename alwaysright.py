import random

async def main():
    while True:
        hi = await input("What fact would you like to check?: ")
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        d = random.randint(1, 100)
        e = random.randint(1, 100)
        print("That is:", max(a, b, c, d, e), "% right.")
        if (await input("Do you want to convert something else? (y/n)\n")).strip().lower() == "n":
            break

globals()["main"] = main
