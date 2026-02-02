from functions.get_files_info import get_files_info

test_cases = [".", "pkg", "/bin", "../"]


def main():
    for case in test_cases:
        if case == ".":
            print("Results for current directory:")
        else:
            print(f"Results for '{case}' directory:")
        results = get_files_info("calculator", case)
        for result in results:
            print(f"  {result}")


if __name__ == "__main__":
    main()
