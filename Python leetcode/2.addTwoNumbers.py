"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

 #first attempt
 class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3= ListNode(0)
        a,b,c=l1,l2,l3
        while True:
            x=a.val+b.val+c.val
            c.val=x%10
            a,b,c.next=a.next,b.next,ListNode(x//10)
            if a==None and b==None:
                if x//10==0:
                    c.next=None
                break
            elif a==None:
                a=ListNode(0)
            elif b==None:
                b=ListNode(0)
            c=c.next
            
        return l3

##best time complexty solution

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            carry = total//10
            tempNode = ListNode(total%10)
            current.next = tempNode
            current = current.next 

        return(dummy.next)

"""very clean wouldn't need temp node but i understan how it works mine solution is more complicated
and complecationg not good"""

"""using while or is a really good way of checking if either the elements exist and 
assigning a crry node outside loop is also great i woukd one day come back and write code like this"""