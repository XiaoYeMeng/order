try:                      # 使用 try，測試內容是否正確
    a = input('輸入數字：')
    print(a + 1)
except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
    print('發生錯誤')
print('hello')
