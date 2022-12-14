import csv


def filter_csv(filename):
    """Filters Csv file given based on year or name"""
    if filename.endswith('.csv') is False:
        return "Cancelled"
    try:
        with open(filename, newline='', encoding="utf-8") as file:

            reader = csv.reader(file, delimiter=',')
            print(
                "Would you like to filter by name or year? (Respond with name or year or cancel to quit")

            while True:
                result = input()

                if result == 'name':

                    print(
                        "Please enter a first name and last name (Format: firstname lastname))")
                    while True:
                        response = input()
                        response = response.split(' ')

                        if len(response) != 2:
                            print('Invalid number of parameters. try again')
                        else:
                            matches = list(
                                filter(lambda a: a[0] == response[0] and a[1] == response[1], reader))
                            return matches

                elif result == 'year':

                    print("please enter a year to filter by")
                    response = input()
                    matches = list(
                        filter(lambda a: a[2][0:4] == response, reader))
                    return matches

                elif result == 'cancel':
                    return 'Cancelled'

                else:
                    print('Invalid input, try again.')

    except Exception as exception:
        print(f'Exception: {exception}')


def main():
    """Main Method"""

    print('Please enter filename: ')
    filename = input()

    matches = filter_csv(filename)

    if matches == 'Cancelled':
        print("Cancelled")
        return

    print(f'Matched Users: {matches}')

    try:
        with open('output.csv', 'w', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(matches)
            print('Information written in output.csv file.')
    except Exception as exception:
        print(f'Exception: {exception}')


if __name__ == '__main__':
    main()
