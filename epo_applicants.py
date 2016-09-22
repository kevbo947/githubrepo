#!/usr/bin/python3

"""store the EPO applicants CSV provided by EPO as DataFrame to be used to cross-reference SalesForce contacts"""

import pandas as pd

#path = 'C:...\epo_applicants_standard.csv'

def epo_applicants(path):

    #import CSV contents
    df = pd.read_csv(r'{0}'.format(path))

    #convert csv data to Pandas Series
    s1 = df['Standard Name;"Variation Name"']

    #split the Pandas Series into two Series
    standard    = s1.str.split(';').str.get(0).rename('standard_name')
    variant     = s1.str.split(';').str.get(1).rename('variation_name')

    #combine the 'standard' and 'variant' Pandas Series' into DataFrame
    result = pd.concat([standard, variant], axis=1)

    return result


epo_applicants = epo_applicants()

if __name__ == '__main__':
    epo_applicants