import pandas as pd

try:
    import seaborn as sns
except ImportError:
    sns = None

import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add overweight column
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)

# Normalize cholesterol and gluc
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


def draw_cat_plot():
    # Melt data
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Create catplot (use seaborn if available, otherwise matplotlib fallback)
    if sns is not None:
        fig = sns.catplot(x="variable", y="total", hue="value", col="cardio",
                          data=df_cat, kind="bar").fig
    else:
        # Fallback plotting with matplotlib
        fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
        for i, ax in enumerate(axes.flatten()):
            part = df_cat[df_cat['cardio'] == i]
            pivot = part.pivot(index='variable', columns='value', values='total').fillna(0)
            pivot.plot(kind='bar', stacked=False, ax=ax)
            ax.set_title(f'cardio={i}')
            ax.set_xlabel('variable')
            ax.set_ylabel('total')
        fig.tight_layout()

    return fig


# Heat Map
def draw_heat_map():
    # Clean data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate correlation matrix
    corr = df_heat
    