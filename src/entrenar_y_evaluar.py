"""Entrenamiento, evaluacion y visualizacion del modelo de Churn (Telco).

Reutiliza la logica del cuaderno modelo_churn_telco.ipynb (TP2 Desarrollo de IA)
y genera las figuras en alta resolucion en la carpeta assets/ para la
documentacion en GitHub y la presentacion final de Practicas Profesionalizantes I.
"""

import os
from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - dependencia opcional
    load_dotenv = None


BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

COLUMNAS_SELECCIONADAS = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "Contract",
    "InternetService",
    "TechSupport",
    "OnlineSecurity",
    "PaymentMethod",
    "SeniorCitizen",
    "Partner",
    "Dependents",
]

ETIQUETAS_VARIABLES = {
    "Contract_Two year": "Contrato: 2 años",
    "Contract_One year": "Contrato: 1 año",
    "tenure": "Antigüedad (meses)",
    "InternetService_Fiber optic": "Internet: Fibra óptica",
    "InternetService_No": "Internet: Sin servicio",
    "MonthlyCharges": "Cargo mensual ($)",
    "TotalCharges": "Cargo total ($)",
    "PaymentMethod_Electronic check": "Pago: Cheque electrónico",
    "OnlineSecurity_Yes": "Seguridad online: Sí",
    "TechSupport_Yes": "Soporte técnico: Sí",
}


