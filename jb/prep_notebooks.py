"""Copy the solution notebooks into jb/ and prepare them for the book.

For each ../soln/NN_name.ipynb, writes NN_name.ipynb here:
- the H1 becomes the page title in TITLES (notebook 1's "# Survival Analysis"
  is too general for a page title);
- the page description goes in the notebook metadata (see GreenTeaPress plans/seo.md).

Also copies ../lamps.csv, so notebook 1 doesn't download it during the build.
"""

import shutil

import nbformat

TITLES = {
    '01_light_bulb': 'Survival and Hazard Functions',
    '02_kaplan_meier': 'Kaplan-Meier Estimation',
}

DESCRIPTIONS = {
    '01_light_bulb': "Four ways to represent a distribution of lifetimes in Python: PMF, CDF, "
                     "survival function and hazard function, using data from 50 light bulbs.",
    '02_kaplan_meier': "Kaplan-Meier estimation in Python: estimate hazard and survival functions "
                       "from incomplete data with pandas, then with the lifelines library.",
}


def prepare(name, title, description):
    nb = nbformat.read(f'../soln/{name}.ipynb', 4)

    first = nb.cells[0]
    assert first.cell_type == 'markdown' and first.source.startswith('# '), name
    heading, _, rest = first.source.partition('\n')
    first.source = f'# {title}' + ('\n' + rest if rest else '')

    nb.metadata['myst'] = {'html_meta': {'description': description}}
    nb.metadata['og:description'] = description
    nbformat.write(nb, f'{name}.ipynb')
    print(f'{name}: {title} ({len(description)} characters)')


for name in TITLES:
    prepare(name, TITLES[name], DESCRIPTIONS[name])

shutil.copy('../lamps.csv', 'lamps.csv')
