**name：Mingyuan Cao   
student ID: 700761039**

# Q2 — 分词实验报告

> 在 `sample_text.txt` 文件中从任何文章中选取一个段落进行分词。

## 1) 对空格切分、手动修正规则和简易“工具”规则的比较
- **空格切分**：无法正确处理邮箱、引号、Unicode 短横等。
- **手动修正**：通过保护 Email、统一标点分隔，得到更合理的 token。
- **工具规则**：仅处理 ASCII 标点（不处理 Unicode 破折号/撇号），与手动版本存在差异。

### 关键对比
**邮箱保护带来的差异**：    
space: test@example.com,（和逗号粘一起）  
manual/tool：test@example.com 与 , 分离

**Unicode 标点（破折号、弯引号）** 处理差异：

manual：'、— 单独成 token；

tool："'tokenization'"、"matters—don’t" 作为单个 token。


## 2) 多词表达（MWE）举例
- United States
- machine learning
- New York City  
**说明**：它们是固定搭配/专名，在 NER、IR 中作为整体更稳定。

## 3) 反思
- 标点、缩写、撇号、URL/Email、数字-单位会增加切分复杂度；
- 英语有空格，但仍有连字符/撇号/多词专名等棘手点；
- 若换为中文、日文，分词本身就是必须步骤；
- 正则预处理 + 规则切分是工程上常见方案；
- 更强的工具（如 spaCy、Stanza）能统一处理多语言与特殊符号，但需要依赖和模型。
