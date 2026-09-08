enemies = 1


def increase_enemies():
    enemies = 2         #  we are not modifiying global variable we are creating new variable
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
