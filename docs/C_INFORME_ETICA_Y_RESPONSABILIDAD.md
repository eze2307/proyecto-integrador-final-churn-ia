# Componente C — Informe Breve de Ética y Responsabilidad Social en el Ámbito del Dato

> **Proyecto Integrador Final — Prácticas Profesionalizantes I (Instituto Nuevos Aires — INA)**  
> **Alumno:** Ezequiel Quiroga | **Peso en rúbrica (Documentación Profesional):** `20 %` (`8 pts`)

---

## 1. Propósito de la Auditoría Ética

Todo modelo de Inteligencia Artificial aplicado a clientes reales impacta en decisiones comerciales concretas (ofertas, bonificaciones, prioridades de atención o condiciones de servicio). Como sostiene el investigador **Enzo Ferrante (CONICET)**, **los algoritmos no son neutrales**: reflejan las decisiones humanas sobre qué datos se recogen, qué variables se incluyen y qué error se decide tolerar.

Este informe evalúa cuatro pilares éticos indispensables antes de utilizar nuestro modelo de predicción de abandono en un entorno real.

---

## 2. Privacidad, Anonimización y Protección de Datos Personales

1. **Principio de minimización de datos:** El archivo original incluía el campo identificador `customerID` junto con atributos demográficos (`SeniorCitizen`, `Partner`, `Dependents`). Durante el preprocesamiento, **`customerID` fue excluido de forma explícita**, evitando asociar predicciones del modelo a identidades nominales en el entrenamiento.
2. **Marco normativo argentino (Ley N.º 25.326 de Protección de Datos Personales):** En un despliegue productivo, el entrenamiento y la inferencia deben operar sobre identificadores seudonimizados, con consentimiento informado del titular y finalidad estrictamente acotada a mejorar la calidad del servicio, nunca para discriminar ni encarecer tarifas de manera opaca.
3. **Seguridad técnica y resguardo:** El código del repositorio separa la configuración mediante variables de entorno (`.env.example` + `.gitignore`) y prohíbe alojar credenciales, tokens de API o copias completas de bases productivas en repositorios públicos.

---

## 3. Análisis de Sesgos Algorítmicos y Desbalance de Clases

Al auditar los datos históricos y la matriz de confusión (`n = 1.409` registros de prueba), emergen dos riesgos relevantes:

### A. Sesgo derivado del desbalance de clases (`73,46 %` vs. `26,54 %`)
- En la base completa, casi tres de cada cuatro clientes pertenecen a la clase mayoritaria (`No abandonó = 5.174`), mientras que el abandono representa solo el **`26,54 %` (`1.869` casos)**.
- Como consecuencia directa, aunque el modelo alcanza una exactitud global del **`79,56 %`**, su comportamiento por clase es asimétrico:
  - Detecta muy bien a quienes permanecen (**sensibilidad del `89,76 %`**, `929 VN`).
  - Detecta aproximadamente la mitad de quienes realmente abandonan (**sensibilidad o *recall* del `51,34 %`**, `192 VP` frente a **`182` falsos negativos**).
- **Lectura responsable:** Confiar solo en la métrica global (*accuracy*) ocultaría que casi **1 de cada 2 clientes en riesgo real pasa desapercibido**. Para una campaña de retención donde perder un cliente es costoso, en futuras iteraciones conviene ajustar pesos (`class_weight="balanced"`) o umbrales de probabilidad.

### B. Vigilancia sobre atributos demográficos y socioeconómicos
- Aunque en nuestro árbol actual (`max_depth=4`) los nodos dominantes fueron la **antigüedad (`46,4 %`)** y el **servicio de fibra óptica (`39,3 %`)** —y no las variables demográficas—, el dataset contiene indicadores como `SeniorCitizen` (adulto mayor), `Partner`, `Dependents` y medio de pago (`Electronic check`).
- Siguiendo las advertencias sobre equidad (*fairness*) documentadas en clase a partir de estudios como *Gender Shades* (Buolamwini y Gebru) y Ferrante (2021), **las variables demográficas deben auditarse por subgrupos** para comprobar que el sistema no ofrezca peores condiciones ni concentre falsas alarmas sobre grupos vulnerables o de mayor edad.

---

## 4. Transparencia, Explicabilidad y Control Humano (*Human-in-the-Loop*)

1. **Elección deliberada de un modelo interpretable:** Optamos por un **Árbol de Decisión con profundidad máxima 4** precisamente porque cualquier integrante no técnico de la empresa puede leer sus reglas paso a paso (*«si tiene contrato mes a mes, poca antigüedad y fibra óptica, presenta alto riesgo de baja»*), a diferencia de modelos complejos de caja negra difíciles de auditar.
2. **Decisión asistida, nunca automatizada de forma punitiva:** Las predicciones del modelo sirven únicamente como **señal de alerta temprana para acciones constructivas** (mejorar soporte técnico, ofrecer planes adecuados al consumo o encuestas de satisfacción). La decisión final siempre recae en un equipo humano responsable.
3. **Ausencia de variables externas críticas:** El modelo no conoce quejas técnicas recientes ni precios de la competencia; explicitar esta limitación evita tomar decisiones comerciales injustificadas asumiendo que el algoritmo «lo ve todo».

---

## Referencias Éticas Aplicadas
- Congreso de la Nación Argentina. (2000). *Ley 25.326 de Protección de los Datos Personales*.
- Ferrante, E. (2021). *Inteligencia artificial y sesgos algorítmicos. ¿Por qué deberían importarnos?* CONICET / Nueva Sociedad.
