def c_to_f(cel):
    fareh_value=(9/5)*cel+32
    return fareh_value

def c_to_k(cel):
    kelvin_value=cel+273.15
    return kelvin_value

def f_to_c(fareh):
    cel=(5/9)*fareh-32
    return cel

choice=input("Press1: Celcius\nPress 2: fareh\n")
if choice=="1":
    cel=int(input("Enter the temperature in celsius :"))
    ch1=int(input("Press1: To convert to kelvin\nPress2: To convert to farehenheit"))
    if ch1==1:
        print(f"The value in kelvin is {c_to_k(cel)}")
    elif ch1==2:
        print(f"The value in farenheit is {c_to_f(cel)}")
    else:
        print("Wrong Choice entered")
elif choice=="2":
    fareh=int(input("Enter the temperature in fareh:"))
    print(f"The temperature in celsius is{f_to_c(fareh)}")
else:
    print("Wrong Choice entered")






