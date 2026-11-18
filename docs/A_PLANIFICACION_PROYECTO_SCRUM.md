# Componente A — Planificación Profesional del Proyecto (Scrum)

> **Proyecto Integrador Final — Prácticas Profesionalizantes I (Instituto Nuevos Aires — INA)**  
> **Alumno:** Ezequiel Quiroga | **Peso en rúbrica:** `25 %` (`10 pts`) | **Fecha de entrega:** 24/11/2026

---

## 1. Definición Clara del Problema y Objetivos

### Contexto Simulado: *TelcoNova S.A.*
La operadora de telecomunicaciones **TelcoNova S.A.** enfrenta una pérdida sostenida de clientes (*Customer Churn*). Sobre una base histórica analizada de **7.043 clientes**, el **26,54 % (`1.869` clientes)** canceló su servicio, frente al **73,46 % (`5.174` clientes)** que permaneció activo. Adquirir un cliente nuevo cuesta entre 5 y 7 veces más que retener a uno existente; sin embargo, el área comercial detecta las bajas cuando ya son irreversibles.

Además, el abandono no se distribuye de manera uniforme: mientras los clientes con **contrato de 2 años** tienen una tasa de fuga de apenas **`2,83 %`** y los de **1 año** un **`11,27 %`**, quienes poseen **contrato mes a mes** alcanzan un **`42,71 %`** de abandono.

### Objetivo General
Diseñar, planificar, entrenar, auditar éticamente y documentar un sistema de **aprendizaje automático supervisado** interpretable (`DecisionTreeClassifier`) que anticipe qué clientes tienen mayor riesgo de abandono, permitiendo al equipo comercial ejecutar campañas preventivas de retención basadas en reglas claras.

### Objetivos Específicos
1. **Calidad del dato:** Auditar y limpiar el dataset histórico (`WA_Fn-UseC_-Telco-Customer-Churn.csv`), resolviendo inconsistencias de formato en `TotalCharges` (`11` registros en blanco con antigüedad `0`) y excluyendo el identificador personal `customerID`.
2. **Modelado interpretable:** Entrenar un Árbol de Decisión con profundidad controlada (`max_depth=4`, criterio Gini) para obtener reglas explicables sin sobreajuste.
3. **Gestión ágil y colaborativa:** Simular la ejecución completa en **3 Sprints de 2 semanas** mediante tablero **Trello**, repositorio seguro en **GitHub** y ceremonias documentadas.
4. **Responsabilidad ética:** Evaluar sesgos derivados del desbalance de clases (`73,46 %` vs `26,54 %`), proteger la privacidad de los datos y proponer supervisión humana (*Human-in-the-Loop*).

---

## 2. Identificación de Roles (Equipo Simulado Scrum)

Siguiendo el marco **Scrum**, el equipo multifuncional simulado está compuesto por 5 roles complementarios:

| Rol en el Proyecto | Perfil Profesional Simulado | Responsabilidades Principales |
| :--- | :--- | :--- |
| **Scrum Master & Líder Técnico de IA** | **Ezequiel Quiroga** *(Estudiante / Rol ejercido)* | Facilitar las ceremonias Scrum, eliminar bloqueos técnicos, coordinar entregas, asegurar buenas prácticas de Git/GitHub, variables de entorno y preparar la presentación ejecutiva final. |
| **Product Owner (PO)** | **Lic. Sofía Méndez** *(Simulado — Gerencia de Retención)* | Representar la voz del negocio, definir el criterio de éxito (priorizar reglas accionables para campañas), ordenar el *Product Backlog* y validar los incrementos en la *Sprint Review*. |
| **Data Engineer / DBA** | **Ing. Martín Pereyra** *(Simulado — Ingeniería de Datos)* | Supervisar la extracción desde la base comercial (sin operar cambios en producción sin orden escrita), limpiar `TotalCharges`, anonimizar `customerID` y asegurar la reproducibilidad del pipeline. |
| **Data Scientist / ML Engineer** | **Lucas Fernández** *(Simulado — Ciencia de Datos)* | Realizar la codificación *One-Hot* (`17` variables), división estratificada `80/20`, entrenamiento del `DecisionTreeClassifier`, ajuste de `max_depth=4` y evaluación con matriz de confusión. |
| **BI & AI Ethics Analyst** | **Lourdes Gómez** *(Simulado — Visualización y Ética)* | Diseñar los gráficos ejecutivos en `matplotlib`, redactar el informe de ética (privacidad y sesgos algorítmicos) y validar la claridad visual de la documentación y diapositivas. |

---

## 3. Product Backlog Priorizado

Escala de estimación utilizada: **Story Points (Fibonacci: 1, 2, 3, 5, 8)**.

