class HeapElement:
    def __init__(self, value, index, compare_value):
        self.value = value
        self.index = index 
        self.compare_value = compare_value

class Heap:
    def __init__(self):
        self.array: list[HeapElement] = []

    def length(self) -> int:
        return len(self.array)

    def contains(self, value) -> bool:
        for item in self.array:
            if(item.value == value):
                return True
        return False

    def append(self, item, compare_value):
        new_element = HeapElement(item, len(self.array), compare_value)
        self.array.append(new_element)
        self.sort_up(new_element)

    def take_first(self):
        first_item = self.array[0]
        new_first_item = self.array.pop()
        if(len(self.array) > 0):
            new_first_item.index = 0
            self.array[0] = new_first_item
            self.sort_down(new_first_item)
        return first_item.value

    def sort_up(self, item: HeapElement):
        parent_index = (item.index - 1)//2
        if(parent_index < 0):
            return

        parent_item = self.array[parent_index]

        if(item.compare_value < parent_item.compare_value):
            self.swap_items(item, parent_item)
            item.index = parent_index
            self.sort_up(item)

    def sort_down(self, item: HeapElement):
        child_left_index = item.index * 2 + 1
        child_right_index = item.index * 2 + 2

        if (child_left_index < len(self.array)):
            swap_index = child_left_index

            if(child_right_index < len(self.array)):
                child_left_item = self.array[child_left_index]
                child_right_item = self.array[child_right_index]
                if(child_left_item.compare_value > child_right_item.compare_value):
                    swap_index = child_right_index

            self.swap_items(item, self.array[swap_index])
            item.index = swap_index
            self.sort_down(item)
          
    def swap_items(self, item_a: HeapElement, item_b: HeapElement):
            item_a.index, item_b.index = item_b.index, item_a.index
            self.array[item_a.index] = item_a
            self.array[item_b.index] = item_b

# some test code

# heap = Heap()
# heap.append(5, 5)
# heap.append(2, 2)
# heap.append(3, 3)
# heap.append(4, 4)
# heap.append(6, 6)
# heap.append(1, 1)
# print(heap.take_first())
# print("heap:")
# for item in heap.array:
#     print(item.value)


