from functions.write_file import write_file

test_cases = [
    ["calculator", "lorem.txt", "wait, this isn't lorem ipsum"],
    ["calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"],
    ["calculator", "/tmp/temp.txt", "this should not be allowed"],
]


def main():
    for case in test_cases:
        results = write_file(case[0], case[1], case[2])

        print(f"{results}")


if __name__ == "__main__":
    main()
