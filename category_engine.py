import numpy as np
import pandas as pd

def yoneda_embedding(returns_df, window, threshold=0.5):
    """
    For each ETF, compute its Hom‑set vector: the number (or weight) of morphisms to every other ETF.
    A morphism exists if the absolute correlation of returns over the window exceeds threshold.
    The Yoneda embedding of an ETF is the vector of morphism strengths (correlation values) to all objects.
    Score = sum of strengths (or degree).
    """
    if len(returns_df) < window:
        return None
    recent = returns_df.iloc[-window:]
    corr = recent.corr().abs().values
    # For each ETF i, the vector of morphism strengths to all j (including self? Usually exclude self)
    n = corr.shape[0]
    scores = {}
    for i, etf in enumerate(returns_df.columns):
        # Hom‑set: edges to other ETFs with correlation > threshold
        # Use correlation as weight (or binary 1)
        # Weighted degree
        weighted_degree = np.sum(corr[i, :]) - corr[i, i]  # exclude self
        # Or use binary count
        binary_degree = np.sum(corr[i, :] > threshold) - (corr[i,i] > threshold)
        # We'll use weighted degree as score
        scores[etf] = weighted_degree
    return scores
