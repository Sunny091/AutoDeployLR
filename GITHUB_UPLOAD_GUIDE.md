# 🚀 GitHub 上傳指南

這個指南將幫助你把專案上傳到 GitHub。

## 📋 前置檢查清單

在上傳之前，確認以下項目：

-   ✅ 所有檔案已整理到正確的資料夾
-   ✅ 文檔完整（README.md, LICENSE, etc.）
-   ✅ .gitignore 已設定
-   ✅ 測試通過（`python3 test_model.py`）
-   ✅ 程式碼已清理（移除不必要的註解）
-   ✅ 敏感資訊已移除（API keys, passwords, etc.）

## 📁 目前的專案結構

```
HW1/
├── 📄 核心程式
│   ├── linear_regression_model.py
│   ├── streamlit_app.py
│   ├── flask_app.py
│   └── templates/
│       └── index.html
│
├── 🧪 測試
│   └── test_model.py
│
├── 📚 文檔
│   ├── README.md
│   ├── LICENSE
│   ├── CONTRIBUTING.md
│   ├── CHANGELOG.md
│   └── docs/
│       ├── CRISP_DM_DOCUMENTATION.md
│       ├── QUICKSTART.md
│       ├── AUTO_UPDATE_FEATURE.md
│       ├── PROJECT_STRUCTURE.md
│       ├── PROJECT_SUMMARY.txt
│       ├── QUICK_REFERENCE.txt
│       └── UPDATE_SUMMARY.txt
│
├── 📦 設定
│   ├── requirements.txt
│   └── .gitignore
│
└── 🖼️ 資源
    └── screenshots/
        └── test_regression_plot.png
```

## 🔧 步驟 1: 初始化 Git（如果還沒有）

```bash
cd "/Users/chenzhixuan/Public/碩一上/物聯網/HW1"

# 初始化 Git repository
git init

# 設定你的身份（第一次使用需要）
git config user.name "你的名字"
git config user.email "your.email@example.com"
```

## 📝 步驟 2: 添加所有檔案

```bash
# 查看會被添加的檔案
git status

# 添加所有檔案
git add .

# 查看將要提交的檔案
git status
```

## 💾 步驟 3: 提交變更

```bash
# 提交到本地 repository
git commit -m "Initial commit: Linear Regression Visualizer with CRISP-DM"

# 或更詳細的提交訊息
git commit -m "feat: Initial release of Linear Regression Visualizer

- Implement CRISP-DM methodology
- Add Streamlit and Flask web interfaces
- Include auto-update feature
- Add comprehensive documentation
- Include unit tests"
```

## 🌐 步驟 4: 在 GitHub 上創建 Repository

### 方法 A: 使用 GitHub 網站

1. 前往 https://github.com
2. 點擊右上角的 **+** → **New repository**
3. 填寫資訊：
    - **Repository name**: `linear-regression-visualizer`
    - **Description**: `Interactive Linear Regression tool with CRISP-DM methodology`
    - **Public** 或 **Private**（根據需求選擇）
    - ⚠️ **不要**勾選 "Add a README file"（我們已經有了）
    - ⚠️ **不要**勾選 "Add .gitignore"（我們已經有了）
    - ⚠️ **不要**選擇 "Choose a license"（我們已經有了）
4. 點擊 **Create repository**

### 方法 B: 使用 GitHub CLI（如果已安裝）

```bash
# 創建並連接 repository
gh repo create linear-regression-visualizer --public --source=. --remote=origin
```

## 🔗 步驟 5: 連接本地和遠端 Repository

```bash
# 添加遠端 repository（替換 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/linear-regression-visualizer.git

# 確認遠端設定
git remote -v
```

## 📤 步驟 6: 推送到 GitHub

```bash
# 推送到 GitHub（第一次需要 -u 參數）
git push -u origin main

# 如果分支名稱是 master，使用：
# git push -u origin master
```

### 如果遇到分支名稱問題

```bash
# 確認當前分支名稱
git branch

# 如果是 master，重命名為 main
git branch -M main

# 然後再推送
git push -u origin main
```

## 🔐 步驟 7: 設定 GitHub 認證

### 如果需要輸入帳號密碼：

1. **使用 Personal Access Token（推薦）**

    - 前往 GitHub → Settings → Developer settings → Personal access tokens
    - Generate new token (classic)
    - 選擇 scopes: `repo` (完整控制)
    - 複製 token（只會顯示一次！）
    - 使用 token 作為密碼

