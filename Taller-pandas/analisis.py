import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())

    ingresos_por_categoria(df)
    canal_que_mas_vende(df)
    clientes_vip_vs_regular(df)
    metodo_pago_mas_usado(df)
    top5_clientes(df)


def ingresos_por_categoria(df):
    """Pregunta 1: ¿Qué categoría genera más ingresos?

    Pista: df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    """
    # TODO 8: calcular e imprimir los ingresos por categoría y la categoría que más ingresa.
    ingresos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print(ingresos)
    pass


def canal_que_mas_vende(df):
    """Pregunta 2: ¿Qué canal vende más?

    Pista: agrupar por "canal" y usar .agg(ventas=("id_venta", "count"), ingresos=("total", "sum")).
    """
    # TODO 9: calcular e imprimir ventas e ingresos por canal.
    por_canal = df.groupby("canal").agg(
        ventas=("id_venta", "count",),
        ingresos=("total", "sum")
    ).sort_values(by="ingresos", ascending=False)
    print(por_canal)
    print(f"canal que mas vende en ingresos", por_canal.index[0])
    pass


def clientes_vip_vs_regular(df):
    """Pregunta 3: ¿Los clientes VIP compran más que los Regulares?

    Pista: como hay más clientes Regular que VIP, compare promedios por cliente, no totales.
    Calcular: número de clientes (nunique), compras y gasto total por segmento,
    y luego dividir compras y gasto entre el número de clientes.
    """
    # TODO 10: calcular e imprimir compras y gasto promedio por cliente según segmento_cliente.

    resumen = df.groupby("segmento_cliente").agg(
        num_clientes=("id_cliente", "nunique"),
        total_compras=("id_venta", "count"),
        gasto_total=("total", "sum")
    ).reset_index()

    resumen["compras_promedio"] = resumen["total_compras"] / resumen["num_clientes"]
    resumen["gasto_promedio"] = resumen["gasto_total"] / resumen["num_clientes"]
    
    print(resumen)


def metodo_pago_mas_usado(df):
    """Pregunta 4: ¿Qué método de pago es más usado?

    Pista: df["metodo_pago"].value_counts()
    """
    # TODO 11: calcular e imprimir el conteo por método de pago y cuál es el más usado.
    pagos= df["metodo_pago"].value_counts()
    print(pagos)
    pass


def top5_clientes(df):
    """Pregunta 5: ¿Top 5 clientes con más compras?

    Pista: agrupar por ["id_cliente", "nombre_cliente"], contar compras y sumar total,
    ordenar por compras (y por gasto como desempate) y tomar las primeras 5 con .head(5).
    """
    # TODO 12: calcular e imprimir el top 5.
    top5= df.groupby(["id_cliente", "nombre_cliente"]).agg(
        compras=("id_venta", "count"),
        gasto_total=("total", "sum"),
    ).sort_values(by=["compras", "gasto_total",], ascending=False).head(5)
    print(top5)
    pass
