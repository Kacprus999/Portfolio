from NeuralNetwork import prediction
import os

def test_all():
    material = 'glass'
    dir = "./resources/trash_dataset/test/" + material
    for i in range(0, 56, 5):
        count = 0
        full_count = 0
        for file in os.listdir(dir):
            full_count += 1
            path = os.path.join(dir, file)
            # print(path)
            result = prediction.getPrediction(path, 'trained_nn_'+str(i)+'.pth')
            if result == material:
                count += 1
        print('siec ' + str(i) + ': ' + str(count) + '/' + str(full_count))

def test_one():
    network = 20
    material = 'paper'
    dir = "./resources/trash_dataset/test/" + material
    count = 0
    full_count = 0
    for file in os.listdir(dir):
        full_count += 1
        path = os.path.join(dir, file)
        result = prediction.getPrediction(path, 'trained_nn_'+str(network)+'.pth')
        if result == material:
            count += 1
        else:
            print(path)
    print('siec ' + str(network) + ': ' + str(count) + '/' + str(full_count))
        

def main():
    test_one()



if __name__ == '__main__':
    main()