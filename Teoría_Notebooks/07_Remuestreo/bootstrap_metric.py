# Del repositorio de Román Picó: https://github.com/RomanPico/salary_prediction

def bootstrap(y_true, y_pred, metric_fn, n_bootstrap=1000, ci=95):
    """
    Computes a confidence interval for a metric using bootstrap resampling.

    Args:
        y_true (np.array): True target values.
        y_pred (np.array): Predicted values.
        metric_fn (function): Metric function to apply (e.g., mean_absolute_error).
        n_bootstrap (int): Number of bootstrap samples.
        ci (int): Confidence interval percentage (e.g., 95).

    Returns:
        tuple: Lower and upper bounds of the confidence interval.
    """

    n = len(y_true)
    scores = []

    for _ in range(n_bootstrap):
        idx = np.random.choice(range(n), size=n, replace=True)
        score = metric_fn(y_true[idx], y_pred[idx])
        scores.append(score)

    alpha = (100 - ci) / 2
    lower = np.percentile(scores, alpha)
    upper = np.percentile(scores, 100 - alpha)

    return lower, upper
