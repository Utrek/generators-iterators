
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self._stopped = False
        self.cursor= 0
        self.next_cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
       if not self._stopped:
            while self.cursor < len(self.list_of_list):
                if self.next_cursor < len(self.list_of_list[self.cursor]):
                    item = self.list_of_list[self.cursor][self.next_cursor]
                    self.next_cursor += 1
                    return item

                self.cursor += 1
                self.next_cursor = 0
            self._stopped = True
            raise StopIteration
      
    

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

