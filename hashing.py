def bucket(key, size):  # Map an integer key to a valid slot.
    return key % size  # Division method.
def chain_insert(table, key):  # Use lists to hold collisions.
    slot = bucket(key, len(table))  # Find the home slot.
    table[slot].append(key)  # Add the key in that slot's chain.
def probe_insert(table, key):  # Use the next free array slot.
    start = bucket(key, len(table))  # Compute the home slot.
    for step in range(len(table)):  # Never probe more than all slots.
        slot = (start + step) % len(table)  # Wrap at the end.
        if table[slot] is None:  # Found an empty slot.
            table[slot] = key  # Store the key.
            return slot  # Report its slot.
    raise OverflowError("Hash table full")  # No free slot remained.
chained = [[] for _ in range(5)]  # Empty chains.
probed = [None] * 5  # Empty open-addressed table.
for key in [12, 7, 18]:  # Insert colliding and other keys.
    chain_insert(chained, key)  # Add to a chain.
    probe_insert(probed, key)  # Or try an empty slot.
print(chained[2])  # Inspect the collision chain.
print(probed)  # Inspect the array layout.