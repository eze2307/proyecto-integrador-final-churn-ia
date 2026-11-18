# Componente D — Guion de Exposición Oral (6 Diapositivas / Regla 10-20-30)

> **Proyecto Integrador Final — Prácticas Profesionalizantes I (Instituto Nuevos Aires — INA)**  
> **Alumno:** Ezequiel Quiroga | **Peso en rúbrica:** `30 %` (`12 pts`) | **Estructura:** `6 diapositivas` (los 6 bloques de la Clase 14) | **Duración objetivo:** `7 a 9 minutos` (tope máximo `10 min`)

---

## 1. Recomendaciones Previas para la Defensa Virtual

- **Cámara encendida y mirada al frente:** mirar a la cámara con postura erguida, usando gestos naturales y evitando leer apuntes al costado.
- **Por qué 6 diapositivas:** la regla **10-20-30** fija un **máximo de 10 diapositivas**. Al concentrarlo en los **6 bloques fundamentales** de la Clase 14, dispones de **1 a 1,5 minutos por diapositiva**, hablando pausado y sin prisas.
- **Anclas visuales:** usa las cifras y palabras en negrita de cada lámina como disparadores de la idea, **sin leer la diapositiva palabra por palabra**.
- **Copia de seguridad y preparación:** tener abiertas con antelación la presentación `.pptx`, tu tablero de Trello y tu repositorio de GitHub.

---

## 2. Guion Cronometrado para las 6 Diapositivas (Con Ejemplos Cotidianos)

### Diapositiva 1 — Portada Institucional *(0:00 – 0:40 | 40 s)*
- **Anclas visuales:** Logo INA, Título del Proyecto, **Ezequiel Quiroga**, Prácticas Profesionalizantes I.
- **Ejemplo cotidiano para recordarla:** Es tu tarjeta de presentación al entrar a la reunión.
- **Qué decir al profesor:**  
  *«Buenas noches profesor y miembros del comité. Soy Ezequiel Quiroga, estudiante de la Tecnicatura Superior en Ciencia de Datos e IA del Instituto Nuevos Aires. Hoy presento mi Proyecto Integrador Final: la simulación profesional completa de un proyecto de predicción de abandono de clientes en telecomunicaciones, integrando gestión ágil con Scrum, Trello, GitHub, ética del dato y aprendizaje automático.»*

---

### Diapositiva 2 — 1. Problema de Negocio y Análisis Exploratorio (EDA) *(0:40 – 2:00 | 1 min 20 s)*
- **Anclas visuales:** Gráfico `01_distribucion_churn.png`, `7.043 clientes`, **`26,54 %` de bajas**, **`42,71 %` en contrato mes a mes vs. `2,83 %` a 2 años**.
- **Ejemplo cotidiano para recordarla:** Como un gimnasio donde se borran 26 de cada 100 socios, y al mirar las fichas descubres que los que se van son los que pagan mes a mes sin compromiso (`42,71 %`), mientras que los que firmaron por 2 años casi no se van (`2,83 %`).
- **Qué decir al profesor:**  
  *«Partimos de un problema real simulado en TelcoNova S.A.: sobre una base de 7.043 clientes, 1.869 —un 26,54 %— se dieron de baja. Como conseguir un cliente nuevo cuesta entre 5 y 7 veces más que retener a uno actual, analizamos dónde ocurre la fuga. En el gráfico de la derecha vemos el hallazgo comercial clave: los clientes con contrato mes a mes alcanzan un 42,71 % de abandono, frente a apenas un 2,83 % en contratos a dos años. Nuestro objetivo fue crear un sistema capaz de anticipar quién está en riesgo antes de que cancele.»*

---

