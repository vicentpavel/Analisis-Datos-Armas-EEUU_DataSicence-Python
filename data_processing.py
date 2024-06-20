import pandas as pd
import matplotlib.pyplot as plt
import folium
import json
import os
from selenium import webdriver
#from selenium.webdriver import FirefoxOptions
#from selenium.webdriver.firefox.options import Options

def read_csv(filepath: str) -> pd.DataFrame: 
    """
    Lee el fichero CSV y devuelve el contenido en un DataFrame.

    Args:
        filepath (str): Ruta al fichero CSV.
    Returns:
        pd.DataFrame: El contenido del CSV en un DataFrame Pandas.
    """
    df = pd.read_csv(filepath)
    print("Primeras cinco filas del dataset:".upper())
    print(df.head(5))
    print("\n\nEstructura del dataset:".upper())
    print(df.info())
    return df

def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el dataset y se quedan solo las columans relevantes.

    Args:
        df (pd.DataFrame): El DataFrame original
    Returns:
        pd.DataFrame: Devuelve el DataFrame limpio solo con las columnas relevantes.
    """
    relevant_columns = ['month', 'state', 'permit', 'handgun', 'long_gun']
    cleaned_df = df[relevant_columns]
    print("\n\nColumnas después de la limpieza:".upper())
    print(cleaned_df.columns)
    return cleaned_df

def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renombre la clumna 'longgun' por 'long_gun' en el DataFrame.    

    Args:
        df (pd.DataFrame): El DataFrame.
    Returns:
        pd.DataFrame: El DataFrame con la columna renombrada.
    """
    if 'longgun' in df.columns:
        df.rename(columns={'longgun': 'long_gun'}, inplace=True)
    print("\n\nColumnas después del renombrado:".upper())
    print(df.columns)
    return df

def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Separa la columna 'month' en las columnas 'year' y 'month'.
    
    Args:
        df (pd.DataFrame): El DataFrame con la columna 'month'.
    
    Returns:
        pd.DataFrame: El DataFrame con las columnas 'year' y 'month'.
    """
    df[['year', 'month']] = df['month'].str.split('-', expand=True)
    df['year'] = df['year'].astype(int) #Convertimos los datos a int pero si tenemos que realizar cálculos posteriores
    df['month'] = df['month'].astype(int)
    print("\nPrimeras cinco filas después de dividir la columna 'month':".upper())
    print(df.head(5))
    return df

def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina la columna 'month' del DataFrame.
    
    Args:
        df (pd.DataFrame): El DataFrame.
    
    Returns:
        pd.DataFrame: El DataFrame sin la colmuna 'month'.
    """
    print("\nColumnas antes de eliminar 'month':".upper())
    print(df.columns)
    df = df.drop(columns=['month'])
    print("\nPrimeras cinco filas después de eliminar la columna 'month':".upper())
    print(df.head(5))
    return df

