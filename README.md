#  Image Classification

本项目基于OpenMMLab图像分类工具包 MMClassification进行构建，使用前请先配置好MMClassification工作环境

具体方法请参考官方文档：[open-mmlab/mmclassification: OpenMMLab Image Classification Toolbox and Benchmark (github.com)](https://github.com/open-mmlab/mmclassification)



## Flower_ImageClassification

该数据集包括5 种类别的花卉图像:

雏菊 daisy 588张，蒲公英 dandelion 556张，玫瑰 rose 583张，向日葵 sunflower 536张，郁金香 tulip 585张。

经过<code>splite.py</code>文件处理为ImageNet格式

DataSet：链接：https://pan.baidu.com/s/1XNlRCclLxRHYXkWqlZ2ILQ  提取码：q7c6

Checkpoint：链接：https://pan.baidu.com/s/1CQHVCr6s7mXP6jaVotb1Ug  提取码：ke7q

训练结果如下：

| Model  | Accuracy_top-1 |
| :-------: | :------------: |
| ResNet-50 |    95.9790     |

![](https://github.com/Rookie-Kai/ImageClassicication/blob/main/Flower_ImageClassification/resnet50_flower.png?raw=true)



## Cifar_ImageClassification

该数据集包含 10 个类别的 RGB 彩色图片：

飞机（ airplane ）、汽车（ automobile ）、鸟类（ bird ）、猫（ cat ）、鹿（ deer ）、狗（ dog ）、蛙类（ frog ）、马（ horse ）、船（ ship ）和卡车（ truck ）。

图片的尺寸为 32×32 ，数据集中一共有 50000 张训练圄片和 10000 张测试图片。

DataSet：链接：https://pan.baidu.com/s/1EPQzNc3F1cjv4aYEpPhinA  提取码：h77k

Checkpoint：链接：https://pan.baidu.com/s/1XWX5s5F9Nra5XCQJbWcl0g  提取码：x8u2

训练结果如下：

|  Model  | Accuracy_top-1 | Accuracy_top-5 |
| :--------: | :------------: | :------------: |
| ResNet-101 |    88.5700     |    99.4500     |

![](https://github.com/Rookie-Kai/ImageClassicication/blob/main/Cifar_ImageClassification/result.jpg?raw=true)

![](https://github.com/Rookie-Kai/ImageClassicication/blob/main/Cifar_ImageClassification/loss.jpg?raw=true)
