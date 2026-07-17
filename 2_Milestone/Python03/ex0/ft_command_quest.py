import sys

print("=== Command Quest ===")
print("Program name:", sys.argv[0])
num_args = len(sys.argv) - 1

if num_args == 0:
    print("No arguments provided!")
else:
    print("Arguments received:", num_args)

    i = 1
    while i < len(sys.argv):
        print("Argumnent", i, ":", sys.argv[i])
        i += 1

print("Total arguments:", len(sys.argv))
