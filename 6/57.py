class ListNode(object):
    """节点"""
  
    def __init__(self, elem):
        self.elem = elem
        self.next = None  
    
    # 初始设置下一节点为空

class Solution:
 
    def initList(self, data):
        # 判断是否为空
        if len(data) == 0:
            return
        else:
            # 创建头结点
            self.head = ListNode(data[0])
            # 头结点
            r = self.head  
            # 指针 
            p = self.head   
            # 逐个为 data 内的数据创建结点, 建立链表
            for i in data[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
            return r
 
if __name__ == "__main__":
    test = Solution()
    data1 = [1, 3, 2]
    l1 = test.initList(data1)
    print(l1.val, "->", l1.next.val, "->", l1.next.next.val)