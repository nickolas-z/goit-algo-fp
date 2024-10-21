from typing import Optional
from LinkedList import LinkedList, Node
import random


class LList(LinkedList):
    def reverse_list(self) -> None:
        """Реверсує список."""
        prev = None
        current = self.head
        while current is not None:
            # Зберігаємо посилання на наступний вузол
            next_node = current.next  
            # Змінюємо посилання поточного вузла на попередній вузол
            current.next = prev  
            # Переміщуємо prev на поточний вузол
            prev = current  
            # Переміщуємо current на наступний вузол
            current = next_node  
        # Змінюємо головний вузол на останній вузол списку
        self.head = prev

    def sort_list(self) -> None:
        """Сортує список."""
        if self.head is None or self.head.next is None:
            # Виходимо якщо список пустий або містить один елемент
            return None

        # Створюємо новий відсортований список
        sorted_list = None  
        current = self.head
        while current:
            # Зберігаємо наступний вузол для проходу по списку
            next_node = current.next  
            sorted_list = self._sorted_insert(
                sorted_list, current
            )  # Вставляє вузол у відсортований список
            current = next_node  # Переходить до наступного вузла
        self.head = sorted_list  # Оновлює голову списку

    def _sorted_insert(self, head: Optional[Node], node: Node) -> Node:
        """Вставляє вузол у відсортований список."""
        if head is None or node.data < head.data:
            # Вставляємо вузол на початку списку
            node.next = head  
            return node
        else:
            current = head
            while current.next and current.next.data < node.data:
                # Шукаємо де потрбітно зробити вставку
                current = (current.next)
            # Вставка вузла
            node.next = current.next
            current.next = node
        return head

    def merge_sorted_lists(self, other: "LList") -> "LList":
        """Об'єднує два відсортованих списки."""
        p1 = self.head
        p2 = other.head
        merged_list = LList()

        while p1 is not None and p2 is not None:
            if p1.data <= p2.data:
                merged_list.insert_at_end(p1.data)
                p1 = p1.next
            else:
                merged_list.insert_at_end(p2.data)
                p2 = p2.next
        # Додаємо залишок першого списку, якщо він існує
        while p1 is not None:
            merged_list.insert_at_end(p1.data)
            p1 = p1.next

        # Додаємо залишок другого списку, якщо він існує
        while p2 is not None:
            merged_list.insert_at_end(p2.data)
            p2 = p2.next

        return merged_list

if __name__ == "__main__":
    # кількість елементів списку для тестування
    n = 3

    ll1 = LList()
    for i in range(n, 0, -1):
        ll1.insert_at_beginning(random.randint(1, 100))

    print(f"Оригінальний список ll1: {ll1}")

    # Реверсування списку
    ll1.reverse_list()
    print(f"Реверсований список ll1: {ll1}", end="\n\n")

    # Сортування списку
    ll1.sort_list()
    print(f"Відсортований список ll1: {ll1}")

    # Об'єднання двох відсортованих списків
    ll2 = LList()
    for i in range(n, 0, -1):
        ll2.insert_at_beginning(random.randint(1, 100))
    ll2.sort_list()
    print(f"Відсортований список ll2: {ll2}")

    merged_list = ll1.merge_sorted_lists(ll2)
    print(f"Об'єднаний відсортований список ll1+ll2: {merged_list}")
