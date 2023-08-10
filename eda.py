from pathlib import Path
from typing import Literal

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_style("white")
sns.set_palette("Set2")

def plot_labels_value_counts(
    df: pd.DataFrame,
    statement_classes: list,
    version: str,
):
    """Plots the classes count when given data is in one hot encoding format.

        Description: Given a multi-class text classification problem when labels are
        present in one hot encoding format
        eg. |label1 | label2 | label3|
            |   1   |     0  |   0   |
            |   0   |     1  |   1   |
            |   0   |     1  |   1   |
            |   0   |     0  |   0   |
        Plots the value counts for all the labels in data to understand the class
        imbalance issues
    Args:
        df (pd.DataFrame): Dataframe with one hot encoding label data
        statement_classes (list): List of labels which are also column names in df
        version (str): Version of class distribution data for image and csv


    """
    # Dataframe for storing label value counts
    df_label = pd.DataFrame(columns=["label", "label_count"])
    for label in statement_classes:
        # Groupby each label into 2 group of 0s and 1s.
        #  Count only group 1 for each # label,
        # ie. length(all data)- length od group 0
        label_count = len(df) - df.groupby(label).size()[0]
        row = {
            "label": label,
            "label_count": label_count,
        }
        df_label.loc[label] = row

    # Plot class distribution
    fig, ax = plt.subplots(
        figsize=(6, 6),
        tight_layout=True,
    )
    sns.barplot(
        data=df_label,
        x="label",
        y="label_count",
        ax=ax,
    )
    ax.set(
        title="Number of classes in Storage Statement",
        xlabel="Classes",
        ylabel="Samples No.",
    )

    ax.tick_params(axis="x", rotation=90)

    fig.savefig(
        Path(
            "statement",
            "develop",
            "eda",
            f"statement_distribution_{version}.png",
        )
    )

    df_label.to_csv(
        Path(
            "statement",
            "develop",
            "eda",
            f"statement_distribution_{version}.csv",
        ),
        index=False,
    )

def updated_plot_labels(df:pd.DataFrame,cols:list[str):
    fig, ax = plt.subplots(
    figsize=(6, 6),
    tight_layout=True,
    )
    
    data = df[cols].apply(sum)
    
    sns.barplot(x = data.index,y = data.values)
    
    ax.set(
        xlabel="Labels",
        ylabel="Samples No.",
    )
    
    ax.tick_params(axis="x", rotation=90)
     fig.savefig(
        Path(
            "statement",
            "develop",
            "eda",
            f"statement_distribution_{version}.png",
        )
    )

    df_label.to_csv(
        Path(
            "statement",
            "develop",
            "eda",
            f"statement_distribution_{version}.csv",
        ),
        index=False,
    )
        
