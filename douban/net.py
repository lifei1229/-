# -*- coding: utf-8 -*
from torch import nn


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

    def forward(self, input):
        return


class Net(nn.Module):

    def __init__(self, num_classes, num_maps=1, kmax=1, kmin=1, alpha=0.7):
        super(Net, self).__init__()
        self.spaXYDenseNet121 = spaXY_densenet121()
        model_dict = self.spaXYDenseNet121.state_dict()
        pretrained_dict = model_zoo.load_url(model_urls['densenet121'])
        pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in model_dict}
        model_dict.update(pretrained_dict)
        self.spaXYDenseNet121.load_state_dict(model_dict)
        self.features = self.spaXYDenseNet121.features
        num_ftrs = self.spaXYDenseNet121.classifier.in_features
        self.classifier = nn.Conv2d(num_ftrs, num_classes*num_maps, kernel_size=1, stride=1, padding=0, bias=True)
#        self.class_wise = ClassWisePool(num_maps)
#        self.spatial_pool = WildcatPool2d(kmax, kmin, alpha)
        self.maxpooling = nn.MaxPool2d(15)

    def forward(self, x):
        x = self.features(x)
        x = F.relu(x, True)
        xm = self.classifier(x)
#        xm = self.class_wise(x)
        xm = F.sigmoid(xm)
        x = self.spatial_pool(xm)
#        x = self.maxpooling(xm).squeeze(2).squeeze(2)
        return xm, x