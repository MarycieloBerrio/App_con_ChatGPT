import streamlit as st

# Título y descripción de la app
st.title("Conversor Universal")
st.write("Seleccione la categoría y el tipo de conversión que desea:")

# Lista de categorías y conversiones disponibles
categorias = [
    "Temperatura",
    "Longitud",
    "Peso/Masa",
    "Volumen",
    "Tiempo",
    "Velocidad",
    "Área",
    "Energía",
    "Presión",
    "Tamaño de Datos"
]

categoria_seleccionada = st.selectbox("Seleccione una categoría:", categorias)

# Conversión de temperatura
if categoria_seleccionada == "Temperatura":
    tipos_conversion = [
        "Celsius a Fahrenheit",
        "Fahrenheit a Celsius",
        "Celsius a Kelvin",
        "Kelvin a Celsius"
    ]
    tipo_seleccionado = st.selectbox("Seleccione el tipo de conversión:", tipos_conversion)

    if tipo_seleccionado == "Celsius a Fahrenheit":
        celsius = st.number_input("Ingrese la temperatura en Celsius:", value=0.0)
        fahrenheit = (celsius * 9/5) + 32
        st.write(f"{celsius} °C equivale a {fahrenheit:.2f} °F")

    elif tipo_seleccionado == "Fahrenheit a Celsius":
        fahrenheit = st.number_input("Ingrese la temperatura en Fahrenheit:", value=0.0)
        celsius = (fahrenheit - 32) * 5/9
        st.write(f"{fahrenheit} °F equivale a {celsius:.2f} °C")

    elif tipo_seleccionado == "Celsius a Kelvin":
        celsius = st.number_input("Ingrese la temperatura en Celsius:", value=0.0)
        kelvin = celsius + 273.15
        st.write(f"{celsius} °C equivale a {kelvin:.2f} K")

    elif tipo_seleccionado == "Kelvin a Celsius":
        kelvin = st.number_input("Ingrese la temperatura en Kelvin:", value=0.0)
        celsius = kelvin - 273.15
        st.write(f"{kelvin} K equivale a {celsius:.2f} °C")

# Conversión de longitud
elif categoria_seleccionada == "Longitud":
    tipos_conversion = [
        "Pies a Metros",
        "Metros a Pies",
        "Pulgadas a Centímetros",
        "Centímetros a Pulgadas"
    ]
    tipo_seleccionado = st.selectbox("Seleccione el tipo de conversión:", tipos_conversion)

    if tipo_seleccionado == "Pies a Metros":
        pies = st.number_input("Ingrese la longitud en pies:", value=0.0)
        metros = pies * 0.3048
        st.write(f"{pies} pies equivale a {metros:.2f} metros")

    elif tipo_seleccionado == "Metros a Pies":
        metros = st.number_input("Ingrese la longitud en metros:", value=0.0)
        pies = metros / 0.3048
        st.write(f"{metros} metros equivale a {pies:.2f} pies")

    elif tipo_seleccionado == "Pulgadas a Centímetros":
        pulgadas = st.number_input("Ingrese la longitud en pulgadas:", value=0.0)
        centimetros = pulgadas * 2.54
        st.write(f"{pulgadas} pulgadas equivale a {centimetros:.2f} centímetros")

    elif tipo_seleccionado == "Centímetros a Pulgadas":
        centimetros = st.number_input("Ingrese la longitud en centímetros:", value=0.0)
        pulgadas = centimetros / 2.54
        st.write(f"{centimetros} centímetros equivale a {pulgadas:.2f} pulgadas")

# Conversión de peso/masa
elif categoria_seleccionada == "Peso/Masa":
    tipos_conversion = [
        "Libras a Kilogramos",
        "Kilogramos a Libras",
        "Onzas a Gramos",
        "Gramos a Onzas"
    ]
    tipo_seleccionado = st.selectbox("Seleccione el tipo de conversión:", tipos_conversion)

    if tipo_seleccionado == "Libras a Kilogramos":
        libras = st.number_input("Ingrese el peso en libras:", value=0.0)
        kilogramos = libras * 0.453592
        st.write(f"{libras} libras equivale a {kilogramos:.2f} kilogramos")

    elif tipo_seleccionado == "Kilogramos a Libras":
        kilogramos = st.number_input("Ingrese el peso en kilogramos:", value=0.0)
        libras = kilogramos / 0.453592
        st.write(f"{kilogramos} kilogramos equivale a {libras:.2f} libras")

    elif tipo_seleccionado == "Onzas a Gramos":
        onzas = st.number_input("Ingrese el peso en onzas:", value=0.0)
        gramos = onzas * 28.3495
        st.write(f"{onzas} onzas equivale a {gramos:.2f} gramos")

    elif tipo_seleccionado == "Gramos a Onzas":
        gramos = st.number_input("Ingrese el peso en gramos:", value=0.0)
        onzas = gramos / 28.3495
        st.write(f"{gramos} gramos equivale a {onzas:.2f} onzas")

