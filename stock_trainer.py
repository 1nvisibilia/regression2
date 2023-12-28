import os
from torch import from_numpy, no_grad, save, load, tensor, double
from torch.utils.data import DataLoader, TensorDataset
from torch.nn.functional import mse_loss as loss_fn
from torch.optim import SGD
from stock_trainer_nn import StockTrainerNN, device

stock_model = StockTrainerNN().to(device)

optimizer = SGD(stock_model.parameters(), lr=1e-2)

if (os.path.isfile("model_data")):
    stock_model.load_state_dict(load("model_data"))

def computeAccuracy(outputs, label_data):
    accuracy_sum = 0
    for output, label in zip(outputs, label_data):
        accuracy = 0
        for output_unit, label_unit in zip(output, label):
            if (output_unit.item() * label_unit.item() >= 0):
                accuracy += min(output_unit.item(), label_unit.item()) / max(output_unit.item(), label_unit.item())
        accuracy_sum += accuracy / len(output)
    return accuracy_sum / len(outputs)

def train_model(inputs, labels, test_input, test_labels):
    inputs = from_numpy(inputs)
    labels = from_numpy(labels)
    test_input = from_numpy(test_input)
    test_labels = from_numpy(test_labels)

    loss_stats = {
        "train": [],
        "val": [],
        "accuracy": []
    }
    dataset = TensorDataset(inputs, labels)
    loader = DataLoader(dataset, batch_size=10, shuffle=True)
    test_dataset = TensorDataset(test_input, test_labels)
    test_loader = DataLoader(test_dataset, batch_size=10, shuffle=True)


    for epoch in range(5):
        train_epoch_loss = 0
        stock_model.train()

        for input_data, label_data in loader:
            optimizer.zero_grad()

            input_data = input_data.to(device)
            label_data = label_data.to(device)

            outputs = stock_model(input_data)

            loss = loss_fn(outputs, label_data)

            # gradient descent
            loss.backward()

            optimizer.step()

            train_epoch_loss += loss.item()
        
        # validations
        with no_grad():
            val_epoch_loss = 0

            stock_model.eval()
            accuracy_list = []
            for input_data, label_data in test_loader:
                input_data = input_data.to(device)
                label_data = label_data.to(device)

                outputs = stock_model(input_data)

                loss = loss_fn(outputs, label_data)
                accuracy_list.append(computeAccuracy(outputs, label_data))

                val_epoch_loss += loss.item()

        epoch_accuracy = sum(accuracy_list) / len(accuracy_list)
        train_loss = train_epoch_loss / len(loader)
        val_loss = val_epoch_loss / len(test_loader)
        loss_stats["train"].append(train_loss)
        loss_stats["val"].append(val_loss)
        loss_stats["accuracy"].append(epoch_accuracy)

        print(f"Epoch {epoch+0:01}: | Train loss: {train_loss:.3f} | Val loss: {val_loss:.3f} | Accuracy: {epoch_accuracy * 100:.6f}%")
    
    save(stock_model.state_dict(), "model_data")

def compute_instance(input_embedding: list[double]):
    # data = [57628.086, 57646.805, 57651.54, 57656.316, 57617.81,
    #         57609.035, 57619.293, 57655.79, 57604.934, 57613.387,
    #         57524.32, 57524.363, 57576.824, 57624.887, 57615.367]
    #         57529.016, 57543.332, 57542.895, 57551.69, 57565.87
    print(stock_model.predict(
        tensor(input_embedding, dtype=double)
    ))
