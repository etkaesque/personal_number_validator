import csv

with open('./testing.csv', 'r') as data_file:
    reader = csv.reader(data_file)

    for row in reader:

        personalCode = row[0]

        if personalCode[0] != "3" and personalCode[0] != "4" and personalCode[0] != "5" and personalCode[0] != "6":
            print(personalCode + ' This one is neither 3,4,5,6. ')

        if len(personalCode) > 11:
            print(personalCode + " This one is longer than 11")

        if len(personalCode) < 11:
            print(personalCode + " This one is smaller than 11")

        if not personalCode.isdigit():
            print(personalCode + " This one is has letter in it")

        if int(personalCode[3:5]) > 12 or int(personalCode[3:5]) < 1:
            print(personalCode + " mėnesis yra:" + personalCode[3:5])

        if int(personalCode[5:7]) > 31 or int(personalCode[3:5]) < 1:
            print(personalCode + " diena yra:" + personalCode[5:7])

        counter = 1
        numbers = []

        for number in personalCode:

            if counter == 10:
                numbers.append(int(number))
                break
            else:
                result = int(number)*counter
                numbers.append(result)
                counter += 1

        remainder = sum(numbers) % 11

        if remainder > 10:
            print("remainder is more than 10")

        if remainder != 10:
            if remainder != int(personalCode[-1]):
                print(
                    f"remainder {remainder} is not the same as {int(personalCode[-1])} in: " + personalCode)
        elif remainder == 10:
            counter = 3
            iteration = 1
            numbers = []

            for num in personalCode:
                if iteration == 2 and counter == 4:
                    break
                if counter == 10:
                    counter = 1
                    iteration += 1

                result = int(num)*counter
                numbers.append(result)
                counter += 1

            remainder = sum(numbers) % 11

            if remainder > 10:
                print("remainder is more than 10")

            if remainder != 10:
                if remainder != int(personalCode[-1]):
                    print(
                        f"remainder {remainder} not the same as {int(personalCode[-1])} in: " + personalCode)
            elif remainder == 10:
                if int(personalCode[-1]) != 0:
                    print(f"remainder is {remainder}, but last digit is not zero: " + personalCode)

    data_file.close()
