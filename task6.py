from math import e

from matplotlib.pylab import f


def calculate_ratios(items) -> dict:
    """
    Розрахунок співвідношення калорій до вартості для кожної страви
    Args:
        items: Список страв
    Returns:
        dict: Співвідношення калорій до вартості для кожної страви
    """
    return {item: items[item]["calories"] / items[item]["cost"] for item in items}


def greedy_algorithm(items, budget) -> dict:
    """
    Жадібний алгоритм для вибору їжі з найкращим співвідношенням калорій до вартості
    Args:
        items: Список страв
        budget: Бюджет
    Returns:
        dict: Результати вибору страв
    """
    ratios = calculate_ratios(items)
    sorted_items = sorted(ratios.items(), key=lambda x: x[1], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, _ in sorted_items:
        item_cost = items[item]["cost"]
        item_calories = items[item]["calories"]
        if total_cost + item_cost <= budget:
            selected_items.append(item)
            total_cost += item_cost
            total_calories += item_calories

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def dynamic_programming(items, budget) -> dict:
    """
    Алгоритм динамічного програмування для оптимального вибору їжі
    Args:
        items: Список страв
        budget: Бюджет
    Returns:
        dict: Результати вибору страв
    """
    names = list(items.keys())
    costs = [items[item]["cost"] for item in names]
    calories = [items[item]["calories"] for item in names]
    n = len(names)

    table = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                table[i][w] = max(
                    calories[i - 1] + table[i - 1][w - costs[i - 1]], table[i - 1][w]
                )
            else:
                table[i][w] = table[i - 1][w]

    selected_items = []
    total_calories = table[n][budget]
    w = budget

    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= costs[i - 1]

    return {
        "selected_items": selected_items[::-1],
        "total_cost": budget - w,
        "total_calories": total_calories,
    }


def test_algorithms(items, budget) -> None:
    """
    Тестування алгоритмів
    Args:
        items: Список страв
        budget: Бюджет
    Returns: None
    """
    print("-" * 50)
    print(f"Тестування з бюджетом {budget} грн", end="\n\n")
    print(f"Список страв: {', '.join(items.keys())}")

    greedy_result = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:")
    print(
        f"\tВибрані страви: {', '.join(greedy_result['selected_items'])}\n"
        f"\tЗагальна вартість: {greedy_result['total_cost']} грн\n"
        f"\tЗагальна калорійність: {greedy_result['total_calories']} кал"
    )

    dp_result = dynamic_programming(items, budget)
    print("Динамічне програмування:")
    print(
        f"\tВибрані страви: {', '.join(dp_result['selected_items'])}\n"
        f"\tЗагальна вартість: {dp_result['total_cost']} грн\n"
        f"\tЗагальна калорійність: {dp_result['total_calories']} кал",
        end="\n\n",
    )


def main():
    """Головна функція"""
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    for i in range(0, 200, 50):
        test_algorithms(items, i)


if __name__ == "__main__":
    main()
