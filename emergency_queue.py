class Patient:
    def __init__(self, name, urgency):
        if urgency < 1 or urgency > 10:
            print(f"{urgency} is not valid. Choose number between 1 and 10")
            self.name = None
            self.urgency = None
            return 
        self.name = name
        self.urgency = urgency



class MinHeap:
    def __init__(self):
        self.data = []

    def print_heap(self):
        """prints heap"""
        if len(self.data) == 0:
            print("List is empty.")
            return False
        else:
            print("\nCurrent Tasks")
            for task in self.data:
                print(f"-{task.name} (Priority: {task.urgency})")
            

    def insert(self, task):
        """inserts heap"""
        if not task.name:
            return
        
        self.data.append(task) # Step 1: Add the item to the end
        self.heapify_up(len(self.data) - 1) # Step 2: Call heapify_up starting at the end of the list where the value was added.

    def remove_min(self):
        """Removes patient with higehst priotiry."""
        if not self.data: # Handle an empty list
            return None
        
        if len(self.data) == 1: # Only one item means its the last value, so no reordering is needed
            return self.data.pop()
        
        min_value = self.data[0] # Get the value to return
        self.data[0] = self.data.pop() # Place last item as the root
        self.heapify_down(0) # Restore the heap order
        return min_value # Return the minimum value 
    
    def peak(self):
        """Returns the patient at index 0 without removing them."""
        if not self.data:
            print("No list")
            return False
        return self.data[0]

    def heapify_up(self, index):
        """Adds the provided value to the end of the list.
        Call heapify_up(index) starting at the index for the last item on the list to move the task up the tree if its priority is smaller (i.e. more urgent) than its parent."""
        while index > 0:
            # Get the parent index for the current child index
            parent_index = (index - 1) // 2
            # Get the tasks
            current_task = self.data[index] 
            parent_task = self.data[parent_index]
            # Check if the current priority value is smaller than the parent. If so, we need to move it up the list. If not, we can stop
            if current_task.urgency < parent_task.urgency:
                # Swap the items position in the list 
                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp

                # Move up the heap
                index = parent_index
            else: 
                break

    def heapify_down(self, index):
        """Swaps the first item in the list with the last item. This allows us to maintain the list structure."""
        # Calculate the index of the left and right child 
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index  # Assume current index has the smallest priority

        # Check if the left child exists and has a smaller priority than current smallest
        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left

        # Check if the right child exists and has a smaller priority than current smallest
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        # If the smallest is not the current index, we need to swap and continue. Otherwise, the function stops
        if smallest != index:
        # Swap current task with the task that has smaller priority
            temp = self.data[index]
            self.data[index] = self.data[smallest]
            self.data[smallest] = temp
        
            # Recursively heapify the affected subtree
            self.heapify_down(smallest)



# # Test your MinHeap class here including edge cases
# Invalid urgency values
print("\n--- Test 1: Invalid Urgency Values ---")
heap = MinHeap()
p1 = Patient("Alice", 0)   # Invalid urgency
p2 = Patient("Bob", 11)    # Invalid urgency
heap.insert(p1)
heap.insert(p2)
heap.print_heap()  # Expected: "List is empty."

# Insert one valid patient
print("\n--- Test 2: Insert One Valid Patient ---")
p3 = Patient("Charlie", 5)
heap.insert(p3)
heap.print_heap()  # Expected: "Charlie (Priority: 5)"

# Remove from an empty heap
print("\n--- Test 3: Remove from Empty Heap ---")
empty_heap = MinHeap()
print(empty_heap.remove_min())  # Expected: None

# Remove when only one patient exists
print("\n--- Test 4: Remove Single Patient ---")
single_heap = MinHeap()
single_heap.insert(Patient("Diana", 3))
removed = single_heap.remove_min()
print("Removed:", removed.name if removed else None)
single_heap.print_heap()  # Expected: "List is empty."

# Insert multiple patients with random priorities
print("\n--- Test 5: Insert Multiple Patients ---")
multi_heap = MinHeap()
patients = [
    Patient("Eve", 8),
    Patient("Frank", 2),
    Patient("Grace", 10),
    Patient("Heidi", 1)
]
for p in patients:
    multi_heap.insert(p)
multi_heap.print_heap()  # Expected: "Heidi (Priority: 1)" at root (first printed)

# Remove min from multi-patient heap
print("\n--- Test 6: Remove Minimum from Multi-Patient Heap ---")
served = multi_heap.remove_min()
print("Served:", served.name)
multi_heap.print_heap()  # Expected: "Frank (Priority: 2)" now root

# Using peak() on different states
print("\n--- Test 7: Peak Behavior ---")
print("Peak on non-empty heap:", multi_heap.peak().name)
empty_heap = MinHeap()
print("Peak on empty heap:", empty_heap.peak())

# Insert duplicate priorities
print("\n--- Test 8: Duplicate Priorities ---")
dup_heap = MinHeap()
dup_heap.insert(Patient("Ivy", 4))
dup_heap.insert(Patient("Jack", 4))
dup_heap.insert(Patient("Ken", 4))
dup_heap.print_heap()  # Expected: all three patients with priority 4

# Removing all until empty
print("\n--- Test 9: Remove All Until Empty ---")
while dup_heap.data:
    removed = dup_heap.remove_min()
    print(f"Removed: {removed.name} ({removed.urgency})")
print(dup_heap.data)

# Stress test with random values
print("\n--- Test 10: Stress Test (Random Priorities) ---")
import random
stress_heap = MinHeap()
for i in range(20):  # insert 20 patients with random urgency 1–10
    stress_heap.insert(Patient(f"Patient{i}", random.randint(1, 10)))

print("Removing all patients (should be in non-decreasing urgency order):")
last = -1
while stress_heap.data:
    patient = stress_heap.remove_min()
    print(patient.urgency, end=" ")
    # Sanity check: heap should never produce a smaller value than previous
    if patient.urgency < last:
        print("\n❌ Heap order violated!")
        break
    last = patient.urgency
print("\n✅ Heap order maintained.")

