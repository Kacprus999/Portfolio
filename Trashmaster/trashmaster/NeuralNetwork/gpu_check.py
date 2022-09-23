import torch

def main():
    print(torch.cuda.is_available())
    print(torch.version.cuda)

if __name__ == '__main__':
    main()