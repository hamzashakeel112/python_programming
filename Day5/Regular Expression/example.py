# regular expression are use to search specific things from specific sites
import re 
text= " user account number is 123-456-7891"
phone_pattern=r'\d{3}-\d{3}-'

phone_number=re.findall(phone_pattern,text)
print(phone_number)


# example 2 
date="23-02-2020"
# date_pattern=r'\d{1,2}-\d{1,2}-\d{4}'
date_re = r"\d{2}-\d{2}-\d{4}"
date_pattern=re.findall(date_re,date)
print(date_pattern)