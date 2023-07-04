from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return t_statistic, p_value

s1 = [1,2,3,4,5]
s2 = [2,4,6,8,10]
t_stat, p_value = perform_hypothesis_test(s1,s2)
print("P-value is ", p_value)
print("t_statistic value is ", t_stat)
