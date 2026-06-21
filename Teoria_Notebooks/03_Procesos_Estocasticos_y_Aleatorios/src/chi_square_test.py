# PROMPT:
# I want to write a function that performs the chi-square 
# test if a sequence of numbers is a random variable 
# of the uniform distribution

import numpy as np
from scipy.stats import chisquare

def chi_square_uniform_test(data, num_bins=10, min_val=0.0, max_val=1.0, alpha=0.05):
    """
    Performs a Chi-Square test to check if a sequence of numbers follows a Uniform(min_val, max_val) distribution.
    
    Parameters:
    - data: array-like sequence of numbers to test.
    - num_bins: int, number of bins to use for the histogram.
    - min_val: float, minimum expected value of the uniform distribution.
    - max_val: float, maximum expected value of the uniform distribution.
    - alpha: float, significance level.
    
    Returns:
    - Test statistics in a visually appealing print format.
    """
    data = np.array(data)
    
    # Filter data that falls outside the expected range
    data_in_range = data[(data >= min_val) & (data <= max_val)]
    
    if len(data_in_range) == 0:
        raise ValueError("No data points fall within the specified min_val and max_val range.")
        
    # Create the histogram (observed frequencies)
    observed_freq, _ = np.histogram(data_in_range, bins=num_bins, range=(min_val, max_val))
    
    # Calculate the expected frequency for a uniform distribution
    expected_freq = np.full(num_bins, len(data_in_range) / num_bins)
    
    # Perform the chi-square test
    stat, p_value = chisquare(f_obs=observed_freq, f_exp=expected_freq)
    
    # The null hypothesis is that the data follows the specified uniform distribution.
    # If p_value < alpha, we reject the null hypothesis.
    is_uniform = p_value >= alpha
    
    result_str = (
        f"==================================================\n"
        f"             CHI-SQUARE UNIFORMITY TEST           \n"
        f"==================================================\n"
        f" Hypothesis: Data follows Uniform({min_val}, {max_val})\n\n"
        f" Sample Size       : {len(data_in_range):,}\n"
        f" Number of Bins    : {num_bins}\n"
        f" Significance (α)  : {alpha}\n"
        f"--------------------------------------------------\n"
        f" Chi-Square Stat   : {stat:.4f}\n"
        f" P-Value           : {p_value:.4g}\n"
        f"--------------------------------------------------\n"
        f" Result            : {'PASSED ✅' if is_uniform else 'FAILED ❌'}\n"
        f"                     ({'Fail to reject' if is_uniform else 'Reject'} H0)\n"
        f"=================================================="
    )

    return result_str

if __name__ == '__main__':
    # Test with uniformly distributed data
    np.random.seed(42)
    uniform_data = np.random.uniform(0, 1, 1000)
    result_uniform = chi_square_uniform_test(uniform_data)
    print("Test with True Uniform Data:")
    print(result_uniform)
    print("-" * 40)
    
    # Test with normal distributed data
    normal_data = np.random.normal(0.5, 0.1, 1000)
    # Clip normal data between 0 and 1 so it fits the range, but clearly not uniformly distributed
    normal_data = np.clip(normal_data, 0, 1) 
    result_normal = chi_square_uniform_test(normal_data)
    print("Test with Non-Uniform (Normal) Data:")
    print(result_normal)
