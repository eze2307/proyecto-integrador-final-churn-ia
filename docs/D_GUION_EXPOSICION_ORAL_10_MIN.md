# Componente D — Guion de Exposición Oral (7–10 Minutos) y Prompt para Gamma

> **Proyecto Integrador Final — Prácticas Profesionalizantes I (Instituto Nuevos Aires — INA)**  
> **Alumno:** Ezequiel Quiroga | **Peso en rúbrica:** `30 %` (`12 pts`) | **Duración objetivo:** `8 a 9 minutos` (tope máximo `10 min`)

---

## 1. Recomendaciones Previas para la Defensa Virtual

- **Cámara encendida y mirada al frente:** mirar a la cámara con postura erguida, usando gestos naturales y evitando leer apuntes al costado.
- **Vocabulario técnico preciso:** decir *Product Backlog*, *Sprint Planning*, *One-Hot Encoding*, *matriz de confusión* o *sensibilidad (recall)* en lugar de expresiones imprecisas como *«esas cosas»*.
- **Anclas visuales:** usar las palabras resaltadas en negrita de cada lámina como disparadores de la idea, **sin leer la diapositiva palabra por palabra**.
- **Copia de seguridad y preparación:** tener abiertas con antelación la presentación `.pptx`, el repositorio GitHub/código y una copia en la nube + pendrive.

---

## 2. Guion Cronometrado Diapositiva por Diapositiva (Regla 10-20-30)

### Diapositiva 1 — Portada *(0:00 – 0:30 | 30 s)*
- **Anclas visuales:** Logo INA, Título del Proyecto, Ezequiel Quiroga, Prácticas Profesionalizantes I.
- **Qué decir:** *«Buenas noches profesor y miembros del comité. Soy Ezequiel Quiroga, estudiante de la Tecnicatura Superior en Ciencia de Datos e IA del Instituto Nuevos Aires. Hoy presento mi Proyecto Integrador Final: la simulación profesional completa de un proyecto de predicción de abandono de clientes en telecomunicaciones, integrando gestión ágil con Scrum, Trello, GitHub, ética del dato y aprendizaje automático.»*

### Diapositiva 2 — Problema de Negocio y Objetivo *(0:30 – 1:20 | 50 s)*
- **Anclas visuales:** `7.043 clientes`, **`26,54 %` de abandono**, objetivo de retención preventiva.
- **Qué decir:** *«Partimos de una situación problema real simulada en TelcoNova S.A.: de 7.043 clientes analizados, 1.869 —un 26,54 %— abandonaron el servicio. Como retener cuesta mucho menos que captar clientes nuevos, nuestro objetivo fue construir un flujo profesional capaz de anticipar qué usuarios tienen mayor riesgo de fuga y explicar por qué.»*

### Diapositiva 3 — Equipo Simulado y Roles Scrum *(1:20 – 2:15 | 55 s)*
- **Anclas visuales:** **Scrum Master (Ezequiel)**, *Product Owner*, *Data Engineer*, *Data Scientist*, *BI & Ethics Analyst*.
- **Qué decir:** *«Para simular cómo trabaja un equipo real de Ciencia de Datos, estructuré cinco roles complementarios bajo el marco Scrum. Yo asumí el rol de Scrum Master y Líder Técnico —facilitando ceremonias y garantizando buenas prácticas de Git— acompañado por un Product Owner enfocado en el negocio, un Data Engineer para el pipeline limpio, un Data Scientist para el modelado y una analista de visualización y ética.»*

### Diapositiva 4 — Planificación: Product Backlog y 3 Sprints *(2:15 – 3:15 | 60 s)*
- **Anclas visuales:** `10 Historias de Usuario`, **`3 Sprints de 2 semanas`**, `28 Story Points comprometidos`.
- **Qué decir:** *«Tradujimos las necesidades del negocio en un Product Backlog de 10 historias de usuario priorizadas por valor. La ejecución se organizó en tres Sprints de dos semanas: el Sprint 1 dedicado a la limpieza del dato y análisis exploratorio; el Sprint 2 al entrenamiento y validación del modelo; y el Sprint 3 a la auditoría ética, la documentación en GitHub y esta presentación. Las tareas de despliegue productivo quedan en el backlog futuro.»*

### Diapositiva 5 — Gestión Visual en Trello y Artefactos *(3:15 – 4:10 | 55 s)*
- **Anclas visuales:** Gráfico `03_tablero_trello_simulacion.png`, **4 columnas** (*Backlog, En proceso, Por verificar, Hecho*), ceremonias documentadas.
- **Qué decir:** *«Como vemos en el tablero de Trello, gestionamos el avance mediante cuatro columnas transparentes, tarjetas con checklists de verificación y responsables claros. Todo quedó acompañado por actas simuladas de Sprint Planning, Daily Scrum, Sprint Review y Retrospectiva para asegurar trazabilidad.»*

