## About project
Predicting 0 or 1 from masked data(No information is available about the variables except for data types).

## Team members
- 이정환, 김동환, 성준혁, 하희나, 이지원, 노정아

## Index
```bash
PSAT31th_Summer_Seminar_Team1

├─EDA
│  ├─NormalityTest
│  │      AndersonDarling_Test.ipynb
│  │      KolmogorovSmirnov_Test.ipynb
│  │      ShapiroWilk_Test.ipynb
│  │      
│  └─Visualization
│          Anomaly.ipynb
│          MissingValue.ipynb
│          TargetRatio.ipynb
│          tSNE.ipynb
│
├─Model
│  ├─DeepLearning
│  │  │  AutoEncoder.ipynb
│  │  │  MLP.ipynb
│  │  │  TabNetClassifier.ipynb
│  │  │  TabNetClassifier_self_pretrain.ipynb
│  │  │  
│  │  └─NeuralObliviousDecisionTree
│  ├─MachineLearning
│  │      CatBoost.ipynb
│  │      IsolationForest.ipynb
│  │      LGBMClassifier.ipynb
│  │      RandomForetClassifier.ipynb
│  │      XGBoostClassifier.ipynb
│  │      
│  └─utils
│          score.ipynb
│          seed.ipynb
│
└─Preporcessing
    ├─Augmentation
    │      OverUnder_Sampling.ipynb
    │
    ├─FeatureSelection
    │      KolmogorovSmirnov.ipynb
    │      MannWhitney.ipynb
    │      PCA.ipynb
    │      RandomForestFeatureImportance.ipynb
    │
    └─NA_Imputation
            Constant_imputation.ipynb
            Drop_MissingValue.ipynb
            KNN_Imputation.ipynb
            mice
```
