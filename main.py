# UPDATE NOTE: To update categories and options, refer to main() and calculateAndDisplayCost()

def getAndValidateInput(choices):
    # Makes the little choice guide that goes in parentheses using all available choices
    choiceGuideText = "/".join(choices)

    # Get Input
    userChoice = input(f"Enter your choice({choiceGuideText}): ").upper()

    # Validate Input
    while userChoice not in choices:
        print("\nInvalid Selection. Please try again. \n")
        userChoice = input(f"Enter your choice({choiceGuideText}): ").upper()

    return userChoice

def getPriceFromChoice(choices, prices, userChoice):
    # Returns price based on choice
    for i in range(len(choices)):
        if userChoice == choices[i]:
            return prices[i]

def displayAndSelectOption(categoryPrompt, optionText, choices, prices):
    # Display Options
    print(categoryPrompt)
    choiceDivider = ")"
    for i in range(len(optionText)):
        print(f"{choices[i]}{choiceDivider:2}{optionText[i]:<26}- ${prices[i]:8.2f}")

    # Select Option
    userChoice = getAndValidateInput(choices)

    return getPriceFromChoice(choices, prices, userChoice)

def calculateAndDisplayCost(basePrice, monitorPrice, interfacePrice, microphonePrice):

    totalCost = basePrice + monitorPrice + interfacePrice + microphonePrice

    # Display Formatting

    print() # line break

    priceLabels = ["Base price: ", "Monitor Price: ", "Interface Price: ", "Microphone Price: ", "Total Cost with accessories: "]
    priceValues = [basePrice, monitorPrice, interfacePrice, microphonePrice, totalCost]
    divider = "-"*10

    for i in range(len(priceValues)):

        # Divide price breakdown from total with dashes
        if priceValues[i] == totalCost:
            print(f"{divider:>40}")

        print(f"{priceLabels[i]:30}${priceValues[i]:9,.2f}")

def calculateAndDisplayCost(basePrice, optionsPrice):

    totalCost = basePrice + sum(optionsPrice)

    # Display Formatting

    print() # line break

    # When adding a new category, add a label in priceLabels
    priceLabels = [
        "Base price: ",
        "Monitor Price: ",
        "Interface Price: ",
        "Microphone Price: ",
        "Headphone Price: ",
        "Total Cost with accessories: "
    ]

    # Creates priceValues array for you to make updates easier
    priceValues = []

    for i in range(len(optionsPrice) + 2):
        if i == 0:
            priceValues.append(basePrice)
        if i >= 1:
            try:
                priceValues.append(optionsPrice[i-1])
            except:
                priceValues.append(totalCost)
                break

    divider = "-"*10

    for i in range(len(priceValues)):

        # Divide price breakdown from total with dashes
        if priceValues[i] == totalCost:
            print(f"{divider:>40}")

        print(f"{priceLabels[i]:30}${priceValues[i]:9,.2f}")

def main():

    print("Welcome to the studio sound system price calculator")

    basePrice = 500


    optionsPrice = [
        displayAndSelectOption(
            "\nStudio Monitor options: ",
            ["5-inch monitors", "8-inch monitors", "Full range + Subwoofers"],
            ["S", "M", "L"],
            [350, 800, 2500]
        ),
        displayAndSelectOption(
            "\nAudio Interface options: ",
            ["Basic Interface", "Professional Interface", "Advanced Interface"],
            ["B", "P", "A"],
            [100, 500, 2000]
        ),
        displayAndSelectOption(
            "\nMicrophone options: ",
            ["Dynamic Microphone", "Condenser Microphone"],
            ["D", "C"],
            [100, 350]
        ),
        displayAndSelectOption(
            "\nHeadphone options: ",
            ["Wire-In", "Bluetooth", "High-End"],
            ["W", "B", "H"],
            [40, 120, 300]
        )
    ]

    calculateAndDisplayCost(basePrice, optionsPrice)

main()

# I had a lot of fun working on this.
# I really enjoyed using a proper problem-solving process to break down the program into something that is easier to update if needed.
# It was really kind of enjoyable to come up with better ways to do things. I've left old code commented at the bottom
# to show code parts I refactored overtime into the full project. Thank you.

# Old Code showing my refactoring work

# Old code from main()
    # ...
    # monitorPrice = selectMonitors()
    # interfacePrice = selectInterface()
    # microphonePrice = selectMicrophone()

    # optionsPrice = [selectMonitors(), selectInterface(), selectMicrophone()]

    # NOTE: Use this variable to modify or add more options and categories

