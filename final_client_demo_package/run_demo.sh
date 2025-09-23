#!/bin/bash
echo "🔓 综合安全漏洞演示工具"
echo "=============================================="
echo "请选择演示模式:"
echo "1. WebSocket 绕过演示"
echo "2. 漏洞分析演示"
echo "3. 实际漏洞利用演示"
echo "4. 完整综合演示"
echo "5. 退出"
echo "=============================================="
read -p "请输入选择 (1-5): " choice

case $choice in
    1)
        echo "运行 WebSocket 绕过演示..."
        python3 simple_websocket_demo.py
        ;;
    2)
        echo "运行漏洞分析演示..."
        python3 pure_python_vulnerability_analysis.py
        ;;
    3)
        echo "运行实际漏洞利用演示..."
        python3 real_vulnerability_exploit.py
        ;;
    4)
        echo "运行完整综合演示..."
        echo "1. 漏洞分析..."
        python3 pure_python_vulnerability_analysis.py
        echo ""
        echo "2. WebSocket 绕过..."
        python3 simple_websocket_demo.py
        echo ""
        echo "3. 实际漏洞利用..."
        python3 real_vulnerability_exploit.py
        ;;
    5)
        echo "退出演示"
        exit 0
        ;;
    *)
        echo "无效选择，退出演示"
        exit 1
        ;;
esac
