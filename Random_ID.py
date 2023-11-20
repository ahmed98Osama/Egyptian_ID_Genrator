import random

# Egyptian governorate codes and names
states = {
    "01": "Cairo",
    "02": "Alexandria",
    "03": "Port Said",
    "04": "El Suez",
    "11": "DOMIATTA",
    "12": "El Dakhalia",
    "13": "El Shariqia",
    "14": "El Qilubia",
    "15": "KAFR ALSHEKH",
    "16": "ALGHRBIH",
    "17": "ALMNOUFIH",
    "18": "El Bahira",
    "19": "ALASMAEILIH",
    "21": "El Giza",
    "22": "Beny Souif",
    "23": "ALFAYOM",
    "24": "ALMNIA",
    "25": "Asuit",
    "26": "Sohag",
    "27": "Qena",
    "28": "Aswan",
    "29": "Luxor",
    "31": "ALBHR ALAHMR",
    "32": "El Waadi El Gedid",
    "33": "Marsa Matrouh",
    "34": "North Sinai",
    "35": "South Sinai",
    "88": "Not Born in Egypt",
}

# Weights for check digit calculation
weights = [2, 7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

def generate_id_without_check_digit():
    # Random year 1950-2005
    year = str(random.randint(1950, 2005))


    # Set first digit based on the year
    first_digit = "3" if int(year) >= 2000 else "2"


    # Random month 1-12
    month = str(random.randint(1, 12)).zfill(2)

    # Random day 1-28
    day = str(random.randint(1, 28)).zfill(2)

    # Random governorate code
    governorate_code = random.choice(list(states.keys()))

    # Random 3 digits
    random_part = str(random.randint(0, 999)).zfill(3)

    # Random gender 0-9
    gender = str(random.randint(0, 9))

    id_without_check = first_digit + year[-2:] + month + day + governorate_code + random_part + gender

    return id_without_check

def generate_egyptian_ids(num_ids=10):
    generated_ids = []

    for _ in range(num_ids):
        # Generate first 13 digits
        id_without_check = generate_id_without_check_digit()

        # Calculate check digit
        step1 = 0
        step2 = 0
        step3 = 0
        step4 = 0

        FormulaCheckDigit = 0
        validations = weights
        NIDWithOutCheckDigit = id_without_check
        NIDstrArr = list(NIDWithOutCheckDigit)
        NIDintArr = []

        for i in range(len(NIDstrArr)):
            num = NIDstrArr[i]
            NIDintArr.append(int(num))
            step1 += validations[i] * NIDintArr[i]

        step2 = step1 / 11
        step3 = int(step2) * 11
        step4 = step1 - step3
        FormulaCheckDigit = (11 - step4) % 10

        check_digit = str(FormulaCheckDigit)

        # Add check digit to get the full ID
        id_number = id_without_check + check_digit

        generated_ids.append(id_number)

    return generated_ids

# Generate 10 sample IDs
generated_ids = generate_egyptian_ids(num_ids=10)
for idx, id_number in enumerate(generated_ids, start=1):
    governorate_name = states[id_number[7:9]]  # Extract governorate code and get the corresponding name
    print(f"Generated ID {idx}: {id_number} - Governorate: {governorate_name}")

