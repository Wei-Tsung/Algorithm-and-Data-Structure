
## What is Quick Sorting Algorithm ?


<img src='https://github.com/Wei-Tsung/Core-Concepts-Visualization/blob/master/quicksort_imperative-1.jpg' width='600' height='800'>




## Introduction 概要 :

快速排序法 : 是目前普遍被認為最快的排序演算法，與 merge sorting 一樣，都採用 divide & conquer (切割成較小單位分而治之)的策略。
不過在切割時不同的是，merge sort 每次切割都只是剖半，而 quick sort 則與該次切割時所選的 pivot 有關

Quick sort 的切割方式為，每次從數列中選出一個元素作為 pivot點 ， 並將剩餘的元素分為兩堆 ， 一半是小於 pivot 的元素，另一半是大於 pivot 的元素，至於相等的依據程式設計的不同可以歸類在任一邊  ， 但是盡可能地標準一致。

Quick sort 切割後通常會有兩半大小不同的情況(經常兩半部大小差距極大  依據基準點的篩選不同而定)

Quick sort 切割後，pivot 並不會向下傳遞，而是將此pivot value擺放到Array中間的位置，因此每次遞迴的總元素數量都會減1。

切割的停止時機設定為，已沒有元素可進行切割(也就是Array的長度 < 2的時候)


## 具有四種類型的基準點

- 以資料結構當中第一個 element 為基準點 (通常使用)
- 以最後一個 element 為基準點
- 以中位數為基準點
- 隨機基準點 
> 隨機化 :
一旦 pivot 選的不好，很有可能造成 quick sort 出現 O(n2) 的時間複雜度。
在一般的做法上，我們可能會每次都固定取數列中的某一個位置的值，例如：中間、最前面、最後面等等。
這樣的話，quick sort 固定基準點方式就比較有可能隨著資料本身序列大小的不同，而出現可能會讓 quick sort 跑特別慢的資料。

所以當我們採用隨機化的策略來選擇 pivot 的話，那麼 quick sort 受到資料本身的影響也會較小，但仍有可能會出現 O(n2) 的情況。







## Time Complexity 時間複雜度
- 最佳時為 O(nlog2n)

- 最差為 O(n^2)




## English / Chinese Reference  


- [Quick Sorting Algorithm](http://typeocaml.com/2015/01/02/immutable/)

- [時間複雜度](https://blog.kuoe0.tw/posts/2013/03/15/sort-about-quick-sort/)
## 圖片參照
