# 东南大学母版（seu）

- 文件：template.pptx（27 页，作为可复制的版式页，build.py 生成后会删掉这些原始页）
- 页面：960×540 pt；正文区约 y=75–498；方法页不放页脚线
- 字体：Noto Sans SC（可用 PPTFLOW_FONT 覆盖）
- 调色板（common.py 中的常量）：GREEN 4F6228、GL E8EDDB、CREAM F5EBDF、BROWN A0622D、BLUE 3F6680、BL E6EDF3、PURPLE 7B5EA7、PL EEE9F5、RED C0392B、RL FBEDEA、CARD FAFBF6、CB DCE0D2、TXT 222222、GR 4A4A4A、GRAY 8C8C8C

## 版式页编号（SRC 下标，从 0 起）
| 下标 | 用途 | 调用 |
|---|---|---|
| 0 | 封面 | cover(title, date) |
| 1 | 目录 | toc(items, active) |
| 16 | 内容页（标题栏 + 正文） | newslide(title, crumb, footer) |
| 26 | 结束页 | thanks() |

## 更换/修改母版
1. 复制本文件夹为新名字（如 mylab），放入你的 .pptx。
2. 在 common.py 里核对上表的下标；改色只需改调色板常量。
3. 运行时设置 PPTFLOW_TEMPLATE 指向新文件。