### Diapositiva 6 — Metodología Técnica y Flujo en GitHub *(4:10 – 5:10 | 60 s)*
- **Anclas visuales:** **`11 nulos en TotalCharges`**, *One-Hot (`17` columnas)*, split `80/20`, ramas + `.env.example`.
- **Qué decir:** *«En la parte técnica reutilizamos el pipeline validado en clase: detectamos 11 valores en blanco en TotalCharges correspondientes a clientes nuevos sin antigüedad y los imputamos con cero; excluimos `customerID`, transformamos las categorías a 17 variables mediante One-Hot Encoding y dividimos el dataset de forma estratificada en 5.634 casos de entrenamiento y 1.409 de prueba. Todo el código vive en GitHub bajo ramas de trabajo, Pull Requests y variables de entorno para no exponer configuraciones sensibles.»*

### Diapositiva 7 — Análisis Exploratorio de Abandono (EDA) *(5:10 – 6:05 | 55 s)*
- **Anclas visuales:** Gráfico `01_distribucion_churn.png`, **`42,71 %` Mes a mes vs. `2,83 %` 2 años**.
- **Qué decir:** *«Si observamos el gráfico izquierdo, el dataset presenta un desbalance moderado: 73,46 % de permanencia frente al 26,54 % de abandono. Al cruzar ese dato con el tipo de contrato a la derecha, aparece un hallazgo clave de negocio: los clientes con contrato mes a mes alcanzan un 42,71 % de abandono, frente a apenas un 2,83 % en contratos a dos años.»*

### Diapositiva 8 — Resultados del Modelo de IA (`DecisionTreeClassifier`) *(6:05 – 7:10 | 65 s)*
- **Anclas visuales:** Gráfico `02_matriz_confusion_metricas.png`, **`79,56 %` Exactitud**, `192 VP / 182 FN`, `tenure (46,4 %)`.
- **Qué decir:** *«Entrenamos un Árbol de Decisión con criterio Gini y profundidad máxima 4 para evitar sobreajuste. En el conjunto de prueba nunca visto alcanzó un 79,56 % de exactitud. La matriz de confusión nos muestra 929 verdaderos negativos y 192 clientes en riesgo detectados a tiempo, pero también nos advierte con honestidad técnica sobre 182 falsos negativos que se nos escapan. A la derecha vemos que las variables más decisivas fueron la antigüedad en meses (46,4 %) y contar con servicio de fibra óptica (39,3 %).»*

### Diapositiva 9 — Ética y Responsabilidad Social del Dato *(7:10 – 8:15 | 65 s)*
- **Anclas visuales:** **Privacidad (Ley 25.326)**, **Sesgos por desbalance (Ferrante, CONICET)**, **Transparencia y Human-in-the-Loop**.
- **Qué decir:** *«Ningún proyecto de ciencia de datos está completo sin su auditoría ética. Primero protegimos la privacidad eliminando identificadores personales en línea con la Ley 25.326. Segundo, siguiendo a Enzo Ferrante, analizamos cómo el desbalance de datos genera casi un 50 % de falsos negativos en la clase minoritaria y recomendamos auditar variables como adulto mayor para evitar cualquier sesgo discriminatorio. Finalmente, elegimos un árbol poco profundo precisamente para explicar cada regla y mantener siempre la decisión comercial en manos humanas.»*

### Diapositiva 10 — Conclusiones, Recomendaciones y Bibliografía *(8:15 – 9:05 | 50 s)*
- **Anclas visuales:** Retención proactiva, ajuste `class_weight`, integración CRM, **Referencias APA 7.ª ed.**
- **Qué decir:** *«Como conclusión, integramos herramientas profesionales reales —Scrum, Trello, GitHub y Python— sobre un problema de alto impacto comercial. Recomendamos enfocar campañas de fidelización en clientes nuevos de fibra óptica con contrato mensual y ajustar el peso de clases en la próxima iteración para reducir los falsos negativos. En pantalla quedan las referencias bibliográficas en normas APA. Muchas gracias, quedo atento a sus preguntas.»*

---

## 3. Banco de Preguntas Posibles del Comité y Respuestas

1. **¿Por qué elegiste un Árbol de Decisión con `max_depth=4` y no un modelo más complejo?**  
   *Respuesta:* Porque en un contexto comercial necesitamos explicabilidad (*transparencia algorítmica*) para que el equipo de marketing entienda el motivo del riesgo, y limitar la profundidad a 4 niveles previene que el modelo memorice ruido de los datos de entrenamiento (*overfitting*).