def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ej.3.1. Calcula los valores acumulados totales agrupando los datos por año y por estado: (columnas year y state).
    
    Args:
        df (pd.DataFrame): El DataFrame con las columnas 'year' y 'state'.
    
    Returns:
        pd.DataFrame: El DataFrame con los valores acumulados.
    """
    grouped_df = df.groupby(['year', 'state']).agg({
        'permit': 'sum',
        'handgun': 'sum',
        'long_gun': 'sum'
    }).reset_index()
    return grouped_df

def print_biggest_handguns(df: pd.DataFrame):
    """
    Imprime por pantalla un mensaje informativo indicando el nombre del estado y el año en donde se ha registrado un mayor numero de hand_guns.
    
    Args:
        df (pd.DataFrame): Dataframe con los datos agrupados por estado y por año como resultado del ejercicio 3.1.
    """
    max_row = df.loc[df['handgun'].idxmax()]
    print(f"\nEl mayor número de handguns se registró en el estado {max_row['state']} en el año {int(max_row['year'])} con {int(max_row['handgun'])} handguns.")

def print_biggest_longguns(df: pd.DataFrame):
    """
    Imprimir por pantalla un mensaje informativo indicando el nombre del estado y el año en donde se ha registrado un mayor numero de long_guns.
    
    Args:
        df (pd.DataFrame): Dataframe con los datos agrupados por estado y por año como resultado del ejercicio 3.1.
    """
    max_row = df.loc[df['long_gun'].idxmax()]
    print(f"\nEl mayor número de long guns se registró en el estado {max_row['state']} en el año {int(max_row['year'])} con {int(max_row['long_gun'])} long guns.\n")

def time_evolution(df: pd.DataFrame):
    """
    Crea un gráfico con series temporales con el número total de permit, hand_gun y long_gun registrado por cada uno de los años.

    Args:
        df (pd.DataFrame): El DataFrame con los datos.

    """
    # Agrupar por año y calcular el total de cada categoría
    yearly_data = df.groupby('year').sum().reset_index()

    # Crear el gráfico
    plt.figure(figsize=(12, 8))
    plt.plot(yearly_data['year'], yearly_data['permit'], label='Permits')
    plt.plot(yearly_data['year'], yearly_data['handgun'], label='Handguns')
    plt.plot(yearly_data['year'], yearly_data['long_gun'], label='Long Guns')

    # Añadir títulos y etiquetas
    plt.title('Series Temporales de Permisos (Permits), Pistolas (handguns) y Rifles de Asalto (long guns)')
    plt.xlabel('Año')
    plt.ylabel('Número Total')
    plt.legend()
    plt.grid(True)
    plt.show()

def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ej.5.1. Muestra los valores totales agrupando los valores únicamente por estado y no por año.
    
    Args:
        df (pd.DataFrame): dataframe con los datos agrupados por estado y por año como resultado del ejercicio 3.1.
    
    Returns:
        pd.DataFrame: DataFrame con los valores agrupados unicamente por estados.
    """
    grouped_df = df.groupby('state').agg({
        'year': 'first',  # Taking the first year value as a representative
        'permit': 'sum',
        'handgun': 'sum',
        'long_gun': 'sum'
    }).reset_index()
    
    print("\nPrimeras cinco filas del dataframe agrupado por estado:")
    print(grouped_df.head(5))
    return grouped_df

def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ej.5.2. Comprueba si existen cuatro estados (Guam, Mariana Islands, Puerto Rico y Virgin Islands) y, en el caso de que existan los eliminará.
    
    Args:
        df (pd.DataFrame): dataframe con los datos agrupados por estado como resultado del ejercicio 5.1.
    
    Returns:
        pd.DataFrame: El mismo DataFrame recibido pero sin los cuatro estados mencionados.
    """
    print("\n\nNúmero de estados diferentes antes de la limpieza:".upper(),df['state'].nunique())
    states_to_remove = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
    df = df[~df['state'].isin(states_to_remove)]
    print("\nNúmero de estados diferentes después de la limpieza:".upper(),df['state'].nunique())
    return df

def merge_datasets(df1: pd.DataFrame, filepath: str) -> pd.DataFrame:
    """
    Ej.5.3. Fusiona los datos de los dos datasets recibidos como parámetros de entrada, incluyendo por cada estado toda la información procedente de las dos fuentes de datos.
    
    Args:
        df1 (pd.DataFrame): DataFrame resultante del ejercicio ejercicio 5.2.
        filepath (str): conjunto de datos poblacionales provenientes del fichero: us-state-populations.csv.
    
    Returns:
        pd.DataFrame: DataFrame fusionado.
    """
    df2 = pd.read_csv(filepath) # El enunciado sugiere usar la función creada en el Ej.1.1 pero no se realiza esa llamada, ya que la carga del dataset en un DataFrame en Pandas es más sencillo.
    merged_df = pd.merge(df1, df2, left_on='state', right_on='state') # utilizamos la clave 'state' como clave de unión entre los dos DataFrames 
    print("\nPrimeras cinco filas del dataframe fusionado:".upper())
    print(merged_df.head(5))
    return merged_df

def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ej.5.4. Crea 3 nuevas columnas llamadas permit_perc, longgun_perc y handgun_perc
    
    Args:
        df (pd.DataFrame): DataFrame resultante del ejercicio ejercicio 5.3.
    
    Returns:
        pd.DataFrame: DataFrame resultante con las tres columnas nuevas: permit_perc, loggun_perc y shotgun_perc y los valores relativos ya calculados.
    """
    df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
    df['handgun_perc'] = (df['handgun'] * 100) / df['pop_2014']
    df['longgun_perc'] = (df['long_gun'] * 100) / df['pop_2014']
    return df

