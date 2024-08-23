import unittest
from client3 import getDataPoint,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], ((quote['top_bid']['price']+quote['top_ask']['price'])/2) ))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
       self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], ((quote['top_bid']['price']+quote['top_ask']['price'])/2) ))

    """ ------------ Add the assertion below ------------ """


  def test_getRatio(self):
      prices = [
          {"priceA": 120.2, "priceB": 212.2},
          {"priceA": 0, "priceB": 212.2},
          {"priceA": 120.2, "priceB": 0},
          {"priceA": 0, "priceB": 0},
          {"priceA": 50, "priceB": 25},
          {"priceA": -50, "priceB": 25},
          {"priceA": 50, "priceB": -25},
          {"priceA": -50, "priceB": -25},
      ]
      
      expected_ratios = [
          120.2 / 212.2,  # Normal case
          0 / 212.2,      # priceA is zero
          None,           # priceB is zero
          None,           # Both prices are zero
          50 / 25,        # Integer values
          -50 / 25,       # Negative priceA
          50 / -25,       # Negative priceB
          -50 / -25       # Both negative
      ]

      for i, price in enumerate(prices):
          price_a = price["priceA"]
          price_b = price["priceB"]
          self.assertEqual(getRatio(price_a, price_b), expected_ratios[i])


  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
