#!/usr/bin/env python3
"""Local runner for core pipeline without Colab or external APIs.

This script uses a small sample contract text, extracts entities with spaCy,
splits text into clauses, and runs a simple rule-based risk classifier.
"""
import os
import re
from dotenv import load_dotenv

load_dotenv()

try:
    import spacy
except Exception as e:
    raise SystemExit("spacy is required. Install with: pip install spacy")


SAMPLE_CONTRACT = '''
AFFILIATE AGREEMENT

1. Payment. The Company will pay the Affiliate a commission on qualifying sales. Commissions are paid monthly.

2. Termination. Either party may terminate this Agreement with 30 days' written notice.

3. Indemnification. The Affiliate shall indemnify, defend and hold harmless the Company from any claim arising out of Affiliate's conduct.

4. Liability. The Company’s liability is limited to the amount of commissions paid in the prior 12 months.

5. Confidentiality. The parties agree to keep confidential information secret.
'''


def ensure_spacy_model(name='en_core_web_sm'):
    try:
        return spacy.load(name)
    except Exception:
        print(f"Model {name} not found — downloading...")
        os.system(f"python -m spacy download {name}")
        return spacy.load(name)


def extract_legal_entities(text, nlp):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        entities.setdefault(ent.label_, set()).add(ent.text)
    return {k: sorted(list(v)) for k, v in entities.items()}


def split_into_clauses(text):
    # naive split on numbered lines
    parts = re.split(r'\n\s*(?=\d+\.)', text)
    cleaned = [p.strip() for p in parts if len(p.strip()) > 40]
    return cleaned


def classify_clause_risk(clause):
    c = clause.lower()
    if any(w in c for w in ['indemn', 'liabil', 'limitation']):
        return {'risk_level': '🔴 High Risk', 'risk_type': 'Liability / Indemnity', 'explanation': 'Clause imposes indemnity or broad liability.'}
    if any(w in c for w in ['terminate', 'notice']):
        return {'risk_level': '🟡 Caution', 'risk_type': 'Termination', 'explanation': 'Clause allows termination with little notice.'}
    return {'risk_level': '🟢 Safe', 'risk_type': 'General', 'explanation': 'No immediate risk signals found.'}


def main():
    print('🔧 Loading spaCy model...')
    nlp = ensure_spacy_model()
    print('✅ spaCy ready')

    print('\n📄 Using sample contract text (short preview):')
    print('-' * 60)
    print(SAMPLE_CONTRACT[:500])
    print('-' * 60)

    print('\n🔍 Extracting entities...')
    entities = extract_legal_entities(SAMPLE_CONTRACT, nlp)
    for label, vals in entities.items():
        print(f"{label}: {vals}")

    print('\n✂️  Splitting into clauses...')
    clauses = split_into_clauses(SAMPLE_CONTRACT)
    for i, cl in enumerate(clauses, 1):
        print(f"\n--- Clause {i} ---")
        print(cl[:300])
        res = classify_clause_risk(cl)
        print(f"Risk: {res['risk_level']} | Type: {res['risk_type']}")
        print(f"Explanation: {res['explanation']}")

    print('\n✅ Local run complete!')


if __name__ == '__main__':
    main()
