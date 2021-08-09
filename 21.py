ip=input("1. Do you want to enter in celcius or farhenheit.if celcius then press c else f\n")
class Temperature:
    temp = 0

    def __init__(self, temp):
        self.temp = temp


    def convert_to_fahrenheit(self):
        result = float((9 * self.temp) / 5 + 32)
        return result

    def convert_to_celsius(self):
        result = float((self.temp - 32) * 5 / 9)
        return result
    
if ip=="c":
    input_temp = float(input("Enter the value: "))
    temp1 = Temperature(input_temp)
    print("The value in farhenheit",temp1.convert_to_fahrenheit())
elif ip=="f":
    input_temp = float(input("Enter the value: "))
    temp1 = Temperature(input_temp)
    print("The value n celcius is ",temp1.convert_to_celsius())
else:
    print("Invalid")
    






