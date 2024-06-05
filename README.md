樹莓派通常運行基於 Linux 的作業系統
因多數程式有使用到LCD面板 所以需要打開虛擬機
切記 請先開啟手機網路並讓樹梅派以及欲使用遠端的電腦連上同一個手機網路
此流程不包含燒錄樹梅派系統

操作流程如下

1.將樹梅派插上電源

2.打開cmd輸入指令$ ping 樹梅派設定的名稱.local -4 查詢並確認手機網路的IP

3.打開putty並輸入剛剛查詢到的手機網路IP

4.輸入樹梅派名稱及密碼即可登入

5.登入後輸入 $ source venv/bin/activate 開啟虛擬機

6.成功開啟虛擬機會在前面顯示(venv)表示成功開啟

7.開啟成功後即可輸入 $ cd .. 以及 $ cd embedded/ 即可找到所有程式位子

8.因為程式皆為python設計，所以可以直接使用python 程式名稱.py執行

