from stock_trainer import predict_prices

# input data, the stock prices from the past 30 minutes
data = [56342.484, 56368.03, 56370.758, 56353.68, 56363.883,
        56375.42, 56370.98, 56361.88, 56303.098, 56376.688,
        56377.9, 56373.008, 56413.66, 56422.902, 56422.414]
#  56435.1, 56432.49, 56394.55, 56367.355, 56302.8]

# the predicted stock prices for the next 10 minutes
predictions = predict_prices(data)

print("The predicted prices for the next 10 mins:")
print(predictions)