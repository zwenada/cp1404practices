STATE_CODES_TO_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}
print(STATE_CODES_TO_NAMES)
state_code = input("Enter a state code: ").upper()
while state_code != "":
    try:
        print(f"{state_code} corresponds to {STATE_CODES_TO_NAMES[state_code]}")
    except KeyError:
        print("Invalid state code")
    state_code = input("Enter a state code: ").upper()

for code, name in STATE_CODES_TO_NAMES.items():
    print(f"{code}: {name}")
