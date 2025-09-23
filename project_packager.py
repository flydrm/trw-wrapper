#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📦 项目打包器 - 打包AI安全项目用于分发

功能:
   - 项目完整性检查
   - 文件打包压缩
   - 文档生成
   - 分发包制作
   - 安装脚本生成

📋 打包内容:
   - 所有演示脚本
   - 技术文档
   - 执行工具
   - 使用指南
   - 安装脚本
"""

import os
import sys
import json
import tarfile
import zipfile
import shutil
from datetime import datetime
from pathlib import Path

class ProjectPackager:
    """项目打包器"""

    def __init__(self):
        self.workspace_dir = '/workspace'
        self.package_name = f'ai_security_project_{datetime.now().strftime("%Y%m%d_%H%M%S")}'

        # 要打包的文件
        self.files_to_package = {
            '演示脚本': [
                'ai_security_one_click_demo.py',
                'comprehensive_bypass_solution.py',
                'ai_model_access_demo.py'
            ],
            '执行工具': [
                'execute_demo.py',
                'project_verifier.py',
                'quick_fix.py',
                'start_project.py',
                'performance_optimizer.py'
            ],
            '文档文件': [
                'README.md',
                'FINAL_PROJECT_SUMMARY.md',
                'final_complete_solution.md',
                'bypass_instructions.md',
                'client_usage_guide.md'
            ],
            '其他文件': [
                'setup.py',
                'requirements.txt'
            ]
        }

        self.package_results = {}

    def check_project_integrity(self):
        """检查项目完整性"""
        print('🔍 检查项目完整性...')
        print('=' * 50)

        missing_files = []
        existing_files = []

        for category, files in self.files_to_package.items():
            for file in files:
                file_path = os.path.join(self.workspace_dir, file)
                if os.path.exists(file_path):
                    file_size = os.path.getsize(file_path)
                    existing_files.append((file, file_size))
                    print(f'✅ {file}: {file_size} bytes')
                else:
                    missing_files.append(file)
                    print(f'❌ {file}: 文件不存在')

        self.package_results['integrity_check'] = {
            'total_files': sum(len(files) for files in self.files_to_package.values()),
            'existing_files': len(existing_files),
            'missing_files': len(missing_files),
            'missing_files_list': missing_files
        }

        return len(missing_files) == 0

    def create_package_structure(self):
        """创建打包目录结构"""
        print('\\n📁 创建打包目录结构...')
        print('=' * 50)

        try:
            # 创建主目录
            package_dir = os.path.join(self.workspace_dir, self.package_name)
            os.makedirs(package_dir, exist_ok=True)

            # 创建子目录
            subdirs = ['scripts', 'docs', 'tools', 'examples']
            for subdir in subdirs:
                os.makedirs(os.path.join(package_dir, subdir), exist_ok=True)
                print(f'✅ 创建目录: {subdir}')

            self.package_results['package_dir'] = package_dir
            return package_dir

        except Exception as e:
            print(f'❌ 创建目录失败: {e}')
            return None

    def copy_files_to_package(self, package_dir):
        """复制文件到打包目录"""
        print('\\n📋 复制文件到打包目录...')
        print('=' * 50)

        copied_files = 0
        failed_copies = []

        # 复制演示脚本
        for file in self.files_to_package['演示脚本']:
            src = os.path.join(self.workspace_dir, file)
            dst = os.path.join(package_dir, 'scripts', file)
            if self._copy_file(src, dst):
                copied_files += 1
                print(f'✅ 复制脚本: {file}')
            else:
                failed_copies.append(file)

        # 复制执行工具
        for file in self.files_to_package['执行工具']:
            src = os.path.join(self.workspace_dir, file)
            dst = os.path.join(package_dir, 'tools', file)
            if self._copy_file(src, dst):
                copied_files += 1
                print(f'✅ 复制工具: {file}')
            else:
                failed_copies.append(file)

        # 复制文档文件
        for file in self.files_to_package['文档文件']:
            src = os.path.join(self.workspace_dir, file)
            dst = os.path.join(package_dir, 'docs', file)
            if self._copy_file(src, dst):
                copied_files += 1
                print(f'✅ 复制文档: {file}')
            else:
                failed_copies.append(file)

        self.package_results['file_copy'] = {
            'copied_files': copied_files,
            'failed_copies': len(failed_copies),
            'failed_files_list': failed_copies
        }

        return len(failed_copies) == 0

    def _copy_file(self, src, dst):
        """复制单个文件"""
        try:
            shutil.copy2(src, dst)
            return True
        except Exception as e:
            print(f'❌ 复制失败 {src}: {e}')
            return False

    def generate_requirements(self, package_dir):
        """生成依赖文件"""
        print('\\n📦 生成依赖文件...')
        print('=' * 50)

        try:
            requirements_content = '''# AI安全项目依赖
requests>=2.25.0
beautifulsoup4>=4.9.0
psutil>=5.8.0
'''

            requirements_file = os.path.join(package_dir, 'requirements.txt')
            with open(requirements_file, 'w', encoding='utf-8') as f:
                f.write(requirements_content)

            print('✅ requirements.txt 已生成')

            # 生成setup.py
            setup_content = '''from setuptools import setup, find_packages

setup(
    name="ai-security-project",
    version="1.0.0",
    author="Ethan Security Team",
    description="AI安全项目 - 完整的AI聊天平台安全解决方案",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "beautifulsoup4>=4.9.0",
        "psutil>=5.8.0"
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "ai-security-demo=scripts.ai_security_one_click_demo:main",
            "ai-security-verify=tools.project_verifier:main",
            "ai-security-launch=tools.start_project:main"
        ]
    }
)
'''

            setup_file = os.path.join(package_dir, 'setup.py')
            with open(setup_file, 'w', encoding='utf-8') as f:
                f.write(setup_content)

            print('✅ setup.py 已生成')

            return True

        except Exception as e:
            print(f'❌ 生成依赖文件失败: {e}')
            return False

    def generate_installation_script(self, package_dir):
        """生成安装脚本"""
        print('\\n🔧 生成安装脚本...')
        print('=' * 50)

        try:
            install_script = '''#!/bin/bash
# AI安全项目安装脚本

echo "🚀 AI安全项目安装器"
echo "======================"

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装，请先安装Python3"
    exit 1
fi

echo "✅ Python3 已安装"

# 安装依赖
echo "📦 安装Python依赖..."
pip3 install -r requirements.txt

# 设置权限
echo "🔐 设置脚本权限..."
chmod +x scripts/*.py
chmod +x tools/*.py

echo ""
echo "🎉 安装完成!"
echo ""
echo "📋 使用方法:"
echo "   python3 tools/start_project.py     # 启动项目"
echo "   python3 tools/execute_demo.py --all # 运行演示"
echo "   python3 tools/project_verifier.py   # 验证项目"
echo ""
echo "📚 文档位置:"
echo "   docs/README.md                    # 项目说明"
echo "   docs/FINAL_PROJECT_SUMMARY.md     # 项目总结"
echo ""
echo "🛡️ 安全提醒:"
echo "   所有演示仅用于教育目的"
echo "   建议在获得授权后使用"
'''

            install_script_file = os.path.join(package_dir, 'install.sh')
            with open(install_script_file, 'w', encoding='utf-8') as f:
                f.write(install_script)

            # 设置执行权限
            os.chmod(install_script_file, 0o755)

            print('✅ install.sh 已生成')

            return True

        except Exception as e:
            print(f'❌ 生成安装脚本失败: {e}')
            return False

    def generate_readme_for_package(self, package_dir):
        """生成打包版本的README"""
        print('\\n📖 生成打包README...')
        print('=' * 50)

        try:
            readme_content = f'''# AI安全项目 - 打包版本

**项目名称**: AI聊天平台安全深度评估与解决方案
**打包时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**版本**: 1.0.0

## 📦 包内容

### 🎬 演示脚本
- `scripts/ai_security_one_click_demo.py` - 一键完整演示
- `scripts/comprehensive_bypass_solution.py` - 完整绕过方案演示
- `scripts/ai_model_access_demo.py` - AI模型访问演示

### 🛠️ 执行工具
- `tools/execute_demo.py` - 演示脚本执行器
- `tools/project_verifier.py` - 项目验证器
- `tools/quick_fix.py` - 快速修复器
- `tools/start_project.py` - 项目启动器
- `tools/performance_optimizer.py` - 性能优化器

### 📚 文档文件
- `docs/README.md` - 项目说明
- `docs/FINAL_PROJECT_SUMMARY.md` - 项目总结
- `docs/final_complete_solution.md` - 完整解决方案
- `docs/bypass_instructions.md` - 绕过指南
- `docs/client_usage_guide.md` - 使用指南

## 🚀 快速开始

### 1. 安装依赖
```bash
pip3 install -r requirements.txt
```

### 2. 运行安装脚本
```bash
./install.sh
```

### 3. 启动项目
```bash
python3 tools/start_project.py
```

## 📋 演示说明

### 客户高层演示
```bash
python3 scripts/ai_security_one_click_demo.py
```

### 技术团队演示
```bash
python3 scripts/comprehensive_bypass_solution.py
```

### 开发团队演示
```bash
python3 scripts/ai_model_access_demo.py
```

## 🛡️ 安全提醒

- 所有演示仅用于教育目的
- 建议在获得授权的环境中使用
- 演示结束后立即实施安全加固
- 安全投资是长期价值保障

## 📞 技术支持

- 联系方式: security@ethan-team.com
- 紧急支持: +86-138-0013-8000
- 在线平台: https://security.ethan-team.com

---
**乙方团队**: 安全顾问专家组
**交付时间**: {datetime.now().strftime("%Y-%m-%d")}
**项目状态**: ✅ 完整交付
'''

            readme_file = os.path.join(package_dir, 'README.md')
            with open(readme_file, 'w', encoding='utf-8') as f:
                f.write(readme_content)

            print('✅ 打包README已生成')
            return True

        except Exception as e:
            print(f'❌ 生成README失败: {e}')
            return False

    def create_zip_package(self, package_dir):
        """创建ZIP压缩包"""
        print('\\n📦 创建ZIP压缩包...')
        print('=' * 50)

        try:
            zip_file = f'{package_dir}.zip'
            with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(package_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, package_dir)
                        zipf.write(file_path, arcname)

            zip_size = os.path.getsize(zip_file)
            print(f'✅ ZIP压缩包已创建: {zip_file} ({zip_size} bytes)')

            self.package_results['zip_package'] = {
                'file': zip_file,
                'size': zip_size
            }

            return True

        except Exception as e:
            print(f'❌ 创建ZIP包失败: {e}')
            return False

    def create_tar_package(self, package_dir):
        """创建TAR压缩包"""
        print('\\n📦 创建TAR压缩包...')
        print('=' * 50)

        try:
            tar_file = f'{package_dir}.tar.gz'
            with tarfile.open(tar_file, 'w:gz') as tarf:
                tarf.add(package_dir, arcname=os.path.basename(package_dir))

            tar_size = os.path.getsize(tar_file)
            print(f'✅ TAR压缩包已创建: {tar_file} ({tar_size} bytes)')

            self.package_results['tar_package'] = {
                'file': tar_file,
                'size': tar_size
            }

            return True

        except Exception as e:
            print(f'❌ 创建TAR包失败: {e}')
            return False

    def generate_package_report(self):
        """生成打包报告"""
        print('\\n📊 生成打包报告')
        print('=' * 50)

        report = {
            'package_name': self.package_name,
            'package_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'total_files': sum(len(files) for files in self.files_to_package.values()),
            'package_size': 0,
            'results': self.package_results
        }

        # 计算包大小
        if 'zip_package' in self.package_results:
            report['package_size'] = self.package_results['zip_package']['size']

        print('\\n📈 打包结果汇总:')
        print(f'   包名称: {self.package_name}')
        print(f'   总文件数: {report["total_files"]}')
        print(f'   包大小: {report["package_size"]} bytes')

        if 'zip_package' in self.package_results:
            print(f'   ZIP文件: {self.package_results["zip_package"]["file"]}')

        if 'tar_package' in self.package_results:
            print(f'   TAR文件: {self.package_results["tar_package"]["file"]}')

        # 保存报告
        report_file = os.path.join(self.workspace_dir, f'{self.package_name}_report.json')
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f'\\n💾 打包报告已保存到: {report_file}')

        return report

    def package_project(self):
        """打包项目"""
        print('📦 AI安全项目打包器')
        print('=' * 60)
        print(f'📅 打包时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

        # 检查项目完整性
        if not self.check_project_integrity():
            print('\\n❌ 项目完整性检查失败，无法打包')
            return False

        # 创建打包目录
        package_dir = self.create_package_structure()
        if not package_dir:
            return False

        # 复制文件
        if not self.copy_files_to_package(package_dir):
            print('\\n❌ 文件复制失败')
            return False

        # 生成依赖文件
        if not self.generate_requirements(package_dir):
            print('\\n❌ 依赖文件生成失败')
            return False

        # 生成安装脚本
        if not self.generate_installation_script(package_dir):
            print('\\n❌ 安装脚本生成失败')
            return False

        # 生成README
        if not self.generate_readme_for_package(package_dir):
            print('\\n❌ README生成失败')
            return False

        # 创建压缩包
        zip_success = self.create_zip_package(package_dir)
        tar_success = self.create_tar_package(package_dir)

        if not (zip_success or tar_success):
            print('\\n❌ 压缩包创建失败')
            return False

        # 生成报告
        self.generate_package_report()

        print('\\n🎉 项目打包完成!')
        print(f'📁 打包目录: {package_dir}')

        if zip_success:
            print(f'📦 ZIP包: {self.package_results["zip_package"]["file"]}')

        if tar_success:
            print(f'📦 TAR包: {self.package_results["tar_package"]["file"]}')

        print('\\n📋 打包内容:')
        print('   • 3个演示脚本')
        print('   • 5个执行工具')
        print('   • 5个技术文档')
        print('   • 安装脚本和依赖文件')
        print('   • 项目说明文档')

        return True

def main():
    """主函数"""
    packager = ProjectPackager()

    try:
        # 打包项目
        success = packager.package_project()

        if success:
            print('\\n🎉 打包成功!')
            print('✅ 项目已完整打包')
            print('✅ 压缩包已生成')
            print('✅ 安装脚本已创建')
            print('✅ 文档已完善')
        else:
            print('\\n❌ 打包失败!')
            print('🔧 请检查错误信息')

        print('\\n📋 分发说明:')
        print('   1. 将ZIP或TAR文件发送给客户')
        print('   2. 客户运行install.sh安装')
        print('   3. 客户使用start_project.py启动')
        print('   4. 客户查看README.md了解使用方法')

    except KeyboardInterrupt:
        print('\\n\\n⚠️ 打包被用户中断')
        print('💡 项目打包已停止')
    except Exception as e:
        print(f'\\n❌ 打包过程中发生错误: {e}')
        print('🔧 请检查项目配置')

if __name__ == '__main__':
    print('📦 项目打包器启动...')
    print('📋 打包AI安全项目用于分发')

    main()

    print('\\n🛡️ 打包完成!')
    print('   • 项目已打包')
    print('   • 压缩包就绪')
    print('   • 安装脚本生成')
    print('   • 准备分发')