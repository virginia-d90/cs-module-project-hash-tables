class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        #DAY 1
        # self.capacity = capacity
        # self.storage = [None] * self.capacity

        #DAY2
        self.capacity = capacity
        self.table = [None] * capacity #changed name from day 1
        self.count = 0 #counter to keep track of number of entries in table

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity 


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity #determines how full the table is

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        # byte_arr= key.encode('utf-8')

        # for b in byte_arr:
        #     hash = ((hash * 33) ^ b) % 0x100000000
        for i in key:
            hash = (hash * 33) + ord(i)
        
        return hash



    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        #DAY 1
        # self.storage[self.hash_index(key)] = value

        #DAY 2
        index = self.hash_index(key)
    
        if self.table[index] is None: #this will be the first entry at a given index
            self.table[index] = HashTableEntry(key, value) #creates entry at given index
            self.count += 1 #keep track of entries in table
        else:#there is already at least one entry at this index
            multiple = self.table[index]

            while multiple is not None:
                if multiple.key == key: #check to see if key already exists
                   multiple.value = value #overrides the previous value
                   return
                if multiple.next is None: #last entry in list
                    multiple.next = HashTableEntry(key, value) #adds new entry
                    self.count += 1 
                    return
                multiple = multiple.next #increments the while loop

        if self.get_load_factor() > 0.7:#monitor how full the table is and resize if needed
            self.resize(self.capacity * 2)#double the size of the table
    




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        #DAY 1
        # try:
        #     self.storage[self.hash_index(key)] = None
        # except KeyError:
        #     return print('Key not found')

        #DAY 2
        index = self.hash_index(key)
        current = self.table[index]

        if current.key == key:#if entry to delete is the first in the list(the head)
            if current.next == None:#there are no other entries in the list
                self.table[index] = None #erase reference to entry
                self.count -= 1 #decrement the load
            else: #there are other entries in the list
                new_head = current.next #new head will be the second entry in list
                current.next = None #remove reference to old head
                current = new_head #assign current to the new head
                self.count -= 1
        else:#entry was not the head or is not found
            if current == None:#there are no entries for that index
                return None
            else:
                prev = None

                while current.next is not None and current.key != key:#look through entries until found or all entries have been searched
                    prev = current
                    current = current.next
                if current.key == key: # key is found
                    prev.next = current.next 
                    self.count -= 1
                    return current.value
                else:
                    return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        #DAY 1
        # try:
        #     return self.storage[self.hash_index(key)]
        # except KeyError:
        #     return None

        #DAY 2
        index = self.hash_index(key)
        entries = self.table[index] #not loving variable name, but haven't come up with something better

        while entries is not None:# at least one entry exists for the index
            if entries.key == key: #key exists at the index
                return entries.value #return the value of the key
            entries = entries.next #advance the loop
        
        return None #entry was not found/does not exist at index


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


        old_table = self.table
        old_capacity = self.capacity

        self.table = [None] * new_capacity
        self.capacity = new_capacity

        for index in range(old_capacity): #loop through the entries of the old table
            entry = old_table[index] 
            while entry is not None: # while there are still entries to be transferred
                self.put(entry.key, entry.value)#add entry to resized table 
                entry = entry.next #advance to the next entry
            



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
