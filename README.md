# 期末考第二題 雜湊表的碰撞處理
本題提供兩個類別，Node和HashTable類別。
Node類別是用來建立單向鏈結串列的節點類別。
HashTable物件有個使用insert方法，它可以插入一連串整數資料，另外HashTable內的data預設為長度50的None陣列(型態 list)，此變數是用來儲存所有輸入資料(key)，data內每個元素皆為Node物件，可視為單向鏈結串列的head。
請完成HashTable類別的三個方法:
Q1. hash方法(7%)
hash方法有個參數為key，代表要插入的資料，請用摺疊法方式生成雜湊，摺疊的規則是將輸入資料以1為長度分割，再將分割後的資料相加。
例如：
key = 3 -> 位址 = 3
key = 87 -> 位址 = 15 (8+7)
key = 123 -> 位址 = 6 (1+2+3)
提示: 可以使用字串分割法求出位址。
此方法需要回傳轉換後的位址數值。

Q2. collision方法(10%)
hash方法有兩個參數，一個是addr，為發生碰撞的位址，另一個是key，代表要插入的資料。
我們要使用鏈結法處理碰撞，也就是利用key建立新的Node物件，把該 addr存放的Node當成單向鏈結串列的head，並把新的Node存放在這個單向鏈結串列的尾端。
此方法不需要回傳值，它能直接改變self.data的內容。

Q3. search方法(8%)
方法有個參數為key，代表要插入的資料，請使用走訪單向鏈結串列的方式搜尋資料。
若該key存在於此雜湊表中，則要回傳地址，若不存在則直接回傳None。
