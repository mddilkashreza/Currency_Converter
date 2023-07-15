def main():
    print("This program converts US dollar Nepali")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    nepali = convert_to_nepali(dollars)

    print("That is", nepali, "nepali.")


convert_to_nepali = lambda dollars: dollars * 120

main()