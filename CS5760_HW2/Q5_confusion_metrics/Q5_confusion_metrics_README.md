# Q5 — Programming Implementation: Multi-Class Metrics

This program computes evaluation metrics from a multi-class confusion matrix.

## Objective
Implement a Python script that:
1. Accepts the given confusion matrix as input.
2. Computes **per-class precision and recall**.
3. Computes **macro-averaged** and **micro-averaged** precision and recall.
4. Prints all results in a clear, readable format.

## Confusion Matrix
The system classified 90 animals into three classes:

| System \ Gold | Cat | Dog | Rabbit |
|--------------:|----:|----:|------:|
| **Cat**       | 5   | 10  | 5     |
| **Dog**       | 15  | 20  | 10    |
| **Rabbit**    | 0   | 15  | 10    |

Rows represent system predictions and columns represent the gold (true) labels.

## Implementation Overview
The Python script `Q5_confusion_metrics.py`:
- Stores the matrix and class labels.
- Calculates **true positives (TP)**, **false positives (FP)**, and **false negatives (FN)** for each class.
- Computes precision, recall, and F1-score for every class using:
  ```
  Precision = TP / (TP + FP)
  Recall    = TP / (TP + FN)
  F1        = 2 * Precision * Recall / (Precision + Recall)
  ```
- Aggregates macro-averaged metrics (simple average across classes).
- Aggregates micro-averaged metrics (pooling all predictions and computing global TP, FP, FN).
- Prints the results with three decimals for clarity.

## Running the Script
From the project root directory:
```bash
python Q5_confusion_metrics.py
```

Example output:
```
Per-class metrics:
  Cat     P=0.250  R=0.250  F1=0.250
  Dog     P=0.444  R=0.444  F1=0.444
  Rabbit  P=0.400  R=0.400  F1=0.400
Macro   : P=0.365  R=0.365  F1=0.365
Micro   : P=0.389  R=0.389  F1=0.389
Accuracy: 0.389
```

These results match the manual calculations and meet the requirements for the third sub-question of Q5.
