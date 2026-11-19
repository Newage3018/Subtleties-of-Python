# Это модуль message, содержащий определение переменной hello и определены несколько функций
# на примере модуля разобран механизм работы if __name__ == "__main__":

hello = "Hello all"
 
 
def print_message(text):
    print(f"Message: {text}")
 
 
def main():
    print_message(hello)
 
 
if __name__ == "__main__": 
    main()
