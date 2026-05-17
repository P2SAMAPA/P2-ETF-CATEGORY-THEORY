# Category Theory Portfolio Engine

Applies categorical concepts to ETF ranking: objects = ETFs, morphisms = rebalancing operations (correlation > threshold). The Yoneda embedding represents each ETF by its Hom‑set of relationships to all others. The weighted degree (sum of correlation strengths) is the Yoneda score – a centrality measure. Higher score = more central = stronger signal.

- **Windows:** 63, 252, 504, 1008, 2016 days (best per ETF)
- **Morphism threshold:** |corr| > 0.5
- **Score:** weighted degree (sum of absolute correlations)
- **Output:** top 3 ETFs per universe by Yoneda score

Runs daily on GitHub Actions.

## Local execution

```bash
pip install -r requirements.txt
export HF_TOKEN=<your_token>
python trainer.py
streamlit run streamlit_app.py
