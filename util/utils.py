# A simple seperator
def examples_separator(example_name="", start=60, end=20):
    if not example_name:
        print()
        print("*"*start)
    else:
        print("*"*end, "Eg.", example_name, "*"*end)