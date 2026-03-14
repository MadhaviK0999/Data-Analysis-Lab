# Python dictionaries are used to search with keys to find values. These dictionaries build for a fast key lookups. 
#But when you want to search woth values to find keys it is not possible with ordinary dictionaries. To solve this problem we can use 
#reverse dictionary. In reverse dictionary we can search with values to find keys.


state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", 
               "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois",
                 "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota",
                   "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", 
                   "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", 
                   "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", 
                   "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

us_state_code = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

'''def get_state_with_code(state_names):
  return (state_names,us_state_code[state_names])
print(get_state_with_code("Alabama")) '''


    
  #  Given a state code (e.g. 'AL'), return a tuple of (State Name, State Code).
    
state_code_to_name = {code: state for state, code in us_state_code.items()}

def get_state_with_code(code):
    state= state_code_to_name.get(code)
    if state:
        return (state, code)
    else:
        return "state not found"

print(get_state_with_code('MD'))

# Assertions - it checks automatically if the fuction is correct or not. if it is correct it will continue to run and print 
# test passed other wise it will through an assertionerror

assert get_state_with_code('DC')== ('District of Columbia', 'DC'), "Test la failed"
print("test la passed")
assert get_state_with_code("MD") == ("Maryland", "MD"), "Test MD failed"
print("test md passed")




