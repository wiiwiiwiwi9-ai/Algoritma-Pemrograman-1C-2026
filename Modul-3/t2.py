n = int(input("Masukkan tinggi menara (2-15): "))

while n < 2 or n > 15:
    print("Tinggi harus 2 sampai 15!")
    n = int(input("Masukkan tinggi menara (2-15): "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()