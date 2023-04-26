from nbconvert.exporters import PythonExporter

# 创建 PythonExporter 实例
exporter = PythonExporter()

# 读取并转换 .ipynb 文件
with open('C:\\AIproject\\Generative\\generative-agents\\notebook\\Release\\generative_model_simple-chatGLM.ipynb', 'r', encoding='utf-8') as f:
    notebook_code, _ = exporter.from_file(f)

# 将转换后的代码保存到 .py 文件中
with open('C:\\AIproject\\Generative\\generative-agents\\notebook\\Release\\generative_model_simple-chatGLM.py', 'w', encoding='utf-8') as f:
    f.write(notebook_code)