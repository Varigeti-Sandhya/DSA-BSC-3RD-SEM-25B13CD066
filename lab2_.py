class stack:
    def __init__(self):
        self._data = []
    def push (self, item):
        self._data.append(item)
        print(f"PUSH '{item}' → Stack: {self._data}")
    def pop(self):
        if self.is_empty():
                        raise IndexError("Stack Underflow — cannot pop from empty stack")  
        item = self._data.pop() 
        print(f"POP  '{item}' ← Stack: {self._data}")    
        return item    
    def peek(self):    
            if self.is_empty():    
                raise IndexError("Stack is empty")    
            return self._data[-1]     
    def is_empty(self):    
            return len(self._data) == 0    
         
    def size(self):    
            return len(self._data)    
         
    def display(self):    
            if self.is_empty():    
                print("Stack: [EMPTY]")    
            else:
                print(f"Stack (top→bottom): {list(reversed(self._data))}")
 # --- Test: Browser history ---    
s = stack()      
         
print("Step 1: Empty stack")    
s.display()    
         
print("\nStep 2: Open pages (push)")    
s.push("google.com")    
s.push("github.com")    
s.push("docs.python.org")    
s.push("stackoverflow.com")    
         
print("\nStep 3: Current page (peek)")    
print(f"Current page: '{s.peek()}'")

print("\nStep 4: Press Back twice (pop)")    
s.pop()    
s.pop()    
         
print("\nStep 5: State after going back")    
s.display()    
print(f"Stack size: {s.size()}")    
         
print("\nStep 6: Underflow protection test")    
s2 = stack()    
try:    
    s2.pop()    
except IndexError as e:    
    print(f"ERROR caught: {e}")