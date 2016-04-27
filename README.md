# Tinydeck ♠ <font color='red'>♥ ♦</font> ♣

A tiny library for dealing playing cards in Python.

## Usage

```python
# First things first
import tinydeck
```

```python
# Vanilla 52-card deck generator.
# The order is randomized.
deck = tinydeck.deal()
```

```python
# Deal hand of size 2
hand = tinydeck.deal(source=deck, limit=2)
```