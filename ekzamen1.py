
def pyramid_number(n):
    pyramid_sum = 0
    for i in range(1, n+1):
        triangle_number = i * (i + 1) // 2
        pyramid_sum += triangle_number
    return pyramid_sum

while True:
    user_input = input("Введіть значення n або 'exit' для виходу: ")
    
    if user_input.lower() == 'exit':
        print("Вихід з програми.")
        break
    
    if user_input.isdigit():
        n = int(user_input)
        print(f"{n}-е пірамідальне число: {pyramid_number(n)}")
    else:
        print("Число або 'exit' для виходу.")
