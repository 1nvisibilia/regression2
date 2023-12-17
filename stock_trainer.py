from torch import from_numpy, no_grad
from torch.utils.data import DataLoader, TensorDataset
from torch.nn.functional import mse_loss as loss_fn
from torch.optim import SGD
from stock_trainer_nn import StockTrainerNN, device

stock_model = StockTrainerNN().to(device)

optimizer = SGD(stock_model.parameters(), lr=1e-2)

def train_model(inputs, labels, test_input, test_labels):
    inputs = from_numpy(inputs)
    labels = from_numpy(labels)
    test_input = from_numpy(test_input)
    test_labels = from_numpy(test_labels)

    loss_stats = {
        "train": [],
        "val": []
    }
    dataset = TensorDataset(inputs, labels)
    loader = DataLoader(dataset, batch_size=10, shuffle=True)
    test_dataset = TensorDataset(test_input, test_labels)
    test_loader = DataLoader(test_dataset, batch_size=10, shuffle=True)


    for epoch in range(100):
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

            for input_data, label_data in test_loader:
                input_data = input_data.to(device)
                label_data = label_data.to(device)

                outputs = stock_model(input_data)

                loss = loss_fn(outputs, label_data)

                val_epoch_loss += loss.item()
        
        train_loss = train_epoch_loss / len(loader)
        val_loss = val_epoch_loss / len(test_loader)
        loss_stats["train"].append(train_loss)
        loss_stats["val"].append(val_loss)

        print(f"Epoch {epoch+0:01}: | Train loss: {train_loss:.3f} | Val loss: {val_loss:.3f}")