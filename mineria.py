import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

def main():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df['class'] = df['target'].map({i: name for i, name in enumerate(iris.target_names)})

    print("Primeiras 5 linhas do dataset:")
    print(df.head(), "\n")

    X = df[iris.feature_names]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.3,
        random_state=42,
        stratify=y
    )

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    print("=== Matriz de Confusão ===")
    cm = confusion_matrix(y_test, y_pred)
    print(cm, "\n")

    print("=== Relatório de Classificação ===")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    sns.pairplot(df, hue='class', corner=True)
    plt.suptitle("Pairplot dos atributos do Iris", y=1.02)
    plt.show()

    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt="d",
                xticklabels=iris.target_names,
                yticklabels=iris.target_names,
                cmap="Blues")
    plt.xlabel("Predito")
    plt.ylabel("Verdadeiro")
    plt.title("Matriz de Confusão")
    plt.show()

if __name__ == "__main__":
    main()
