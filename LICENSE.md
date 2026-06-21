# Licencia

Este repositorio mezcla material propio con adaptaciones de código de terceros. Por eso **no existe una única licencia global**: cada bloque de contenido conserva la licencia que le corresponde según su origen. Esta página detalla cuál aplica a qué.

---

## 1. Material original (la mayoría del repositorio)

Las presentaciones de `Teoría_Clases/`, el programa de la materia, y los notebooks que **no** llevan una nota de atribución a otro repositorio (incluidos los notebooks generados con asistencia de Claude, sufijo `_Claude`) están bajo:

**Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)**

Esto permite:

- **Compartir** — copiar y redistribuir el material en cualquier medio o formato.
- **Adaptar** — remezclar, transformar y construir a partir del material.

Bajo los siguientes términos:

- **Atribución** — dar crédito adecuado, brindar un enlace a la licencia, e indicar si se realizaron cambios.
- **No Comercial** — no se puede utilizar el material para fines comerciales.
- **Compartir Igual** — las obras derivadas deben distribuirse bajo la misma licencia que el original.

Texto completo: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

---

## 2. Código adaptado de *Hands-On Simulation Modeling with Python* (Ciaburro / Packt)

Los siguientes archivos están basados en o adaptados del libro de Giuseppe Ciaburro, *Hands-On Simulation Modeling with Python* (Packt Publishing), cuyo código fuente está publicado bajo licencia **MIT** (Copyright © 2022 Packt):

- `Teoría_Notebooks/03_Procesos_Estocasticos_y_Aleatorios/Von-Neumann_RNG.ipynb`
- `Teoría_Notebooks/04_Monte_Carlo/Monte_Carlo_integracion_numerica.ipynb`
- `Teoría_Notebooks/05_Cadenas_Markov/simulating_random_walk.py`
- `Teoría_Notebooks/05_Cadenas_Markov/weather_forecasting.py`
- `Teoría_Notebooks/06_MDP_y_Bellman/ejemplo_schelling_model.ipynb`
- `Teoría_Notebooks/07_Remuestreo/bootstrap_estimator.ipynb`
- `Teoría_Notebooks/07_Remuestreo/jackknife_estimator.ipynb`
- `Teoría_Notebooks/07_Remuestreo/kfold_cross_validation.py`
- `Teoría_Notebooks/08_Optimizacion/GradientDescent.ipynb`
- `Teoría_Notebooks/08_Optimizacion/Newton-Raphson.ipynb`
- `Teoría_Notebooks/08_Optimizacion/gaussian_mixtures.ipynb`
- `Teoría_Notebooks/09_metaheuristicas/Ciaburro_genetic_algorithm.ipynb`
- `Teoría_Notebooks/09_metaheuristicas/Ciaburro_SciPyOptimize.ipynb`
- `Teoría_Notebooks/09_metaheuristicas/Ciaburro_simulated_annealing.ipynb`

Fuente original: https://github.com/PacktPublishing/Hands-On-Simulation-Modeling-with-Python-Second-Edition

La licencia MIT permite el uso, copia, modificación y redistribución de este código (incluso con fines comerciales), con la única condición de conservar el aviso de copyright original. Ese aviso se mantiene íntegro a continuación:

```
MIT License

Copyright (c) 2022 Packt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Importante:** estos archivos específicos NO están bajo CC BY-NC-SA. Su licencia MIT permite explícitamente reutilización comercial; no se les puede agregar la restricción "No Comercial" sin reescribir el código de forma sustancial.

---

## 3. Código adaptado de `helcsnewsxd/models-and-simulation-subject`

El siguiente archivo está basado en ejemplos del repositorio de cátedra *Modelos y Simulación* (FAMAF, Universidad Nacional de Córdoba), publicado bajo licencia **MIT**:

- `Teoría_Notebooks/05_Cadenas_Markov/matrices_transicion.ipynb`

Fuente original: https://github.com/helcsnewsxd/models-and-simulation-subject

Igual que en el caso de Ciaburro, este archivo conserva su licencia MIT original y no está sujeto a la restricción "No Comercial" de CC BY-NC-SA.

---

## 4. Código de Román Picó (`bootstrap_metric.py`)

El archivo `Teoría_Notebooks/07_Remuestreo/bootstrap_metric.py` está adaptado del repositorio personal de Román Picó ([RomanPico/salary_prediction](https://github.com/RomanPico/salary_prediction)), que no publica una licencia open-source explícita en GitHub.

Su inclusión en este repositorio cuenta con **autorización expresa del autor** para Alejandro Mezio, otorgada de forma directa fuera de GitHub. Esta nota documenta esa autorización; cualquier reutilización de ese archivo específico por parte de terceros debería contar con autorización propia del autor original, dado que no está cubierto por una licencia pública.

---

## Resumen rápido

| Origen | Licencia | Restricción comercial |
|--------|----------|------------------------|
| Material propio / generado con Claude | CC BY-NC-SA 4.0 | Sí, no comercial |
| Ciaburro / Packt | MIT | No |
| helcsnewsxd (FAMAF-UNC) | MIT | No |
| Román Picó | Sin licencia pública — uso autorizado caso por caso | No aplica (autorización directa) |

Ante cualquier duda sobre qué licencia aplica a un archivo puntual, verificar primero si tiene una nota de atribución al inicio del notebook o script.

---

© 2026 Alejandro Mezio — Cátedra de Simulación y Procesos Estocásticos, Universidad Católica Argentina, para el material propio. Los derechos sobre el código de terceros listado arriba pertenecen a sus autores originales.
