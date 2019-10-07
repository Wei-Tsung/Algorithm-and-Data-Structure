## What is Linked-List ?

![LinkedList](https://github.com/Wei-Tsung/Core-Concepts-Visualization/blob/master/LinkedList.jpg)

#### Overview : 
<strong>Linked-list</strong> 的資料結構構成方式 : 是由節點<strong>Node</strong>儲存數值 , 同時這個<strong>Node</strong>包含一個<strong>指標(pointer)</strong>指向下一個<strong>Node</strong> , 而位於最後的Node則被設置為指向<strong>None</strong> 

---

與Array不同 , Array在查詢資料的時候可以直接使用index 查詢 , 效率較高 ;

Linked - list卻要透過第一個節點開始走訪每一個節點才能查詢到該資料 ;

--- 


但是Array無法彈性有效的使用到許多殘餘的記憶體空間 , 無法有效使硬體發揮其最大的效能

使用Linked-list結構就能有效彈性的運用這些散落在各處的記憶體空間 , 使硬體發揮其最大的功效

#### Memory Management 動態記憶體管理

![MemoryManagement](https://github.com/Wei-Tsung/Core-Concepts-Visualization/blob/master/Dynamic%20memeory%20management.jpeg)
![MemoryManagement](width='10')




![RemoveLinkedList](https://github.com/Wei-Tsung/Core-Concepts-Visualization/blob/master/RemoveLinkedList.jpg)


![InsertLinkedList](https://github.com/Wei-Tsung/Core-Concepts-Visualization/blob/master/InsertLinkedList.jpg)

Leetcode : Desigining Linkedlist

需要建立的 function

>get(index) : 輸入 index 可以取得在 linked-List 裡對應的 val。

>addAtHead(val) : 將輸入的 val 新增在 linked-List 的第一個位置。

>addAtTail(val) : 將輸入的 val 新增在 linked-List 的最後一個位置。

>addAtIndex(index, val) : 在 linked-List 中，指定 index 的位置插入 val。

> addAtIndex:
>>當 index 等於 linked-List 的長度，將 val 插在最後一個位置。
>>當 index 大於 linked-List 的長度，則 val 不會插入 linked-List。
>>當 index 為負數，將 val 插在第一個位置。

>deleteAtIndex(index) : 如果 index 在 linked-List 裡是有效的，刪除對應的 val。
