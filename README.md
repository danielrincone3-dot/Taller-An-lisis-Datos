# 📊 Taller de Análisis de Datos con Pandas

Este proyecto corresponde al desarrollo de un flujo completo de ingeniería y análisis de datos utilizando **Python** y la librería **Pandas**. El sistema procesa, limpia, unifica, analiza y visualiza información comercial para la toma de decisiones basada en datos.

---

## 📂 Estructura del Proyecto

El proyecto está modularizado para separar las responsabilidades de cada etapa del pipeline:

- `main.py`: Punto de entrada principal que despliega el menú interactivo con las opciones del taller.
- `limpieza.py`: Módulo encargado de la limpieza, normalización y preparación inicial de los datos.
- `merge.py`: Módulo responsable de la validación previa e integración (merge) entre las tablas de clientes y ventas.
- `analisis.py`: Módulo que calcula métricas y responde a las preguntas clave del negocio (KPIs).
- `graficos.py`: Módulo que genera y exporta visualizaciones gráficas utilizando `Matplotlib`.
- `Data/`: Carpeta que contiene los datos crudos, procesados y los gráficos exportados.

---

## 🛠️ Detalle de los Módulos y Entregables

### 1. Limpieza de Datos (`limpieza.py`)
Se encargó de depurar los datasets originales, gestionar valores nulos, estandarizar formatos y preparar las tablas base para su posterior cruce.

### 2. Validación y Integración / Merge (`merge.py` - Opción 3)
* **Validación Previa (`validar_premerge`):** Implementa una función de control de calidad antes de fusionar los datos. Verifica:
  1. La existencia de la llave foránea `id_cliente` en ambos DataFrames.
  2. La ausencia de duplicados en la tabla de clientes para garantizar la unicidad de las filas.
  3. La concordancia estricta en los tipos de datos de las llaves.
  4. Cuantifica de forma informativa posibles transacciones huérfanas o sin cliente asociado.
* **Cruce de Datos:** Se realizó un `left join` (`how="left"` sobre el DataFrame de ventas) para asegurar que no se pierda ninguna transacción comercial, aplicando además el parámetro estadístico `validate="m:1"` para confirmar formalmente la relación de varios a uno.

### 3. Análisis de Negocio (`analisis.py` - Opción 4)
Se resolvieron 5 preguntas clave de negocio mediante agrupaciones avanzadas (`groupby`, `agg`, `value_counts`):
1. **Ingresos por Categoría:** Identificación de la categoría de productos que aporta mayor facturación global.
2. **Canal más vendedor:** Comparativa de volumen de transacciones e ingresos totales entre los canales online y físico/tienda.
3. **Clientes VIP vs. Regulares:** Análisis normalizado por cantidad de clientes en cada segmento (`nunique`) para comparar el gasto promedio real y evitar sesgos por volumen de clientes.
4. **Métodos de pago:** Conteo de preferencias de pago de los consumidores.
5. **Top 5 Clientes:** Ranking de fidelidad de clientes basado en frecuencia de compra y volumen de gasto total como factor de desempate.

### 4. Visualización de Datos (`graficos.py` - Opción 5)
* Se automatizó la creación de gráficos de barras utilizando `Matplotlib`.
* Se diseñaron gráficos específicos para:
  - Ventas totales por categoría.
  - Ventas totales por canal de distribución.
* Las imágenes se generan y guardan automáticamente en la ruta `Data/processed/graficos/` para su inclusión en el informe final.

---

## 🚀 Instrucciones de Ejecución

1. Asegúrate de tener instalado Python y las librerías necesarias (como `pandas` y `matplotlib`) en tu entorno virtual.
2. Ejecuta el archivo principal desde tu terminal:
   ```bash
   python main.py
