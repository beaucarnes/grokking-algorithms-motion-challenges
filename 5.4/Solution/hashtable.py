'''
DO IT! CHALLENGE - 5.4 Hash Table
It was said that you’ll almost never have to implement a hash table yourself. Well, in this challenge,
that's exactly what you are going to do! But don't worry, it has already been started for you. You just need to finish
`get` and the `get_hash function`. Looking at the `set` and `_set_linked_list` functions may help you with the `get`
function. For the `get_hash` function, the important thing is returning a distinct number for each string that is
passed in. The number should always be the same for the same string. Test you code by running 'contactapp.py'.
'''


class HashEntry(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None


class HashTable():
    def __init__(self):
        self.capacity = 20
        self.cur_capacity = 0
        self.slots = [None] * self.capacity

    def set(self, key, value):

        key_hash = self.get_hash(key)
        slot = key_hash % self.capacity

        if self.slots[slot] is None:
            self.slots[slot] = HashEntry(key, value)
        else:
            self._set_linked_list(key, value, self.slots, slot)

    def _set_linked_list(self, key, value, slots, slot):
        cur_node = slots[slot]
        while cur_node is not None:
            if cur_node.key == key:
                cur_node.value = value
                cur_node = None
            elif cur_node.next is None:
                cur_node.next = HashEntry(key, value)
                cur_node = None
            else:
                cur_node = cur_node.next

    def get(self, key):

        key_hash = self.get_hash(key)
        slot = key_hash % self.capacity

        if self.slots[slot] is not None:
            cur_node = self.slots[slot]
            while cur_node is not None:
                if cur_node.key == key:
                    return cur_node.value
                cur_node = cur_node.next

    def get_hash(self, key):
        total = 0
        for i in range(len(key)):
            total += ord(key[i]) * (7 ** i)
        return (len(key) * total) % 256

ht = HashTable()
ht.set('Beau', '555-555-5555')
ht.set('Corwin', '555-555-5225')
print(ht.get('Corwin'))