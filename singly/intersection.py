class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    Pa=headA
    Pb=headB

    while Pa!=Pb:
        Pa=Pa.next if Pa else headB
        Pb=Pb.next if Pb else headA
    return Pa