# Conversión de volumen
elif categoria_seleccionada == "Volumen":
    tipos_conversion = [
        "Galones a Litros",
        "Litros a Galones",
        "Pulgadas cúbicas a Centímetros cúbicos",
        "Centímetros cúbicos a Pulgadas cúbicas"
    ]
    tipo_seleccionado = st.selectbox("Seleccione el tipo de conversión:", tipos_conversion)

    if tipo_seleccionado == "Galones a Litros":
        galones = st.number_input("Ingrese el volumen en galones:", value=0.0)
        litros = galones * 3.78541
        st.write(f"{galones} galones equivale a {litros:.2f} litros")

    elif tipo_seleccionado == "Litros a Galones":
        litros = st.number_input("Ingrese el volumen en litros:", value=0.0)
        galones = litros / 3.78541
        st.write(f"{litros} litros equivale a {galones:.2f} galones")

    elif tipo_seleccionado == "Pulgadas cúbicas a Centímetros cúbicos":
        pulgadas_cubicas = st.number_input("Ingrese el volumen en pulgadas cúbicas:", value=0.0)
        cm_cubicos = pulgadas_cubicas * 16.3871
        st.write(f"{pulgadas_cubicas} pulgadas cúbicas equivale a {cm_cubicos:.2f} centímetros cúbicos")

    elif tipo_seleccionado == "Centímetros cúbicos a Pulgadas cúbicas":
        cm_cubicos = st.number_input("Ingrese el volumen en centímetros cúbicos:", value=0.0)
        pulgadas_cubicas = cm_cubicos / 16.3871
        st.write(f"{cm_cubicos} centímetros cúbicos equivale a {pulgadas_cubicas:.2f} pulgadas cúbicas")

# Conversión de área
elif categoria_seleccionada == "Área":
    tipos_conversion = [
        "Metros cuadrados a Pies cuadrados",
        "Pies cuadrados a Metros cuadrados",
        "Kilómetros cuadrados a Millas cuadradas",
        "Millas cuadradas a Kilómetros cuadrados"
    ]
    tipo_seleccionado = st.selectbox("Seleccione el tipo de conversión:", tipos_conversion)

    if tipo_seleccionado == "Metros cuadrados a Pies cuadrados":
        metros_cuadrados = st.number_input("Ingrese el área en metros cuadrados:", value=0.0)
        pies_cuadrados = metros_cuadrados * 10.7639
        st.write(f"{metros_cuadrados} metros cuadrados equivale a {pies_cuadrados:.2f} pies cuadrados")

    elif tipo_seleccionado == "Pies cuadrados a Metros cuadrados":
        pies_cuadrados = st.number_input("Ingrese el área en pies cuadrados:", value=0.0)
        metros_cuadrados = pies_cuadrados / 10.7639
        st.write(f"{pies_cuadrados} pies cuadrados equivale a {metros_cuadrados:.2f} metros cuadrados")

    elif tipo_seleccionado == "Kilómetros cuadrados a Millas cuadradas":
        km_cuadrados = st.number_input("Ingrese el área en kilómetros cuadrados:", value=0.0)
        millas_cuadradas = km_cuadrados * 0.386102
        st.write(f"{km_cuadrados} kilómetros cuadrados equivale a {millas_cuadradas:.2f} millas cuadradas")

    elif tipo_seleccionado == "Millas cuadradas a Kilómetros cuadrados":
        millas_cuadradas = st.number_input("Ingrese el área en millas cuadradas:", value=0.0)
        km_cuadrados = millas_cuadradas / 0.386102
        st.write(f"{millas_cuadradas} millas cuadradas equivale a {km_cuadrados:.2f} kilómetros cuadrados")

