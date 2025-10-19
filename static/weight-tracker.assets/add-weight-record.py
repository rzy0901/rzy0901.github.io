#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
体重记录添加工具
快速添加体重数据到CSV文件
"""

import csv
import os
from datetime import datetime

# CSV_FILE = 'static/weight-tracker.assets/weight-data.csv'
CSV_FILE = 'weight-data.csv'

def add_weight_record():
    """添加体重记录"""
    print("=" * 50)
    print("体重记录添加工具")
    print("=" * 50)
    
    # 检查CSV文件是否存在
    if not os.path.exists(CSV_FILE):
        print(f"错误: 找不到文件 {CSV_FILE}")
        return
    
    # 获取今天的日期
    today = datetime.now().strftime('%Y-%m-%d')
    print(f"\n当前日期: {today}")
    
    # 输入日期
    date_input = input(f"请输入日期 (直接回车使用今天 {today}): ").strip()
    if not date_input:
        date_input = today
    
    # 验证日期格式
    try:
        datetime.strptime(date_input, '%Y-%m-%d')
    except ValueError:
        print("错误: 日期格式不正确，应为 YYYY-MM-DD")
        return
    
    # 输入体重
    while True:
        weight_input = input("请输入体重 (kg): ").strip()
        try:
            weight = float(weight_input)
            if weight <= 0 or weight > 300:
                print("错误: 体重数值不合理，请重新输入")
                continue
            break
        except ValueError:
            print("错误: 请输入有效的数字")
    
    # 输入备注
    remark = input("请输入备注 (可选，直接回车跳过): ").strip()
    
    # 读取现有数据
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # 检查是否已存在该日期的记录
    existing_dates = [row[0] for row in rows[1:]]  # 跳过表头
    if date_input in existing_dates:
        overwrite = input(f"警告: {date_input} 的记录已存在。是否覆盖? (y/n): ").lower()
        if overwrite != 'y':
            print("操作已取消")
            return
        # 删除旧记录
        rows = [rows[0]] + [row for row in rows[1:] if row[0] != date_input]
    
    # 添加新记录
    new_row = [date_input, str(weight), remark]
    rows.append(new_row)
    
    # 按日期排序（保留表头）
    header = rows[0]
    data_rows = rows[1:]
    data_rows.sort(key=lambda x: x[0])
    sorted_rows = [header] + data_rows
    
    # 写回文件
    with open(CSV_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sorted_rows)
    
    print("\n✓ 记录添加成功！")
    print(f"  日期: {date_input}")
    print(f"  体重: {weight} kg")
    if remark:
        print(f"  备注: {remark}")
    print("\n提示: 刷新博客页面即可看到更新的图表")

def view_recent_records():
    """查看最近的记录"""
    if not os.path.exists(CSV_FILE):
        print(f"错误: 找不到文件 {CSV_FILE}")
        return
    
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    print("\n最近10条记录:")
    print("-" * 50)
    print(f"{'日期':<12} {'体重(kg)':<10} {'备注'}")
    print("-" * 50)
    
    for row in rows[-10:]:
        if len(row) >= 3:
            date, weight, remark = row[0], row[1], row[2] if len(row) > 2 else ''
            print(f"{date:<12} {weight:<10} {remark}")

def show_statistics():
    """显示统计信息"""
    if not os.path.exists(CSV_FILE):
        print(f"错误: 找不到文件 {CSV_FILE}")
        return
    
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)[1:]  # 跳过表头
    
    if not rows:
        print("暂无数据")
        return
    
    weights = [float(row[1]) for row in rows if len(row) >= 2 and row[1]]
    
    if not weights:
        print("暂无有效数据")
        return
    
    print("\n统计信息:")
    print("-" * 50)
    print(f"记录天数: {len(weights)} 天")
    print(f"起始体重: {weights[0]:.2f} kg ({rows[0][0]})")
    print(f"当前体重: {weights[-1]:.2f} kg ({rows[-1][0]})")
    print(f"最高体重: {max(weights):.2f} kg")
    print(f"最低体重: {min(weights):.2f} kg")
    print(f"平均体重: {sum(weights)/len(weights):.2f} kg")
    change = weights[-1] - weights[0]
    print(f"总变化: {'+' if change > 0 else ''}{change:.2f} kg")

def main():
    """主菜单"""
    while True:
        print("\n" + "=" * 50)
        print("体重追踪工具")
        print("=" * 50)
        print("1. 添加体重记录")
        print("2. 查看最近记录")
        print("3. 查看统计信息")
        print("4. 退出")
        print("=" * 50)
        
        choice = input("请选择操作 (1-4): ").strip()
        
        if choice == '1':
            add_weight_record()
        elif choice == '2':
            view_recent_records()
        elif choice == '3':
            show_statistics()
        elif choice == '4':
            print("再见！")
            break
        else:
            print("无效的选择，请重新输入")

if __name__ == '__main__':
    main()

