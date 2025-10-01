# ⚡ 自動更新功能說明

## 🎯 更新內容

Flask 應用程式已升級為**自動更新模式**，現在就像 Streamlit 版本一樣，調整參數後會自動重新生成數據和圖表，**不需要再按「Generate & Visualize」按鈕**！

---

## ✨ 新功能特點

### 1. **實時自動更新**

-   移動任何滑桿（n_points, coefficient_a, noise_variance）
-   修改 Random Seed 數值
-   **自動觸發數據生成和視覺化更新**

### 2. **智能防抖動 (Debounce)**

-   滑桿調整時延遲 **500ms** 才觸發更新
-   避免在快速移動滑桿時產生過多請求
-   優化性能和用戶體驗

### 3. **視覺提示**

-   新增藍色提示框顯示「⚡ Auto-update enabled」
-   按鈕已隱藏（但保留在程式碼中以備需要）
-   Loading 動畫在更新時顯示

---

## 🎨 介面變化

### 修改前：

```
┌────────────────────────────┐
│  參數控制                   │
│  [滑桿]                     │
│  [滑桿]                     │
│  [滑桿]                     │
│  [輸入框]                   │
│  [🔄 Generate & Visualize] │ ← 需要按這個按鈕
└────────────────────────────┘
```

### 修改後：

```
┌────────────────────────────┐
│  參數控制                   │
│  [滑桿] ← 移動就自動更新     │
│  [滑桿] ← 移動就自動更新     │
│  [滑桿] ← 移動就自動更新     │
│  [輸入框] ← 改變就自動更新   │
│  ┌──────────────────────┐  │
│  │ ⚡ Auto-update enabled│  │
│  └──────────────────────┘  │
└────────────────────────────┘
```

---

## 🔧 技術實現細節

### JavaScript Debounce 函數

```javascript
let debounceTimer;
function debounce(func, delay) {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(func, delay);
}
```

### 事件監聽器更新

-   **滑桿 (input 事件)**：500ms debounce
-   **Random Seed (change 事件)**：立即更新

### CSS 調整

-   按鈕設為 `display: none`（隱藏但保留）
-   新增 `.auto-update-info` 樣式類別

---

## 🚀 使用方式

### 啟動應用

```bash
cd "/Users/chenzhixuan/Public/碩一上/物聯網/HW1"
python3 flask_app.py
```

### 訪問網頁

```
http://localhost:3000
或
http://127.0.0.1:3000
```

### 操作方式

1. **移動滑桿** → 停止移動後 0.5 秒自動更新
2. **修改 Random Seed** → 離開輸入框後立即更新
3. **觀察 Loading 動畫** → 顯示更新進度
4. **查看結果** → 自動顯示新的圖表和數據

---

## 📊 更新流程圖

```
使用者操作
    │
    ├─ 移動滑桿
    │     │
    │     ├─ 更新顯示值
    │     └─ 觸發 debounce (500ms)
    │           │
    │           └─ 呼叫 generateData()
    │
    └─ 修改 Random Seed
          │
          └─ 立即呼叫 generateData()
                │
                ▼
          顯示 Loading 動畫
                │
                ▼
          發送 POST /generate 請求
                │
                ▼
          接收 JSON 回應
                │
                ├─ updatePlot()
                ├─ updateCoefficients()
                └─ updateOutliersTable()
                │
                ▼
          隱藏 Loading 動畫
                │
                ▼
          顯示更新結果
```

---

## ⚙️ 自訂設定

### 調整 Debounce 延遲時間

在 `templates/index.html` 中修改延遲時間（單位：毫秒）：

```javascript
// 目前設定：500ms
debounce(generateData, 500);

// 更快速回應（300ms）
debounce(generateData, 300);

// 更慢回應（1000ms = 1秒）
debounce(generateData, 1000);
```

### 重新啟用按鈕

如果想保留手動按鈕，修改 CSS：

```css
.generate-btn {
    display: block; /* 改為 block 顯示按鈕 */
}
```

---

## 🆚 Streamlit vs Flask 比較

| 特性     | Streamlit | Flask (更新後)  |
| -------- | --------- | --------------- |
| 自動更新 | ✅ 內建   | ✅ 已實現       |
| 即時回應 | ✅ 超快   | ✅ 快速 (500ms) |
| UI 自訂  | ⭐⭐⭐    | ⭐⭐⭐⭐⭐      |
| 部署彈性 | ⭐⭐⭐    | ⭐⭐⭐⭐⭐      |
| 學習曲線 | 簡單      | 中等            |
| 使用體驗 | 流暢      | 流暢            |

---

## 💡 使用建議

### 適合 Streamlit 的情境：

-   快速原型開發
-   數據科學展示
-   內部工具

### 適合 Flask 的情境：

-   需要完全自訂 UI
-   整合到現有網站
-   需要 RESTful API
-   生產環境部署

**現在兩者都提供相同的自動更新體驗！** 🎉

---

## 🐛 疑難排解

### 問題：滑桿移動後沒有更新

**解決方案**：

-   檢查瀏覽器開發者工具 (F12) Console 是否有錯誤
-   確認 Flask 後端正在運行
-   清除瀏覽器快取重新載入 (Ctrl+Shift+R / Cmd+Shift+R)

### 問題：更新太頻繁或太慢

**解決方案**：

-   調整 debounce 延遲時間（見上方「自訂設定」）

### 問題：網頁顯示錯誤

**解決方案**：

-   檢查 Flask 終端機輸出的錯誤訊息
-   確認端口 3000 或 5000 沒有被其他程式佔用

---

## 📝 技術筆記

### 修改的文件：

-   `templates/index.html` （主要修改）

### 新增的 CSS 類別：

-   `.auto-update-info` - 藍色提示框樣式

### 修改的 JavaScript：

-   新增 `debounce()` 函數
-   更新所有 input 事件監聽器
-   新增 change 事件監聽器

### 保留的功能：

-   按鈕功能（隱藏但可用）
-   原有 API 端點不變
-   所有原始功能完整保留

---

## 🎊 總結

✅ **自動更新功能已成功實現**  
✅ **使用體驗大幅提升**  
✅ **與 Streamlit 版本功能對等**  
✅ **防抖動機制避免過度請求**  
✅ **視覺提示清楚明確**

現在 Flask 版本提供與 Streamlit 相同的流暢體驗，同時保留完整的 UI 自訂能力！

---

**更新日期**：2025 年 10 月 1 日  
**版本**：2.0 (Auto-Update)  
**狀態**：✅ 已完成並測試
