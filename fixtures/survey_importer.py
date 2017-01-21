import os
import pandas as pd
import numpy as np

survey_builder_df = pd.read_excel(os.path.join(os.getcwd(), 'survey_builder.xls'))
section_df = survey_builder_df[['section_seq', 'section_text']]
section_df = section_df.drop_duplicates()
section_df['id'] = np.arange(1, len(section_df) + 1)

page_df = survey_builder_df[['section_seq', 'page_seq', 'page_header']]
page_df = page_df.drop_duplicates()
page_df['page_id'] = np.arange(1, len(page_df) + 1)
page_df = pd.merge(page_df, section_df, on='section_seq')
page_df = page_df.drop('section_text', axis=1)
page_df = page_df.rename(columns={'id': 'section', 'page_id': 'id'})
page_df = page_df[['id', 'page_seq', 'page_header', 'section']]
print(page_df)
