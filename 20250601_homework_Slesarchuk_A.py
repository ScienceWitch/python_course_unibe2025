import pandas as pd
from scipy.stats import shapiro

# load data
expression_df = pd.read_csv("GSE5859_ExpressionValues.csv", index_col=0)
sample_info_df = pd.read_csv("GSE5859_SampleInformation.csv")

# transpose df so samples are rows and genes are columns
expression_df_T = expression_df.T

# Add group information to the expression data
expression_df_T['group'] = sample_info_df.set_index('filename').loc[expression_df_T.index, 'group']

# Separate expression values by group
group_0 = expression_df_T[expression_df_T['group'] == 0].drop(columns='group')
group_1 = expression_df_T[expression_df_T['group'] == 1].drop(columns='group')

# Perform Shapiro-Wilk normality test on each gene in both groups
# A gene is considered normally distributed in a group if the Shapiro-Wilk test p-value is greater than 0.05
normality_results = []
for gene in group_0.columns:
    stat_0, p_0 = shapiro(group_0[gene])
    stat_1, p_1 = shapiro(group_1[gene])
    normal_0 = p_0 > 0.05
    normal_1 = p_1 > 0.05
    normality_results.append({
        'Gene': gene,
        'Group0_Normal': normal_0,
        'Group1_Normal': normal_1,
        'Group0_pvalue': p_0,
        'Group1_pvalue': p_1
    })

normality_df = pd.DataFrame(normality_results)
print(normality_df.head())

