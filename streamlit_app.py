
import streamlit as st
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

# Function to randomize parameters
@st.cache(allow_output_mutation=True)
@st.cache_resource
def randomize_parameters():
    Year = random.randint(1960, 2005)
    Month = random.randint(1, 12)
    Day = random.randint(1, 28)
    governorate_values = list(states.keys())
    random_governorate = random.choice(governorate_values)
    Government=governorate_values.index(random_governorate)
    Gender = random.randint(0, 1)
    return Year,Month,Day,Government,Gender
    

Year,Month,Day,Government,Gender=randomize_parameters()

year = st.sidebar.slider("Year", 1950, 2005, key="year_slider",value=Year)
month = st.sidebar.slider("Month", 1, 12, key="month_slider",value=Month)
day = st.sidebar.slider("Day", 1, 28, key="day_slider",value=Day)
governorate_dropdown = st.sidebar.selectbox("Governorate", list(states.values()), key="governorate_dropdown",index=Government)
gender_radio = st.sidebar.radio("Gender", ['Male', 'Female'], key="gender_radio",index=Gender)


def generate_id_without_check_digit():

    

    selected_governorate = [code for code, name in states.items() if name == governorate_dropdown][0]
   
    # Random 3 digits
    random_part = str(random.randint(0, 999)).zfill(3)

    # Random gender and gender-specific number
    gender_number = random.choice(range(0, 10, 2)) if gender_radio == 'Female' else random.choice(range(1, 10, 2))

    # Set the first digit based on the year
    first_digit = "3" if year >= 2000 else "2"

    id_without_check = f"{first_digit}{year % 100:02d}{month:02d}{day:02d}{selected_governorate}{random_part}{gender_number}"

    return id_without_check

def generate_egyptian_ids(num_ids=10):
    generated_ids = []

    for idx in range(1, num_ids + 1):
        id_without_check = generate_id_without_check_digit()

        try:
            # Calculate check digit
            step1 = sum(int(num) * weight for num, weight in zip(id_without_check, weights))
            step2 = step1 / 11
            step3 = int(step2) * 11
            step4 = step1 - step3
            formula_check_digit = (11 - step4) % 10

            # Add check digit to get the full ID
            id_number = id_without_check + str(formula_check_digit)

            generated_ids.append(id_number)
        except ValueError:
            st.warning(f"Error generating ID {idx}: Invalid characters in generated values.")

    return generated_ids
    


# Streamlit app
st.title("Egyptian ID Generator")
# Add a "Randomize" button
if st.sidebar.button("Randomize Parameters"):
    st.cache_resource.clear()
    randomize_parameters.clear()
    randomize_parameters()
    st.cache_resource.clear()
    randomize_parameters.clear()


num_ids = st.sidebar.slider("Number of IDs to generate", 1, 100, 10, key="num_ids_slider")
generated_ids = generate_egyptian_ids(num_ids)

st.write("Generated IDs:")
for idx, id_number in enumerate(generated_ids, start=1):
    governorate_name = states[id_number[7:9]]
    st.write(f"Generated ID {idx}: {id_number} - Governorate: {governorate_name}")
