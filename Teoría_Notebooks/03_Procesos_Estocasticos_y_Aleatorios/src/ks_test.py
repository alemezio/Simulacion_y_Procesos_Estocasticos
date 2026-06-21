# PROMPT:
# Similarly to the recent chi-square function,
# now I want to write a function that performs
# the kolmogorov-smirnov test if a sequence of
# numbers is a random variable of the uniform distribution

import numpy as np
from scipy.stats import kstest

def kolmogorov_smirnov_uniform_test(data, min_val=0.0, max_val=1.0, alpha=0.05):
    """
    Performs a Kolmogorov-Smirnov test to check if a sequence of numbers 
    follows a Uniform(min_val, max_val) distribution.
    
    Parameters:
    - data: array-like sequence of numbers to test.
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
        
    # The uniform distribution expected in scipy stats takes loc and scale parameters:
    # loc = min_val, scale = max_val - min_val
    loc = min_val
    scale = max_val - min_val
    
    # Perform the Kolmogorov-Smirnov test against a uniform distribution
    stat, p_value = kstest(data_in_range, 'uniform', args=(loc, scale))
    
    # The null hypothesis is that the data follows the specified uniform distribution.
    # If p_value < alpha, we reject the null hypothesis.
    is_uniform = p_value >= alpha
    
    # Create a visually appealing formatted summary
    result_str = (
        f"==================================================\n"
        f"          KOLMOGOROV-SMIRNOV UNIFORMITY TEST      \n"
        f"==================================================\n"
        f" Hypothesis: Data follows Uniform({min_val}, {max_val})\n\n"
        f" Sample Size       : {len(data_in_range):,}\n"
        f" Significance (α)  : {alpha}\n"
        f"--------------------------------------------------\n"
        f" K-S Statistic     : {stat:.4f}\n"
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
    result_uniform = kolmogorov_smirnov_uniform_test(uniform_data)
    print("Test with True Uniform Data:")
    print(result_uniform)
    print()
    
    # Test with normal distributed data
    normal_data = np.random.normal(0.5, 0.1, 1000)
    # Clip normal data between 0 and 1 so it fits the range
    normal_data = np.clip(normal_data, 0, 1) 
    result_normal = kolmogorov_smirnov_uniform_test(normal_data)
    print("Test with Non-Uniform (Normal) Data:")
    print(result_normal)
