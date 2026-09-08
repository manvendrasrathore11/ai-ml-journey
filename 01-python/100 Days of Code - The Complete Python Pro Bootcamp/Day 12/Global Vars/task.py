# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1              #agar global  enemies ko mai uper nhi likhta toh ye error dikhata
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")



a = 1
def my_function():
    a += 1
    print(a)    # ye error dikha reha ha  because we are modifing glodal varaible