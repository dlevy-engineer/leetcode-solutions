from typing import Optional
import sys
import time

# definition for singly-linked list
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def constructSinglyLinkedList(size):

    # base case for a list of length 0
    if int(size) == 0:
        return
    
    # initiate the head node
    head = ListNode(1)
    # construct a pointer to the head node
    cur_node = head
    
    # instantiate a counter
    i = 2
    # add new nodes until we reach the desired linked list length
    while i <= int(size):

        # create a new node with current counter value
        new_node = ListNode(i)
        # point the current node to the new node
        cur_node.next = new_node
        # set new node as current node for next iteration
        cur_node = new_node
        # increment the counter
        i += 1

    return head


def listify(ll):

    ret_list = []
    while ll:
        ret_list.append(ll.val)
        ll = ll.next

    return ret_list


########

class Solution:

    ## RECURSIVE APPROACH
    def recursiveSwapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # address the case where we don't have at least two nodes to swap
        if not (head and head.next):
            return head
        
        # instantiate a reference to the node following the current "head"
        sec_node = head.next

        # recursively point the head to the node returned by
        # calling this function on the node two spaces away
        head.next = self.recursiveSwapPairs(head.next.next)

        # point the node following the current head back to the the current head
        sec_node.next = head

        return sec_node
    
    ## ITERATIVE APPROACH
    def iterativeSwapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur_node = head

        while (cur_node and cur_node.next):
            cur_node.next, cur_node.next.next = cur_node.next, cur_node
            cur_node = cur_node.next.next

        return head


########

def main():
    l = input('\nWhat size list would you like to work with?   ')

    linked_list = constructSinglyLinkedList(l)
    node = linked_list

    disp_list = []
    while node:
        disp_list.append(node.val)
        node = node.next

    print(f'\nGreat then we are going to swap nodes in pairs for the following singly linked list:\n\n{disp_list}\n\n')

    sol = Solution()

    rec_start = time.time()
    rec_sol = sol.recursiveSwapPairs(linked_list)
    rec_stop = time.time()

    #it_sol = sol.iterativeSwapPairs(linked_list)

    print(f"""With the recursive method, we get an answer of:  {listify(rec_sol)}
    Clocking in at a runtime of {rec_stop-rec_start} seconds.""")

    #print(f'With the iterative method, we get an answer of:  {it_sol}')

if __name__ == '__main__':
    sys.exit(main())