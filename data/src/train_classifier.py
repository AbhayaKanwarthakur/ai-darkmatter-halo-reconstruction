from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier
)

rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

et = ExtraTreesClassifier(
    n_estimators=200,
    random_state=42
)

gb = GradientBoostingClassifier(
    random_state=42
)
