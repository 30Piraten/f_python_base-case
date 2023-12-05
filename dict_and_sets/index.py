dialing_codes = [
    (880, "Bangladesh"),
    (55, "Brazil"),
    (86, "China"),
    (91, "India"),
    (62, "Indonesia"),
    (81, "Japan"),
    (234, "Nigeria"),
    (92, "Pakistan"),
    (7, "Russia"),
    (1, "United States")
]

# Using dictionary comprehension
# here, country is key, and code is value
country_dailing_code = {country: code for code,
                        country in dialing_codes}
print(country_dailing_code)

# code is key, country is value
sort_country_dailing_code = {code: country.upper()
                             for country, code in sorted(country_dailing_code.items())
                             if code < 70}

print(sort_country_dailing_code)

# an attempt with a list comprehension
# list does not support key:value pairs
# hence we can only have one value iter
# from the sample list of tuples created

# surrounding country,upper() and code as
# a dict, we can get both key and value pair.
# we get a dict nested in a list*
result = [{country.upper(): code}
          for code, country in sorted(dialing_codes) if code < 70]
# this now prints both key and value pair.
# as a dict within a list*
# the result is sorted based on the integer
print(result)
