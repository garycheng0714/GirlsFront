# Girls' Frontline

auto-play script for mobile game Girls' Frontline, is implemented by used AutomatorX (https://github.com/NetEaseGame/AutomatorX)

The introduce for Girls' Frontline
https://acg.gamer.com.tw/acgDetail.php?s=84628


概敘
與一般遊戲一樣, Girls' Frontline(後文簡稱GF)中的角色要透過升等(練等)來提升能力, 而GF的練等方式非常有規律性, 選擇腳色、進入關卡、打怪。
故興起寫自動化腳本取代人力, 一方面節省時間, 另一方面則剛好可練習python。

開發過程
1. Sikuli
遊戲自動化需要做圖像比對, 一開始使用易上手的 Sikuli 搭配 Android emulator。由於Sikuli是直接控制滑鼠做相對應的行為，跑Sikuli script 等於把滑鼠控制權讓給Sikuli，導致PC只能跑script完全不能做其他事。如何在背景裡執行就是下個課題。

2. Selenium
網頁自動化測試工具。稍為研究後發現無法在此應用上。

3. Appium
手機自動化測試工具。可透過python script使手機做相對應的事情，但是無圖像比對功能，且遊戲介面也沒有UIautomator元素可供操作。

4. AutomatorX(ATX)
原本打算研究opencv, 但有幸在網路上看到AutomatorX, 省下研究opencv的時間。AutomatorX 確實符合了我的需求，圖像比對、自動化且可以直接在手機上跑而非局限於模擬器。

使用ATX後順利地自動化人工部分，但因為點擊坐標都是定點會被判定為外掛，故稍微修改ATX 的 source code讓坐標能在有效範圍內變動