# Conversión de energía
elif categoria_seleccionada == "Energía":
    tipos_conversion = [
        "Julios a Calorías",
        "Calorías a Kilojulios",
        "Kilovatios-hora a Megajulios",
        "Megajulios a Kilovatios-hora"
    ]
    tipo_seleccionado = st.selectbox("Seleccione el tipo de conversión:", tipos_conversion)

    if tipo_seleccionado == "Julios a Calorías":
        julios = st.number_input("Ingrese la energía en julios:", value=0.0)
        calorias = julios * 0.239006
        st.write(f"{julios} julios equivale a {calorias:.2f} calorías")

    elif tipo_seleccionado == "Calorías a Kilojulios":
        calorias = st.number_input("Ingrese la energía en calorías:", value=0.0)
        kilojulios = calorias / 0.239006
        st.write(f"{calorias} calorías equivale a {kilojulios:.2f} kilojulios")

    elif tipo_seleccionado == "Kilovatios-hora a Megajulios":
        kilovatios_hora = st.number_input("Ingrese la energía en kilovatios-hora:", value=0.0)
        megajulios = kilovatios_hora * 3.6
        st.write(f"{kilovatios_hora} kilovatios-hora equivale a {megajulios:.2f} megajulios")

    elif tipo_seleccionado == "Megajulios a Kilovatios-hora":
        megajulios = st.number_input("Ingrese la energía en megajulios:", value=0.0)
        kilovatios_hora = megajulios / 3.6
        st.write(f"{megajulios} megajulios equivale a {kilovatios_hora:.2f} kilovatios-hora")

# Conversión de presión
elif categoria_seleccionada == "Presión":
    tipos_conversion = [
        "Pascales a Atmósferas",
        "Atmósferas a Pascales",
        "Barras a Libras por pulgada cuadrada",
        "Libras por pulgada cuadrada a Bares"
    ]
    tipo_seleccionado = st.selectbox("Seleccione el tipo de conversión:", tipos_conversion)

    if tipo_seleccionado == "Pascales a Atmósferas":
        pascales = st.number_input("Ingrese la presión en pascales:", value=0.0)
        atm = pascales / 101325
        st.write(f"{pascales} pascales equivale a {atm:.6f} atmósferas")

    elif tipo_seleccionado == "Atmósferas a Pascales":
        atm = st.number_input("Ingrese la presión en atmósferas:", value=0.0)
        pascales = atm * 101325
        st.write(f"{atm} atmósferas equivale a {pascales:.2f} pascales")

    elif tipo_seleccionado == "Barras a Libras por pulgada cuadrada":
        barras = st.number_input("Ingrese la presión en barras:", value=0.0)
        psi = barras * 14.5038
        st.write(f"{barras} barras equivale a {psi:.2f} libras por pulgada cuadrada")

    elif tipo_seleccionado == "Libras por pulgada cuadrada a Bares":
        psi = st.number_input("Ingrese la presión en libras por pulgada cuadrada:", value=0.0)
        barras = psi / 14.5038
        st.write(f"{psi} libras por pulgada cuadrada equivale a {barras:.2f} bares")

# Conversión de tamaño de datos
elif categoria_seleccionada == "Tamaño de Datos":
    tipos_conversion = [
        "Megabytes a Gigabytes",
        "Gigabytes a Terabytes",
        "Kilobytes a Megabytes",
        "Terabytes a Petabytes"
    ]
    tipo_seleccionado = st.selectbox("Seleccione el tipo de conversión:", tipos_conversion)

    if tipo_seleccionado == "Megabytes a Gigabytes":
        megabytes = st.number_input("Ingrese el tamaño en megabytes:", value=0.0)
        gigabytes = megabytes / 1024
        st.write(f"{megabytes} megabytes equivale a {gigabytes:.6f} gigabytes")

    elif tipo_seleccionado == "Gigabytes a Terabytes":
        gigabytes = st.number_input("Ingrese el tamaño en gigabytes:", value=0.0)
        terabytes = gigabytes / 1024
        st.write(f"{gigabytes} gigabytes equivale a {terabytes:.6f} terabytes")

    elif tipo_seleccionado == "Kilobytes a Megabytes":
        kilobytes = st.number_input("Ingrese el tamaño en kilobytes:", value=0.0)
        megabytes = kilobytes / 1024
        st.write(f"{kilobytes} kilobytes equivale a {megabytes:.6f} megabytes")

    elif tipo_seleccionado == "Terabytes a Petabytes":
        terabytes = st.number_input("Ingrese el tamaño en terabytes:", value=0.0)
        petabytes = terabytes / 1024
        st.write(f"{terabytes} terabytes equivale a {petabytes:.6f} petabytes")

