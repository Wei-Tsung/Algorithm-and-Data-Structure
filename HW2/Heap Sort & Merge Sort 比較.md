> 此圖原創作者，來自參考連結一



### Merge Sorting　合併排序法 :

Merge Sorting 是分治(Divide and Conquer)演算法的一種，與Quick Sort一樣，<br>一定會有切割到最小單位並進行處理的過程(Atomize)<br>

如圖一所示，演算法會把原始的數據Array切割成單位為1的最小單位，然後兩兩排序過後合併起來，一步一步重新再構築成經過排序過的原始的大小，<br>


與Qucik sort不一樣的地方在，Merge Sort 無論如何總是頃向對稱的方式切割(若奇數個有其中一邊會多一個)，Quick Sort則是會以某個位置的值為基準點
視情況而定來切割，也因此左右兩邊大小更常會呈現高度不對稱的情況，也因此效率上Quick Sort更加好一點　<br>





## Reference 參考
> [Merge sorting](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)

> [Infinite Loop](http://program-lover.blogspot.com/2008/10/mergesort.html)

> [<strong>Algorithmic Analysis</strong>](https://hashanp.xyz/algorithms.html)
