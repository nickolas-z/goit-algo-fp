import turtle


def treeFractal(TTL, recursionLevel, branchLength, branchReduction, angle):
    """Малює фрактальне дерево за допомогою рекурсії."""
    if recursionLevel == 0:
        return
    else:
        # Малюємо поточну гілку
        TTL.forward(branchLength)
        # Малюємо ліву гілку
        TTL.left(angle)
        treeFractal(
            TTL,
            recursionLevel - 1,
            branchLength - branchReduction,
            branchReduction,
            angle,
        )
        # Малюємо праву гілку
        TTL.right(2 * angle)
        treeFractal(
            TTL,
            recursionLevel - 1,
            branchLength - branchReduction,
            branchReduction,
            angle,
        )
        # Повертаємося на початкову позицію
        TTL.left(angle)
        TTL.backward(branchLength)


def main():
    # Отримати введення користувача для рівня рекурсії
    recursionLevel = int(
        input("Введіть рівень рекурсії для створення фрактала “дерево Піфагора”: ")
    )

    # Налаштування вікна
    screen = turtle.Screen()
    screen.setup(800, 600)

    # Налаштування
    TTL = turtle.Turtle()
    TTL.speed(0)
    TTL.color("brown")
    TTL.pensize(2)

    # Встановлюємо початкову позицію
    TTL.penup()
    TTL.setposition(0, -250)
    TTL.pendown()
    TTL.hideturtle()
    TTL.setheading(90)

    # Вихідні параметри для дерева
    branchLength = 100
    branchReduction = 10
    angle = 25

    # Малюємо фрактальне дерево
    treeFractal(TTL, recursionLevel, branchLength, branchReduction, angle)

    screen.exitonclick()


if __name__ == "__main__":
    main()
