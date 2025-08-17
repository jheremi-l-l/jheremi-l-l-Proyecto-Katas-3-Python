# Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
#     e. Mostrar el precio final de la compra, considerando o no el descuento.
#     f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.


try:
    #     a. Solicitar al usuario el precio original de un artículo.

    precio_original = float(input("Introduce el precio original del artículo (€): "))

    #     b. Preguntar si tiene un cupón de descuento (respuesta sí o no).

    cupon_descuento = input("¿Tienes un cupón de descuento (si/no)?: ").strip().lower()

    #     c. Si la respuesta es sí, solicitar el valor del cupón de descuento.

    if cupon_descuento == "si":
        cupon_valor = float(input("Introduzca el valor del cupón(€): "))
        #     d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
        if cupon_valor > 0:
            precio_final = precio_original - cupon_valor

            # Controlamos en caso de ser menor de 0
            if precio_final < 0:
                precio_final = 0
            print(f"✅ Descuento aplicado. Precio final: €{precio_final:.2f}")
        else: 
            print("⚠️ Cupón no válido. Se ignorará el descuento.")
            print(f"💰 Precio final: €{precio_original:.2f}")
    
    elif cupon_descuento == "no":
        # Sin cupón
        print(f"💰 Precio final sin descuento: €{precio_original:.2f}")

    else:
        print("❌ Respuesta no válida. Escribe 'sí' o 'no'.")

except ValueError:
    print("❌ Entrada no válida. Asegúrate de introducir números correctamente.")