# Old code from getAndValidateInput()
# Replaced by learning about the join function
    # ...
    # choiceGuideText = ""
    # for i in range(len(choices)):
    #     choiceGuideText += choices[i]
    #     if i != len(choices) - 1:
    #         choiceGuideText += "/"

# Old function to displayOptions now added in displayAndSelectOption()
# def displayOptions(choices, prices, categoryPrompt, optionText):
#     print(categoryPrompt)
#     choiceDivider = ")"
#     for i in range(len(optionText)):
#         print(f"{choices[i]}{choiceDivider:2}{optionText[i]:<26}- ${prices[i]:8.2f}")

# Old option select functions
# def selectMonitors():
#
#     choices = ["S", "M", "L"]
#     prices = [350, 800, 2500]
#     optionText = ["5-inch monitors", "8-inch monitors", "Full range + Subwoofers"]
#
#     print("\nStudio Monitor options: ")
#
#     # Old options display
#     # print("S) 5-inch monitors         - $350")
#     # print("M) 8-inch monitors         - $800")
#     # print("L) Full range + Subwoofers - $2500")
#
#     displayOptions(choices, prices, optionText)
#
#     # Old Validation Code
#     # userChoice = input("Enter your choice(S/M/L): ")
#     # while userChoice not in choices:
#     #     print("\nInvalid Selection. Please try again. \n")
#     #     userChoice = input("Enter your choice(S/M/L): ")
#
#     # Old if block
#     # if userChoice == "S":
#     #     return 150
#     # elif userChoice == "M":
#     #     return 400
#     # elif userChoice == "L":
#     #     return 2500
#     # else:
#     #     print("ERROR: validation problem occurred")
#
#     userChoice = getAndValidateInput(choices)
#     return getPriceFromChoice(choices, prices, userChoice)
#
# def selectInterface():
#
#     choices = ["B", "P", "A"]
#     prices = [100, 500, 2000]
#
#     print("\nAudio Interface options: ")
#     optionText = ["Basic Interface", "Professional Interface", "Advanced Interface"]
#
#     # Old options display
#     # print("B) Basic Interface        - $100")
#     # print("P) Professional Interface - $500")
#     # print("A) Advanced Interface     - $2000")
#
#     displayOptions(choices, prices, optionText)
#
#     # Old Code
#     # userChoice = input("Enter your choice(B/P/A): ")
#     # while userChoice not in choices:
#     #     print("\nInvalid Selection. Please try again. \n")
#     #     userChoice = input("Enter your choice(B/P/A): ")
#
#     # Old if block
#     # if userChoice == "B":
#     #     return 100
#     # elif userChoice == "P":
#     #     return 500
#     # elif userChoice == "A":
#     #     return 2000
#     # else:
#     #     print("ERROR: validation problem occurred")
#
#     userChoice = getAndValidateInput(choices)
#     return getPriceFromChoice(choices, prices, userChoice)
#
# def selectMicrophone():
#
#     choices = ["D", "C"]
#     prices = [100, 350]
#
#     print("\nMicrophone options: ")
#     optionText = ["Dynamic Microphone", "Condenser Microphone"]
#
#     # Old options display
#     # print("D) Dynamic Microphone   - $100")
#     # print("C) Condenser Microphone - $350")
#
#     displayOptions(choices, prices, optionText)
#
#     # Old Code
#     # userChoice = input("Enter your choice(D/C): ")
#     # while userChoice not in choices:
#     #     print("\nInvalid Selection. Please try again. \n")
#     #     userChoice = input("Enter your choice(D/C): ")
#
#     # Old if block
#     # if userChoice == "D":
#     #     return 100
#     # elif userChoice == "C":
#     #     return 350
#     # else:
#     #     print("ERROR: validation problem occurred")
#
#     userChoice = getAndValidateInput(choices)
#     return getPriceFromChoice(choices, prices, userChoice)

# Old Code from calculateAndDisplayCost()
    # ...
    # print(f"\nBase Price: ${basePrice:9,.2f}")
    # print(f"Monitor Price: ${monitorPrice:9,.2f}")
    # print(f"Interface Price: ${interfacePrice:9,.2f}")
    # print(f"Microphone Price: ${microphonePrice:9,.2f}")
    # print(f"\nTotal Cost with accessories: ${totalCost:9,.2f}")