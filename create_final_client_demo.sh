#!/bin/bash

echo "📦 创建最终客户端演示包..."
echo "=============================================="

# 创建演示包目录
mkdir -p final_client_demo_package
cd final_client_demo_package

# 复制所有演示文件
cp ../websocket_bypass_demo.py .
cp ../simple_websocket_demo.py .
cp ../pure_python_vulnerability_analysis.py .
cp ../real_vulnerability_exploit.py .
cp ../CLIENT_DEMO_README.md .

# 创建启动脚本
cat > run_demo.sh << 'EOL'
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
EOL

chmod +x run_demo.sh

# 创建 Windows 批处理文件
cat > run_demo.bat << 'EOL'
@echo off
echo 🔓 综合安全漏洞演示工具
echo ==============================================
echo 请选择演示模式:
echo 1. WebSocket 绕过演示
echo 2. 漏洞分析演示
echo 3. 实际漏洞利用演示
echo 4. 完整综合演示
echo 5. 退出
echo ==============================================
set /p choice=请输入选择 (1-5): 

if "%choice%"=="1" (
    echo 运行 WebSocket 绕过演示...
    python websocket_bypass_demo.py
) else if "%choice%"=="2" (
    echo 运行漏洞分析演示...
    python pure_python_vulnerability_analysis.py
) else if "%choice%"=="3" (
    echo 运行实际漏洞利用演示...
    python real_vulnerability_exploit.py
) else if "%choice%"=="4" (
    echo 运行完整综合演示...
    echo 1. 漏洞分析...
    python pure_python_vulnerability_analysis.py
    echo.
    echo 2. WebSocket 绕过...
    python simple_websocket_demo.py
    echo.
    echo 3. 实际漏洞利用...
    python real_vulnerability_exploit.py
) else if "%choice%"=="5" (
    echo 退出演示
    exit /b 0
) else (
    echo 无效选择，退出演示
    exit /b 1
)
EOL

# 创建演示说明
cat > FINAL_DEMO_INSTRUCTIONS.md << 'EOL'
# 综合安全漏洞演示包

## 🎯 快速开始

### Linux/Mac 用户
```bash
chmod +x run_demo.sh
./run_demo.sh
```

### Windows 用户
```cmd
run_demo.bat
```

## 📁 文件说明

- `websocket_bypass_demo.py` - WebSocket 绕过演示工具
- `simple_websocket_demo.py` - 简化版 WebSocket 演示工具
- `pure_python_vulnerability_analysis.py` - 漏洞分析工具
- `real_vulnerability_exploit.py` - 实际漏洞利用工具
- `run_demo.sh` - Linux/Mac 启动脚本
- `run_demo.bat` - Windows 启动脚本
- `CLIENT_DEMO_README.md` - 详细说明文档

## 🔍 演示内容

### 1. WebSocket 绕过演示
- 测试 10 种 WebSocket 协议
- 实时连接测试
- 消息发送测试
- 详细结果分析

### 2. 漏洞分析演示
- 分析发现的 5 个关键漏洞
- 测试漏洞利用可行性
- 生成渗透方案
- 提供修复建议

### 3. 实际漏洞利用演示
- 基于真实发现的漏洞
- 使用实际的 Token 和 Cookie
- 测试各种绕过方法
- 生成详细报告

### 4. 完整综合演示
- 依次运行所有演示
- 提供全面的安全评估
- 生成综合报告

## ⚠️ 使用前准备

1. 确保已安装 Python 3.6+
2. 确保网络连接正常
3. 确保有权限测试目标系统

## 📞 技术支持

如有问题，请联系乙方专业安全团队。

---
**演示包版本**: 2.0  
**创建日期**: 2025-01-23
EOL

# 创建压缩包
cd ..
tar -czf final_client_demo_package.tar.gz final_client_demo_package/

echo "✅ 最终客户端演示包创建完成!"
echo "�� 演示包位置: final_client_demo_package/"
echo "📦 压缩包位置: final_client_demo_package.tar.gz"
echo ""
echo "🚀 使用方法:"
echo "1. 解压演示包: tar -xzf final_client_demo_package.tar.gz"
echo "2. 进入目录: cd final_client_demo_package"
echo "3. 运行演示: ./run_demo.sh (Linux/Mac) 或 run_demo.bat (Windows)"
echo ""
echo "🎯 演示特点:"
echo "- 基于真实发现的漏洞"
echo "- 使用实际的 Token 和 Cookie"
echo "- 提供多种演示模式"
echo "- 生成详细的分析报告"
