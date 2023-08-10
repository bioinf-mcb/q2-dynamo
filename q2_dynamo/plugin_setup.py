# -----------------------------------------------------------------------------
# Copyright (c) 2023, Bioinformatics at Małopolska Centre of Biotechnology
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

import q2_dynamo

from q2_dynamo._dynamo import longitudinal_dimred
from qiime2.plugin import Int, Plugin, Citations, Metadata, Visualization
from q2_types.feature_table import FeatureTable, Frequency, RelativeFrequency
from q2_types.ordination import PCoAResults


plugin = Plugin(
    name='dynamo',
    version=q2_dynamo.__version__,
    website="https://github.com/bioinf-mcb/q2-dynamo",
    package='q2_dynamo',
    # citations=Citations.load('citations.bib', package='q2_dynamo'),
    description='Analyze longitudinal data',
    short_description='Analyze longitudinal data',
)


plugin.pipelines.register_function(
    function=longitudinal_dimred,
    inputs={'table': FeatureTable[Frequency | RelativeFrequency]},
    parameters={
        'n_dim': Int,
        'metadata': Metadata,
    },
    outputs=[
        ('pca_results', PCoAResults),
        ('pca_plot', Visualization)
    ],
    input_descriptions={'table': 'Featue table with features as columns '
                                 'and samples as rows.'},
    parameter_descriptions={
        'n_dim': 'Number of PCA components.',
        'metadata': 'Metadata used for visualization [REQUIRED].',
    },
    output_descriptions={
        'pca_results': 'Table containing PCA components joined with metadata.',
        'pca_plot': 'Scatter plot of principal components.',
    },
    name='Compositional PCA',
    description='Perform PCA dimensionality reduction on normalized '
         'Aitchinson distance.',
)
