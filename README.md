# Proyecto de Análisis de Datos para Permisos de Armas en EEUU de América

Este proyecto tiene como objetivo analizar el comportamiento de la población de Estados Unidos de América respecto al uso de armas de fuego utilizando datos de verificación de antecedentes. Para ello utiliza dos datasets 'nics-firearm-background-checks.csv' y 'us-state-populations.csv'.
Para generar mapas coropléticos utiliza datos del 'us-states.json' y del 'US_Unemployment_Oct2012.csv'.


## Estructura del Proyecto

- `main.py`: Ejecuta todas las funciones de la PEC.
- `data_processing.py`: Contiene las funciones para leer, limpiar, dividir y renombrar columnas del DataFrame.
- `tests.py`: Contiene los tests para verificar la correcta implementación de las funciones.
- `README.md`: Documentación del proyecto.
- `requirements.txt`: Dependencias del proyecto.

## Instrucciones para Ejecutar el Proyecto

1. Clona el repositorio.
2. Instala las dependencias ejecutando:
   ```bash
   pip3 install -r requirements.txt
3. Ejecuta: python3 main.py

## Análisis del Gráfico Generado

En el gráfico generado por la función `time_evolution`, podemos observar las tres series temporales solicitadas en el ejercicio: los permisos de armas, pistolas y rifles de asalto desde 1998 hasta 2020.

### Observaciones:

1. **Correlación**:
   - Las tres series temporales (permits, handguns y long guns) parecen seguir una tendencia similar, lo que nos hace interpretar una correlación entre ellas. Cuando aumentan los permisos de armas, también lo hacen las solicitudes de pistolas y rifles de asalto.

2. **Tendencia**:
   - La tendencia general es ascendente, con un aumento significativo en el número de permisos, pistolas y rifles de asalto a lo largo de los años. Cabe destacar que de 2018 a 2020 hay una fuerte caída.

3. **Impacto de la Pandemia**:
   - Se observa un cambio significativo en los datos correspondientes a los años de la pandemia (2019-2020). La tendencia ascendente hasta 2018 cae por completo a niveles anteriores al año 2000.

4. **Eventos Notables**:
   - En 2017, hay un pico notable en las tres series temporales, coincidiendo con un aumento en los tiroteos masivos en Estados Unidos, tal y como se puede observar en la gráfica de víctimas de tiroteos masivos en el enlace proporcionado.

### Expectativas para los Próximos Años:

Basándonos en la tendencia observada y sin tener en cuenta la caída en los dos últimos años de la pandemia (2019-2020), podemos esperar que el número de permisos, pistolas y rifles de asalto continúe aumentando en los próximos años.

Este análisis sugiere que los permisos de armas y las solicitudes de pistolas y rifles de asalto están correlacionados y que las fluctuaciones en una categoría tienden a reflejarse en las otras.

### Licencia

Véase el fichero LICENSE