def cargar_configuracion() -> tuple[Path, int, int, float]:
    """Lee configuracion desde variables de entorno sin exponer secretos."""
    if load_dotenv is not None:
        load_dotenv(BASE_DIR / ".env")
    dataset_rel = os.getenv("DATASET_PATH", "data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    max_depth = int(os.getenv("MODEL_MAX_DEPTH", "4"))
    seed = int(os.getenv("RANDOM_SEED", "42"))
    test_size = float(os.getenv("TEST_SIZE", "0.2"))
    return BASE_DIR / dataset_rel, max_depth, seed, test_size


def cargar_y_preparar_datos(ruta_csv: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series]:
    """Carga el dataset original, limpia TotalCharges y aplica One-Hot Encoding."""
    df = pd.read_csv(ruta_csv)
    datos = df[COLUMNAS_SELECCIONADAS + ["Churn"]].copy()
    datos["TotalCharges"] = pd.to_numeric(datos["TotalCharges"], errors="coerce")
    nulos_tc = int(datos["TotalCharges"].isnull().sum())
    datos["TotalCharges"] = datos["TotalCharges"].fillna(0.0)

    X = pd.get_dummies(datos[COLUMNAS_SELECCIONADAS], drop_first=True)
    y = datos["Churn"].map({"No": 0, "Yes": 1})
    print(f"Dataset: {len(df)} filas, {df.shape[1]} columnas iniciales | Nulos TotalCharges={nulos_tc}")
    print(f"Matriz preparada: X={X.shape}, y={y.shape}")
    return df, X, y


def entrenar_modelo(
    X: pd.DataFrame,
    y: pd.Series,
    max_depth: int,
    seed: int,
    test_size: float,
) -> tuple[DecisionTreeClassifier, np.ndarray, pd.Series, np.ndarray, pd.Series]:
    """Divide 80/20 estratificado y entrena el Arbol de Decision."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=seed
    )
    modelo = DecisionTreeClassifier(criterion="gini", max_depth=max_depth, random_state=seed)
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    return modelo, X_train, y_train, y_pred, y_test


def generar_grafico_eda(df: pd.DataFrame, salida: Path) -> None:
    """Genera el grafico doble de distribucion de Churn y tasa por contrato."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.8), dpi=180)
    fig.patch.set_facecolor("#FFFFFF")

    conteos = df["Churn"].value_counts().reindex(["No", "Yes"])
    tot = len(df)
    colores_1 = ["#1B4F72", "#D9534F"]
    barras1 = ax1.bar(["Permaneció (No)", "Abandonó (Yes)"], conteos.values, color=colores_1, width=0.55)
    ax1.set_title("Distribución General de Abandono (n = 7.043)", fontsize=13, fontweight="bold", color="#0D233A", pad=12)
    ax1.set_ylabel("Cantidad de clientes", fontsize=11, color="#0D233A")
    ax1.set_ylim(0, max(conteos.values) * 1.18)
    ax1.spines[["top", "right"]].set_visible(False)
    for barra, val in zip(barras1, conteos.values):
        pct = (val / tot) * 100
        val_txt = f"{val:,}".replace(",", ".")
        pct_txt = f"{pct:.2f}%".replace(".", ",")
        ax1.text(
            barra.get_x() + barra.get_width() / 2,
            val + 110,
            f"{val_txt}\n({pct_txt})",
            ha="center",
            va="bottom",
            fontsize=10.5,
            fontweight="bold",
            color="#0D233A",
        )

    orden_contrato = ["Month-to-month", "One year", "Two year"]
    etiquetas_es = ["Mes a mes", "1 año", "2 años"]
    tasa = (
        df.assign(churn_bin=(df["Churn"] == "Yes").astype(int))
        .groupby("Contract")["churn_bin"]
        .mean()
        .reindex(orden_contrato)
        * 100
    )
    for c, v in tasa.items():
        print(f"Tasa Churn [{c}]: {v:.2f}%")

    colores_2 = ["#D9534F", "#2E86C1", "#1B4F72"]
    barras2 = ax2.bar(etiquetas_es, tasa.values, color=colores_2, width=0.55)
    ax2.set_title("Tasa de Abandono por Tipo de Contrato", fontsize=13, fontweight="bold", color="#0D233A", pad=12)
    ax2.set_ylabel("Tasa de abandono (%)", fontsize=11, color="#0D233A")
    ax2.set_ylim(0, 52)
    ax2.spines[["top", "right"]].set_visible(False)
    for barra, val in zip(barras2, tasa.values):
        ax2.text(
            barra.get_x() + barra.get_width() / 2,
            val + 1.2,
            f"{val:.2f}%".replace(".", ","),
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
            color="#0D233A",
        )

    plt.tight_layout(pad=2.0)
    plt.savefig(salida, dpi=180, bbox_inches="tight")
    plt.close(fig)


def generar_grafico_modelo(
    modelo: DecisionTreeClassifier,
    columnas: pd.Index,
    cm: np.ndarray,
    exactitud: float,
    salida: Path,
) -> None:
    """Genera el grafico doble con Matriz de Confusion e Importancia de Variables."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 4.9), dpi=180)
    fig.patch.set_facecolor("#FFFFFF")

    im = ax1.imshow(cm, cmap="Blues")
    ax1.set_title(
        f"Matriz de Confusión (Exactitud: {exactitud * 100:.2f}%)".replace(".", ","),
        fontsize=13,
        fontweight="bold",
        color="#0D233A",
        pad=12,
    )
    ax1.set_xticks([0, 1])
    ax1.set_yticks([0, 1])
    ax1.set_xticklabels(["Predicho: No (0)", "Predicho: Sí (1)"], fontsize=10.5)
    ax1.set_yticklabels(["Real: No (0)", "Real: Sí (1)"], fontsize=10.5)
    ax1.set_xlabel("Predicción del modelo", fontsize=11, color="#0D233A")
    ax1.set_ylabel("Valor real en prueba (n = 1.409)", fontsize=11, color="#0D233A")

    nombres_celda = [["VN", "FP"], ["FN", "VP"]]
    umbral = cm.max() / 2
    for i in range(2):
        for j in range(2):
            color_txt = "#FFFFFF" if cm[i, j] > umbral else "#0D233A"
            ax1.text(
                j,
                i,
                f"{cm[i, j]}\n({nombres_celda[i][j]})",
                ha="center",
                va="center",
                fontsize=12,
                fontweight="bold",
                color=color_txt,
            )
    fig.colorbar(im, ax=ax1, fraction=0.046, pad=0.04)

    importancias = (
        pd.Series(modelo.feature_importances_, index=columnas)
        .sort_values(ascending=False)
    )
    top5 = importancias[importancias > 0].head(6)[::-1]
    print("Importancias principales:")
    for feat, imp in importancias[importancias > 0].items():
        print(f"  - {feat}: {imp:.4f}")

    etiquetas = [ETIQUETAS_VARIABLES.get(f, f) for f in top5.index]
    barras = ax2.barh(etiquetas, top5.values * 100, color="#1E88E5", height=0.58)
    ax2.set_title("Factores Más Influyentes en el Árbol (Gini)", fontsize=13, fontweight="bold", color="#0D233A", pad=12)
    ax2.set_xlabel("Importancia relativa (%)", fontsize=11, color="#0D233A")
    ax2.set_xlim(0, max(top5.values * 100) * 1.24)
    ax2.spines[["top", "right"]].set_visible(False)
    for barra, val in zip(barras, top5.values * 100):
        ax2.text(
            val + 0.8,
            barra.get_y() + barra.get_height() / 2,
            f"{val:.1f}%".replace(".", ","),
            va="center",
            fontsize=10.5,
            fontweight="bold",
            color="#0D233A",
        )

    plt.tight_layout(pad=2.0)
    plt.savefig(salida, dpi=180, bbox_inches="tight")
    plt.close(fig)


def generar_grafico_trello(salida: Path) -> None:
    """Dibuja una maqueta visual clara del tablero Trello de 4 columnas."""
    fig, ax = plt.subplots(figsize=(14.5, 6.8), dpi=180)
    fig.patch.set_facecolor("#0D3B66")
    ax.set_facecolor("#0D3B66")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    ax.text(
        2.0,
        94.5,
        "Tablero Ágil en Trello — Predicción de Abandono (Telco Churn IA) | Scrum Master: Ezequiel Quiroga",
        fontsize=13.5,
        fontweight="bold",
        color="#FFFFFF",
        va="center",
    )

    columnas = [
        {
            "titulo": "1. Lista de Tareas\n(Backlog)",
            "tarjetas": [
                ("[HU-09] Despliegue API\nde alertas CRM", "#8E44AD", "Sprint 3 | PO + Dev", "0/3"),
                ("[HU-10] Monitoreo de\nderiva de datos", "#7F8C8D", "Mejora futura", "0/2"),
            ],
        },
        {
            "titulo": "2. En proceso\n",
            "tarjetas": [
                ("[HU-08] Ensayo oral\n(guion 10 minutos)", "#2980B9", "Sprint 3 | Ezequiel Q.", "2/3"),
                ("[HU-07] Ajuste final\ndiapositivas 10-20-30", "#E67E22", "Sprint 3 | BI Analyst", "3/4"),
            ],
        },
        {
            "titulo": "3. Por verificar\ncon el Cliente",
            "tarjetas": [
                ("[HU-05] Informe breve\nde ética y sesgos", "#16A085", "Sprint 3 | Revisión PO", "4/4"),
                ("[HU-06] README HTML\ny repositorio GitHub", "#27AE60", "Sprint 3 | Revisión PO", "4/4"),
            ],
        },
        {
            "titulo": "4. Hecho\n",
            "tarjetas": [
                ("[HU-01] Problema y\nroles Scrum simulados", "#27AE60", "Sprint 1 | Equipo", "3/3"),
                ("[HU-02] Limpieza datos\nTotalCharges y EDA", "#27AE60", "Sprint 1 | Data Eng.", "4/4"),
                ("[HU-03] One-Hot Encoding\ny partición 80/20", "#27AE60", "Sprint 2 | Data Sci.", "3/3"),
                ("[HU-04] Árbol Gini\nmax_depth=4 (79,56%)", "#27AE60", "Sprint 2 | Data Sci.", "5/5"),
            ],
        },
    ]

    ancho_col = 22.8
    separacion = 1.6
    x_ini = 2.0

    for idx, col in enumerate(columnas):
        x = x_ini + idx * (ancho_col + separacion)
        fondo_col = patches.FancyBboxPatch(
            (x, 4),
            ancho_col,
            85.5,
            boxstyle="round,pad=0.6,rounding_size=1.4",
            facecolor="#EBECF0",
            edgecolor="none",
        )
        ax.add_patch(fondo_col)
        ax.text(
            x + 1.0,
            84.8,
            col["titulo"].strip(),
            fontsize=10.2,
            fontweight="bold",
            color="#172B4D",
            va="center",
            linespacing=1.15,
        )

        y_top = 77.5
        alto_tarjeta = 16.5
        for titulo, color_etq, meta, chk in col["tarjetas"]:
            tarjeta = patches.FancyBboxPatch(
                (x + 0.9, y_top - alto_tarjeta),
                ancho_col - 1.8,
                alto_tarjeta - 1.3,
                boxstyle="round,pad=0.35,rounding_size=1.0",
                facecolor="#FFFFFF",
                edgecolor="#D0D7DE",
                linewidth=0.8,
            )
            ax.add_patch(tarjeta)
            barra_etq = patches.FancyBboxPatch(
                (x + 1.6, y_top - 3.3),
                6.2,
                1.4,
                boxstyle="round,pad=0.1,rounding_size=0.5",
                facecolor=color_etq,
                edgecolor="none",
            )
            ax.add_patch(barra_etq)
            ax.text(
                x + 1.6,
                y_top - 8.1,
                titulo,
                fontsize=8.3,
                fontweight="bold",
                color="#172B4D",
                va="center",
                linespacing=1.2,
            )
            ax.text(x + 1.6, y_top - 13.5, f"{meta} | {chk}", fontsize=7.5, color="#5E6C84", va="center")
            y_top -= alto_tarjeta + 1.2

    plt.savefig(salida, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def main() -> None:
    """Ejecuta el flujo completo de datos, modelo y generacion de graficos."""
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    ruta_csv, max_depth, seed, test_size = cargar_configuracion()
    df, X, y = cargar_y_preparar_datos(ruta_csv)
    modelo, X_train, y_train, y_pred, y_test = entrenar_modelo(X, y, max_depth, seed, test_size)

    exactitud = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    print(f"Train={len(X_train)} | Test={len(y_test)}")
    print(f"Exactitud (Accuracy): {exactitud * 100:.2f}%")
    print(f"Matriz Confusion -> VN={cm[0,0]}, FP={cm[0,1]}, FN={cm[1,0]}, VP={cm[1,1]}")
    print(classification_report(y_test, y_pred, target_names=["No (0)", "Yes (1)"], digits=4))

    generar_grafico_eda(df, ASSETS_DIR / "01_distribucion_churn.png")
    generar_grafico_modelo(modelo, X.columns, cm, exactitud, ASSETS_DIR / "02_matriz_confusion_metricas.png")
    generar_grafico_trello(ASSETS_DIR / "03_tablero_trello_simulacion.png")
    print("Graficos guardados correctamente en assets/.")


if __name__ == "__main__":
    main()
