# -----------------------------------------------------------------------------
# Copyright (c) 2023, Bioinformatics at Małopolska Centre of Biotechnology
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from setuptools import setup, find_packages
import versioneer

setup(
    name="q2-dynamo",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    author="Zuzanna Karwowska",
    author_email="zuzanna.karwowska@doctoral.uj.edu.pl",
    description="Analyze longitudinal data",
    license='BSD-3-Clause',
    url="https://github.com/bioinf-mcb/q2-dynamo",
    entry_points={
        'qiime2.plugins':
        ['q2-dynamo=q2_dynamo.plugin_setup:plugin']
    },
    package_data={
    },
    zip_safe=False,
)