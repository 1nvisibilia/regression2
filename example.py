from stock_trainer import predict_prices

# input data, the stock prices from the past 30 minutes
data = [57628.086, 57646.805, 57651.54, 57656.316, 57617.81,
        57609.035, 57619.293, 57655.79, 57604.934, 57613.387,
        57524.32, 57524.363, 57576.824, 57624.887, 57615.367]

# the predicted stock prices for the next 10 minutes
predictions = predict_prices(data)

print("The predicted prices for the next 10 mins:")
print(predictions)