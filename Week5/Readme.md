
## What is Quick Sorting Algorithm ?


<img src='https://github.com/Wei-Tsung/Core-Concepts-Visualization/blob/master/quicksort_imperative-1.jpg' width='600' height='800'>




## Introduction 概要 :

快速排序法 : 是目前普遍被認為最快的排序演算法，與 merge sorting 一樣，都採用 divide & conquer (切割成較小單位分而治之)的策略。
不過在切割時不同的是，merge sort 每次切割都只是剖半，而 quick sort 則與該次切割時所選的 pivot 有關

Quick sort 的切割方式為，每次從數列中選出一個元素作為 pivot點 ， 並將剩餘的元素分為兩堆 ， 一半是小於 pivot 的元素，另一半是大於 pivot 的元素，至於相等的依據程式設計的不同可以歸類在任一邊  ， 但是盡可能地標準一致。

quick sort 切割後通常會有兩半大小不同的情況(經常兩半部大小差距極大  依據基準點的篩選不同而定)

此外，quick sort 切割後，pivot 並不會傳遞下去，而是將此pivot value 擺放到Array的中間
因此每次遞回的總元素數量都會減1。

切割的停止時機設定為，已沒有元素可進行切割(也就是Array的長度 < 2的時候)


## 具有四種類型的基準點

- 以資料結構當中第一個 element 為基準點 (最常使用)
- 以最後一個 element 為基準點
- 以中位數為基準點
- 隨機基準點 








## Time Complexity 時間複雜度





## English Reference  


[Quick Sorting Algorithm](http://typeocaml.com/2015/01/02/immutable/)

## 圖片參照
