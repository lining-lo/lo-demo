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
:: 获取 年-月-日 格式日期作为提交备注
for /f "tokens=2 delims==" %%a in ('wmic os get localdatetime /value') do set "datetime=%%a"
set "today=!datetime:~0,4!-!datetime:~4,2!-!datetime:~6,2!"
echo [2/3] ✍️ 执行本地提交，提交信息：!today!
git commit -m "!today!"
if !errorlevel! equ 0 (
    echo ✅ 本地提交成功！
) else (
    echo.
    echo ⚠️  当前无文件改动，跳过提交步骤
)

echo.
set "branch=master"
echo [3/3] 🚀 推送代码到远程GitHub分支：!branch!
git push origin !branch!
if !errorlevel! equ 0 (
    echo ✅ 代码推送远程仓库成功！
) else (
    echo.
    echo ❌ 推送失败！检查网络、账号权限或分支冲突
    pause
    exit /b 1
)

echo.
echo ==============================================
echo 🎉 全部Git操作执行完毕，按任意键关闭窗口
echo ==============================================
echo.

pause