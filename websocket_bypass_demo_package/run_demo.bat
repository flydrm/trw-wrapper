@echo off
echo 🔓 WebSocket 绕过漏洞演示工具
echo ==============================================
echo 请选择演示模式:
echo 1. 完整版演示 (详细分析)
echo 2. 简化版演示 (快速演示)
echo 3. 退出
echo ==============================================
set /p choice=请输入选择 (1-3): 

if "%choice%"=="1" (
    echo 运行完整版演示...
    python websocket_bypass_demo.py
) else if "%choice%"=="2" (
    echo 运行简化版演示...
    python simple_websocket_demo.py
) else if "%choice%"=="3" (
    echo 退出演示
    exit /b 0
) else (
    echo 无效选择，退出演示
    exit /b 1
)