2. **使用 SSH（進階）**

    ```bash
    # 生成 SSH key
    ssh-keygen -t ed25519 -C "your.email@example.com"

    # 添加到 ssh-agent
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519

    # 複製公鑰並添加到 GitHub
    cat ~/.ssh/id_ed25519.pub
    ```

## ✅ 步驟 8: 驗證上傳

1. 前往你的 GitHub repository 頁面
2. 確認所有檔案都已上傳
3. 檢查 README.md 是否正確顯示
4. 測試文檔連結是否正常

## 🎨 步驟 9: 美化你的 Repository

### 添加 Topics（標籤）

在 GitHub repository 頁面：

1. 點擊右側的齒輪圖示（About）
2. 添加 topics：
    - `python`
    - `machine-learning`
    - `linear-regression`
    - `data-science`
    - `streamlit`
    - `flask`
    - `crisp-dm`
    - `visualization`
    - `interactive`
    - `education`

### 添加描述

在 About 區域添加：

```
Interactive Linear Regression visualizer with CRISP-DM methodology.
Built with Python, Streamlit, Flask, and scikit-learn.
```

### 設定主頁顯示

在 Settings：

-   ✅ 選擇 "Use your GitHub profile README"
-   ✅ 啟用 "Releases"
-   ✅ 啟用 "Packages"

## 📸 步驟 10: 添加更多截圖（可選）

```bash
# 在 screenshots/ 資料夾添加更多圖片
# 例如：streamlit_interface.png, flask_interface.png

# 提交並推送
git add screenshots/
git commit -m "docs: Add interface screenshots"
git push
```

## 🏷️ 步驟 11: 創建 Release（可選）

```bash
# 創建 tag
git tag -a v2.0.0 -m "Version 2.0.0 - Auto-update feature"

# 推送 tag
git push origin v2.0.0
```

然後在 GitHub：

1. 前往 Releases
2. 點擊 "Create a new release"
3. 選擇 tag: v2.0.0
4. 填寫 Release notes（可以從 CHANGELOG.md 複製）
5. 點擊 "Publish release"

## 🔄 未來的更新流程

```bash
# 1. 修改檔案

# 2. 查看變更
git status
git diff

# 3. 添加變更
git add .

# 4. 提交
git commit -m "描述你的變更"

# 5. 推送到 GitHub
git push
```

## 🆘 常見問題

### Q: 推送時被拒絕 (rejected)

```bash
# 先拉取遠端變更
git pull origin main --rebase

# 然後再推送
git push
```

### Q: 忘記添加 .gitignore

```bash
# 移除已追蹤的檔案
git rm -r --cached __pycache__/
git rm --cached .DS_Store

# 提交變更
git commit -m "chore: Update .gitignore"
git push
```

### Q: 想要修改最後一次 commit 訊息

```bash
# 修改最後一次 commit
git commit --amend -m "新的提交訊息"

# 強制推送（小心使用！）
git push --force
```

### Q: 不小心提交了敏感資訊

```bash
# 從歷史記錄中移除檔案
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch 敏感檔案" \
  --prune-empty --tag-name-filter cat -- --all

# 強制推送
git push --force --all
```

## 📋 推送後的檢查清單

-   ✅ README.md 在 GitHub 上顯示正常
-   ✅ 圖片正確顯示
-   ✅ 文檔連結都能正常開啟
-   ✅ LICENSE 檔案存在
-   ✅ .gitignore 正確運作（敏感檔案未上傳）
-   ✅ Repository 描述和 topics 已設定
-   ✅ 所有檔案都已正確上傳

## 🎉 完成！

你的專案現在已經在 GitHub 上了！

### 下一步：

1. **分享你的專案**

    - 複製 repository URL
    - 分享給老師或同學
    - 添加到你的履歷或作品集

2. **維護你的專案**

    - 回應 issues
    - 審查 pull requests
    - 持續更新文檔

3. **推廣你的專案**
    - 在 LinkedIn 分享
    - 寫部落格文章
    - 提交到 awesome lists

## 📞 需要幫助？

-   GitHub 文檔: https://docs.github.com
-   Git 教學: https://git-scm.com/doc
-   GitHub CLI: https://cli.github.com/

---

**祝你上傳順利！** 🚀✨
