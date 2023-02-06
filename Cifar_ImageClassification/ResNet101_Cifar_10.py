_base_ = ['../_base_/models/resnet101.py', '../_base_/datasets/cifar10_bs16.py', '../_base_/default_runtime.py']

model = dict(
    head=dict(
        num_classes=10,
        topk=(1, 5)
    )
)


dataset_type = 'CIFAR10'
img_norm_cfg = dict(
    mean=[125.307, 122.961, 113.8575],
    std=[51.5865, 50.847, 51.255],
    to_rgb=False)
train_pipeline = [
    dict(type='RandomCrop', size=32, padding=4),
    dict(type='RandomFlip', flip_prob=0.5, direction='horizontal'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='ToTensor', keys=['gt_label']),
    dict(type='Collect', keys=['img', 'gt_label'])
]
test_pipeline = [
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='Collect', keys=['img'])
]

data = dict(
    samples_per_gpu=128,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        data_prefix='data/',
        pipeline=train_pipeline
    ),
    val=dict(
        data_prefix='data/',
        pipeline=test_pipeline,
        test_mode=True
    ),
    test=dict(
        data_prefix='data/',
        pipeline=test_pipeline,
        test_mode=True
    )
)

evaluation = dict(metric_options={'topk': (1, 5)})

optimizer = dict(
    type='SGD',
    lr=0.1,
    momentum=0.9,
    weight_decay=0.0001
)
optimizer_config = dict(grad_clip=None)

lr_config = dict(
    policy='step',
    step=[100, 150],
)

runner = dict(type='EpochBasedRunner', max_epochs=200)

load_from = '/data/home/scv9243/run/mmclassification/checkpoints/resnet101_cifar10_checkpoints/resnet101_b16x8_cifar10_20210528-2d29e936.pth'