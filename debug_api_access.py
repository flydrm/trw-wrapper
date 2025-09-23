#!/usr/bin/env python3
"""
调试 API 访问测试
================
检查是否真的可以直接访问 chat API
"""

import urllib.request
import urllib.parse
import urllib.error
import json
import time
from datetime import datetime

class DebugAPIAccess:
    def __init__(self):
        self.base_url = "https://iwoozie.baby"
        self.api_endpoint = "/api/quick/createAITask"
    
    def print_header(self):
        print("=" * 80)
        print("🔍 调试 API 访问测试")
        print("=" * 80)
        print("🎯 目标: 验证是否可以直接访问 chat API")
        print("⏰ 时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("=" * 80)
        print()
    
    def test_basic_api_access(self):
        """测试基本 API 访问"""
        print("🔍 测试基本 API 访问...")
        
        # 使用最简单的请求
        url = f"{self.base_url}{self.api_endpoint}?model=GPT-5&stream=true"
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        data = {
            "Content": [
                {"role": "user", "content": "Hello"}
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
                print(f"   响应内容: {content[:500]}...")
                
                if status_code == 200:
                    print("   ✅ 基本 API 访问成功!")
                    return True
                else:
                    print("   ❌ 基本 API 访问失败")
                    return False
                    
        except Exception as e:
            print(f"   💥 基本 API 访问异常: {str(e)}")
            return False
    
    def test_with_real_headers(self):
        """使用真实请求头测试"""
        print("🔍 使用真实请求头测试...")
        
        url = f"{self.base_url}{self.api_endpoint}?model=GPT-5&stream=true"
        
        # 使用您提供的真实请求头
        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Origin": "https://iwoozie.baby",
            "Referer": "https://iwoozie.baby/chat?RG_Token=e84e184e-c04e-4a55-9c2d-08cb40951852",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Priority": "u=1, i",
            "Cookie": "session=.eJwFwUtygjAAANC7sGUBtQRCZ7pAtAgKBpTvxkkiX4O0QBDo9O5971eo465bbybLcY-fNL9thA9hme644dz3Ijvu5pcEdAkk30aKCl45nKlb-aCj-r1vNSnS_bE7Xq2sIka8JpFmVsR5g-Wy-rGDe42glp9RdpmoOnKsFAds7l2fyqUWQjeG1LZ8xQUjgjkYFoZCtpNOOg1GjtSwcGCbsix50oMINlpFrobpIMVOu_kK-32yn-ZCk5c1GjZ856VhKWksu7PGFfPhEZSitTbGl0mHC4qO6jIG6FEkVtXDLTXOo-IOctngwLEzone5CEh6qmebRSUSQfi4x177UurzkXteTqBOfhT7U_j7B-8CZa8.aNIbHQ.WVxrUwkr3kPXmZ4KV0WDp_1hs4c"
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
                print(f"   响应内容: {content[:500]}...")
                
                if status_code == 200:
                    print("   ✅ 真实请求头测试成功!")
                    return True
                else:
                    print("   ❌ 真实请求头测试失败")
                    return False
                    
        except Exception as e:
            print(f"   💥 真实请求头测试异常: {str(e)}")
            return False
    
    def test_different_models(self):
        """测试不同模型"""
        print("🔍 测试不同模型...")
        
        models = ["GPT-4", "GPT-5", "Grok-4-Fast", "Claude-Sonnet-4", "Gemini-2.5-Pro"]
        
        for model in models:
            print(f"   测试模型: {model}")
            
            url = f"{self.base_url}{self.api_endpoint}?model={model}&stream=true"
            
            headers = {
                "Content-Type": "application/json",
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Origin": "https://iwoozie.baby",
                "Referer": "https://iwoozie.baby/chat"
            }
            
            data = {
                "Content": [
                    {"role": "user", "content": f"Hello, test {model}"}
                ]
            }
            
            try:
                json_data = json.dumps(data).encode('utf-8')
                req = urllib.request.Request(url, data=json_data, headers=headers, method='POST')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    status_code = response.getcode()
                    content = response.read().decode('utf-8')
                    
                    print(f"     状态码: {status_code}")
                    print(f"     响应长度: {len(content)}")
                    
                    if status_code == 200:
                        print(f"     ✅ {model} 访问成功!")
                    else:
                        print(f"     ❌ {model} 访问失败")
                        
            except Exception as e:
                print(f"     💥 {model} 访问异常: {str(e)}")
            
            time.sleep(1)  # 避免请求过于频繁
    
    def test_without_stream(self):
        """测试不使用流式响应"""
        print("🔍 测试不使用流式响应...")
        
        url = f"{self.base_url}{self.api_endpoint}?model=GPT-5"
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Origin": "https://iwoozie.baby",
            "Referer": "https://iwoozie.baby/chat"
        }
        
        data = {
            "Content": [
                {"role": "user", "content": "Hello, test without stream"}
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
                print(f"   响应内容: {content[:500]}...")
                
                if status_code == 200:
                    print("   ✅ 非流式响应测试成功!")
                    return True
                else:
                    print("   ❌ 非流式响应测试失败")
                    return False
                    
        except Exception as e:
            print(f"   💥 非流式响应测试异常: {str(e)}")
            return False
    
    def run_debug_test(self):
        """运行调试测试"""
        self.print_header()
        
        print("🚀 开始调试 API 访问测试...")
        print()
        
        # 1. 测试基本 API 访问
        print("=" * 60)
        print("1. 测试基本 API 访问")
        print("=" * 60)
        basic_success = self.test_basic_api_access()
        print()
        
        # 2. 使用真实请求头测试
        print("=" * 60)
        print("2. 使用真实请求头测试")
        print("=" * 60)
        real_headers_success = self.test_with_real_headers()
        print()
        
        # 3. 测试不同模型
        print("=" * 60)
        print("3. 测试不同模型")
        print("=" * 60)
        self.test_different_models()
        print()
        
        # 4. 测试不使用流式响应
        print("=" * 60)
        print("4. 测试不使用流式响应")
        print("=" * 60)
        no_stream_success = self.test_without_stream()
        print()
        
        # 生成报告
        self.generate_report(basic_success, real_headers_success, no_stream_success)
    
    def generate_report(self, basic_success, real_headers_success, no_stream_success):
        """生成调试报告"""
        print("=" * 80)
        print("📋 调试 API 访问报告")
        print("=" * 80)
        
        print("🎯 测试结果:")
        print(f"1. 基本 API 访问: {'✅ 成功' if basic_success else '❌ 失败'}")
        print(f"2. 真实请求头测试: {'✅ 成功' if real_headers_success else '❌ 失败'}")
        print(f"3. 非流式响应测试: {'✅ 成功' if no_stream_success else '❌ 失败'}")
        print()
        
        if basic_success or real_headers_success or no_stream_success:
            print("🚨 发现: API 可以直接访问!")
            print("💡 这意味着系统存在严重的安全漏洞")
        else:
            print("✅ 系统防护正常: API 无法直接访问")
            print("💡 需要进一步分析其他攻击向量")
        
        print("\n" + "=" * 80)

def main():
    """主函数"""
    debug = DebugAPIAccess()
    debug.run_debug_test()

if __name__ == "__main__":
    main()
