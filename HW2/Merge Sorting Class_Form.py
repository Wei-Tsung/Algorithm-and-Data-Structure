
# coding: utf-8

# In[3]:


class Solution(object):

    def merge_sort(self,arr):
    
    
        length = len(arr)
        
        if length > 1:
            midpoint = int(length/2)
            left = arr[:midpoint]
            right = arr[midpoint:]
        
            Solution().merge_sort(left) # 左右再一直不斷地遞迴切割 直到length = 1
            Solution().merge_sort(right) #
        

        #arr是已經遞迴切割到最底層的arr子集合 , 跟原始引入的arr母集合並不相同
    
        if length <= 1:  # 設定中止條件  若array <= 1 不必執行其他過程直接回傳
            return arr
   
  
        n1 = 0 # left_section array的index
        n2 = 0 # right_section array 的index
        sort = 0 # 重新排序放入array時的index
        over = 0 # 表示左半邊或右半邊的array已經有一邊已經全數比較並排序完的信號
    
        #把所有的element依據大小排進array
        while ( n1 < len(left) ) | (n2 < len(right) ):
        
        
            if over == 1 : # 信號表示其中一邊的array已經重新排序完成
                if n2 == len(right):
               
                    arr[sort:] = left[n1:] 
                    n1 = len(left)
                else :
                 
                    arr[sort:] = right[n2:]
                    n2 = len(right)
        
            if over == 0 : # 左右半邊的array都尚未重新排序
                if  left[n1] <= right[n2] :
                    arr[sort] = left[n1]
                    n1 += 1
                 
                elif left[n1] > right[n2]:
                    arr[sort] = right[n2]
                    n2 += 1
                
                if (len(left) == n1) | (len(right) == n2) :
                    over = 1
            
                sort += 1
    
        return print('Merging Processes : ' , arr) #將排序過程輸出　,  debug會比較清楚容易   


# In[4]:


original_arr = [11,2,5,4,7,6,8,1,23] # original_array 當引入 merge sort 
# 在每一次遞迴當中arr所表示的array皆不是相同的  而是original array的子集合

Solution().merge_sort(original_arr)


# In[ ]:


#https://stackoverflow.com/questions/18761766/mergesort-with-python 

#曾參考過StackFlow討論版  但僅止於了解Merge Sort背後的原理 
#實際程式碼撰寫內容為原創  與原參考來源的相似度極低 , 幾乎等於0

#參考書 蔡明志 : 資料結構 : 使用Python : Sorting原理說明

  

