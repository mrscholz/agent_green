from functions.get_file_content import get_file_content

test_cases = [
    "lorem.txt",
    "main.py",
    "pkg/calculator.py",
    "/bin/cat",
    "pkg/doesnotexist.py",
]


def main():
    for case in test_cases:
        results = get_file_content("calculator", case)

        print(f"{results}")


if __name__ == "__main__":
    main()
