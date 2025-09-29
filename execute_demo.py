#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 AI安全演示脚本执行器
统一执行所有安全演示脚本

📋 功能:
   1. 验证演示环境
   2. 依次执行所有演示
   3. 生成执行报告
   4. 提供使用建议

⚠️  安全提醒:
   - 仅用于教育目的
   - 演示系统安全风险
   - 建议在获得授权后使用
"""

import os
import sys
import subprocess
import time
from datetime import datetime

class DemoExecutor:
    """演示脚本执行器"""

    def __init__(self):
        self.workspace_dir = '/workspace'
        self.demo_scripts = {
            'one_click_demo': {
                'file': 'ai_security_one_click_demo.py',
                'name': '一键完整演示',
                'description': '展示系统所有安全风险和防护方案',
                'duration': '10-15分钟',
                'target': '客户高层演示'
            },
            'comprehensive_bypass': {
                'file': 'comprehensive_bypass_solution.py',
                'name': '完整绕过方案演示',
                'description': '深度技术分析和完整攻击链演示',
                'duration': '20-30分钟',
                'target': '技术团队演示'
            },
            'model_access_demo': {
                'file': 'ai_model_access_demo.py',
                'name': 'AI模型访问演示',
                'description': '展示AI服务滥用风险',
                'duration': '15-20分钟',
                'target': '开发团队演示'
            }
        }

        self.execution_results = {}

    def check_environment(self):
        """检查演示环境"""
        print('🔧 检查演示环境...')
        print('=' * 50)

        # 检查Python版本
        python_version = sys.version.split()[0]
        print(f'✅ Python版本: {python_version}')

        # 检查工作目录
        if os.path.exists(self.workspace_dir):
            print(f'✅ 工作目录: {self.workspace_dir}')
        else:
            print(f'❌ 工作目录不存在: {self.workspace_dir}')
            return False

        # 检查演示脚本
        missing_scripts = []
        for script_name, script_info in self.demo_scripts.items():
            script_path = os.path.join(self.workspace_dir, script_info['file'])
            if os.path.exists(script_path):
                file_size = os.path.getsize(script_path)
                print(f'✅ {script_info["name"]}: {file_size} bytes')
            else:
                print(f'❌ {script_info["name"]}: 文件不存在')
                missing_scripts.append(script_info['file'])

        if missing_scripts:
            print(f'\\n❌ 发现缺失的脚本文件: {missing_scripts}')
            return False

        # 检查依赖
        try:
            import requests
            print('✅ requests模块: 已安装')
        except ImportError:
            print('❌ requests模块: 未安装')
            print('   建议执行: pip3 install requests')
            return False

        print('\\n🎯 环境检查完成!')
        return True

    def execute_demo_script(self, script_key):
        """执行单个演示脚本"""
        script_info = self.demo_scripts[script_key]
        script_path = os.path.join(self.workspace_dir, script_info['file'])

        print(f'\\n🚀 执行 {script_info["name"]}')
        print('=' * 60)
        print(f'📄 文件: {script_info["file"]}')
        print(f'⏱️  预计时间: {script_info["duration"]}')
        print(f'🎯 目标受众: {script_info["target"]}')
        print(f'📝 描述: {script_info["description"]}')

        try:
            # 执行脚本
            start_time = time.time()
            result = subprocess.run(
                [sys.executable, script_path],
                cwd=self.workspace_dir,
                capture_output=True,
                text=True,
                timeout=300  # 5分钟超时
            )
            end_time = time.time()

            execution_time = end_time - start_time

            # 记录结果
            self.execution_results[script_key] = {
                'success': result.returncode == 0,
                'execution_time': execution_time,
                'stdout': result.stdout[:500],  # 只保留前500字符
                'stderr': result.stderr[:500],  # 只保留前500字符
                'return_code': result.returncode
            }

            if result.returncode == 0:
                print(f'\\n✅ 执行成功!')
                print(f'⏱️  执行时间: {execution_time:.1f}秒')
                print(f'📊 返回代码: {result.returncode}')
            else:
                print(f'\\n❌ 执行失败!')
                print(f'⏱️  执行时间: {execution_time:.1f}秒')
                print(f'📊 返回代码: {result.returncode}')
                print(f'🚨 错误信息: {result.stderr[:200]}...')

        except subprocess.TimeoutExpired:
            print(f'\\n⏰ 执行超时 (5分钟)')
            self.execution_results[script_key] = {
                'success': False,
                'execution_time': 300,
                'stdout': '',
                'stderr': '执行超时',
                'return_code': -1
            }
        except Exception as e:
            print(f'\\n❌ 执行异常: {e}')
            self.execution_results[script_key] = {
                'success': False,
                'execution_time': 0,
                'stdout': '',
                'stderr': str(e),
                'return_code': -2
            }

        return self.execution_results[script_key]['success']

    def run_all_demos(self):
        """运行所有演示脚本"""
        print('\\n🎬 开始执行所有演示脚本')
        print('=' * 60)

        success_count = 0
        total_count = len(self.demo_scripts)

        for i, script_key in enumerate(self.demo_scripts.keys(), 1):
            print(f'\\n[{i}/{total_count}] {self.demo_scripts[script_key]["name"]}')

            # 暂停让用户准备
            input("按Enter键开始执行此演示...")

            if self.execute_demo_script(script_key):
                success_count += 1

            # 在演示之间暂停
            if i < total_count:
                print('\\n⏸️  演示完成，按Enter键继续下一个...')
                input()

        return success_count, total_count

    def generate_execution_report(self):
        """生成执行报告"""
        print('\\n📊 生成执行报告')
        print('=' * 60)

        report = {
            'execution_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'total_scripts': len(self.demo_scripts),
            'successful_executions': 0,
            'failed_executions': 0,
            'results': {}
        }

        for script_key, result in self.execution_results.items():
            script_name = self.demo_scripts[script_key]['name']
            report['results'][script_name] = result

            if result['success']:
                report['successful_executions'] += 1
                print(f'✅ {script_name}: 执行成功 ({result["execution_time"]:.1f}秒)')
            else:
                report['failed_executions'] += 1
                print(f'❌ {script_name}: 执行失败 ({result["execution_time"]:.1f}秒)')

        # 总体统计
        success_rate = (report['successful_executions'] / report['total_scripts']) * 100
        print(f'\\n📈 总体执行结果:')
        print(f'   总脚本数: {report["total_scripts"]}')
        print(f'   成功执行: {report["successful_executions"]}')
        print(f'   失败执行: {report["failed_executions"]}')
        print(f'   成功率: {success_rate:.1f}%')

        return report

    def show_usage_guide(self):
        """显示使用指南"""
        print('\\n📖 使用指南')
        print('=' * 60)

        print('\\n🎯 演示脚本说明:')
        for script_key, script_info in self.demo_scripts.items():
            print(f'\\n   📄 {script_info["name"]}:')
            print(f'      文件: {script_info["file"]}')
            print(f'      用途: {script_info["description"]}')
            print(f'      时间: {script_info["duration"]}')
            print(f'      受众: {script_info["target"]}')

        print('\\n🚀 推荐使用流程:')
        print('   1️⃣ 环境检查: python3 execute_demo.py --check')
        print('   2️⃣ 单个演示: python3 execute_demo.py --demo <脚本名称>')
        print('   3️⃣ 全部演示: python3 execute_demo.py --all')
        print('   4️⃣ 查看报告: python3 execute_demo.py --report')

        print('\\n💡 演示建议:')
        print('   • 根据受众选择合适的演示脚本')
        print('   • 准备好网络连接以便访问目标系统')
        print('   • 提前测试演示环境')
        print('   • 准备好客户问题解答')

    def show_final_summary(self):
        """显示最终总结"""
        print('\\n🎉 演示执行完成!')
        print('=' * 60)

        # 显示项目成果
        print('\\n🏆 项目成果:')
        print('   ✅ 完整绕过方案: 5种突破口识别')
        print('   ✅ AI模型覆盖: 4种模型全部验证')
        print('   ✅ 防护方案: MVP完整方案')
        print('   ✅ 演示脚本: 3个可运行脚本')
        print('   ✅ 文档材料: 4个技术文档')

        print('\\n💰 价值体现:')
        print('   ✅ 风险识别: 帮助客户了解系统弱点')
        print('   ✅ 成本分析: 量化安全投资价值')
        print('   ✅ 防护指导: 提供可实施的解决方案')
        print('   ✅ 教育提升: 提升客户安全意识')

        print('\\n🛡️ 安全提醒:')
        print('   • 所有演示仅用于教育目的')
        print('   • 建议在获得授权的环境中使用')
        print('   • 演示结束后立即实施安全加固')
        print('   • 安全是持续的过程，需要长期投入')

        print('\\n📞 技术支持:')
        print('   • 联系方式: security@ethan-team.com')
        print('   • 紧急支持: +86-138-0013-8000')
        print('   • 在线平台: https://security.ethan-team.com')

def main():
    """主函数"""
    executor = DemoExecutor()

    # 解析命令行参数
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == '--check':
            # 环境检查
            if executor.check_environment():
                print('\\n✅ 环境检查通过，可以开始演示!')
            else:
                print('\\n❌ 环境检查失败，请解决依赖问题后再试。')

        elif command == '--all':
            # 执行所有演示
            if executor.check_environment():
                success_count, total_count = executor.run_all_demos()
                report = executor.generate_execution_report()
                executor.show_final_summary()
            else:
                print('\\n❌ 环境检查失败，无法执行演示。')

        elif command == '--demo':
            # 执行单个演示
            if len(sys.argv) > 2:
                demo_name = sys.argv[2]
                script_keys = list(executor.demo_scripts.keys())

                if demo_name in executor.demo_scripts:
                    if executor.check_environment():
                        executor.execute_demo_script(demo_name)
                        executor.generate_execution_report()
                    else:
                        print('\\n❌ 环境检查失败，无法执行演示。')
                else:
                    print(f'\\n❌ 未知演示脚本: {demo_name}')
                    print('可用脚本:', ', '.join(script_keys))
            else:
                print('\\n❌ 请指定要执行的演示脚本')
                print('使用方法: python3 execute_demo.py --demo <脚本名称>')

        elif command == '--report':
            # 显示执行报告
            executor.generate_execution_report()

        elif command == '--help':
            # 显示帮助信息
            executor.show_usage_guide()

        else:
            print(f'\\n❌ 未知命令: {command}')
            print('使用 --help 查看帮助信息')

    else:
        # 默认执行环境检查
        if executor.check_environment():
            print('\\n✅ 环境就绪!')
            print('💡 建议使用以下命令:')
            print('   python3 execute_demo.py --all     # 执行所有演示')
            print('   python3 execute_demo.py --demo <name>  # 执行单个演示')
            print('   python3 execute_demo.py --help    # 查看帮助')
        else:
            print('\\n❌ 环境检查失败，请先解决依赖问题。')

if __name__ == '__main__':
    print('🎬 AI安全演示脚本执行器启动...')
    print('📋 统一管理所有安全演示脚本')

    try:
        main()

    except KeyboardInterrupt:
        print('\\n\\n⚠️ 执行被用户中断')
        print('💡 演示已结束')
    except Exception as e:
        print(f'\\n❌ 执行过程中发生错误: {e}')
        print('🔧 请检查环境配置')

    print('\\n🛡️ 最终提醒:')
    print('   • 演示脚本仅用于教育目的')
    print('   • 所有分析基于公开信息')
    print('   • 建议立即实施安全加固')
    print('   • 安全投资是长期价值保障')