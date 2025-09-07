**name：Mingyuan Cao   
student ID: 700761039**

# Q4 — 编辑距离（Sunday → Saturday）

运行 `python edit_distance.py`，得到两种代价模型下的距离与一条可行编辑路径：
- **模型 A**（Sub=1, Ins=1, Del=1）：期望最小距离为 3
- **模型 B**（Sub=2, Ins=1, Del=1）：期望最小距离为 4（替换更贵，倾向用插入+删除）

请将 `edit_distance_output.json` 的关键结果粘贴于下：
```json
{
  "modelA": {"a": "Sunday", "b": "Saturday",
    "costs": {"sub": 1, "ins": 1, "del": 1},
    "distance": 3,
    "ops": ["Keep 'S'", 
      "Insert 'a'", 
      "Insert 't'", 
      "Keep 'u'", 
      "Substitute 'n' -> 'r'", 
      "Keep 'd'", 
      "Keep 'a'", 
      "Keep 'y'"]
  },
  "modelB": {"a": "Sunday", "b": "Saturday",
    "costs": {"sub": 2, "ins": 1, "del": 1},
    "distance": 4,
    "ops": [
      "Keep 'S'",
      "Insert 'a'",
      "Insert 't'",
      "Keep 'u'",
      "Substitute 'n' -> 'r'",
      "Keep 'd'",
      "Keep 'a'",
      "Keep 'y'"]
  }
}
```

**反思**：编辑距离的代价矩阵会直接影响“最优路径”的选择，例如在模型 A 中，替换和插入/删除的代价相同，因此算法更自由地选择替换；而在模型 B 中替换代价更高，算法自然倾向于通过插入和删除来达到目标。
这种差异体现了动态规划在寻找最优路径时对代价参数的敏感性，实际应用必须根据任务特点合理设定。
在拼写检查任务中，如果替换一个字母与用户的输入错误更常见，那么应当给替换较低的代价，从而更好地匹配用户真实的拼写习惯。
因此，编辑距离不仅是一个计算问题，更是一个需要结合应用领域知识进行调参的过程。
