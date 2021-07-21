import data.texts as texts
from common.name import Name

def main():
    name = Name(input(texts.what_is_your_name))
    print(f"Ahoj {name.get_name5p()}")

if __name__ == "__main__":
    main()
