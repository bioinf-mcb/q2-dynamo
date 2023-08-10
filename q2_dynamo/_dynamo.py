# -----------------------------------------------------------------------------
# Copyright (c) 2023, Bioinformatics at Małopolska Centre of Biotechnology
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------


import qiime2
import pandas as pd

from skbio.stats import composition
from q2_types.feature_table import FeatureTable, Frequency
from q2_dynamo.utilities import (_create_normalized_aitchinson_distance_matrix,
                                 _load_metadata)
from q2_diversity import pcoa
from q2_types.ordination import PCoAResults

PSEUDOCOUNT = 1


def longitudinal_dimred(ctx,
                        table=None,
                        n_dim=2,
                        metadata=None):

    assert table.type == FeatureTable[Frequency]
    # Load metadata and convert to Qiime2 type
    metadata_df = _load_metadata(metadata)
    metadata_df = qiime2.Metadata(metadata_df)
    # Transform input to Pandas dataframe
    table_df = table.view(pd.DataFrame)
    # Perform centered log ratio transformation
    table_df = composition.clr(table_df + PSEUDOCOUNT)
    # Create normalized distance matrix
    dm = _create_normalized_aitchinson_distance_matrix(table_df)
    # Perform principal value decomposition
    pcoa_results = pcoa(dm.values, number_of_dimensions=n_dim)
    pcoa_results = ctx.make_artifact(PCoAResults, pcoa_results)
    # Create PCoA plot
    make_plot = ctx.get_action('emperor', 'plot')
    pcoa_viz = make_plot(pcoa_results, metadata_df)
    return pcoa_results, pcoa_viz[0]

