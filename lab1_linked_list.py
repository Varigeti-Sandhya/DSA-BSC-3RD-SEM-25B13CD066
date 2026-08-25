class Node:    
    def __init__(self, data):    
        self.data = data     
        self.next = None    
class LinkedList:    
    def __init__(self):    
        self.head = None     
    def insert_at_end(self, data):    
        new_node = Node(data)                
        if self.head is None:                
            self.head = new_node    
            return    
        current = self.head                  
        while current.next is not None:      
            current = current.next    
        current.next = new_node        
    def insert_at_beginning(self, data):    
        new_node = Node(data)                
        new_node.next = self.head   # new node points to old head    
        self.head = new_node        # new node becomes head    
    def insert_at_position(self, data, position):    
        new_node = Node(data)    
        if position == 0:                        
            new_node.next = self.head    
            self.head = new_node    
            return    
        current = self.head    
        for i in range(position - 1):                
            if current is None:    
                raise IndexError("Position out of bounds")    
            current = current.next    
        new_node.next = current.next            
        current.next = new_node                     
    def delete_by_value(self, data):    
        if self.head is None:                             
            print("List is empty.")    
            return    
        if self.head.data == data:                    
            self.head = self.head.next    
            return    
        current = self.head    
        while current.next is not None:                 
           if current.next.data == data:    
               current.next = current.next.next       
               return    
           current = current.next    
        print(f"Value {data} not found.")    
    def search(self, data):    
        current = self.head    
        position = 0    
        while current is not None:    
            if current.data == data:    
                return position           
            current = current.next    
            position += 1    
        return -1                        
    def display(self):    
        if self.head is None:    
            print("[Empty List]")    
            return    
        current = self.head    
        elements = []    
        while current is not None:    
            elements.append(str(current.data))    
            current = current.next    
        print("HEAD → " + " → ".join(elements) + " → NULL")    
         
    def length(self):    
        count = 0    
        current = self.head    
        while current is not None:    
            count += 1    
            current = current.next    
        return count    
# --- Test ---    
ll = LinkedList()    
         
print("Step 1: Empty list")    
ll.display()    
         
print("\nStep 2: Insert at end")    
ll.insert_at_end("192.168.1.1")    
ll.insert_at_end("10.0.0.5")    
ll.insert_at_end("172.16.0.3")    
ll.display()    
         
print("\nStep 3: Insert at beginning")    
ll.insert_at_beginning( "8.8.8.8" )    
ll.display()    
         
print("\nStep 4: Insert at position 2")    
ll.insert_at_position("127.0.0.1", 2)    
ll.display()    
         
print("\nStep 5: Search")    
print("'10.0.0.5' at position:", ll.search("10.0.0.5"))    
print("'8.8.8.8' at position:", ll.search("8.8.8.8"))    
         
print("\nStep 6: Delete '172.16.0.3'")    
ll.delete_by_value("172.16.0.3")    
ll.display()    
         
print(f"\nStep 7: Length = {ll.length()}")    
         
         
         
         
 
    
         
         
         
