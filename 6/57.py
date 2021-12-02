# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        new = ListNode('head')
        new_cur = new
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                new_cur.next = l1
                new_cur = new_cur.next
                l1 = l1.next
            else:
                new_cur.next = l2
                new_cur = new_cur.next
                l2 = l2.next

        if l1 is None:
            new_cur.next = l2
        else:
            new_cur.next = l1

        return new.next


def Init_node(s: str) -> ListNode:
    # s = s.split('->')
    head_node = ListNode('head')

    for i in s:
        new_node = ListNode(int(i))
        cur_node = head_node
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node

    return head_node.next
def show_node(node:ListNode):
    while node is not None:
        print(node.val,end=' ')
        node = node.next
    print('')



s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]
list_node_1 = Init_node(s1)
list_node_2 = Init_node(s2)

solu = Solution()
merge = solu.mergeTwoLists(list_node_1, list_node_2)
show_node(merge)
