# Exercise 3
Gender = input(" Enter your gender: ")
Hemoglobin_Value = float(input("Enter your hemoglobin value: "))
if Gender == "FEMALE" and  Hemoglobin_Value < 117:
        print("Hemoglobin value is low.")
elif Gender == "FEMALE" and Hemoglobin_Value > 155:
        print("Hemoglobin value is high.")
elif  Gender == "FEMALE" and 117 <= Hemoglobin_Value <= 155:
        print("Normal Hemoglobin value.")
elif   Gender == "MALE" and Hemoglobin_Value < 134:
        print("Hemoglobin value is low.")
elif Gender == "MALE" and Hemoglobin_Value > 167:
        print("Hemoglobin value is high.")
elif Gender == "MALE" and 134 <= Hemoglobin_Value <= 167:
        print("Normal hemoglobin value")
