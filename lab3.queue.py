from collections import deque    
class Queue:    
    def __init__(self):    
        self._data = deque()
           
    def enqueue(self, item):    
        self._data.append(item)                      
        print(f"ENQUEUE '{item}' → Queue: {list(self._data)}")    
    def dequeue(self):    
        if self.is_empty():    
            raise IndexError("Queue Underflow — cannot dequeue from empty queue")    
        item = self._data.popleft()                  
        print(f"DEQUEUE '{item}' ← Queue: {list(self._data)}")    
        return item    

    def front(self):    
        if self.is_empty():    
            raise IndexError("Queue is empty")    
        return self._data[0]
            
    def rear(self):    
        if self.is_empty():    
             raise IndexError("Queue is empty")    
        return self._data[-1]  
        
    def is_empty(self):    
        return len(self._data) == 0    
    def size(self):    
        return len(self._data)    
    def display(self):    
        if self.is_empty():    
            print("Queue: [EMPTY]")    
        else:    
            items = list(self._data)    
            print("FRONT → " + " → ".join(str(x) for x in items) + " ← REAR")    
# --- Test: Network packet queue ---    
q = Queue()    
         
print("Step 1: Empty queue")    
q.display()    
         
print("\nStep 2: Packets arrive (enqueue)")    
q.enqueue("PKT#001 [SYN]")    
q.enqueue("PKT#002 [SYN-ACK]")    
q.enqueue("PKT#003 [ACK]")    
q.enqueue("PKT#004 [DATA]")    
         
print("\nStep 3: Inspect front and rear")    
print(f"Front (next to inspect): {q.front()}")    
print(f"Rear  (last to arrive):  {q.rear()}")    
         
print("\nStep 4: IDS processes first two packets (dequeue)")    
q.dequeue()    
q.dequeue()    
         
print("\nStep 5: Queue state")    
q.display()    
print(f"Remaining packets: {q.size()}")    
         
print("\nStep 6: New packet arrives, then drain all")    
q.enqueue("PKT#005 [FIN]")    
print("\nProcessing all remaining:")    
while not q.is_empty():    
    q.dequeue()    
q.display()    