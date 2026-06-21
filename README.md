# Simulación y Procesos Estocásticos

Material de teoría de la materia **Simulación y Procesos Estocásticos**, Licenciatura en Ciencia de Datos.
Facultad de Química e Ingeniería del Rosario, Universidad Católica Argentina (UCA), 2026.

Este repositorio reúne las presentaciones de clase y los notebooks de ejemplos prácticos que acompañan cada unidad teórica de la materia.

---

## Programa

El programa completo de la materia está disponible en [`SyPE_programa_2026.pdf`](./SyPE_programa_2026.pdf).

---

## Contenido del repositorio

Cada unidad temática tiene una presentación en `Teoria_Clases/` y su carpeta correspondiente de notebooks en `Teoria_Notebooks/`.

| Unidad | Tema | Presentación | Notebooks |
|--------|------|---------------|-----------|
| 01 | Modelos y Teoría de Colas | [`01_presentacion_Modelos_y_Colas.pdf`](./Teoria_Clases/01_presentacion_Modelos_y_Colas.pdf) | — |
| 02 | Probabilidad y Estadística | [`02_presentacion_Prob_y_Est.pdf`](./Teoria_Clases/02_presentacion_Prob_y_Est.pdf) | [`02_Probabilidad_Estadistica/`](./Teoria_Notebooks/02_Probabilidad_Estadistica) |
| 03 | Procesos Estocásticos y Generadores Aleatorios | [`03_presentacion_Procesos_y_Generador_Aleatorios.pdf`](./Teoria_Clases/03_presentacion_Procesos_y_Generador_Aleatorios.pdf) | [`03_Procesos_Estocasticos_y_Aleatorios/`](./Teoria_Notebooks/03_Procesos_Estocasticos_y_Aleatorios) |
| 04 | Simulación de Monte Carlo | [`04_presentacion_Monte_Carlo.pdf`](./Teoria_Clases/04_presentacion_Monte_Carlo.pdf) | [`04_Monte_Carlo/`](./Teoria_Notebooks/04_Monte_Carlo) |
| 05 | Cadenas de Markov | [`05_presentacion_Markov.pdf`](./Teoria_Clases/05_presentacion_Markov.pdf) | [`05_Cadenas_Markov/`](./Teoria_Notebooks/05_Cadenas_Markov) |
| 06 | Procesos de Decisión de Markov (MDP) y Ecuación de Bellman | [`06_presentacion_MDP_y_Bellman.pdf`](./Teoria_Clases/06_presentacion_MDP_y_Bellman.pdf) | [`06_MDP_y_Bellman/`](./Teoria_Notebooks/06_MDP_y_Bellman) |
| 07 | Métodos de Remuestreo (Jackknife, Bootstrap, k-Fold CV) | [`07_presentacion_Remuestreo.pdf`](./Teoria_Clases/07_presentacion_Remuestreo.pdf) | [`07_Remuestreo/`](./Teoria_Notebooks/07_Remuestreo) |
| 08 | Optimización (Gradiente Descendente, Newton-Raphson, Verosimilitud) | [`08_presentacion_optimizacion.pdf`](./Teoria_Clases/08_presentacion_optimizacion.pdf) | [`08_Optimizacion/`](./Teoria_Notebooks/08_Optimizacion) |
| 09 | Metaheurísticas (Simulated Annealing, Algoritmos Genéticos) | [`09_presentacion_metaheuristicas.pdf`](./Teoria_Clases/09_presentacion_metaheuristicas.pdf) | [`09_metaheuristicas/`](./Teoria_Notebooks/09_metaheuristicas) |
| 10 | Algoritmos Genéticos (repaso) | [`10_Algoritmos_Geneticos_(repaso).html`](./Teoria_Clases/10_Algoritmos_Geneticos_(repaso).html) | — |

---

## Cómo usar este repositorio

### Requisitos

Los notebooks usan Python 3.11 con las librerías científicas estándar del ecosistema: NumPy, SciPy, Matplotlib, pandas, scikit-learn y seaborn.

### Clonar el repositorio e instalar dependencias

```bash
git clone <URL-del-repositorio>
cd Repositorio_Simulacion_y_Procesos_Estocasticos
pip install -r requirements.txt
```

### Abrir los notebooks

```bash
jupyter notebook Teoria_Notebooks/
```

o abrirlos directamente en VS Code / JupyterLab / Google Colab.

---

## Fuentes y atribución

Este repositorio mezcla material propio con notebooks y scripts adaptados de otras fuentes. Cada archivo adaptado lleva una nota de atribución en su primera celda o línea. Las fuentes externas son:

- **Ciaburro, G.** — *Hands-On Simulation Modeling with Python* (Packt Publishing). Repositorio: [PacktPublishing/Hands-On-Simulation-Modeling-with-Python-Second-Edition](https://github.com/PacktPublishing/Hands-On-Simulation-Modeling-with-Python-Second-Edition) (licencia MIT). Cubre la mayoría de los notebooks de generadores aleatorios, Monte Carlo, cadenas de Markov, remuestreo, optimización y metaheurísticas marcados como "Ejemplo del libro de Ciaburro".
- **helcsnewsxd** — cátedra *Modelos y Simulación*, FAMAF (Universidad Nacional de Córdoba). Repositorio: [helcsnewsxd/models-and-simulation-subject](https://github.com/helcsnewsxd/models-and-simulation-subject) (licencia MIT). Usado en `matrices_transicion.ipynb`.
- **Román Picó** — repositorio [RomanPico/salary_prediction](https://github.com/RomanPico/salary_prediction), usado con autorización directa del autor en `bootstrap_metric.py`.

Los notebooks con sufijo `_Claude` fueron generados con asistencia de IA (Claude, Anthropic) como material complementario de ejemplos para la materia, y son material original de la cátedra.

**El detalle completo de qué licencia aplica a cada archivo está en [`LICENSE.md`](./LICENSE.md)** — no toda la atribución implica MIT, ni toda la atribución implica CC BY-NC-SA. Conviene revisarlo antes de reutilizar cualquier archivo puntual.

---

## Licencia

Este repositorio no tiene una única licencia global: mezcla material propio con código de terceros, cada uno con su propia licencia.

- El material original de la cátedra (presentaciones, notebooks propios y los generados con asistencia de Claude) está bajo **Creative Commons BY-NC-SA 4.0**.
- Los notebooks adaptados de Ciaburro/Packt y de helcsnewsxd conservan su licencia **MIT** original, que es más permisiva (sin restricción de uso comercial).
- El archivo `bootstrap_metric.py` de Román Picó se incluye con autorización directa del autor, fuera de cualquier licencia pública.

Ver **[`LICENSE.md`](./LICENSE.md)** para el detalle completo, archivo por archivo.

---

## Contacto

**Dr. Alejandro Mezio**
Cátedra de Simulación y Procesos Estocásticos
Licenciatura en Ciencia de Datos — UCA

- alejandro.mezio@gmail.com
- mezioalejandro@uca.edu.ar
