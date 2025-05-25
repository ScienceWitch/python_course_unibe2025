import pandas as pd
from lifelines import CoxPHFitter
from scipy.stats import spearmanr
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# load dataset
animal_exp = pd.read_csv("animal_experiment_biomarkers.txt")
print(animal_exp.head())
print()
animal_exp['E'] = animal_exp['Death'].notna().astype(int)
animal_exp['T'] = animal_exp['Death']  # Or use 'Last follow-up' if needed

# identify biomarker columns
biomarker_cols = [col for col in animal_exp.columns if col.startswith('M')]

results = []

# analyze each biomarker
for col in biomarker_cols:
    data = animal_exp[['T', 'E', col]].dropna()
    if data[col].nunique() <= 1:
        continue

    # Cox model
    cph = CoxPHFitter()
    cph.fit(data, duration_col='T', event_col='E')
    hr = cph.hazard_ratios_[col]
    p_val = cph.summary.loc[col, 'p']

    # Spearman correlation
    corr, _ = spearmanr(data['T'], data[col])

    results.append({
        'biomarker': col,
        'log_hazard_ratio': np.log(hr),
        'spearman_corr': corr,
        'abs_corr': abs(corr),
        'cox_p': p_val
    })

# Create DataFrame with results
results_animal_exp = pd.DataFrame(results)
print(results_animal_exp.head())
# top 10 biomarkers by correlation
top = results_animal_exp.sort_values('abs_corr', ascending=False).head(10)
heatmap_data = top.set_index('biomarker')[['log_hazard_ratio', 'spearman_corr']]

# plot correlation eatmap
plt.figure(figsize=(8, len(heatmap_data) * 0.5 + 2))
sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="vlag", center=0, linewidths=0.5)
plt.title("Top Biomarkers Associated with Survival")
plt.tight_layout()
plt.show()