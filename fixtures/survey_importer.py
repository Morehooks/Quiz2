import os
import pandas as pd
import numpy as np
import tablib
from import_export import resources
from quiz_site2.models import Section, Page, SubPage, Question, Response


# section
survey_builder_df = pd.read_excel(os.path.join(os.getcwd(), 'survey_builder.xls'))
section_df = survey_builder_df[['section_seq', 'section_text']]
section_df = section_df.drop_duplicates()
section_df['id'] = np.arange(1, len(section_df) + 1)

# page
page_df = survey_builder_df[['section_seq', 'page_seq', 'page_header']]
page_df = page_df.drop_duplicates()
page_df['page_id'] = np.arange(1, len(page_df) + 1)
page_df = pd.merge(page_df, section_df, on='section_seq')
page_df = page_df.rename(columns={'id': 'section', 'page_id': 'id'})
page_df = page_df[['id', 'page_seq', 'page_header', 'section']]

# sub page
sub_page_df = survey_builder_df[['page_seq', 'sub_page_seq', 'sub_page_header']]
sub_page_df = sub_page_df.drop_duplicates()
sub_page_df['sub_page_id'] = np.arange(1, len(sub_page_df) + 1)
sub_page_df = pd.merge(sub_page_df, page_df, on='page_seq')
sub_page_df = sub_page_df.rename(columns={'id': 'page', 'sub_page_id': 'id'})
sub_page_df = sub_page_df[['id', 'sub_page_seq', 'sub_page_header', 'page']]

# question
question_df = survey_builder_df[['question_seq', 'question_text', 'question_type', 'sub_question', 'sub_page_seq']]
# dropping duplicates apart from multi choice, might be better to split and combine
question_df[question_df.question_type != 'Multi Choice Question'] = \
    question_df[question_df.question_type != 'Multi Choice Question'].drop_duplicates()
question_df = question_df.dropna()
question_df[['question_seq', 'sub_page_seq']] = question_df[['question_seq', 'sub_page_seq']].astype(int)
question_df['question_id'] = np.arange(1, len(question_df) + 1)
question_df = pd.merge(question_df, sub_page_df, on='sub_page_seq')
question_df = question_df.rename(columns={'id': 'sub_page', 'question_id': 'id'})
question_df = question_df[['id', 'question_seq', 'question_text', 'question_type', 'sub_question', 'sub_page_seq']]

# response
response_df = survey_builder_df[['response_seq', 'response_text', 'response_value', 'response_ops',
                                 'response_columns', 'question_seq']]
response_df = response_df.dropna()
response_df[['response_seq', 'response_value', 'response_columns', 'question_seq']] = \
    response_df[['response_seq', 'response_value', 'response_columns', 'question_seq']].astype(int)
response_df['response_id'] = np.arange(1, len(response_df) + 1)
response_df = pd.merge(response_df, question_df, on='question_seq')
response_df = response_df.rename(columns={'id': 'question', 'response_id': 'id'})
response_df = response_df[['id', 'response_seq', 'response_text', 'response_value', 'response_ops',
                           'response_columns', 'question']]
print(response_df.head())

section_resource = resources.modelresource_factory(model=Section)()