def analyze_relative_values(df: pd.DataFrame):
    """
    Ej.5.5. Calcula la media de permisos permit_perc con dos decimales y muestra el resultado en pantalla. Muestra por pantalla toda la información relativa al estado de Kentucky
    
    Args:
        df (pd.DataFrame): DataFrame resultante del ejercicio ejercicio 5.4.
    """
    # 1 - En primer lugar, calcularemos la media de permisos permit_perc con dos decimales y mostraremos el resultado en pantalla. 
    mean_permit_perc = df['permit_perc'].mean()
    print(f"\nMedia de permisos permit_perc: {mean_permit_perc:.2f}")

    # 2 - En segundo lugar, mostraremos por pantalla toda la información relativa al estado de Kentucky.
    kentucky_info = df[df['state'] == 'Kentucky']
    print("\nInformación del estado de Kentucky:")
    print(kentucky_info)

    # El enunciado de la práctica nos dice que el estado de Kentucky es un outlier (valor atípico). 
    # Vamos a realizar los cambios solicitados en la práctica y más tarde si el resultado es diferente, obtendremos conclusiones.

    # 3- Reemplazar el valor permit_perc de Kentucky con el valor de la media de esta columna. 
    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = mean_permit_perc

    # 4- Volveremos a calcular la media con dos decimales. 
    new_mean_permit_perc = df['permit_perc'].mean()
    print(f"\nNueva media de permisos permit_perc después de eliminar el outlier: {new_mean_permit_perc:.2f}")

    # 5- ¿Ha cambiado mucho el valor? Comparamos las medias
    print(f"\nCambio en la media: {abs(mean_permit_perc - new_mean_permit_perc):.2f}")

    # 5- ¿Entiendes el proceso de quitar valores atípicos? Escribe tus conclusiones.
    if mean_permit_perc != new_mean_permit_perc:
        print("\nConclusión: El proceso de eliminar outliers puede ayudar a obtener una medida más representativa de los datos.")
    else:
        print("\nConclusión: En este caso, la eliminación del outlier no tuvo un impacto significativo en la media.")


def generate_choropleth_map(df: pd.DataFrame, variable: str, output_filepath: str):
    """
    Genera un mapa coroplético para una variable especificada y guarda el mapa como un documento html.
    
    Args:
        df (pd.DataFrame): DataFrame con datos.
        variable (str): La variable a ser visualizada/medida en el mapa.
        geojson_filepath (str): Ruta del fichero GeoJSON con datos.
        output_filepath (str): Nombre de fichero html a ser guardado.
    """
    # initialize the map and store it in a m object
    m = folium.Map(location=[40, -95], zoom_start=4)
    
    state_geo = f"Data/us-states.json"
    state_unemployment = f"Data/US_Unemployment_Oct2012.csv"
    state_data = pd.read_csv(state_unemployment)

    merged_df = pd.merge(df, state_data, left_on='code', right_on='State')

    # Añadir capa coroplética
    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=merged_df,
        columns=['state', variable],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=.1,
        legend_name=variable,
    ).add_to(m)

    folium.LayerControl().add_to(m)
    
    # Guardamos el documento html
    m.save(output_filepath + '.html')
    
    # Convertir el HTML en imagen. Primero se intentó con Firefox ya que era el que estaba instalado pero después de varios intentos fallidos se pasó a usar el driver de Chrome.

    # options = Options()
    # options.headless = True
    # options.binary_location = '/usr/bin/firefox'  # Especifica la ruta al binario de Firefox
    # driver = webdriver.Firefox(options=options, executable_path='/usr/local/bin/geckodriver')
    # driver.get('file:///' + os.path.abspath(output_filepath + '.html'))
    # driver.save_screenshot(output_filepath + '.png')
    # driver.quit()
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('file:///' + os.path.abspath(output_filepath + '.html'))
    driver.save_screenshot(output_filepath + '.png')
    driver.quit()
