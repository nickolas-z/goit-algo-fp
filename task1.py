from LinkedList import LinkedList

class LList(LinkedList):
    def sort_list(self):
        if self.head is None:
            return
        cur = self.head
        while cur:
            min_node = cur
            next_node = cur.next
            while next_node:
                if min_node.data > next_node.data:
                    min_node = next_node
                next_node = next_node.next
            cur.data, min_node.data = min_node.data, cur.data
            cur = cur.next

    def merge_sorted_lists(self, ll2: LinkedList) -> LinkedList:
        merged = LList()
        cur1 = self.head
        cur2 = ll2.head
        while cur1 and cur2:
            if cur1.data < cur2.data:
                merged.insert_at_end(cur1.data)
                cur1 = cur1.next
            else:
                merged.insert_at_end(cur2.data)
                cur2 = cur2.next
        while cur1:
            merged.insert_at_end(cur1.data)
            cur1 = cur1.next
        while cur2:
            merged.insert_at_end(cur2.data)
            cur2 = cur2.next
        return merged

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

def main():
    # Приклад використання
    ll1 = LList()
    ll1.insert_at_end(3)
    ll1.insert_at_end(1)
    ll1.insert_at_end(5)

    ll2 = LinkedList()
    ll2.insert_at_end(2)
    ll2.insert_at_end(4)
    ll2.insert_at_end(6)

    print("List 1 before sorting:")
    ll1.print_list()

    ll1.sort_list()
    print("List 1 after sorting:")
    ll1.print_list()

    print("Merged list:")
    merged = ll1.merge_sorted_lists(ll2)
    merged.print_list()

    print("Reversed merged list:")
    merged.reverse()
    merged.print_list()

if __name__ == "__main__":
    main()
