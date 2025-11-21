# user 1 
- model :- Resnet 18
- Dataset Description   Found 8005 images belonging to 2 classes.
                        Found 2023 images belonging to 2 classes.
- result "accuracy": 1.0,
    "precision": 0.0,
    "recall": 0.0,
    "f1_score": 0.0,
    "train_loss_history": [
        9.438427560777214e-05,
        9.145302128926127e-05
    ]
- observation model was getting overfitting

# user 2
- model  :- Sequential with 4 layers, each integrated with . 2 dropouts
- Dataset Description :-  The train folder contains 25,000 images of dogs and cats. Each image in this folder has the label as part of the filename. The test folder contains 12,500 images, named according to a numeric id.
- result {
    "Cat": {
        "precision": 0.8819250139899273,
        "recall": 0.8405333333333334,
        "f1-score": 0.8607318405243036,
        "support": 1875.0
    },
    "Dog": {
        "precision": 0.847682119205298,
        "recall": 0.8874666666666666,
        "f1-score": 0.8671182907764461,
        "support": 1875.0
    },
    "accuracy": 0.864,
    "macro avg": {
        "precision": 0.8648035665976126,
        "recall": 0.864,
        "f1-score": 0.8639250656503749,
        "support": 3750.0
    },
    "weighted avg": {
        "precision": 0.8648035665976126,
        "recall": 0.864,
        "f1-score": 0.8639250656503747,
        "support": 3750.0
    }
}
- observation - model become better 





## Link to user 1 
https://github.com/Mudit-Sharma-30/Collaborative_cnn_team11

## Link to user 2 
https://github.com/surajcsz/Collaborative_cnn_team11
