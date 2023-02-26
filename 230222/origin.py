from datetime import datetime

now = datetime.now()

print(now.time())
time_string = now.strftime('%H:%M:%S')
print("문자열 변환 : ", time_string)

if time_string == "09:00:00":
    print("09:00:00")