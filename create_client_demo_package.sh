#!/bin/bash

echo "📦 创建客户端演示包..."
echo "=============================================="

# 创建演示包目录
mkdir -p websocket_bypass_demo_package
cd websocket_bypass_demo_package

# 复制演示文件
cp ../websocket_bypass_demo.py .
cp ../simple_websocket_demo.py .
cp ../CLIENT_DEMO_README.md .

# 创建启动脚本
cat > run_demo.sh << 'EOL'
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
EOL

chmod +x run_demo.sh

# 创建 Windows 批处理文件
cat > run_demo.bat << 'EOL'
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
EOL

# 创建演示说明
cat > DEMO_INSTRUCTIONS.md << 'EOL'
# WebSocket 绕过漏洞演示包

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

- `websocket_bypass_demo.py` - 完整版演示工具
- `simple_websocket_demo.py` - 简化版演示工具
- `run_demo.sh` - Linux/Mac 启动脚本
- `run_demo.bat` - Windows 启动脚本
- `CLIENT_DEMO_README.md` - 详细说明文档

## ⚠️ 使用前准备

1. 确保已安装 Python 3.6+
2. 确保网络连接正常
3. 确保有权限访问目标系统

## 📞 技术支持

如有问题，请联系乙方专业安全团队。

---
**演示包版本**: 1.0  
**创建日期**: 2025-01-23
EOL

# 创建压缩包
cd ..
tar -czf websocket_bypass_demo_package.tar.gz websocket_bypass_demo_package/

echo "✅ 客户端演示包创建完成!"
echo "📁 演示包位置: websocket_bypass_demo_package/"
echo "📦 压缩包位置: websocket_bypass_demo_package.tar.gz"
echo ""
echo "🚀 使用方法:"
echo "1. 解压演示包: tar -xzf websocket_bypass_demo_package.tar.gz"
echo "2. 进入目录: cd websocket_bypass_demo_package"
echo "3. 运行演示: ./run_demo.sh (Linux/Mac) 或 run_demo.bat (Windows)"
