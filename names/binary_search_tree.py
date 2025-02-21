class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if not self.value:
            self.value = value
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE
        # if element == target
        if self.value == target:
            # return true
            return True
        # LEFT CASE
        # if target < element
        if target < self.value:
            if not self.left:
                return False
            # return left.contains(target)
            return self.left.contains(target)
        # RIGHT CASE
        # else 
        else:
            if not self.right:
                return False
            # return right.contains(target)
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # go to right until there is no more elements
        if self.right:
            return self.right.get_max()
        # return the last element
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
