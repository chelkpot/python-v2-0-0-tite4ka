# tasks/task2.py

def solve():




    X, Y, Z = map(int, input().split())
    price_of_pencil = 3
    price_of_pen = price_of_pencil + 2
    price_of_marker = price_of_pen + 7
    
    total_cost = (X * price_of_pencil) + (Y * price_of_pen) + (Z * price_of_marker)
    print(total_cost)
# Ниже пишите решение задачи

   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()