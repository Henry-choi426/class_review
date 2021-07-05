# import pyttsx3
# engine = pyttsx3.init()
# engine.say('한글도 되나요')
# engine.runAndWait()

# import pyautogui
# num=int(input("Enter a value to divide 100"))
# if num == 0:
#     pyautogui.alert(" Alert!!! 100 cannot be divided by 0")
# else:
#     print(f'The value is {100/num}')

from faker import Faker

fake = Faker("ko_KR")
# # print(fake.name())
# # print(fake.email())
# # print(fake.country())

# print(fake.profile())                                                        

print("======")

i = 0
while True:
    if not fake.name in ['최한승','이현수','이홍주','정일균','김혜경']:
        print(i)
        print(fake.name)
        break
    # elif i == 10000:
    #     print('끗')
    else:
        i += 1