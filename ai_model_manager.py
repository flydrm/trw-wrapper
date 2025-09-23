#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🤖 AI模型管理器 - 统一管理所有AI模型

功能:
   - 统一管理所有支持的AI模型
   - 提供模型配置和端点信息
   - 模型可用性检查
   - 绕过方法管理
   - 性能监控集成

📋 管理范围:
   - GPT系列模型
   - Claude系列模型
   - Gemini系列模型
   - Llama/Mistral系列
   - 自定义模型支持
"""

import json
import time
import requests
from datetime import datetime
from typing import Dict, List, Optional, Any

class AIModelManager:
    """AI模型管理器"""

    def __init__(self):
        self.supported_models = {
            'gpt_series': {
                'name': 'GPT系列',
                'provider': 'OpenAI',
                'models': {
                    'gpt-3.5-turbo': {
                        'name': 'GPT-3.5 Turbo',
                        'context_length': 16385,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.0015,
                        'cost_per_1k_output': 0.002,
                        'endpoints': ['/v1/chat/completions', '/api/chat', '/api/v1/chat/completions'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection', 'parameter_pollution'],
                        'risk_level': 'high'
                    },
                    'gpt-3.5-turbo-16k': {
                        'name': 'GPT-3.5 Turbo 16K',
                        'context_length': 16385,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.003,
                        'cost_per_1k_output': 0.004,
                        'endpoints': ['/v1/chat/completions', '/api/chat'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection'],
                        'risk_level': 'high'
                    },
                    'gpt-4': {
                        'name': 'GPT-4',
                        'context_length': 8192,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.03,
                        'cost_per_1k_output': 0.06,
                        'endpoints': ['/v1/chat/completions', '/api/chat'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection'],
                        'risk_level': 'critical'
                    },
                    'gpt-4-turbo': {
                        'name': 'GPT-4 Turbo',
                        'context_length': 128000,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.01,
                        'cost_per_1k_output': 0.03,
                        'endpoints': ['/v1/chat/completions', '/api/chat', '/api/v1/chat/completions'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection', 'parameter_pollution'],
                        'risk_level': 'critical'
                    },
                    'gpt-4-turbo-preview': {
                        'name': 'GPT-4 Turbo Preview',
                        'context_length': 128000,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.01,
                        'cost_per_1k_output': 0.03,
                        'endpoints': ['/v1/chat/completions', '/api/chat'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection'],
                        'risk_level': 'high'
                    },
                    'gpt-4-0125-preview': {
                        'name': 'GPT-4-0125 Preview',
                        'context_length': 128000,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.01,
                        'cost_per_1k_output': 0.03,
                        'endpoints': ['/v1/chat/completions', '/api/chat'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection'],
                        'risk_level': 'high'
                    },
                    'gpt-4-1106-preview': {
                        'name': 'GPT-4-1106 Preview',
                        'context_length': 128000,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.01,
                        'cost_per_1k_output': 0.03,
                        'endpoints': ['/v1/chat/completions', '/api/chat'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection'],
                        'risk_level': 'high'
                    }
                }
            },
            'claude_series': {
                'name': 'Claude系列',
                'provider': 'Anthropic',
                'models': {
                    'claude-3-opus-20240229': {
                        'name': 'Claude 3 Opus',
                        'context_length': 200000,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.015,
                        'cost_per_1k_output': 0.075,
                        'endpoints': ['/v1/chat/completions', '/api/messages', '/api/v1/messages'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection'],
                        'risk_level': 'critical'
                    },
                    'claude-3-sonnet-20240229': {
                        'name': 'Claude 3 Sonnet',
                        'context_length': 200000,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.003,
                        'cost_per_1k_output': 0.015,
                        'endpoints': ['/v1/chat/completions', '/api/messages', '/api/v1/messages'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection'],
                        'risk_level': 'high'
                    },
                    'claude-3-haiku-20240307': {
                        'name': 'Claude 3 Haiku',
                        'context_length': 200000,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.00025,
                        'cost_per_1k_output': 0.00125,
                        'endpoints': ['/v1/chat/completions', '/api/messages', '/api/v1/messages'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection'],
                        'risk_level': 'medium'
                    },
                    'claude-2.1': {
                        'name': 'Claude 2.1',
                        'context_length': 200000,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.008,
                        'cost_per_1k_output': 0.024,
                        'endpoints': ['/v1/chat/completions', '/api/messages'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection'],
                        'risk_level': 'high'
                    },
                    'claude-2.0': {
                        'name': 'Claude 2.0',
                        'context_length': 100000,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.008,
                        'cost_per_1k_output': 0.024,
                        'endpoints': ['/v1/chat/completions', '/api/messages'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection'],
                        'risk_level': 'medium'
                    },
                    'claude-instant-1.2': {
                        'name': 'Claude Instant 1.2',
                        'context_length': 100000,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.0008,
                        'cost_per_1k_output': 0.0024,
                        'endpoints': ['/v1/chat/completions', '/api/messages'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection'],
                        'risk_level': 'low'
                    }
                }
            },
            'gemini_series': {
                'name': 'Gemini系列',
                'provider': 'Google',
                'models': {
                    'gemini-pro': {
                        'name': 'Gemini Pro',
                        'context_length': 30720,
                        'max_tokens': 8192,
                        'cost_per_1k_input': 0.00025,
                        'cost_per_1k_output': 0.0005,
                        'endpoints': ['/v1/chat/completions', '/api/generate', '/api/v1/generate'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection', 'parameter_pollution'],
                        'risk_level': 'high'
                    },
                    'gemini-pro-vision': {
                        'name': 'Gemini Pro Vision',
                        'context_length': 16384,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.00025,
                        'cost_per_1k_output': 0.0005,
                        'endpoints': ['/v1/chat/completions', '/api/generate', '/api/v1/generate'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection', 'parameter_pollution'],
                        'risk_level': 'high'
                    },
                    'gemini-1.5-pro': {
                        'name': 'Gemini 1.5 Pro',
                        'context_length': 2097152,
                        'max_tokens': 8192,
                        'cost_per_1k_input': 0.00125,
                        'cost_per_1k_output': 0.005,
                        'endpoints': ['/v1/chat/completions', '/api/generate', '/api/v1/generate'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection', 'parameter_pollution'],
                        'risk_level': 'critical'
                    },
                    'gemini-1.5-flash': {
                        'name': 'Gemini 1.5 Flash',
                        'context_length': 1048576,
                        'max_tokens': 8192,
                        'cost_per_1k_input': 0.000075,
                        'cost_per_1k_output': 0.0003,
                        'endpoints': ['/v1/chat/completions', '/api/generate', '/api/v1/generate'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection', 'parameter_pollution'],
                        'risk_level': 'medium'
                    },
                    'gemini-1.0-pro': {
                        'name': 'Gemini 1.0 Pro',
                        'context_length': 30720,
                        'max_tokens': 8192,
                        'cost_per_1k_input': 0.0005,
                        'cost_per_1k_output': 0.0015,
                        'endpoints': ['/v1/chat/completions', '/api/generate', '/api/v1/generate'],
                        'bypass_methods': ['token_reuse', 'api_direct_access', 'header_injection', 'parameter_pollution'],
                        'risk_level': 'medium'
                    }
                }
            },
            'other_models': {
                'name': '其他模型',
                'provider': 'Various',
                'models': {
                    'llama-2-70b-chat': {
                        'name': 'Llama 2 70B Chat',
                        'context_length': 4096,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.0007,
                        'cost_per_1k_output': 0.0008,
                        'endpoints': ['/v1/chat/completions', '/api/chat', '/api/v1/chat/completions', '/api/generate'],
                        'bypass_methods': ['token_reuse', 'api_direct_access'],
                        'risk_level': 'medium'
                    },
                    'llama-2-13b-chat': {
                        'name': 'Llama 2 13B Chat',
                        'context_length': 4096,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.0001,
                        'cost_per_1k_output': 0.0001,
                        'endpoints': ['/v1/chat/completions', '/api/chat', '/api/v1/chat/completions', '/api/generate'],
                        'bypass_methods': ['token_reuse', 'api_direct_access'],
                        'risk_level': 'low'
                    },
                    'llama-2-7b-chat': {
                        'name': 'Llama 2 7B Chat',
                        'context_length': 4096,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.00005,
                        'cost_per_1k_output': 0.00005,
                        'endpoints': ['/v1/chat/completions', '/api/chat', '/api/v1/chat/completions', '/api/generate'],
                        'bypass_methods': ['token_reuse', 'api_direct_access'],
                        'risk_level': 'low'
                    },
                    'codellama-34b-instruct': {
                        'name': 'CodeLlama 34B Instruct',
                        'context_length': 16384,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.0008,
                        'cost_per_1k_output': 0.0008,
                        'endpoints': ['/v1/chat/completions', '/api/chat', '/api/v1/chat/completions'],
                        'bypass_methods': ['token_reuse', 'api_direct_access'],
                        'risk_level': 'medium'
                    },
                    'codellama-13b-instruct': {
                        'name': 'CodeLlama 13B Instruct',
                        'context_length': 16384,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.00015,
                        'cost_per_1k_output': 0.00015,
                        'endpoints': ['/v1/chat/completions', '/api/chat', '/api/v1/chat/completions'],
                        'bypass_methods': ['token_reuse', 'api_direct_access'],
                        'risk_level': 'low'
                    },
                    'codellama-7b-instruct': {
                        'name': 'CodeLlama 7B Instruct',
                        'context_length': 16384,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.0001,
                        'cost_per_1k_output': 0.0001,
                        'endpoints': ['/v1/chat/completions', '/api/chat', '/api/v1/chat/completions'],
                        'bypass_methods': ['token_reuse', 'api_direct_access'],
                        'risk_level': 'low'
                    },
                    'mistral-7b-instruct': {
                        'name': 'Mistral 7B Instruct',
                        'context_length': 32768,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.0001,
                        'cost_per_1k_output': 0.0001,
                        'endpoints': ['/v1/chat/completions', '/api/chat', '/api/v1/chat/completions'],
                        'bypass_methods': ['token_reuse', 'api_direct_access'],
                        'risk_level': 'medium'
                    },
                    'mistral-8x7b-instruct': {
                        'name': 'Mistral 8x7B Instruct',
                        'context_length': 32768,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.0002,
                        'cost_per_1k_output': 0.0002,
                        'endpoints': ['/v1/chat/completions', '/api/chat', '/api/v1/chat/completions'],
                        'bypass_methods': ['token_reuse', 'api_direct_access'],
                        'risk_level': 'medium'
                    },
                    'mixtral-8x7b-instruct': {
                        'name': 'Mixtral 8x7B Instruct',
                        'context_length': 32768,
                        'max_tokens': 4096,
                        'cost_per_1k_input': 0.0002,
                        'cost_per_1k_output': 0.0002,
                        'endpoints': ['/v1/chat/completions', '/api/chat', '/api/v1/chat/completions'],
                        'bypass_methods': ['token_reuse', 'api_direct_access'],
                        'risk_level': 'medium'
                    }
                }
            }
        }

        self.test_results = {}
        self.base_url = 'https://iwoozie.baby'

    def get_all_models(self) -> List[str]:
        """获取所有模型列表"""
        all_models = []
        for series in self.supported_models.values():
            all_models.extend(series['models'].keys())
        return all_models

    def get_model_info(self, model_name: str) -> Optional[Dict]:
        """获取模型信息"""
        for series in self.supported_models.values():
            if model_name in series['models']:
                return series['models'][model_name]
        return None

    def get_models_by_series(self, series_name: str) -> List[str]:
        """按系列获取模型列表"""
        if series_name in self.supported_models:
            return list(self.supported_models[series_name]['models'].keys())
        return []

    def get_bypass_methods(self, model_name: str) -> List[str]:
        """获取模型的绕过方法"""
        model_info = self.get_model_info(model_name)
        if model_info:
            return model_info.get('bypass_methods', [])
        return []

    def test_model_access(self, model_name: str, endpoint: str = None) -> bool:
        """测试模型访问"""
        model_info = self.get_model_info(model_name)
        if not model_info:
            return False

        if not endpoint:
            endpoint = model_info['endpoints'][0]

        try:
            url = f"{self.base_url}{endpoint}"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer cf-turnstile-response-token'
            }
            payload = {
                'model': model_name,
                'messages': [{'role': 'user', 'content': 'Hello'}],
                'max_tokens': 10
            }

            response = requests.post(url, headers=headers, json=payload, timeout=10)

            if response.status_code == 200:
                return True
            return False

        except Exception as e:
            return False

    def calculate_risk_score(self, model_name: str) -> Dict:
        """计算模型风险评分"""
        model_info = self.get_model_info(model_name)
        if not model_info:
            return {'risk_level': 'unknown', 'risk_score': 0}

        risk_levels = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4}
        risk_score = risk_levels.get(model_info.get('risk_level', 'low'), 1)

        # 根据绕过方法数量调整风险
        bypass_count = len(model_info.get('bypass_methods', []))
        risk_score += min(bypass_count * 0.5, 2)

        # 根据成本调整风险
        input_cost = model_info.get('cost_per_1k_input', 0)
        if input_cost > 0.01:
            risk_score += 1
        elif input_cost > 0.001:
            risk_score += 0.5

        return {
            'risk_level': model_info.get('risk_level', 'low'),
            'risk_score': min(risk_score, 5),
            'bypass_methods_count': bypass_count,
            'cost_per_1k_input': input_cost
        }

    def get_models_by_risk_level(self, risk_level: str) -> List[str]:
        """按风险等级获取模型"""
        models = []
        for series in self.supported_models.values():
            for model_name, model_info in series['models'].items():
                if model_info.get('risk_level') == risk_level:
                    models.append(model_name)
        return models

    def generate_model_report(self) -> Dict:
        """生成模型报告"""
        report = {
            'total_models': len(self.get_all_models()),
            'series_count': len(self.supported_models),
            'risk_summary': {},
            'cost_analysis': {},
            'test_results': self.test_results
        }

        # 风险汇总
        for risk_level in ['low', 'medium', 'high', 'critical']:
            models = self.get_models_by_risk_level(risk_level)
            report['risk_summary'][risk_level] = len(models)

        # 成本分析
        total_cost_per_1k = 0
        model_count = 0

        for series in self.supported_models.values():
            for model_name, model_info in series['models'].items():
                cost = model_info.get('cost_per_1k_input', 0) + model_info.get('cost_per_1k_output', 0)
                total_cost_per_1k += cost
                model_count += 1

        report['cost_analysis'] = {
            'average_cost_per_1k': total_cost_per_1k / model_count if model_count > 0 else 0,
            'total_models': model_count
        }

        return report

    def test_all_models(self) -> Dict:
        """测试所有模型"""
        print('🤖 测试所有AI模型...')
        print('=' * 50)

        total_models = len(self.get_all_models())
        tested_models = 0
        successful_tests = 0

        for series_name, series_info in self.supported_models.items():
            print(f'\\n🎯 测试 {series_info["name"]} ({len(series_info["models"])} 个模型)')

            for model_name, model_info in series_info['models'].items():
                tested_models += 1
                print(f'   🤖 {model_name}: 测试中...')

                # 测试模型访问
                test_success = False
                for endpoint in model_info['endpoints']:
                    if self.test_model_access(model_name, endpoint):
                        test_success = True
                        break

                if test_success:
                    successful_tests += 1
                    print(f'      ✅ 访问成功')
                else:
                    print(f'      ❌ 访问失败')

                # 记录测试结果
                self.test_results[model_name] = {
                    'series': series_name,
                    'provider': series_info['provider'],
                    'access_test': test_success,
                    'risk_info': self.calculate_risk_score(model_name)
                }

        print(f'\\n📊 测试完成: {successful_tests}/{tested_models} 成功')

        return self.generate_model_report()

def main():
    """主函数"""
    manager = AIModelManager()

    try:
        # 测试所有模型
        report = manager.test_all_models()

        print('\\n📋 模型管理器测试完成!')
        print('=' * 50)

        print(f'\\n📊 模型统计:')
        print(f'   总模型数: {report["total_models"]}')
        print(f'   系列数量: {report["series_count"]}')

        print(f'\\n⚠️ 风险分布:')
        for risk_level, count in report['risk_summary'].items():
            print(f'   {risk_level.upper()}: {count} 个模型')

        print(f'\\n💰 成本分析:')
        print(f'   平均每1K成本: ${report["cost_analysis"]["average_cost_per_1k"]:.4f}')

        print(f'\\n📈 测试结果:')
        successful_tests = sum(1 for result in manager.test_results.values() if result['access_test'])
        total_tests = len(manager.test_results)
        print(f'   成功测试: {successful_tests}/{total_tests}')

        print('\\n🎯 所有模型已测试完成!')

    except Exception as e:
        print(f'❌ 测试过程中发生错误: {e}')

if __name__ == '__main__':
    print('🤖 AI模型管理器启动...')
    print('📋 管理所有支持的AI模型')

    main()

    print('\\n🛡️ 管理器运行完成!')
    print('   • 所有模型已管理')
    print('   • 风险已评估')
    print('   • 报告已生成')
    print('   • 成本已分析')