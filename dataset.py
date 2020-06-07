import torch
import matplotlib.pyplot as plt
from torchvision import datasets, transforms

DATA_DIR = "./data"


def mnist_loader(val_split=0.2, batch_size=5):
    # normalize = transforms.Normalize((0.1307,), (0.3081,))
    transform = transforms.Compose([transforms.ToTensor()])

    # load the dataset
    train_dataset = datasets.MNIST(root=DATA_DIR, train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST(root=DATA_DIR, train=False, download=True, transform=transform)
    
    #Shuffle and split train and validations set
    val_size = int(val_split * len(train_dataset))
    train_size = int((1-val_split) * len(train_dataset))
    train_dataset, val_dataset = torch.utils.data.random_split(train_dataset, [train_size, val_size])

    #Define dataloader
    train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=False)
    val_dataloader = torch.utils.data.DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=True)

    print("-"*30+"MNIST DATASET"+"-"*30)
    print("Train Set size: ", len(train_dataset))
    print("Validation Set size: ", len(val_dataset))
    print("Test Set size: ", len(test_dataset))

    return train_dataloader, val_dataloader, test_dataloader


def visualize_dataset(datasets=["train", "val","test"]):
    fig, big_axes = plt.subplots( figsize=(20, 15) , nrows=3, ncols=1) 
    for i in range(3):
        big_axes[i]._frameon = False
        big_axes[i].set_axis_off()
        data_iter = iter(datasets[i])
        if i==0:  big_axes[0].set_title("Train Set", fontsize=16)
        if i==1: big_axes[1].set_title("Validation Set", fontsize=16)
        if i==2: big_axes[2].set_title("Test Set", fontsize=16)
        #Plot 5 images the selected dataset
        for j in range(5):
            fig.add_subplot(3,5,(i*5)+j+1)
            plt.imshow(transforms.ToPILImage()(next(data_iter)[0][0]), cmap=plt.get_cmap('gray'))
            plt.axis('off')
    plt.show()


if __name__ == "__main__":
    train, validation, test = mnist_loader()
    visualize_dataset([train, validation, test])
