# 原包回归示例

这些片段与两张图来自原始 ppt-flow.zip，用于验证绘图函数与旧示例兼容，不是新的论文事实核对结果，也不是当前用户已确认的最终稿。

例子仍包含旧的分类章节、文献助手情境和较密集的页面。当前制作应优先遵循根目录 SKILL.md 及 references/，并读取用户最新 PPT；不要由这个例子恢复已取消的章节或替换已选案例。

在仓库根目录使用已配置依赖的解释器运行：

```bash
python scripts/build.py outputs/legacy.pptx examples/legacy-agent-memory/part1.py examples/legacy-agent-memory/part2a.py examples/legacy-agent-memory/part2b.py examples/legacy-agent-memory/part3.py
```

原包约定生成 33 页，输出仅用于检查；论文内容、数字和图表应另行对照原始来源。
