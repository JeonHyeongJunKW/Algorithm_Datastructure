
class DLinkedList:

    class Node:
        def __init__(self,v,n=None,p=None):
            self.value= v
            self.next = n
            self.prev = p


    def __init__(self):
        self.head = None
        self.tail = None

    def insertNodeBefore(self, v):
        # 새로운 노드를 넣는과정에서 신경써야하는 것
        """
        1. 현재 head가 가리키는 기존노드의 prev를 새로 생성하는 노드로 지정
        2. 새로 생성한 노드의 next를 기존 노드로 지정
        3. head를 새로 생성한 노드로 변경
        """

        if self.head is None:
            self.head = self.Node(v)
            self.tail = self.head
        else:
            self.head.prev = self.Node(v,n=self.head)# 1,2 번을 동시에 함.
            self.head = self.head.prev

    def insertNodeAfter(self, v):
        # 새로운 노드를 넣는과정에서 신경써야하는 것
        """
        1. 현재 tail이 가리키는 기존노드의 next를 새로 생성하는 노드로 지정
        2. 새로 생성한 노드의 prev를 기존 노드로 지정
        3. tail을 새로 생성한 노드로 변경
        """
        if self.tail is None:
            self.tail = self.Node(v)
            self.head = self.tail
        else:
            self.tail.next = self.Node(v, p=self.tail)
            self.tail = self.tail.next
    def printNodeBefore(self):

        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            print("<현재 리스트 구조>", end='\t')
            link = self.head

            while link:
                print(link.value,"<->",end= ' ')
                link= link.next
            print("")
    def printNodeAfter(self):

        if self.tail is None:
            print("저장된 데이터가 없음")
            return
        else:
            print("<현재 리스트 구조>", end='\t')
            link = self.tail

            while link:
                print(link.value,"<->",end= ' ')
                link= link.prev
            print("")
    def deleteNodeBefore(self):

        if self.head is None:
            print("삭제할 노드가 없습니다.")
            return
        else:
            #1 현재 head가 가리키는 노드의 next를 새로운 헤드로 지정
            self.head = self.head.next
            #2 새로운 head의 prev를 None으로 변경
            self.head.prev = None

    def deleteNodeAfter(self):

        if self.tail is None:
            print("삭제할 노드가 없습니다.")
            return
        else :
            #1 현재 tail이 가리키는 노드의 prev를 tail로  지정
            self.tail = self.tail.prev
            #2. 현재 tail의 next를 None로 지정
            self.tail.next = None

    def searchNodeBefore(self,v):
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.head
            index = 0
            while link:

                if v == link.value:
                    return index
                else :
                    link = link.next
                    index +=1

    def searchNodeAfter(self, v):
        if self.tail is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.tail
            index = 0
            while link:

                if v == link.value:
                    return index
                else:
                    link = link.prev
                    index -= 1

if __name__=="__main__":
    dl = DLinkedList()
    dl.insertNodeBefore('1stF')
    dl.insertNodeAfter('1stB')
    dl.insertNodeBefore('2ndF')
    dl.insertNodeAfter('2ndB')
    dl.printNodeBefore()

    print("<head로 위치 탐색>")
    result = dl.searchNodeBefore('2ndF')
    print("2ndF 위치 : {}".format(result))

    result = dl.searchNodeBefore('1stF')
    print("1stF 위치 : {}".format(result))

    # tail로 탐색
    print("<tail로 위치 탐색>")
    result = dl.searchNodeAfter('2ndB')
    print("2ndB 위치 : {}".format(result))

    result = dl.searchNodeAfter('1stF')
    print("1stF 위치 : {}".format(result))