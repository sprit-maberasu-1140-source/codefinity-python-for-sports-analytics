from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Hardcoded match data: features are [home_team_rank, away_team_rank, home_advantage]
X = [
    [1, 5, 1],
    [2, 8, 1],
    [3, 2, 0],
    [6, 3, 0],
    [7, 9, 1],
    [4, 1, 1],
    [8, 7, 0],
    [5, 4, 1],
    [9, 6, 0],
    [2, 3, 1]
]

# Labels: 1 = home team wins, 0 = away team wins
y = [1, 1, 0, 0, 1, 1, 0, 1, 0, 1]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model= LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)

print(accuracy)
