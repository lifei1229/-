import torch
from torch import optim, nn
from torchvision import transforms
from torchvision.models import resnet18
from utils import Flatten, softmax
from PIL import Image
import os
import numpy as np


def predicts(img):

    device = torch.device('cuda')
    torch.manual_seed(1234)
    resize = 224
    className = {
        '0': 'bulbasaur',
        '1': 'charmander',
        '2': 'mewtw',
        '3': 'pikachu',
        '4': 'squirtle'}

    # model = ResNet18(5).to(device)
    trained_model = resnet18(pretrained=True)
    model = nn.Sequential(*list(trained_model.children())[:-1],  # [b, 512, 1, 1]
                          Flatten(),  # [b, 512, 1, 1] => [b, 512]
                          nn.Linear(512, 5)
                          ).to(device)
    # x = torch.randn(2, 3, 224, 224)
    # print(model(x).shape)
    basepath = os.path.dirname(__file__)  # 当前文件所在路径
    ckpt_path = os.path.join(basepath, 'best.mdl')
    print(ckpt_path)
    model.load_state_dict(torch.load(ckpt_path))
    print('loaded from ckpt!')

    tf = transforms.Compose([
        lambda x: Image.open(x).convert('RGB'),  # string path= > image data
        transforms.Resize(
            (int(resize), int(resize))),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    # img = 'pokeman\\pikachu\\00000003.jpg'
    x = tf(img)
    x = x.unsqueeze(0)
    x = x.to(device)

    model.eval()
    with torch.no_grad():
        logits = model(x)
        pred = logits.argmax(dim=1).item()
        prob = np.max(softmax(logits.cpu().numpy()), axis=1)[0]
    # print('Our model predicts : %s'%className[str(pred)])
    return className[str(pred)], str(round(prob * 100, 2)) + '%'


if __name__ == '__main__':
    img = r'C:\spyder\imgshow\static\images\00000009.png'
    pres = predicts(img)
