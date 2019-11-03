
# coding: utf-8

# In[65]:


class Solution(object):  # 依據課堂的規定 , 格式後來才補上的  
    
    def heap(self,data) :   
        
        data = [0] + data
          
        size = len(data)
        print('原始陣列 :' , data[1:] , end = '')
        #先進行堆積還沒有排序

        for i in range(int(size/2) , 0 , -1):
            Solution().add_heap(data , i , size-1) #引入的時候size的意義會變成index 所以要-1 因為data[size] = None
        
        print()
        print("堆積內容 :", data[1:] , '\n')
    
        # 開始堆積排序 樹建立起來 每次都取最上面的值->最小值 然後再重新建立新的樹
    
        ###本來想直接把第一個直取出 讓剩下的tree重新排列  但是直接取掉第一個根部會破壞掉整個樹的結構
        for n in range(size-2,0,-1): # -2是為了讓data[n+1]的index不超出範圍
            data[n+1] , data[1] = data[1] , data[n+1] # 不知道這算不算是正規的作法
        
            Solution().add_heap(data,1,n) # n就是每次遞減1的size  
        
        return print('排序結果: ' , data[-1:0:-1] , end= '' )
    
    def add_heap(self, data , i , size): #Tree由下而上堆積　Mini-heap 
        j = 2 * i
        temp = data[i] # 暫時紀錄index i的樹根為temp　
        tag = 0
    
        while (j <= size) and (tag == 0): #只要tag沒有完成　就再繼續往下比較&交換
            if j < size: # 這裡容易出差錯　:　必須要多寫一個if 以免j+1的index out of range　
                if data[j] > data[j+1] :#比較左右子節點的大小
                    j += 1
            if temp <= data[j]:   #父節點一律使用temp比較
                tag = 1 #tag這一層完成排序
        
            elif temp > data[j]:
                data[j//2] = data[j]
                j = j * 2
                #這部分是最難的注意
        
    
        data[j//2] = temp #這個位置要再重新理解一遍  最後確定位置之後再放進來

    
    
  


# In[69]:


data = [-3,-4,5,6,4,8,3,2,7,1,13,5,6,50,1,2,3,1,101] # 測試值 加入一些負值


# In[67]:


Solution().heap(data)


# In[ ]:


#參考資料 1.圖說演算法 , 博碩出版 2.資料結構使用python 蔡明志

#閱讀資料僅止於了解Sorting本身的原理為何 , 實際的程式碼內容撰寫為原創
#可以參考原書籍 兩者的相似度極低 

