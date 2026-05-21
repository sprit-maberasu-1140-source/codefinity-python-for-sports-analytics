from scipy import stats

def compare_player_scores(team_a_scores, team_b_scores):
    t_statistic, p_value = stats.ttest_ind(team_a_scores, team_b_scores)
    if p_value < 0.05:
        interpretation = "There is a statistically significant difference between the two teams' scores."
    else:
        interpretation = "There is no statistically significant difference between the two teams' scores."
    return t_statistic, p_value, interpretation

team_a_scores = [15, 18, 21, 17, 19, 20, 16, 18, 22, 20]
team_b_scores = [12, 14, 15, 13, 16, 15, 14, 13, 16, 15]

result = compare_player_scores(team_a_scores, team_b_scores)
print(result)