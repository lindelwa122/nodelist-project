from colorful_test.testcase import TestCase
from colorful_test.message import show_message

from nodelist import NodeList

class TestNodeList(TestCase):
    # Test that _Node exists
    @show_message(
        fail='_Node object (class) does not exist',
        success='_Node object (class) does exist'
    )
    def test_that__Node_exists_0(self):
        self.assert_true(hasattr(NodeList, 'Node'))
        
    # Test that _Node has value and next as properties
    @show_message(
        fail='_Node object doesn\'t have either value or next',
        success='_Node object has all expected properties'
    )
    def test_that__Node_props_exist_1(self):
        self.assert_true(hasattr(NodeList.Node(1), '_value'))
        self.assert_true(hasattr(NodeList.Node(1), '_next'))
        
    @show_message(fail='''
        When printed or stringified your NodeList must have all elements surrounded by square brackes ([])
        and seperated by a comma and a space, eg [1, 2, 3].
        
        Yours show %f instead of %s
    ''')
    # Test that the NodeList representation is what is expected to be
    def test_NodeList_representation_2(self):
        ndl = NodeList()
        self.assert_equal(str(ndl), '[]')
        
        ndl = NodeList(1)
        self.assert_equal(str(ndl), '[1]')
        
        ndl = NodeList(1, 2, 3)
        self.assert_equal(str(ndl), '[1, 2, 3]')
        
    # Test that the length of NodeList is accurate
    @show_message(
        fail='''
            The length of the NodeList is not working as expected. 
            Use the __len__ magic method to implement the length.
            
            The __len__ magic method is what python calls when you
            call len on an object.
            
            Yours returns %f instead of %s
        ''',
        success='The length of the NodeList is handled accurately.'
    )
    def test_len_3(self):
        ndl = NodeList()
        self.assert_equal(len(ndl), 0)
        
        ndl = NodeList(1)
        self.assert_equal(len(ndl), 1)
        
        ndl = NodeList(1, 2, 3, 'banana')
        self.assert_equal(len(ndl), 4)
    
    # Test that elements are appended to the list
    @show_message(
        fail='''
            Elements are not appended to the NodeList. Check your
            implementation of append.
            
            I received %f but I expected %s.
        ''',
        success='append works as expected.'
    )  
    def test_append_4(self):
        ndl = NodeList()
        self.assert_equal(len(ndl), 0)
        
        ndl.append(1)
        self.assert_equal(len(ndl), 1)
        
        ndl.append(2)
        self.assert_equal(len(ndl), 2)
        self.assert_equal(str(ndl), '[1, 2]')
        
        ndl.append(3)
        self.assert_equal(len(ndl), 3)
        self.assert_equal(str(ndl), '[1, 2, 3]')
        
    # Test that elements are extended to the list
    @show_message(
        fail='''
        The extend method should extend your NodeList. It must receive an
        an iterable and use that to extend the list.
        
        Here's an example and its usage:
        
        n = NodeList(1, 2, 3)
        n.extend([4, 5, 6]) 
        
        The above code should extend your current NodeList by adding 3
        additional nodes. The new NodeList should look like: 
        [1, 2, 3, 4, 5, 6]
        
        Expected output: %s
        Received: %f
        ''',
        success='extend works as expected'
    )
    def test_extend_5(self):
        ndl = NodeList(1, 2, 3)
        ndl.extend([4])
        
        self.assert_equal(len(ndl), 4)
        self.assert_equal(str(ndl), '[1, 2, 3, 4]')
        
        ndl.extend([5, 6, 7])
        self.assert_equal(len(ndl), 7)
        self.assert_equal(str(ndl), '[1, 2, 3, 4, 5, 6, 7]')
        
        ndl.extend([])
        self.assert_equal(len(ndl), 7)
        self.assert_equal(str(ndl), '[1, 2, 3, 4, 5, 6, 7]')
    
    # Test that you can insert an item to the list
    @show_message(
        fail='''
        The insert method should insert an item at any given index in your
        NodeList. 
        
        Here's an example:
        
        n = NodeList(1, 2, 3)
        n.insert(1, 'banana')
        
        The above code should add 'banana' at location 1 (as the second element)
        of your NodeList. NodeList should not look like this: [1, banana, 2, 3]
        
        Expected output: %s
        Received: %f
        '''
    )
    def test_insert_6(self):
        ndl = NodeList(1, 2, 3)
        ndl.insert(1, 'a')
        self.assert_equal(str(ndl), '[1, a, 2, 3]')
        
        ndl.insert(0, 'b')
        self.assert_equal(str(ndl), '[b, 1, a, 2, 3]')
        
        ndl.insert(5, 'c')
        self.assert_equal(str(ndl), '[b, 1, a, 2, 3, c]')
        
        ndl.insert(100, 'd')
        self.assert_equal(str(ndl), '[b, 1, a, 2, 3, c, d]')
        
        ndl.insert(-1, 'e')
        self.assert_equal(str(ndl), '[b, 1, a, 2, 3, c, e, d]')
        
        ndl.insert(-23, 'f')
        self.assert_equal(str(ndl), '[f, b, 1, a, 2, 3, c, e, d]')
        
    # Test that insert handles errors correctly
    @show_message(
        fail='the insert method should only work with integers as indices',
        success='insert works as expected'
    )
    def test_insert_exception_7(self):
        ndl = NodeList()
        i = '0'
        self.assert_raises(
            TypeError,
            ndl.insert,
            i
        )
        
        ndl = NodeList()
        i = []
        self.assert_raises(
            TypeError,
            ndl.insert,
            i
        )
        
    # Test that an unwanted item can be removed from the list
    @show_message(
        fail='''
        The remove method should remove the first occurrence of the 
        specified item from your NodeList.

        Here's an example:

        n = NodeList(1, 2, 3, 4)
        n.remove(3)
        
        The above code should remove the first occurrence of 3 from your 
        NodeList. The updated NodeList should look like this: [1, 2, 4].

        Expected output: %s
        Received: %f
        '''
    )
    def test_remove_8(self):
        ndl = NodeList(1, 2, 3)
        ndl.remove(2)
        self.assert_equal(str(ndl), '[1, 3]')
        
        ndl.extend([4, 4, 5, 6, 4, 7])
        ndl.remove(4)
        self.assert_equal(str(ndl), '[1, 3, 4, 5, 6, 4, 7]')
        
        ndl.remove(7)
        self.assert_equal(str(ndl), '[1, 3, 4, 5, 6, 4]')
        
    # Test that remove handles errors correctly
    @show_message(
        fail='the remove method should raise an error if the target is not in the list',
        success='remove works as expected'
    )
    def test_remove_exception_9(self):
        ndl = NodeList(1, 2, 3)
        self.assert_raises(
            ValueError,
            ndl.remove,
            4
        )
        
        self.assert_raises(
            ValueError,
            ndl.remove,
            7
        )
        
    # Test that you can pop an item from list
    @show_message(
        fail='''
        The pop method should remove and return an item at the specified 
        index from your NodeList. If no index is provided, it should 
        remove and return the last item.

        Here's an example:

        n = NodeList(1, 2, 3, 4)
        item = n.pop(2)
        
        The above code should remove the item at index 2 (the third 
        element), which is 3, from your NodeList. After the operation, 
        NodeList should look like this: [1, 2, 4], and the returned value 
        should be 3.

        Expected output: %s
        Received: %f
        '''
    )
    def test_pop_10(self):
        ndl = NodeList(1, 2, 3)
        
        ndl.pop()
        self.assert_equal(str(ndl), '[1, 2]')
        
        ndl.pop(0)
        self.assert_equal(str(ndl), '[2]')
        
        ndl.extend([4, 5, 6])
        ndl.pop(1)
        self.assert_equal(str(ndl), '[2, 5, 6]')
        
        ndl.pop(-2)
        self.assert_equal(str(ndl), '[2, 6]')
        
    # Test that pop returns an item
    @show_message(
        fail='pop should return the item after its removal',
    )
    def test_pop_11(self):
        ndl = NodeList(1, 2, 3)
        item = ndl.pop()
        self.assert_equal(item, 3)
        
        item = ndl.pop(1)
        self.assert_equal(item, 2)
        
    # Test that you cannot pop from an empty list
    @show_message(
        fail='pop should not pop from an empty list',
    )
    def test_pop_exception_12(self):
        ndl = NodeList()
        self.assert_raises(
            IndexError,
            ndl.pop,
        )
        
    # Test that you cannot pop out of index
    @show_message(
        fail='pop should not pop using an index out of range',
    )
    def test_pop_exception_13(self):
        ndl = NodeList(1, 2, 3)
        self.assert_raises(
            IndexError,
            ndl.pop,
            98,
        )
        
    # Test that you can only use integers to pop
    @show_message(
        fail='pop should only when index is an integer',
        success='pop works as expected'
    )
    def test_pop_exceptions_14(self):
        ndl = NodeList(1, 2, 3)
        i = 'i am an integer too'
        self.assert_raises(
            TypeError,
            ndl.pop,
            i
        )
        
    # Test that you can clear a list
    @show_message(
        fail='''
        The clear method should remove all items from your NodeList, 
        leaving it empty.

        Here's an example:

        n = NodeList(1, 2, 3, 4)
        n.clear()
        
        The above code should remove all elements from your NodeList. 
        After the operation, NodeList should look like this: [].

        Expected output: %s
        Received: %f
        ''',
        success='clear works as expected'
    )
    def test_clear_15(self):
        ndl = NodeList(1, 2, 3)
        ndl.clear()
        self.assert_equal(len(ndl), 0)
        
        ndl = NodeList(1, 2, 3, 4, 5)
        ndl.clear()
        self.assert_equal(len(ndl), 0)
        
        ndl = NodeList()
        ndl.clear()
        self.assert_equal(len(ndl), 0)
        
    # Test that you can get an index of an item
    @show_message(
        fail='''
        The index method should return the first index of a given item in
        your NodeList.

        Here's an example:

        n = NodeList(1, 2, 3, 4, 2)
        idx = n.index(2)
        
        The above code should return 1 because 2 first appears at index 1
        in the NodeList.

        Expected output: %s
        Received: %f
        '''
    )
    def test_index_16(self):
        ndl = NodeList('apple', 'banana', 'blueberry', 'strawberry', 'lemon')
        index = ndl.index('banana')
        self.assert_equal(index, 1)
        
        index = ndl.index('lemon')
        self.assert_equal(index, 4)
        
        index = ndl.index('apple')
        self.assert_equal(index, 0)
        
        index = ndl.index('lemon', 2)
        self.assert_equal(index, 4)
        
    # Test that slice indices in index are only integers
    @show_message(
        fail='a TypeError error should be raised if slice indices are not integers',
    )
    def test_index_exception_17(self):
        ndl = NodeList('apple', 'banana', 'blueberry', 'strawberry', 'lemon')
        self.assert_raises(
            TypeError,
            ndl.index,
            'blueberry',
            [],
            'it\'s my life',
        )
        
    # Test that you cannot index something not in the list
    @show_message(
        fail='a ValueError should be raised the item is not in the list',
        success='index works as expected'
    )
    def test_index_exception_18(self):
        ndl = NodeList('apple', 'banana', 'blueberry', 'strawberry', 'lemon')
        self.assert_raises(
            ValueError,
            ndl.index,
            'pie'
        )
        
    @show_message(
        fail='''
        The count method should return the number of occurrences of a 
        given item in your NodeList.

        Here's an example:
        
        n = NodeList(1, 2, 3, 2, 4, 2)
        cnt = n.count(2)
        
        The above code should return 3 because 2 appears three times in
        the NodeList.

        Expected output: %s
        Received: %f
        ''',
        success='count works as expected'
    )
    # Test that you can count the items in the list
    def test_count_19(self):
        ndl = NodeList(1, 2, 4, 4, 42, 1, 3, 5, 6, 3, 6, 6, 7, 4, 7)
        
        self.assert_equal(ndl.count(1), 2)
        self.assert_equal(ndl.count(4), 3)
        self.assert_equal(ndl.count('bananas'), 0)
        
    # Test that you can copy a list
    @show_message(
        fail='the copy of a NodeList should also be a NodeList'
    )
    def test_copy_20(self):
        ndl = NodeList(1, 2, 3)
        copy = ndl.copy()     
        self.assert_is_instance(copy, NodeList)
        
    # Test that you can copy a list
    @show_message(
        fail='the copy of the list should have the same elements as the original'
    )
    def test_copy_21(self):
        ndl = NodeList(1, 2, 3)
        copy = ndl.copy()
        self.assert_equal(str(copy), str(copy))
        
        ndl = NodeList('a', 'c', 'd')
        copy = ndl.copy()
        self.assert_equal(str(copy), str(ndl))
        
    # Test that a copy is not the same as the original
    @show_message(
        fail='''
        When copying a NodeList the copy should have the same 
        elements as the original but they should not be identical. This
        just means both NodeLists should be have different references (or
        stored in different locations in memory). 
        
        Mutating the other original should not affect the copy, and vice 
        versa.
        
        Expected output: %s
        Received: %f
        ''',
        success='copy works as expected'
    )
    def test_copy_22(self):
        ndl = NodeList(1, 2, 3)
        copy = ndl.copy()
        
        ndl.append(4)
        self.assert_equal(str(copy), '[1, 2, 3]')
        
        copy.append(5)
        self.assert_equal(str(ndl), '[1, 2, 3, 4]')
        
    # Test that you can reverse the list
    @show_message(
        fail='''
        The reverse method should reverse the order of elements in your
        NodeList in place.

        Here's an example:

        n = NodeList(1, 2, 3, 4)
        n.reverse()
        
        The above code should modify the NodeList to look like this: [4, 3, 2, 1].

        Expected output: %s
        Received: %f
        ''',
        success='reverse works as expected'
    )
    def test_reverse_23(self):
        ndl = NodeList(1, 2, 3)
        ndl.reverse()
        self.assert_equal(str(ndl), '[3, 2, 1]')
        
        ndl = NodeList('monkeys', 'cats', 'dogs')
        ndl.reverse()
        self.assert_equal(str(ndl), '[dogs, cats, monkeys]')
        
        ndl = NodeList(3, 'd', 4, 0)
        ndl.reverse()
        self.assert_equal(str(ndl), '[0, 4, d, 3]')
        
    # Test that you can sort the list
    def test_sort_24(self):
        ndl = NodeList(3, 1, 5, 2)
        ndl.sort()
        self.assert_equal(str(ndl), '[1, 2, 3, 5]')
        
        
        ndl.sort(reverse=True)
        self.assert_equal(str(ndl), '[5, 3, 2, 1]')
        
        ndl = NodeList('Johannesburg', 'Jakarta', 'Tokyo', 'Lisbon', 'NYC', 'Namaqualand')
        ndl.sort(key=lambda item: len(item))
        self.assert_equal(str(ndl), '[NYC, Tokyo, Lisbon, Jakarta, Namaqualand, Johannesburg]')
        
    # Test that you can get an item from the list
    def test___getitem___25(self):
        ndl = NodeList(1, 2, 3)
        self.assert_equal(ndl[0], 1)
        self.assert_equal(ndl[1], 2)
        self.assert_equal(ndl[2], 3)
        self.assert_equal(ndl[-1], 3)
        self.assert_equal(ndl[-2], 2)
        self.assert_equal(ndl[-3], 1)
        
    # Test that you cannot get item out of index
    def test___getitem___exception_26(self):
        ndl = NodeList(1, 2, 3)
        
        def test_1(): ndl[100]
        self.assert_raises(
            IndexError,
            test_1,
        )
        
        def test_2(): ndl[-4]
        self.assert_raises(
            IndexError,
            test_2,
        )
        
    # Test that you can set an item to list using an index
    def test___setitem___27(self):
        ndl = NodeList(1, 2, 3, 4, 5, 6)
        ndl[0] = 'banana'
        ndl[2] = 'Lana'
        ndl[4] = 'Friday'
        ndl[-1] = 'found'
        
        self.assert_equal(str(ndl), '[banana, 2, Lana, 4, Friday, found]')
        
    # Test that only integers can be used as indices to set items
    def test___setitem___exception_28(self):
        ndl = NodeList(1, 2, 3)
        
        def test(): ndl['last index'] = 'Billy'
        self.assert_raises(
            TypeError,
            test,
        )
        
    # Test that you can only use indices within range to assign items
    def test___setitem___exception_29(self):
        ndl = NodeList(1, 2, 3)
        
        def test_1(): ndl[-7] = 'Bobby'
        self.assert_raises(
            IndexError,
            test_1
        )
        
        def test_2(): ndl[7] = 'Cecil'
        self.assert_raises(
            IndexError,
            test_2
        )
        
    # Test that you can delete an item from the list
    def test___delitem___30(self):
        ndl = NodeList(1, 2, 3)
        del ndl[1]
        self.assert_equal(str(ndl), '[1, 3]')
        
        del ndl[-2]
        self.assert_equal(str(ndl), '[3]')
        
    # Test that you can only use integers or slices to delete an item
    def test___delitem___exception_31(self):
        ndl = NodeList(1, 2, 3)
        def test(): del ndl['integer']
        
        self.assert_raises(
            TypeError,
            test,
        )
        
    # Test that you can concatenate a NodeList to a NodeList
    def test___add___32(self):
        ndl = NodeList(1, 2, 3)
        ndl += NodeList(4, 5, 6)
        self.assert_equal(str(ndl), '[1, 2, 3, 4, 5, 6]')
        
        ndl += NodeList('banana', 'grape')
        self.assert_equal(str(ndl), '[1, 2, 3, 4, 5, 6, banana, grape]')
        
    # Test that you can only concatenate a NodeList to a NodeList
    def test___add___exception_33(self):
        ndl = NodeList(1, 2, 3)
        def test(ndl): ndl += [4, 5, 6]
        
        self.assert_raises(
            TypeError,
            test,
            ndl
        )
        
if __name__ == '__main__':
    TestNodeList.run_and_output_results()
        