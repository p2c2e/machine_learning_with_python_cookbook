# Cross-validate model using macro averaged F1 score
cross_val_score(logit, features, target, scoring='f1_macro')