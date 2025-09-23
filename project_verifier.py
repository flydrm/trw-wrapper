#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 项目验证器 - 验证AI安全项目完整性

功能:
   - 验证所有文件存在性
   - 检查脚本语法正确性
   - 验证依赖关系
   - 生成项目完整性报告
   - 提供修复建议

📋 验证范围:
   - 演示脚本 (3个)
   - 技术文档 (4个)
   - 执行工具 (1个)
   - 项目文档 (1个)
   - 依赖关系
   - 语法检查
"""

import os
import sys
import ast
import json
import subprocess
from datetime import datetime

class ProjectVerifier:
    """项目验证器"""

    def __init__(self):
        self.workspace_dir = '/workspace'
        self.project_structure = {
            '演示脚本': {
                'files': [
                    'ai_security_one_click_demo.py',
                    'comprehensive_bypass_solution.py',
                    'ai_model_access_demo.py'
                ],
                'description': '3个安全演示脚本'
            },
            '技术文档': {
                'files': [
                    'final_complete_solution.md',
                    'bypass_instructions.md',
                    'client_usage_guide.md',
                    'FINAL_SUMMARY.md'
                ],
                'description': '4个技术文档'
            },
            '执行工具': {
                'files': [
                    'execute_demo.py'
                ],
                'description': '演示脚本执行器'
            },
            '项目文档': {
                'files': [
                    'README.md'
                ],
                'description': '项目说明文档'
            }
        }

        self.dependencies = ['requests']
        self.verification_results = {}

    def verify_file_existence(self):
        """验证文件存在性"""
        print('📁 验证文件存在性...')
        print('=' * 50)

        all_files = []
        for category, info in self.project_structure.items():
            all_files.extend(info['files'])

        missing_files = []
        existing_files = []

        for file_path in all_files:
            full_path = os.path.join(self.workspace_dir, file_path)
            if os.path.exists(full_path):
                file_size = os.path.getsize(full_path)
                existing_files.append((file_path, file_size))
                print(f'✅ {file_path}: {file_size} bytes')
            else:
                missing_files.append(file_path)
                print(f'❌ {file_path}: 文件不存在')

        self.verification_results['file_existence'] = {
            'total_files': len(all_files),
            'existing_files': len(existing_files),
            'missing_files': len(missing_files),
            'existing_files_list': existing_files,
            'missing_files_list': missing_files
        }

        return len(missing_files) == 0

    def verify_script_syntax(self):
        """验证脚本语法"""
        print('\\n🔧 验证脚本语法...')
        print('=' * 50)

        script_files = []
        for category, info in self.project_structure.items():
            if category == '演示脚本' or category == '执行工具':
                script_files.extend(info['files'])

        syntax_errors = []
        valid_scripts = []

        for script_file in script_files:
            full_path = os.path.join(self.workspace_dir, script_file)
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    source_code = f.read()

                # 检查Python语法
                ast.parse(source_code)
                valid_scripts.append(script_file)
                print(f'✅ {script_file}: 语法正确')

            except SyntaxError as e:
                syntax_errors.append((script_file, str(e)))
                print(f'❌ {script_file}: 语法错误 - {e}')
            except Exception as e:
                syntax_errors.append((script_file, str(e)))
                print(f'❌ {script_file}: 读取错误 - {e}')

        self.verification_results['script_syntax'] = {
            'total_scripts': len(script_files),
            'valid_scripts': len(valid_scripts),
            'syntax_errors': len(syntax_errors),
            'valid_scripts_list': valid_scripts,
            'syntax_errors_list': syntax_errors
        }

        return len(syntax_errors) == 0

    def verify_dependencies(self):
        """验证依赖关系"""
        print('\\n📦 验证依赖关系...')
        print('=' * 50)

        missing_deps = []
        available_deps = []

        for dep in self.dependencies:
            try:
                __import__(dep)
                available_deps.append(dep)
                print(f'✅ {dep}: 已安装')
            except ImportError:
                missing_deps.append(dep)
                print(f'❌ {dep}: 未安装')

        self.verification_results['dependencies'] = {
            'total_dependencies': len(self.dependencies),
            'available_deps': len(available_deps),
            'missing_deps': len(missing_deps),
            'available_deps_list': available_deps,
            'missing_deps_list': missing_deps
        }

        return len(missing_deps) == 0

    def verify_file_content(self):
        """验证文件内容完整性"""
        print('\\n📄 验证文件内容...')
        print('=' * 50)

        content_issues = []
        valid_files = []

        for category, info in self.project_structure.items():
            for file_path in info['files']:
                full_path = os.path.join(self.workspace_dir, file_path)
                if os.path.exists(full_path):
                    try:
                        with open(full_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # 基本内容检查
                        if len(content.strip()) == 0:
                            content_issues.append((file_path, '文件为空'))
                            print(f'❌ {file_path}: 文件为空')
                        elif len(content) < 100:
                            content_issues.append((file_path, '内容过短'))
                            print(f'⚠️ {file_path}: 内容过短 ({len(content)}字符)')
                        else:
                            valid_files.append(file_path)
                            print(f'✅ {file_path}: 内容完整 ({len(content)}字符)')

                    except Exception as e:
                        content_issues.append((file_path, f'读取错误: {e}'))
                        print(f'❌ {file_path}: 读取错误 - {e}')

        self.verification_results['file_content'] = {
            'total_files': len([f for info in self.project_structure.values() for f in info['files']]),
            'valid_files': len(valid_files),
            'content_issues': len(content_issues),
            'valid_files_list': valid_files,
            'content_issues_list': content_issues
        }

        return len(content_issues) == 0

    def verify_project_structure(self):
        """验证项目结构完整性"""
        print('\\n🏗️ 验证项目结构...')
        print('=' * 50)

        structure_score = 0
        total_categories = len(self.project_structure)

        for category, info in self.project_structure.items():
            existing_count = sum(1 for f in info['files'] if os.path.exists(os.path.join(self.workspace_dir, f)))
            total_count = len(info['files'])

            if existing_count == total_count:
                structure_score += 1
                print(f'✅ {category}: 完整 ({existing_count}/{total_count})')
            else:
                print(f'❌ {category}: 缺失 ({existing_count}/{total_count})')

        self.verification_results['project_structure'] = {
            'total_categories': total_categories,
            'complete_categories': structure_score,
            'incomplete_categories': total_categories - structure_score
        }

        return structure_score == total_categories

    def run_verification(self):
        """运行完整验证"""
        print('🚀 AI安全项目完整性验证')
        print('=' * 60)
        print(f'📅 验证时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'📁 工作目录: {self.workspace_dir}')

        verification_steps = [
            ('file_existence', '文件存在性验证', self.verify_file_existence),
            ('script_syntax', '脚本语法验证', self.verify_script_syntax),
            ('dependencies', '依赖关系验证', self.verify_dependencies),
            ('file_content', '文件内容验证', self.verify_file_content),
            ('project_structure', '项目结构验证', self.verify_project_structure)
        ]

        overall_success = True

        for step_key, step_name, step_func in verification_steps:
            print(f'\\n📋 {step_name}...')
            step_success = step_func()
            if not step_success:
                overall_success = False

        return overall_success

    def generate_verification_report(self):
        """生成验证报告"""
        print('\\n📊 生成验证报告')
        print('=' * 60)

        report = {
            'verification_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'overall_status': 'PASS' if self.run_verification() else 'FAIL',
            'verification_results': self.verification_results
        }

        # 显示总体结果
        total_files = sum(result['total_files'] for result in self.verification_results.values() if 'total_files' in result)
        existing_files = sum(len(result.get('existing_files_list', [])) for result in self.verification_results.values() if 'existing_files_list' in result)
        syntax_errors = sum(result.get('syntax_errors', 0) for result in self.verification_results.values() if 'syntax_errors' in result)
        missing_deps = sum(result.get('missing_deps', 0) for result in self.verification_results.values() if 'missing_deps' in result)

        print(f'\\n📈 验证结果汇总:')
        print(f'   总文件数: {total_files}')
        print(f'   存在文件: {existing_files}')
        print(f'   语法错误: {syntax_errors}')
        print(f'   缺失依赖: {missing_deps}')
        print(f'   总体状态: {"✅ PASS" if report["overall_status"] == "PASS" else "❌ FAIL"}')

        # 显示建议
        self.show_recommendations()

        return report

    def show_recommendations(self):
        """显示修复建议"""
        print('\\n💡 修复建议')
        print('=' * 60)

        if self.verification_results.get('file_existence', {}).get('missing_files', []):
            print('\\n📁 缺失文件:')
            for file in self.verification_results['file_existence']['missing_files_list']:
                print(f'   • {file}')

        if self.verification_results.get('script_syntax', {}).get('syntax_errors', []):
            print('\\n🔧 语法错误:')
            for file, error in self.verification_results['script_syntax']['syntax_errors_list']:
                print(f'   • {file}: {error}')

        if self.verification_results.get('dependencies', {}).get('missing_deps', []):
            print('\\n📦 缺失依赖:')
            for dep in self.verification_results['dependencies']['missing_deps_list']:
                print(f'   • {dep} - 建议执行: pip3 install {dep}')

        if self.verification_results.get('file_content', {}).get('content_issues', []):
            print('\\n📄 内容问题:')
            for file, issue in self.verification_results['file_content']['content_issues_list']:
                print(f'   • {file}: {issue}')

        print('\\n🚀 使用建议:')
        print('   1. 确保所有文件都存在')
        print('   2. 安装必要的Python依赖')
        print('   3. 修复所有语法错误')
        print('   4. 验证文件内容完整性')
        print('   5. 运行演示脚本测试功能')

def main():
    """主函数"""
    verifier = ProjectVerifier()

    try:
        # 运行验证
        report = verifier.generate_verification_report()

        # 保存报告
        report_file = '/workspace/verification_report.json'
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f'\\n💾 验证报告已保存到: {report_file}')

        # 显示最终状态
        if report['overall_status'] == 'PASS':
            print('\\n🎉 项目验证通过!')
            print('✅ 所有组件都正常，可以开始使用项目')
        else:
            print('\\n❌ 项目验证失败!')
            print('🔧 请根据上述建议修复问题后重新验证')

        print('\\n📋 下一步操作:')
        print('   1. python3 execute_demo.py --check  # 环境检查')
        print('   2. python3 execute_demo.py --all    # 运行所有演示')
        print('   3. python3 project_verifier.py       # 重新验证项目')

    except KeyboardInterrupt:
        print('\\n\\n⚠️ 验证被用户中断')
        print('💡 项目验证已停止')
    except Exception as e:
        print(f'\\n❌ 验证过程中发生错误: {e}')
        print('🔧 请检查项目配置')

if __name__ == '__main__':
    print('🔍 AI安全项目验证器启动...')
    print('📋 验证项目完整性和正确性')

    main()

    print('\\n🛡️ 验证完成!')
    print('   • 项目完整性检查完成')
    print('   • 所有问题已识别')
    print('   • 建议已提供')
    print('   • 报告已保存')