# Q8 — Bigram Language Model Implementation

This program trains a simple bigram language model on a small corpus and computes
sentence probabilities using maximum likelihood estimation (MLE).

## Objective
Implement a Python script that:
1. Reads the training corpus.
2. Computes unigram and bigram counts.
3. Estimates bigram probabilities with MLE:
   P(w_i | w_{i-1}) = Count(w_{i-1}, w_i) / sum_{w'} Count(w_{i-1}, w').
4. Provides a function to calculate the probability of any given sentence.
5. Tests this function on two example sentences and reports which one the model prefers.

## Training Corpus
```
<s> I love NLP </s>
<s> I love deep learning </s>
<s> deep learning is fun </s>
```

## Implementation Overview
The Python script `Q8_bigram_model.py`:
- Tokenizes each sentence into words including start `<s>` and end `</s>` tokens.
- Counts unigrams and bigrams across the corpus.
- Computes P(w_i | w_{i-1}) = Count(w_{i-1}, w_i) / sum_{w'} Count(w_{i-1}, w').
- Defines `prob_sentence(sentence)` to compute the probability of a full sentence.

## Example Computation
Two test sentences:
1. `<s> I love NLP </s>`
2. `<s> I love deep learning </s>`

MLE bigram probabilities yield:
- P(S1) = (2/3) * 1 * (1/2) * 1 = **1/3 ≈ 0.333**
- P(S2) = (2/3) * 1 * (1/2) * 1 * (1/2) = **1/6 ≈ 0.167**

The model therefore **prefers S1** because it requires fewer low-probability transitions.

## Running the Script
From the project root directory:
```bash
python Q8_bigram_model.py
```

Expected output:
```
P(S1)=0.333333   <s> I love NLP </s>
P(S2)=0.166667   <s> I love deep learning </s>
Model prefers S1 because P(NLP | love) = 1/2 while P(</s> | learning) = 1/2 introduces an extra factor.
```

This satisfies the third programming question of Q8 and provides clear reproducible results.
