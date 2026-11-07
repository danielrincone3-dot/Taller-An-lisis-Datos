from pathlib import Path

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
   # Revisa que el merge se pueda hacer. Devuelve True si todo está bien, False si no.

    
    #- Que exista la columna "id_cliente" en los dos dataframes.
    if "id_cliente" not in clientes.columns or "id_cliente" not in ventas.columns:
        print("Error no se encontro la columna (id_cliente)")
        return False

    #- Que "id_cliente" no esté repetido en clientes.
    if clientes["id_cliente"].duplicated().any():
        print("Se encontraron clientes duplicados.")
        return False
    
    #- Que "id_cliente" tenga el mismo tipo en los dos dataframes.
    if clientes["id_cliente"].dtype != ventas["id_cliente"].dtype:
        print(f"Error Los tipos de dato del cliente no coinciden. Clientes: {clientes['id_cliente'].dtype}, Ventas: {ventas['id_cliente'].dtype}")
        return False
    
    #- Cuántas ventas no tienen cliente asociado (esto solo se informa, no falla).
    ventas_sin_clientes = (~ventas["id_cliente"].isin(clientes["id_cliente"])).sum()
    print(f"Ventas sin clientes en la tabla", ventas_sin_clientes)

    return True
   
    


def unir(clientes, ventas):
    """Une ventas con clientes usando "id_cliente" y guarda el resultado en Data/processed/merge.csv.

    Pistas:
    - Usar pd.merge(...) o ventas.merge(...).
    - Usar how="left" para no perder ventas.
    - Usar validate="m:1" para confirmar que cada venta tiene un solo cliente.
    - Guardar con df.to_csv(...) en PROCESSED / "merge.csv".
    """
    # TODO 7: validar con validar_premerge(), hacer el merge, guardar el CSV y devolver el dataframe.
    if not validar_premerge(clientes, ventas):
        print("El premerge ha fallado")
        return None
    PROCESSED.mkdir(parents=True, exist_ok=True)
    df_merge = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")
    salida= PROCESSED / "merge.csv"
    df_merge.to_csv(salida, index=False)
    print(f"union exitosa, guardado en ", salida)


    return df_merge
