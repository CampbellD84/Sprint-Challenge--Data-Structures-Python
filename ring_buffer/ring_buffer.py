from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < 0 or item is None:
            return
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            # if DLL length is 1, current is tail
            if self.storage.length == 1:
                self.current = self.storage.tail
        else:
            # if there is a next value on the current node
            if self.current.next:
                # store in variable
                nxt_nde = self.current.next
                # add to tail
                self.storage.add_to_tail(item)
                # if current equals head of DLL
                if self.current == self.storage.head:
                    # move tail to front of DLL
                    self.storage.move_to_front(self.storage.tail)
                else:
                    # or insert tail value before
                    self.current.insert_before(self.storage.tail.value)
                    # increment DLL length
                    self.storage.length += 1
                    # delete DLL tail node
                    self.storage.delete(self.storage.tail)
                # delete current node
                self.storage.delete(self.current)
                # set next node as current
                self.current = nxt_nde
            else:
                self.storage.add_to_tail(item)
                self.storage.delete(self.current)
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        curr_nde = self.storage.head
        while curr_nde:
            list_buffer_contents.append(curr_nde.value)
            curr_nde = curr_nde.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
