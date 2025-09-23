#!/bin/bash
echo "🔓 WebSocket 绕过漏洞演示工具"
echo "=============================================="
echo "请选择演示模式:"
echo "1. 完整版演示 (详细分析)"
echo "2. 简化版演示 (快速演示)"
echo "3. 退出"
echo "=============================================="
read -p "请输入选择 (1-3): " choice

case $choice in
    1)
        echo "运行完整版演示..."
        python3 websocket_bypass_demo.py
        ;;
    2)
        echo "运行简化版演示..."
        python3 simple_websocket_demo.py
        ;;
    3)
        echo "退出演示"
        exit 0
        ;;
    *)
        echo "无效选择，退出演示"
        exit 1
        ;;
esac
