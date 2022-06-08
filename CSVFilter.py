import sys

# Handles any invalid date input and returns a valid 8-digit birth year
def dateSelect():
    while True:
        filterInput = input("Enter birth year (YYYYMMDD) to filter:\n")
        try:
            if len(filterInput) == 8 and filterInput.isdigit():
                return filterInput
            else:
                print("Invalid birth year, please enter a birth year following the format (YYYYMMDD)")
        except:
            print("Invalid birth year, please enter a birth year following the format (YYYYMMDD)")
                
    
# Handles any invalid filter selection including non-integers
def numberSelect():
    while True:
        filterNumber = input("Please select (1-3) how you want to filter:\n1) First Name\n2) Last Name\n3) Birth Year\n")
        try:
            if int(filterNumber) > 0 and int(filterNumber) < 4:
                return int(filterNumber)
            else:
                print("Invalid selection, please choose a number from 1-3")
        except:
            print("Invalid selection, please choose a number from 1-3")
            
# Opens the CSV file, splits up file by lines, and matches based on filter input
# Also handles any invalid CSV files
# file - String, holds CSV file name
# filterNumber - int, holds filter type selection
# filterInput - String, holds the user's specific filter
def filterFile(file, filterNumber, filterInput):
    while True:
        try:
            with open("CSVFiles/" + file) as filepath:
                fileline = filepath.read().splitlines()
                matchCount = 0
                for line in fileline:
                    line = line.split(",")
                    if line[filterNumber - 1].lower() == filterInput.lower():
                        print(line)
                        matchCount += 1
                if matchCount == 0:
                    print("There is no matches based on the given filter")
                return
        except:
            print(file + " is not a valid csv file")
            sys.exit()
            
if __name__ == "__main__":
    file = input("Please enter the csv file you want to parse:\n")
    filterNumber = numberSelect()

    if filterNumber == 1 or filterNumber == 2:
        filterInput = input("Enter name to filter:\n")
    else:
        filterInput = dateSelect()
    
    filterFile(file, filterNumber, filterInput)
        
    
        
