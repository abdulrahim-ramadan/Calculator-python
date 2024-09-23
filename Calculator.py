import sys
from colorama import init, Fore

# Initialize Colorama
init()

# Define color constants
w = Fore.WHITE
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
y = Fore.YELLOW
c = Fore.CYAN

# Logo
logo = f"""{c}
  
    A    
   / \   
  / _ \  
 / ___ \ 
/_/   \_\ 

{c}"""

def display_welcome_message():
    print(logo)
    print(f"{y}مرحبًا بك في آلة الحاسبة! Welcome to the Calculator!{w}")

def calculate(num1, num2, operator):
    """Perform basic arithmetic operations."""
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print(f"{r} !لا يمكن القسمة على الصفر / Cannot divide by zero")
            return None
    else:
        print(f"{r}عملية غير صحيحة. Please try again.")
        return None

def main():
    display_welcome_message()

    while True:
        try:
            num1 = float(input(f"{c} : ادخل الرقم الأول (Enter the first number): "))
            num2 = float(input(f"{c} : ادخل الرقم الثاني (Enter the second number): "))
            operator = input(f"{c}ادخل العملية ( + , - , * , / ): Enter the operation: ")
            result = calculate(num1, num2, operator)

            if result is not None:
                print(f"{g}النتيجة: {result} / Result: {result}")

            choice = input(f"{c} هل تريد الاستمرار؟ (نعم/لا): Do you want to continue? (yes/no): ")
            if choice.lower() == 'لا' or choice.lower() == 'no':
                print(f"{y}شكرًا لاستخدامك الآلة الحاسبة! Thank you for using the calculator!{w}")
                sys.exit()
        except ValueError:
            print(f"{r} يجب إدخال أرقام فقط. You must enter numbers only.")

if __name__ == "__main__":
    main()
