#단일 링크드 리스트
class SLinkedList:

    class Node:
        def __init__(self, v, n = None):
            self.value = v #저장된 데이터
            self.next = n # 다음노드를 가리키는 변수

    #S_L_List에서 필요한 변수
    def __init__(self):
        self.head =None #처음 리스트 생성시에는 내부에 노드가 없기 때문에

    def insertNode(self, v):

        if self.head is None:
            # 헤드에 새노드를 저장한다.
            self.head = self.Node(v)
        else :
            self.head = self.Node(v,self.head)

    def printNode(self):

        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else :
            print("<현재 리스트 구조>", end='\t')
            link = self.head
            while link :
                print(link.value, '->', end=' ')
                link = link.next
            print()

    def deleteNode(self):

        if self.head is None:
            print("삭제할 노드가 없습니다.")
            return
        else:
            self.head = self.head.next

    def searchNode(self,v):

        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.head
            index =0
            while link:

                if v==link.value:
                    return index
                else :
                    link = link.next
                    index -=1


if __name__=="__main__":
    sl = SLinkedList()
    sl.insertNode('1st')
    sl.insertNode('2nd')
    sl.insertNode('3rd')
    print("<위치탐색>")
    result = sl.searchNode('1st')
    print("1st의 위치 : {}".format(result))

    result = sl.searchNode('555')
    print("555의 위치 : {}".format(result))
