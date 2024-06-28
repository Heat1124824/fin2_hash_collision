class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class HashTable:
    def __init__(self):
        self.data=[None]*50
        
    def insert(self, key):
        # 使用雜湊函式 hash() 取址(使用摺疊法)
        # 若此地址沒有資料(=None)，則在該地址建立一個 Node 物件並設定 key
        # 若此地址有資料，則處理碰撞(使用鏈結法)
        addr = self.hash(key)
        if not self.data[addr]:
            self.data[addr] = Node(key)
        else:
            self.collision(addr, key)

#========================題目=========================
    def hash(self, key):
        return sum([int(n) for n in str(key)])

    def collision(self, addr, key):
        cur = self.data[addr]
        while cur.next:
            cur = cur.next
        cur.next = Node(key)

    def search(self, key):
        addr = self.hash(key)
        cur = self.data[addr]
        while cur:
            if cur.val == key:
                return addr
            cur = cur.next
        return None
#========================================================

def traversal(cur):
        while cur:
            print(cur.val, end = " -> ")
            cur = cur.next
        print(None)

def main():
    ht = HashTable()
    # keys = [9, 42, 12, 48, 123, 345, 999, 1000, 66]
    keys = [69, 78, 4, 22, 24, 544, 85, 1, 75]
    for key in keys:
        ht.insert(key)
    print("======== 搜尋所有插入的 key ========")
    #search_keys = [12, 23, 45, 123, 42, 35, 48, 66, 345, 999, 1000]
    search_keys = [22, 4, 544, 86, 69, 1, 544, 92, 78]
    for key in search_keys:
        print(f"key : {key:<4} -> addr : {ht.search(key)}")
    print("==== 確認相同地址的 key 是否鏈結成功 ====")
    # print("addr = 6 , keys =", end = " ")
    # traversal(ht.data[6])
    # print("addr = 12 , keys =", end = " ")
    # traversal(ht.data[12])
    print("addr = 4 , keys =", end = " ")
    traversal(ht.data[4])
    print("addr = 13 , keys =", end = " ")
    traversal(ht.data[13])
    print("addr = 15 , keys =", end = " ")
    traversal(ht.data[15])
    


if __name__ == "__main__":
    main()