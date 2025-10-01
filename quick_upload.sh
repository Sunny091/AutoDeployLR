#!/bin/bash
# 快速 GitHub 上傳腳本
# 使用方法: chmod +x quick_upload.sh && ./quick_upload.sh

echo "🚀 Linear Regression Visualizer - GitHub 上傳腳本"
echo ""

# 設定變數（請修改這些值）
GITHUB_USERNAME="yourusername"
REPO_NAME="linear-regression-visualizer"

echo "📋 步驟 1: 初始化 Git repository..."
git init

echo ""
echo "📋 步驟 2: 設定 Git 使用者資訊..."
echo "請輸入你的 Git 使用者名稱："
read git_name
git config user.name "$git_name"

echo "請輸入你的 Git email："
read git_email
git config user.email "$git_email"

echo ""
echo "📋 步驟 3: 添加所有檔案..."
git add .

echo ""
echo "📋 步驟 4: 查看將要提交的檔案..."
git status

echo ""
read -p "確認要提交這些檔案嗎？(y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "❌ 取消上傳"
    exit 1
fi

echo ""
echo "📋 步驟 5: 提交到本地 repository..."
git commit -m "Initial commit: Linear Regression Visualizer with CRISP-DM

- Implement complete CRISP-DM methodology
- Add Streamlit and Flask web interfaces  
- Include auto-update feature
- Add comprehensive documentation
- Include unit tests and visualization"

echo ""
echo "📋 步驟 6: 連接遠端 repository..."
echo "請確保你已在 GitHub 上創建了 repository: $REPO_NAME"
read -p "已創建？繼續？(y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "⏸️  請先前往 https://github.com/new 創建 repository"
    echo "Repository 名稱: $REPO_NAME"
    exit 1
fi

git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

echo ""
echo "📋 步驟 7: 推送到 GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ 完成！"
echo ""
echo "🌐 你的 repository URL:"
echo "https://github.com/$GITHUB_USERNAME/$REPO_NAME"
echo ""
echo "📝 接下來的步驟："
echo "1. 前往 GitHub repository"
echo "2. 添加 Topics（標籤）"
echo "3. 設定 About 描述"
echo "4. 檢查 README.md 顯示"
echo ""
echo "🎉 恭喜！專案已成功上傳到 GitHub！"
