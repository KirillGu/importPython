import datetime
import time
import salary
import people

DateToday = datetime.datetime.today().strftime("%d-%m-%Y")
TimeNow = time.strftime("%H.%M.%S")

print("Local Date: ", TimeNow + " " + DateToday, "\n")


print("выполнение if __name__ == '__main__'", "\n")
print("Перекличка", "\n")
if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
print("Код завершен")
