@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo ==============================================
echo          📚 代码一键Git提交推送工具
echo ==============================================
echo.
echo [1/3] 📥 正在添加全部变更文件到暂存区...
git add .
if !errorlevel! equ 0 (
    echo ✅ 文件添加完成！
) else (
    echo.
    echo ❌ Git add 添加文件失败！
    pause
    exit /b 1
)
echo.

:: 使用PowerShell获取标准日期，彻底解决wmic隐藏换行bug
for /f "delims=" %%a in ('powershell "(Get-Date).ToString('yyyy-MM-dd')"') do set today=%%a
echo [2/3] ✍️ 正在提交代码（信息：!today! 代码更新）...
git commit -m "!today! 代码更新"
if !errorlevel! equ 0 (
    echo ✅ 本地提交成功！
) else (
    echo.
    echo ⚠️  无文件修改，无需提交
)
echo.

set "branch=master"
echo [3/3] 🚀 正在推送到 GitHub（分支：!branch!）...
git push origin !branch!
if !errorlevel! equ 0 (
    echo ✅ 推送成功！
) else (
    echo.
    echo ❌ 推送失败！请检查网络/分支/登录状态
    pause
    exit /b 1
)
echo.
echo ==============================================
echo 🎉 全部操作完成！请按任意键关闭窗口~
echo ==============================================
echo.
pause