| ID | Historia de Usuario | Prioridad | Story Points | Sprint | Responsable Principal | Criterios de Aceptación |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **HU-01** | *Como PO, quiero definir el problema, alcance y roles del equipo para alinear las expectativas del proyecto.* | Alta | 2 | Sprint 1 | Ezequiel Quiroga + PO | Documento de problema, roles asignados y repositorio inicializado con `.gitignore`. |
| **HU-02** | *Como Data Engineer, quiero limpiar los 11 nulos de `TotalCharges` y realizar el EDA para entender las causas de fuga.* | Alta | 5 | Sprint 1 | Data Engineer | Cero valores nulos tras imputación; gráfico `01_distribucion_churn.png` generado con tasas por contrato. |
| **HU-03** | *Como Data Scientist, quiero excluir `customerID`, aplicar One-Hot Encoding y dividir 80/20 estratificado para preparar el entrenamiento.* | Alta | 3 | Sprint 2 | Data Scientist | Matriz de entrada `(7.043, 17)`, `5.634` registros de entrenamiento y `1.409` de prueba con `random_state=42`. |
| **HU-04** | *Como Data Scientist, quiero entrenar un Árbol de Decisión (`max_depth=4`) y evaluar su matriz de confusión para medir aciertos y falsos negativos.* | Alta | 5 | Sprint 2 | Data Scientist | Exactitud verificada (`79,56 %`), matriz (`929 VN`, `106 FP`, `182 FN`, `192 VP`) y gráfico `02_matriz_confusion_metricas.png`. |
| **HU-05** | *Como Analista de Ética, quiero auditar los sesgos del desbalance de datos y la privacidad de clientes para garantizar un uso responsable.* | Alta | 3 | Sprint 3 | BI & Ethics Analyst | Informe `C_INFORME_ETICA_Y_RESPONSABILIDAD.md` aprobado cubriendo Ley 25.326 y análisis de falsos negativos. |
| **HU-06** | *Como Scrum Master, quiero documentar el proyecto en un `README.md` profesional con HTML y flujo Git seguro para su publicación en GitHub.* | Alta | 3 | Sprint 3 | Ezequiel Quiroga | `README.md` completo, `.env.example` presente, cero claves en el código y pruebas ejecutables (`src/entrenar_y_evaluar.py`). |
| **HU-07** | *Como BI Analyst, quiero construir la presentación de 10 láminas aplicando la regla 10-20-30 para defender el proyecto ante el comité.* | Alta | 5 | Sprint 3 | BI & Ethics Analyst | Archivo `.pptx` con 10 diapositivas, logo INA, tipografía >= 20 pt y gráficos explicados. |
| **HU-08** | *Como Scrum Master, quiero preparar y ensayar el guion oral de 10 minutos para cumplir el tiempo máximo de exposición.* | Media | 2 | Sprint 3 | Ezequiel Quiroga | Guion cronometrado en `D_GUION_EXPOSICION_ORAL_10_MIN.md` con respuestas al comité. |
| **HU-09** | *Como PO, quiero integrar alertas automáticas diarias al CRM para que los ejecutivos contacten clientes en riesgo.* | Baja | 8 | Backlog Futuro | PO + Dev | Pendiente para fase productiva posterior al piloto analítico. |
| **HU-10** | *Como Data Engineer, quiero monitorear deriva de datos mensual para detectar cambios en el perfil de abandono.* | Baja | 5 | Backlog Futuro | Data Engineer | Definido como mejora evolutiva tras la puesta en producción. |

---

## 4. Planificación de Sprints (*Sprint Planning*)

El proyecto se organiza en **3 Sprints de 2 semanas** (6 semanas totales simuladas, comprometiendo **28 Story Points** de los 41 del Product Backlog):

### Sprint 1 — Descubrimiento, Roles y Calidad del Dato *(Semanas 1–2 | 7 pts)*
- **Objetivo del Sprint:** Comprender el negocio, conformar el equipo simulado, inicializar el repositorio Git seguro y entregar un dataset limpio con análisis exploratorio visual.
- **Historias incluidas:** `HU-01` (2 pts), `HU-02` (5 pts).
- **Entregable (Incremento 1):** Base limpia (`7.043` filas, `0` nulos), tabla de tasas por contrato y gráfico `01_distribucion_churn.png`.

### Sprint 2 — Modelado Predictivo e Interpretabilidad *(Semanas 3–4 | 8 pts)*
- **Objetivo del Sprint:** Transformar variables categóricas, construir un Árbol de Decisión reproducible e interpretable y evaluar su desempeño sobre datos nunca vistos.
- **Historias incluidas:** `HU-03` (3 pts), `HU-04` (5 pts).
- **Entregable (Incremento 2):** Modelo `DecisionTreeClassifier` entrenado (`79,56 %` de exactitud), script modular `src/entrenar_y_evaluar.py` y gráfico `02_matriz_confusion_metricas.png`.

### Sprint 3 — Auditoría Ética, Documentación y Presentación Ejecutiva *(Semanas 5–6 | 13 pts)*
- **Objetivo del Sprint:** Consolidar la auditoría ética, actualizar el tablero Trello, completar la documentación profesional en GitHub (`README.md` con HTML) y cerrar la presentación final (regla `10-20-30`).
- **Historias incluidas:** `HU-05` (3 pts), `HU-06` (3 pts), `HU-07` (5 pts), `HU-08` (2 pts).
- **Entregable (Incremento 3):** Repositorio completo listo para entrega (`24/11/2026`), informes en `docs/` y presentación PowerPoint en `presentacion/`.
