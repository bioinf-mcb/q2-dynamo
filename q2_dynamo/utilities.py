import numpy as np
import pandas as pd

from qiime2.plugin import Metadata


# TODO: optimize
def _create_normalized_aitchinson_distance_matrix(clr_df):
    X1_idx = []
    X2_idx = []
    norm_aitchison_distance = []
    for i in range(len(clr_df)):
        for j in range(len(clr_df)):
            x1 = clr_df[i]
            x2 = clr_df[j]
            dist = 0.5 * (np.std(x1 - x2) ** 2) /\
                   (np.std(x1) ** 2 + np.std(x2) ** 2)

            X1_idx.append(i)
            X2_idx.append(j)
            norm_aitchison_distance.append(dist)

    norm_aitchison_distance_df = pd.DataFrame(
        list(zip(X1_idx, X2_idx, norm_aitchison_distance)),
        columns=['x1', 'x2', 'normalized_aitchinson_distance']
    )
    norm_aitchison_distance_matrix = norm_aitchison_distance_df.\
        pivot(index='x1', columns='x2', values='normalized_aitchinson_distance')

    return norm_aitchison_distance_matrix


def _load_metadata(metadata: Metadata = None):
    if not metadata:
        raise ValueError('Metadata parameter not provided!')
    metadata = metadata.to_dataframe()
    return metadata
