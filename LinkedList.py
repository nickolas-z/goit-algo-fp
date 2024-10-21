from typing import Optional

class Node:
    def __init__(self, data: int = None)-> None:
        self.data = data  # Зберігає дані вузла
        self.next = None  # Посилання на наступний вузол


class LinkedList:
    def __init__(self)-> None:
        """Ініціалізує список."""
        self.head = None  # Початок списку, спочатку пустий

    def insert_at_beginning(self, data)-> None:
        """Додає вузол на початок списку."""
        new_node = Node(data)  # Створює новий вузол з даними
        new_node.next = (
            self.head
        )  # Вказує, що новий вузол має посилатися на поточний головний вузол
        self.head = new_node  # Робить новий вузол головним вузлом списку

    def insert_at_end(self, data)-> None:
        """Додає вузол в кінець списку."""
        new_node = Node(data)  # Створює новий вузол з даними
        if self.head is None:  # Якщо список пустий
            self.head = new_node  # Робить новий вузол головним вузлом
        else:
            cur = self.head  # Починає з головного вузла
            while cur.next:  # Проходить до кінця списку
                cur = cur.next
            cur.next = new_node  # Додає новий вузол в кінці списку

    def insert_after(self, prev_node: Node, data)-> None:
        """Додає вузол після певного вузла."""
        if prev_node is None:  # Перевіряє, чи існує попередній вузол
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)  # Створює новий вузол з даними
        new_node.next = (
            prev_node.next
        )  # Вказує, що новий вузол має посилатися на вузол після попереднього вузла
        prev_node.next = new_node  # Вставляє новий вузол після попереднього вузла

    def delete_node(self, key: int)-> None:
        """Видаляє вузол з певними даними."""
        cur = self.head  # Починає з головного вузла
        if cur and cur.data == key:  # Якщо головний вузол містить потрібні дані
            self.head = cur.next  # Робить наступний вузол головним
            cur = None  # Видаляє вузол
            return
        prev = None  # Змінна для зберігання попереднього вузла
        while cur and cur.data != key:  # Проходить список у пошуках потрібних даних
            prev = cur
            cur = cur.next
        if cur is None:  # Якщо вузол з потрібними даними не знайдено
            return
        prev.next = cur.next  # Видаляє вузол з потрібними даними
        cur = None  # Звільняє пам'ять, видаляючи вузол

    def search_element(self, data: int) -> Optional[Node]:
        """Пошук вузла з певними даними."""
        cur = self.head  # Починає з головного вузла
        while cur:  # Проходить список у пошуках потрібних даних
            if cur.data == data:  # Якщо знайдено потрібні дані
                return cur  # Повертає вузол з потрібними даними
            cur = cur.next
        return None  # Якщо вузол з потрібними даними не знайдено

    def print_list(self)-> None:
        """Виводить список."""
        current = self.head  # Починає з головного вузла
        while current:  # Проходить весь список
            print(current.data, end=" -> ")  # Виводить дані вузла
            current = current.next  # Переходить до наступного вузла
        print("None")  # Вказує на кінець списку
    
    def __str__(self) -> str:
        """Представлення списку у вигляді рядка."""
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> None"

if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_beginning(3)
    llist.insert_at_beginning(2)
    llist.insert_at_end(4)
    llist.insert_after(llist.head.next, 5)
    llist.print_list()
    llist.delete_node(3)
    llist.print_list()
    print(llist.search_element(2).data)
