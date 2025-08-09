from abc import abstractmethod, ABC


class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"


class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"


class CryptoPayment(PaymentStrategy):
    def process_payment(self, amount):
        return f"Processing ${amount} via Cryptocurrency"


class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process(self, amount):
        return self._strategy.process_payment(amount)


# Usage - can switch strategies at runtime
processor = PaymentProcessor(CreditCardPayment())
result1 = processor.process(100)

processor.set_strategy(PayPalPayment())
result2 = processor.process(150)
