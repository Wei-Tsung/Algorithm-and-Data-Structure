### Merge Sorting 流程圖 : 


<img src='https://github.com/Wei-Tsung/Core-Concepts-Visualization/blob/master/%E6%9C%AA%E5%AE%8C%E6%88%90%E6%B5%81%E7%A8%8B%E5%9C%96%20Diagram%20(5)%20(1).jpg' width=200%>


一開始在看完演算法的抽象概念描述之後

- 第一個想法是想要把Merge-Sorting分成三個部分的函數<br>

- 第一部分的函數是切割用的Partition()，<br>
- 第二個函數部分視合併&排列用的Merge_sort()<br>
- 第三個函數部分當然就是執行用的主程式main()

使用此種寫法是三個函數條理分明，模組化的方式看起來很舒服<br>

而且每個模組在別的程式若有相同的或類似的場景也可以重複使用 ; <br>
不過若區分成幾個不同的函數，很容易在互相引入函數之間參數的時候不小心引入錯誤參數或是回傳錯誤的值<br>

因為區域變數的名字和全域變數的名字取的類似的關係，最後蠻容易搞亂了哪一個變數分別代表著什麼意思；<br>

但是其中最大的問題都不在那裏 ;<p>

而是模組化的方式分成三個函數模組來寫似乎很難有效利用到遞迴關係<br>

Error尤其非常容易出現在從Partitioning要轉換為Merging的轉折點上，<br>
因為從一個Function轉移到另一個Function的過程當中，很多區域變數的資訊常常會在過程當中遺失掉，即使費了一番功夫成果還是很有限；<p>

所以後來在經過深思過後，發覺這種做法似乎並不是很有效的做法，<br>
所以將這部份的工作暫時擱置並且迅速改弦易轍- <p>

---

在第二次重新思考演算法抽象概念的描述中發現：既然Merge Sorting有著連續切割成部分在沿著同樣的線重新還原相同大小的相互繼承性質<br>

有效的使用遞迴關係必然是一條非常簡潔優雅的道路，可以大量減少程式碼繁冗的數量<br>

這種結果當然是再好也不過，debug應該也會比較容易

---

第二次的思考架構 :


- 只寫一個Merge_sort的函數<br>


- 引入的函數若長度大於1時就進行不斷的遞迴right,left對半切割　，　直到right,left長度的size小於等於1時就中止回傳開始進行合併過程


- 從最底層的長度1單位arr開始兩兩排序並合併，因為遞迴關係有線性的連續繼承關係，所以回傳後同樣的過程可以將排序合併，擴及到整個整個arr


- 排序方式為left,right array依大小依序重新排入arr[]，arr以sort為index從0開始，left的index為n1，right的index則設定為n2 


- left,right若有一邊的element已經使用完了，設定信號over=1，直接將另一串剩下的array element直接全數排入，因為這些array剩下的elememt順序從最小1單位開始時早就已經依序排序過，所以已經不必再進行另外的排序了；


- 此過程從最小單位開始一路擴展到最大，合併直到Array的length與原始的Array相同時就回傳


- (新補充)後來依據老師新的規定引入了class 將程式碼重新改寫過

---

參考資料：https://stackoverflow.com/questions/18761766/mergesort-with-python　<br>
思考概念有參考StackFlow的討論，從以下Stackoverflow討論版中，思考並了解Merge_Sort背後的原理
 
<strong>但是除了在一些思考概念上得到啟發之外，實際程式碼的撰寫內容完全原創<br>

若點進去看就會發現實際的程式碼相似度極低，幾乎可以說是等於0</strong>