### Diapositiva 3 — 2. Gestión Ágil: Equipo Scrum, 3 Sprints y Tablero Trello *(2:00 – 3:30 | 1 min 30 s)*
- **Anclas visuales:** Tablero `03_tablero_trello_simulacion.png`, **5 Roles Scrum (Ezequiel = Scrum Master)**, **10 Historias (`HU-01` a `HU-10`)**, **3 Sprints** y **4 columnas en Trello**.
- **Ejemplo cotidiano para recordarla:** Los 5 roles son como la cocina de un restaurante donde tú eres el jefe de cocina (*Scrum Master*); los 3 Sprints son las 3 etapas de una obra quincenal; y Trello es la pantalla de pedidos donde cada tarea pasa de *Lista de tareas* a *En proceso*, luego a *Por verificar con el cliente* y finalmente a *Hecho*.
- **Qué decir al profesor:**  
  *«Para trabajar como un equipo real de Ciencia de Datos, estructuré cinco roles Scrum donde asumí el papel de Scrum Master y Líder Técnico, acompañado por un Product Owner, un Ingeniero de Datos, un Científico de Datos y una Analista de BI y Ética. Dividimos el trabajo en 10 historias de usuario a lo largo de tres Sprints de dos semanas: el Sprint 1 para limpieza y exploración; el Sprint 2 para entrenar el modelo; y el Sprint 3 para auditoría ética, GitHub y defensa, dejando las mejoras productivas en el backlog futuro. Todo se gestionó en este tablero público de Trello de cuatro columnas con etiquetas de estado, checklists y actas de las cuatro ceremonias Scrum.»*

---

### Diapositiva 4 — 3. Metodología Técnica, GitHub Seguro y Ética del Dato *(3:30 – 5:00 | 1 min 30 s)*
- **Anclas visuales:** **`11 vacíos en TotalCharges`**, sin `customerID`, **One-Hot (`17` columnas)**, partición **`80/20`**, GitHub con `.env`, **Ley 25.326**, **Enzo Ferrante (CONICET)** y **Human-in-the-Loop**.
- **Ejemplo cotidiano para recordarla:** A la izquierda, la cocina técnica (poner `0` a los 11 clientes nuevos sin primera factura, traducir palabras a unos y ceros para la calculadora, separar 80 % para estudiar y 20 % para el examen, y no dejar contraseñas en GitHub). A la derecha, las reglas éticas (tapar el DNI del cliente por la Ley 25.326, vigilar el desbalance de datos y que la IA sea como un GPS donde la decisión final siempre la toma una persona).
- **Qué decir al profesor:**  
  *«En la tarjeta izquierda vemos el flujo técnico: detectamos 11 celdas vacías en TotalCharges de clientes recién ingresados y las imputamos con cero; quitamos el identificador customerID, transformamos las categorías a 17 columnas numéricas con One-Hot Encoding y dividimos el dataset 80/20 de forma estratificada. Todo el código se publicó en GitHub usando ramas, Pull Requests y variables de entorno para no exponer claves. En la tarjeta derecha integramos la auditoría ética: cumplimos la Ley 25.326 de protección de datos personales, analizamos el sesgo por desbalance de clases siguiendo a Enzo Ferrante y garantizamos transparencia con supervisión humana.»*

---

### Diapositiva 5 — 4. Resultados del Árbol de Decisión (`n = 1.409` prueba) *(5:00 – 6:30 | 1 min 30 s)*
- **Anclas visuales:** Gráfico `02_matriz_confusion_metricas.png`, **`79,56 %` de exactitud**, **`192 VP` detectados**, **`182 FN` que escapan**, **Antigüedad (`46,4 %`)** y **Fibra óptica (`39,3 %`)**.
- **Ejemplo cotidiano para recordarla:** El Árbol de nivel 4 (`max_depth=4`) es como jugar al *«¿Quién es quién?»* con solo 4 preguntas para que no memorice de memoria. La Matriz de Confusión es la alarma: acertó en 929 clientes fieles y cazó a 192 que se iban a ir, tuvo 106 falsas alarmas y se le escaparon 182 porque en los datos históricos había muchos más clientes que se quedaban que los que se iban.
- **Qué decir al profesor:**  
  *«Entrenamos un Árbol de Decisión con criterio Gini y profundidad máxima 4 para evitar sobreajuste y poder explicar cada regla al negocio. En los 1.409 clientes del examen alcanzó un 79,56 % de exactitud. La matriz de confusión confirma 929 verdaderos negativos y 192 clientes en riesgo detectados a tiempo, pero también nos muestra con honestidad técnica 182 falsos negativos que se escapan debido al desbalance 73/27 del dataset. A la derecha vemos que los dos factores más decisivos son la antigüedad en meses (46,4 %) y tener fibra óptica (39,3 %).»*

---

