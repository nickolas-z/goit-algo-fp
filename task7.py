import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fractions import Fraction


def simulate_dice_rolls(num_simulations=100000) -> np.ndarray:
    """
    Симулює кидання двох кубиків задану кількість разів
    Args:
        num_simulations: кількість симуляцій
    Returns:
        sums: список сум кількостей
    """
    dice1 = np.random.randint(1, 7, num_simulations)
    dice2 = np.random.randint(1, 7, num_simulations)
    return dice1 + dice2


def calculate_probabilities(sums) -> dict:
    """
    Обчислює ймовірності для кожної можливої суми
    Args:
        sums: список сум кількостей
    Returns:
        probabilities: словник ймовірностей
    """
    unique, counts = np.unique(sums, return_counts=True)
    probabilities = counts / len(sums)
    return dict(zip(unique, probabilities))


def decimal_to_fraction_str(decimal)->str:
    """
    Конвертує десяткове число в дріб у вигляді рядка
    Args:
        decimal: десяткове число
    Returns:
        fraction_str: дріб у вигляді рядка
    """
    fraction = Fraction(decimal).limit_denominator(36)
    return f"{fraction.numerator}/{fraction.denominator}"


def create_comparison_df(monte_carlo_probs, theoretical_probs) -> pd.DataFrame:
    """
    Створює DataFrame для порівняння теоретичних та експериментальних ймовірностей
    Args:
        monte_carlo_probs: словник експериментальних ймовірностей
    Returns:
        df: DataFrame
    """
    df = pd.DataFrame(
        {
            "Сума": list(theoretical_probs.keys()),
            "Теоретична ймовірність": [
                f"{n/d*100:.2f}% ({n}/{d})" for n, d in theoretical_probs.values()
            ],
            "Експериментальна ймовірність": [
                f"{v*100:.2f}% ({decimal_to_fraction_str(v)})"
                for k, v in monte_carlo_probs.items()
            ],
            "Різниця": [
                abs(n / d - monte_carlo_probs.get(k, 0)) * 100
                for k, (n, d) in theoretical_probs.items()
            ],
        }
    )
    return df


def plot_probabilities(monte_carlo_probs, theoretical_probs) -> plt:
    """
    Створює візуалізацію порівняння теоретичних та експериментальних ймовірностей
    Args:
        monte_carlo_probs: словник експериментальних ймовірностей
        plot_probabilities: словник теоретичних ймовірностей
    Returns:
        plt: об'єкт візуалізації
    """

    df = pd.DataFrame(
        {
            "Сума": list(theoretical_probs.keys()),
            "Теоретична": [n / d for n, d in theoretical_probs.values()],
            "Експериментальна": [
                monte_carlo_probs.get(k, 0) for k in theoretical_probs.keys()
            ],
        }
    )

    plt.figure("Візуалізація", figsize=(15, 10))
    x = np.arange(len(df["Сума"]))
    width = 0.35

    # Створюємо стовпчики
    bars1 = plt.bar(x - width / 2, df["Теоретична"], width, label="Теоретична", alpha=0.8)
    bars2 = plt.bar(x + width / 2, df["Експериментальна"], width, label="Експериментальна", alpha=0.8)

    def autolabel(bars, is_theoretical=True)->None:
        """ Додає підписи до стовпчиків """
        for bar in bars:
            height = bar.get_height()
            if is_theoretical:
                percentage = f"{height*100:.2f}%"
                fraction = f"({int(height*36)}/36)"
            else:
                percentage = f"{height*100:.2f}%"
                fraction = f"({decimal_to_fraction_str(height)})"
            plt.text(bar.get_x() + bar.get_width() / 2, height, f"{percentage}\n{fraction}",
                     ha="center", va="bottom", fontsize=8,
                     bbox=dict(facecolor="white", alpha=0.7, edgecolor="none", pad=1))

    # Додаємо підписи
    autolabel(bars1, True)
    autolabel(bars2, False)

    plt.xlabel("Сума", fontsize=12)
    plt.ylabel("Ймовірність", fontsize=12)
    plt.title(
        "Порівняння теоретичних та експериментальних ймовірностей", fontsize=14, pad=20
    )
    max_height = max(max(df["Теоретична"]), max(df["Експериментальна"]))
    plt.ylim(0, max_height * 1.2)
    plt.xticks(x, df["Сума"], fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    return plt


def main():
    # Виконання симуляції
    np.random.seed(42)  # для відтворюваності результатів
    num_simulations = 1000000
    sums = simulate_dice_rolls(num_simulations)
    monte_carlo_probs = calculate_probabilities(sums)

    theoretical_probs = {
        2: (1, 36),
        3: (2, 36),
        4: (3, 36),
        5: (4, 36),
        6: (5, 36),
        7: (6, 36),
        8: (5, 36),
        9: (4, 36),
        10: (3, 36),
        11: (2, 36),
        12: (1, 36),
    }

    # Створення порівняльної таблиці
    comparison_df = create_comparison_df(monte_carlo_probs, theoretical_probs)
    print("\nПорівняльна таблиця ймовірностей:")
    print(comparison_df.to_string(index=False))

    # Створення візуалізації
    plt = plot_probabilities(monte_carlo_probs, theoretical_probs)
    plt.savefig('probabilities_comparison.png')
    plt.show()


if __name__ == "__main__":
    main()
