"""
This code is used to generate test-retest repeatability of a measurement using the intraclass 
correlation  coefficient (ICC). The UCLA repeated measures exercise dataset is used for 
demonstration. The example data is read from a CSV file and the ICC and its 95% confidence interval 
are calculated using the pingouin library.
"""
import pandas as pd
import pingouin as pg


def get_icc(df, subject_variable, measurement_variable, repetition_variable):
    """ 
    Calculate the intraclass correlation coefficient (ICC) and its 95% confidence interval for a 
    given dataset.
    """
    # compute ICC
    icc = pg.intraclass_corr(data=df,
                             targets=subject_variable,
                             raters=repetition_variable,
                             ratings=measurement_variable)
    # store 'two-way random', 'single measures', 'absolute agreement' ICC value
    value = icc.set_index('Type').loc['ICC(A,1)']['ICC'].item()
    # store ICC confidence interval
    ci = icc.set_index('Type').loc['ICC(A,1)', 'CI95']
    return value, ci


if __name__ == '__main__':

    # --- read data ---
    EXAMPLE_DATA_PATH = r'.\exer.csv'
    example_data_df = pd.read_csv(EXAMPLE_DATA_PATH)
    # obtain example data subset : (1) at rest, (2) walking leisurely or (3) running
    subset_data_df = example_data_df[example_data_df['exertype'] == 1]

    # --- variables setup ---
    # assign data-specific variables
    example_subject_variable = subset_data_df.columns.tolist()[0]
    example_measurement_variable = subset_data_df.columns.tolist()[3]
    example_repetition_variable = subset_data_df.columns.tolist()[4]

    # --- obtain repeatability ---
    icc_value, icc_ci = get_icc(subset_data_df,
                                example_subject_variable,
                                example_measurement_variable,
                                example_repetition_variable)

    # show results
    print(f"ICC(A,1): {icc_value:.3f} [95% CI: {icc_ci[0].item():.3f}, {icc_ci[1].item():.3f}]")
