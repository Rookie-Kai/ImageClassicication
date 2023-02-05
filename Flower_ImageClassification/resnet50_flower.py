_base_ = ['../_base_/models/resnet50.py', '../_base_/datasets/imagenet_bs32.py', '../_base_/default_runtime.py']

# 模型配置
model = dict(
    # 分类头设置
    head=dict(
        num_classes=5,
        topk=(1,)
    )
)

data = dict(
    # 指定batch_size 与 num_workers
    samples_per_gpu=64,
    workers_per_gpu=2,

    # 训练集路径
    train=dict(
        data_prefix='data/flower_dataset/train',
        ann_file='data/flower_dataset/train.txt',
        classes='data/flower_dataset/classes.txt'
    ),
    # 指定验证集路径
    val=dict(
        data_prefix='data/flower_dataset/val',
        ann_file='data/flower_dataset/val.txt',
        classes='data/flower_dataset/classes.txt'
    ),
)

# 定义评估方法
evaluation = dict(metric_options={'topk': (1,)})

# 配置优化器
optimizer = dict(
    type='SGD',
    lr=0.001,
    momentum=0.9,
    weight_decay=0.0001
)
optimizer_config = dict(grad_clip=None)

# 学习率策略
lr_config = dict(
    policy='step',
    step=[1],
    by_epoch=True,
    warmup='linear',
    warmup_iters=5
)

# 运行器设置
runner = dict(
    type='EpochBasedRunner',
    max_epochs=100
)

# 预训练模型
load_from = '/data/home/scv9243/run/mmclassification/checkpoints/resnet50_checkpoints/resnet50_8xb32_in1k_20210831-ea4938fc.pth'