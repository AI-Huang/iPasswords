from src.ios import generate_default_password


def main():
    print("Hello from ipasswords!")

    pwd = generate_default_password()
    print(f"pwd: {pwd}")


if __name__ == "__main__":
    main()
