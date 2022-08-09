import  csv
import  json

def readCSV():
    file = open('iso_countries.csv', encoding="utf8")
    reader = csv.reader(file)
    data = [rows for rows in reader]
    return data

def readJSON():
    file = open("vn-provinces.json", "r")
    data = json.load(file)
    return data

def getCountries(s: str) -> str:
    data = readCSV()
    for i in range(196):
        if s == data[i][1]:
            return data[i][3]
    return "Nothing"

def getProvinces(s: str) -> str:
    data = readJSON()
    return data[str(int(s))]

def getBorn(s: str) -> str:
    if (s[0] == "0"):
        return getProvinces(s)
    return getCountries(s)

def getBirth(s: str) -> int:
    year = int(s[1:])
    if (int(s[0]) % 2 == 1):
        century = int((int(s[0]) - 1)/2)*100 + 1900
        sex = "Female"
    else:
        century = int(int(s[0])/2)*100 + 1900
        sex = "Male"
    birth = century + year
    return [sex, birth]

def getID():
    perID = input("Enter ID: ")
    perID = [perID[:3], perID[3:6], perID[6:]]
    return perID

def run():
    perID = getID()

    print("\nINFO\t\t\t\t|\t VALUE")
    print("-------------------------------------------------")
    print("Birth registration place\t|\t", getBorn(perID[0]))
    print("Birthyear\t\t\t|\t", getBirth(perID[1])[1])
    print("Gender\t\t\t\t|\t", getBirth(perID[1])[0])
    print("Random number\t\t\t|\t", perID[2])


if __name__ == '__main__':
    run()
