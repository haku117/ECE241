""" Shifted Binary search (get position of the product).
A shelf contains some products sorted according to their width,
we place more already sorted products with lesser width than
the one that are already present. |||10,20||1,2,4,7|||
find the position of a given book (no sorting allowed and find it in O(log N))
"""


class CorrectShelf:

    def search_product(self, shelf_contents, lower_l, upper_l, product):
        if not shelf_contents:
            return -1

        if lower_l is upper_l:
            return lower_l if shelf_contents[lower_l] is product else -1

        mid = int((lower_l + upper_l) / 2)

        if shelf_contents[mid] is product:
            return mid

        # somewhere in 2nd sorted part
        if shelf_contents[lower_l] <= shelf_contents[mid]:
            if shelf_contents[lower_l] <= product <= shelf_contents[mid]:
                return self.search_product(shelf_contents, lower_l, mid - 1, product)
            return self.search_product(shelf_contents, mid + 1, upper_l, product)

        if shelf_contents[mid] <= product <= shelf_contents[upper_l]:
            return self.search_product(shelf_contents, mid + 1, upper_l, product)
        return self.search_product(shelf_contents, lower_l, mid - 1, product)


    def locate_product(self, pos, shelf_contents):
        '''
        Notifies the position of the product under consideration
        '''
        if pos <-1:
            print("\nNo such product!!")

        if pos is not -1:
            print("\n########### Found product on the Shelf ###########")
            for i, width in enumerate(reversed(shelf_contents)):
                if i is len(shelf_contents) - 1 - pos:
                    print("found product with width:{} ".format(width))
            print("\n##################################################")
        else:
            print("\nNo such product!!")

def main():

    shelf_contents = [10, 20, 1, 2, 3, 6, 7]
    shelf_obj = CorrectShelf()
    product_to_be_found = 1
    pos = shelf_obj.search_product(shelf_contents, 0, len(shelf_contents) - 1, product_to_be_found)
    print("pos:{}".format(pos))
    shelf_obj.locate_product(pos, shelf_contents)

if __name__ == '__main__':
    main()
