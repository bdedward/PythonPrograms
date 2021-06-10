#This Solution will take two Singly-Linked Lists and return the summation 
#of the two numbers in a new linked list

#The Most Significant digit for each number is the tail element of the linked lists

#The Most Significant digit for the final number is the head element of the final list

#Example:
#        List1: 9->9->9->9->9
#        List2: 9->9->9
# Result: 
#        Final List: 1->0->0->9->9->8

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        num2 = []
        while l1 or l2:
            while l1:
                num1.append(l1.val)
                l1 = l1.next
            while l2:
                num2.append(l2.val)
                l2 = l2.next
        
        x = 0
        if len(num2) > len(num1):
            x = len(num2)
            for i in range(len(num1)-1,len(num2)-1):
                num1.insert(len(num1),0)
        else:
            x = len(num1)
            for i in range(len(num2)-1,len(num1)-1):
                num2.insert(len(num2),0)
            
        carry = -1
        summation = ""    
        resultList = []
        for i in range(x):
            temp = ListNode(0)
            if carry == -1:
                sumnum = num1[i] + num2[i]
            else:
                sumnum = num1[i] + num2[i] + carry
                carry = -1
                
            if sumnum > 9:
                temp.val = sumnum - 10
                carry = 1
            else:
                temp.val = sumnum
                
            resultList.append(temp)
        
        if carry != -1:
            tempNode = ListNode(carry)
            resultList.append(tempNode)
            
        for i in range(len(resultList)-1):
            resultList[i].next = resultList[i+1]

            
        return resultList[0]