2. **¿Cómo manejaste el riesgo de subir claves o datos sensibles a GitHub?**  
   *Respuesta:* Trabajamos sobre una base anonimizada sin `customerID`, excluimos cualquier archivo `.env` mediante `.gitignore`, documentamos los parámetros en `.env.example` y aplicamos ramas con *Pull Request* antes de tocar `main`.
3. **¿Por qué hay 182 falsos negativos en la matriz de confusión y cómo los reducirías?**  
   *Respuesta:* Porque la clase de abandono es minoritaria (`26,54 %`). Si en el negocio cuesta más perder un cliente que enviar un descuento preventivo, usaríamos `class_weight="balanced"` o bajaríamos el umbral de decisión para ganar sensibilidad (*recall*).
4. **Si el proyecto se atrasaba a mitad del Sprint 2, ¿qué hacías como Scrum Master?**  
   *Respuesta:* Detectábamos el bloqueo en la *Daily*, priorizábamos junto al *Product Owner* las historias críticas del núcleo del modelo, apoyábamos al compañero rezagado y nunca mostrábamos trabajo incompleto o roto en la *Sprint Review*.
5. **¿Qué rol cumple el informe de ética en un proyecto comercial de IA?**  
   *Respuesta:* Evita que el algoritmo opere como una «caja negra» que reproduzca sesgos por edad o forma de pago, asegura el cumplimiento legal de privacidad (Ley 25.326) y limita las predicciones a un apoyo para decisiones humanas constructivas.
6. **¿Por qué aplicaste la regla 10-20-30 en esta presentación?**  
   *Respuesta:* Para condensar todo el proyecto en 10 láminas visuales limpias, respetar estrictamente el límite de 10 minutos de exposición y garantizar una lectura clara desde cualquier pantalla usando tipografías grandes *Sans Serif*.

---

## 4. Prompt Listo para Copiar en Gamma (`gamma.app`) *(Alternativa / Respaldo IA)*

> **Contexto y rol:** Actúa como un especialista en Ciencia de Datos y gestión ágil que presenta su Proyecto Integrador Final ante un tribunal académico de la carrera Tecnicatura Superior en Ciencia de Datos e IA del Instituto Nuevos Aires (INA).  
> **Audiencia y tono:** Tribunal técnico y docente; tono profesional, claro, estructurado y orientado tanto a negocio como a rigurosidad metodológica.  
> **Instrucción y estructura exacta (10 diapositivas):** Crea una presentación de exactamente 10 diapositivas siguiendo la regla 10-20-30 (texto conciso con palabras clave, sin párrafos largos, diseño sobrio azul oscuro corporativo y celeste). Estructura obligatoria:  
> 1. Portada: «Proyecto Integrador Final: Simulación Profesional en Ciencia de Datos e IA — Predicción de Abandono de Clientes», autor Ezequiel Quiroga, Instituto Nuevos Aires (INA), Noviembre 2026.  
> 2. Introducción y Problema de Negocio: TelcoNova S.A., 7.043 clientes, 26,54 % de abandono, impacto económico de la retención.  
> 3. Equipo Simulado y Roles Scrum: Scrum Master (Ezequiel Quiroga), Product Owner, Data Engineer, Data Scientist y BI & Ethics Analyst.  
> 4. Planificación Ágil: Product Backlog de 10 historias de usuario y 3 Sprints de 2 semanas (28 Story Points).  
> 5. Gestión Visual en Trello: Tablero de 4 columnas (Backlog, En proceso, Por verificar, Hecho) y ceremonias Scrum documentadas.  
> 6. Metodología Técnica y GitHub: Limpieza de 11 nulos en TotalCharges, One-Hot Encoding (17 variables), split estratificado 80/20, ramas Git y seguridad con variables de entorno.  
> 7. Hallazgos Exploratorios (EDA): 42,71 % de abandono en contratos mes a mes frente a 2,83 % a dos años.  
> 8. Resultados del Árbol de Decisión (`max_depth=4`, Gini): 79,56 % de exactitud, matriz de confusión (929 VN, 106 FP, 182 FN, 192 VP) y variables clave (antigüedad 46,4 %, fibra óptica 39,3 %).  
> 9. Ética y Responsabilidad del Dato: Privacidad (Ley 25.326), sesgos por desbalance (Enzo Ferrante, CONICET), explicabilidad y control humano.  
> 10. Conclusiones, Recomendaciones de Negocio y Bibliografía en formato APA 7.ª edición.  
> **Nota importante:** Tras generarla y exportarla a PowerPoint (`.pptx`), insertar nuestras 3 gráficas reales de `assets/` y el logo transparente oficial del INA en la portada y encabezados.
