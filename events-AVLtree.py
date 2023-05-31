class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date


class AVLNode:
    def __init__(self, event):
        self.event = event
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, event):
        self.root = self._insert(self.root, event)

    def _insert(self, node, event):
        if node is None:
            return AVLNode(event)

        if event.date < node.event.date:
            node.left = self._insert(node.left, event)
        else:
            node.right = self._insert(node.right, event)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance_factor = self._get_balance_factor(node)

        if balance_factor > 1:
            if event.date < node.left.event.date:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance_factor < -1:
            if event.date > node.right.event.date:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def search_range(self, start_date, end_date):
        result = []
        self._search_range(self.root, start_date, end_date, result)
        return result

    def _search_range(self, node, start_date, end_date, result):
        if node is None:
            return

        if start_date <= node.event.date <= end_date:
            result.append(node.event)

        if start_date < node.event.date:
            self._search_range(node.left, start_date, end_date, result)

        if node.event.date < end_date:
            self._search_range(node.right, start_date, end_date, result)


# Contoh penggunaan
avl_tree = AVLTree()

# Menjadwalkan event-event
event1 = Event("Event A", "2023-05-31")
event2 = Event("Event B", "2023-06-02")
event3 = Event("Event C", "2023-06-01")
event4 = Event("Event D", "2023-06-03")

avl_tree.insert(event1)
avl_tree.insert(event2)
avl_tree.insert(event3)
avl_tree.insert(event4)

# Mencari event-event dalam rentang tanggal tertentu
result = avl_tree.search_range("2023-05-31", "2023-06-02")
for event in result:
    print(event.name)  # Output: Event A, Event C, Event B