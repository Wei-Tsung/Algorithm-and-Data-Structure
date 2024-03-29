
>>演算法效率比較圖(Comparison)

<img src='https://github.com/Wei-Tsung/Core-Concepts-Visualization/blob/master/%E4%BD%9C%E6%A5%AD%E4%BA%8C%20%E6%BC%94%E7%AE%97%E6%B3%95%E6%95%88%E7%8E%87%E6%AF%94%E8%BC%83%E5%9C%96.png'>

> 此圖原創作者，來自參考連結Algorithmic Analysis

### 時間複雜度 :
> Heap Sorting : >　Merge Sorting : > Quick Sorting : 


### Merge Sorting　合併排序法 :
---

<img src='https://github.com/Wei-Tsung/Core-Concepts-Visualization/blob/master/%E5%88%86%E6%B2%BB%E6%B3%95.png' width=650 height=500>

> 此原圖作者來自參考連結中的

---

Merge Sorting 是分治(Divide and Conquer)演算法的一種，與Quick Sort一樣，<br>一定會有切割到最小單位並進行處理的過程(Atomize)<br>

如圖一所示，演算法會把原始的資料Array切割成單位為1的最小單位，然後兩兩排序過後合併起來，一步一步重新再構築成經過排序過的原始的大小；<br>


與Qucik sort不一樣的地方在，Merge Sort 無論如何總是頃向對稱的方式切割(若奇數個有其中一邊會多一個)；<br>Quick Sort則是會以某個位置的值為基準點
視情況而定來切割，左右兩邊大小更常會呈現不對稱的情況，效率上Quick Sort更加好一些<br>


---

#### 實現過程：

---

首先會將這 n 筆資料對半切割成兩等分（大小皆為 n/2）；<br>　

把這兩等分的中間的index設置為midpoint<br>
其中左半邊為left_Section，右半邊為right_Section

接著，再將這兩堆大小為 n/2 的資料各自分為兩等分（大小皆為 n/2^2）；<br>同樣的，我們再將這四堆大小為 n/4 的資料各自再切為兩等分（大小皆為 n/2^3）。<br>

如此循環進行切割下去，直到每個片段的資料量足夠小（一般為1單位）之後，我們就分別將小單位的資料進行排序，
再將這些資料單位兩兩一對進行合併，直到全部排序完成，同時還原原本資料的大小。

---

<strong>Insight:</strong><br>

因為Merge Sorting從一開始的切割，到最後的還原過程，彼此之間有相互繼承的連續性關係，所以使用遞迴關係來實現可以讓程式碼更加的簡潔優雅

---


### Heap Sorting 堆積排序法 :

<img src='https://github.com/Wei-Tsung/Core-Concepts-Visualization/blob/master/Heap%20Sort%20%E4%BD%9C%E6%A5%AD%E4%BA%8C.png' width=800 height=550>

> 此原圖作者為參考連結中的 James Le <p>


- 時間複雜度 : n(logn)


> 堆積排序法主要是使用到堆積二元樹為基礎架構，以進行排序的方式<br>


主要可以分為最大堆積樹還有最小堆積樹 :

---

>> 最大堆積樹需滿足以下三個條件 : <br>
> - 是一個完整的二元樹<br>
> - 所有節點的值都大於或等於其左右子節點的值<br>
> - 樹根是堆積樹中最大的

---

>> 最小堆積樹則是需滿足以下三個條件 :<br>
> - 是一個完整的二元樹<br>
> - 所有的節點都小於或等於其左右子傑 (與最大堆積樹相反)<br>
> - 樹根是堆積樹中最小的(與最大堆積樹相反) <br>


---

#### 實現過程：

---

排序的過程則是先建成堆積樹之後，每一次都取出最上面的根結點(最大或是最小值，依序實作方式而定)，<br>

秩序破壞掉後，再重新使用函數建立新的堆積樹，一直循環進行取出，重建，依據每次取出的次序依序進行排序，<br>

直到將樹中所有值全部取出時，就能依序由小到大排序或由大到小排序了

---

<strong>Insight</strong>:

雖然抽象概念是如此，<br>
但是在程式語言實作上不能直接取出或刪除根節點，因為那會破壞掉整體堆積樹定義下數值大小的結構 ; <br>

所以實作上根節點(最大或最小)的值會跟index最後一項的葉節點交換，以表示排序完成，將樹的整體大小減1，<br>
並在下一次的重建迭代過程中省略 ;<br>

可以這麼做的原因是因為在完全樹當中，樹最後一個的子節點不可能同時還是父節點，<br>
所以即使修剪掉也不會破壞整體堆積樹的定義結構 <p> 

---


#### Reference 參考

> [Sorting Algorithm](https://www.hackerearth.com/zh/practice/algorithms/sorting/merge-sort/tutorial/) <br>

> [Merge sorting](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html) <br>

> [Infinite Loop](http://program-lover.blogspot.com/2008/10/mergesort.html) <br>

> [<strong>Algorithmic Analysis</strong>](https://hashanp.xyz/algorithms.html) <br>

> [Data science - James Le](https://medium.com/cracking-the-data-science-interview/heap-sort-merge-sort-and-convex-hull-4cd108ae3ed4)<<br>
