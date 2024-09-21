import re
pattern=r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b'

text="When Raj received his new PAN card, he was relieved to see it was registered under ABCDF3445L. He also helped his brother apply for his own card, which came through as XYZGH5678M. Meanwhile, their cousin’s application was approved with the number PQRSJ9012N. Each card not only represented their unique identities but also facilitated important financial transactions in their everyday lives."
li=re.findall(pattern,text)
print(li)