### Diapositiva 6 — 5. Conclusiones, Recomendaciones y Bibliografía (APA) *(6:30 – 7:45 | 1 min 15 s)*
- **Anclas visuales:** Fidelizar fibra óptica mensual, **`class_weight='balanced'`**, conexión CRM (`HU-09`) y **Bibliografía APA 7.ª ed.**
- **Ejemplo cotidiano para recordarla:** La receta final del médico: hoy mismo cuidamos a los clientes nuevos de fibra óptica con contrato mensual; en la versión 2 ajustamos la sensibilidad de la alarma (`class_weight='balanced'`) para atrapar a esos 182 que se escaparon; y cerramos con las fuentes oficiales en formato APA.
- **Qué decir al profesor:**  
  *«Como conclusión, logramos articular Scrum, Trello, GitHub y Python en una solución aplicable al negocio. Recomendamos enfocar campañas preventivas en clientes nuevos de fibra óptica con contrato mes a mes y, en la siguiente iteración técnica, aplicar balanceo de pesos de clase para reducir los 182 falsos negativos antes de conectar las alertas al CRM. A la derecha quedan las referencias bibliográficas en formato APA séptima edición. Muchas gracias, quedo a disposición para sus preguntas.»*

---

## 3. Banco de Preguntas Posibles del Comité y Respuestas Cortas

1. **¿Por qué hiciste 6 diapositivas en lugar de 10?**  
   *Respuesta:* Porque la regla 10-20-30 establece un tope máximo de 10 diapositivas, y al estructurarla exactamente en los **6 bloques fundamentales** vimos en la Clase 14 logramos mayor síntesis visual y mejor control del tiempo sin omitir ningún componente.
2. **¿Por qué elegiste un Árbol de Decisión con `max_depth=4`?**  
   *Respuesta:* Porque el área comercial necesita entender el porqué de cada alerta (*transparencia algorítmica*), y limitar el árbol a 4 niveles evita que memorice ruido (*overfitting*).
3. **¿Cómo protegiste la seguridad al subir el proyecto a GitHub?**  
   *Respuesta:* Eliminamos `customerID`, excluimos archivos `.env` mediante `.gitignore`, dejamos una plantilla `.env.example` sin claves y trabajamos con ramas y *Pull Requests*.
4. **¿Por qué hay 182 falsos negativos y cómo los bajarías?**  
   *Respuesta:* Porque solo el `26,54 %` del dataset son bajas. Para atrapar más casos en riesgo aplicaríamos `class_weight="balanced"` o ajustaríamos el umbral de probabilidad.

---

## 4. Prompt Listo para Gamma (`gamma.app`) — Versión 6 Diapositivas

> **Instrucción:** Crea una presentación ejecutiva de exactamente **6 diapositivas** (regla 10-20-30, diseño azul marino corporativo y celeste, texto conciso con viñetas cortas) para el Proyecto Integrador Final de Ezequiel Quiroga en el Instituto Nuevos Aires (INA):  
> 1. **Portada:** Simulación Profesional en Ciencia de Datos e IA — Predicción de Abandono de Clientes (Telco Churn), Ezequiel Quiroga, INA, Noviembre 2026.  
> 2. **Problema de Negocio y Exploración (EDA):** TelcoNova S.A. (7.043 clientes, 26,54 % de baja); hallazgo crítico: 42,71 % de abandono en contratos mes a mes frente a 2,83 % en contratos a 2 años.  
> 3. **Gestión Ágil con Scrum y Trello:** 5 roles simulados (Ezequiel Quiroga como Scrum Master), 10 historias de usuario (`HU-01` a `HU-10`) en 3 Sprints de 2 semanas y tablero Trello de 4 columnas.  
> 4. **Metodología Técnica, GitHub y Ética:** Limpieza de 11 vacíos en `TotalCharges`, One-Hot Encoding (17 columnas), partición 80/20, GitHub seguro con `.env`, cumplimiento de Ley 25.326, análisis de sesgos (Enzo Ferrante, CONICET) y *Human-in-the-Loop*.  
> 5. **Resultados del Modelo (`DecisionTreeClassifier`, `max_depth=4`):** 79,56 % de exactitud sobre 1.409 clientes de prueba, matriz de confusión (929 VN, 106 FP, 182 FN, 192 VP) e importancia de variables (antigüedad 46,4 % y fibra óptica 39,3 %).  
> 6. **Conclusiones, Recomendaciones y Bibliografía APA 7.ª ed.:** Campañas en clientes nuevos de fibra con contrato mensual, ajuste `class_weight='balanced'` y referencias APA.
