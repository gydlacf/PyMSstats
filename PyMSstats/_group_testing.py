from scipy.stats._stats_py import (_ttest_ind_from_stats,
                                   _unequal_var_ttest_denom,
                                   Ttest_indResult)
                                   
def _average_basic(na, meana, vara,
                   nb, meanb, varb):
    """$\frac{\overline{y}_{i..} - \overline{y}_{i'..}}{\sqrt{\frac{2}{n_a} \sigma^2_a + \frac{2}{n_b} \sigma^2_b}}$"""
    df = na + nb - 2
    
    _, denom = _unequal_var_ttest_denom(vara, na,
                                        varb, nb)
                                        
    return _ttest_ind_from_stats(mean, meanb, 
                                 denom, df,
                                 alternative='two-sided')
                                 
                                 
def _fixed_basic(na, meana, vara,
                 nb, meanb, varb,
                 f):
    
    df = (f - 1) * (na + nb - 2)
    
    _, denom = _unequal_var_ttest_denom(vara, f * na,
                                        varb, f * nb)
                                        
    return _ttest_ind_from_stats(mean, meanb,
                                 denom, df,
                                 alternative='two-sided')
                                 
def _mixed_basic(na, meana, vara,
                 nb, meanb, varb):
    df = (na + nb - 2)
    
    
    
