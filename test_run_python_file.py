from functions.run_python_file import run_python_file

test_cases = [
    ["calculator", "main.py", []],
    ["calculator", "main.py", ["3 + 5"]],
    ["calculator", "tests.py", []],
    ["calculator", "../main.py", []],
    ["calculator", "nonexistent.py", []],
    ["calculator", "lorem.txt", []],
]


def main():
    for case in test_cases:
        results = run_python_file(case[0], case[1], case[2])

        print(f"{results}")


if __name__ == "__main__":
    main()
