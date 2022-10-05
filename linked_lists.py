from typing import List, Optional


class LinkedListNode:
    def __init__(self, val: str, next: Optional['LinkedListNode'] = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head: Optional['LinkedListNode'] = None):
        self.head = head

    def insert(self, val: str) -> None:
        if self.head is None:
            self.head = LinkedListNode(val)
        else:
            curr_ptr: Optional[LinkedListNode] = self.head
            while curr_ptr.next:
                curr_ptr = curr_ptr.next
            curr_ptr.next = LinkedListNode(val)

    def to_print_string(self) -> str:
        items_in_list: List[str] = []
        curr_ptr: Optional[LinkedListNode] = self.head

        while curr_ptr:
            items_in_list.append(curr_ptr.val)
            curr_ptr = curr_ptr.next

        return ",".join(items_in_list)


if __name__ == "__main__":
    """
    a list is a linear data structure, storing a continuous block of content
    
    under the hood, the contents of the list, is stored in a continuous block of memory
    
    typically, this list will be assigned memory that is way larger than the contents of the list
    
    under the hood, these are in our RAM (random-access memory) in a continuous block of memory
    ["ma la", "mc spicy", "satay", <unfilled>, "unfilled", .... <unfilled>]
    
    lets say this list was assigned 1,024 slots 
    
    if the list size exceeds 1,024 slots, python will make a copy of this list
    and assign it enough memory to store 2,048 elements
    """

    # elson_list: List[str] = ["ma la", "mc spicy", "satay"]

    elson_linked_list: LinkedList = LinkedList()
    elson_linked_list.insert("ma la")
    elson_linked_list.insert("mcspicy")
    elson_linked_list.insert("satay")
    elson_print: str = elson_linked_list.to_print_string()
    print(f"elson_print: {elson_print}")
