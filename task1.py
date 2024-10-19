def reverse(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev

def sorted_insert(self, new_node: Node):
    if self.head is None or self.head.data >= new_node.data:
        new_node.next = self.head
        self.head = new_node
    else:
        current = self.head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

def insertion_sort(self):
    sorted_list = None
    current = self.head
    while current:
        next_node = current.next
        current.next = None
        if sorted_list is None:
            sorted_list = current
        else:
            self.head = sorted_list
            self.sorted_insert(current)
            sorted_list = self.head
            current = next_node
    self.head = sorted_list
def merge_sorted_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    dummy = Node(0)
    tail = dummy

    a = l1.head
    b = l2.head

    while a and b:
        if a.data < b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    if a:
        tail.next = a
    elif b:
        tail.next   
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Реверсування списку
llist.reverse()
print("\nРеверсований список:")
llist.print_list()

# Сортування списку
llist.insertion_sort()
print("\nВідсортований список:")
llist.print_list()

# Об'єднання двох відсортованих списків
llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

merged_list = merge_sorted_lists(llist1, llist2)
print("\nОб'єднаний відсортований список:")
merged_list.print_list()
