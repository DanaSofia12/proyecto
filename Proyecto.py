
CrearRegistro= []
CrearProducto= []
CrearProveedor= []
Inventario_Productos= []


#REGISTRO DE USUARIO E INICIO DE SESIÓN

def registrar():
    nombre= str(input ("Ingrese su nombre: "))
    if not nombre:
        print("Es obligatorio llenar este espacio. Vuelve a intentarlo")
        registrar()
    correo= input ("Ingrese su correo:  ")
    if not correo:
        print("Es obligatorio llenar este espacio. Vuelve a intentarlo")
        registrar()
    telefono= input ("Ingrese su número de teléfono: ")
    if not telefono:
        print("Es obligatorio llenar este espacio. Vuelve a intentarlo")
        registrar()
    usuario = input ("Ingrese un nombre de usuario: ")
    if not usuario:
        print("Es obligatorio llenar este espacio. Vuelve a intentarlo")
        registrar()
    contraseña = input("Ingrese una contraseña: ")
    if not contraseña:
        print("Es obligatorio llenar este espacio. Vuelve a intentarlo")
        registrar()
    confirmar_contraseña= input("Ingrese nuevamente la contraseña: ")
    if not confirmar_contraseña:
        print("Es obligatorio llenar este espacio. Vuelve a intentarlo")
        registrar()
    if contraseña== confirmar_contraseña:
        print(" Contraseña válida")
    else:
        print("Las contraseñas no coinciden. Inténtalo de nuevo.")

    rol = int(input("Elige 1= Cliente 2=Administrador"))
    if not rol:
        print("Es obligatorio llenar este espacio. Vuelve a intentarlo")
        registrar()
    codigo = 123
    if rol ==2:
        codigo1=int(input("Ingresa el código de validación"))
        if codigo1==codigo:
            print("Administrador registrado con éxito")
        else:
            print("Código incorrecto. Inténtelo nuevamente.")
            registrar()
    elif rol ==1: 
        print("Cliente registrado correctamente")

    Registro = {"Nombre":nombre,
                 "Correo":correo,
                 "Telefono": telefono,
                 "Usuario": usuario,
                 "Contraseña": contraseña,
                 "Rol": rol, 
                }              
    print (Registro)
    CrearRegistro.append(Registro)
    print ("El usuario ha sido registrado correctamente. ")

#INICIAR SESION 
    opcion=int(input("¿Desea iniciar sesión 1=sí 2=No?"))
    if opcion==1:
        usuario = input("Introduce tu nombre de usuario: ")
        for Registro in CrearRegistro: 
            if Registro["Usuario"] == usuario:
                print("Usuario encontrado")
                contraseña1 = input("Introduce tu contraseña: ")
                if contraseña == contraseña1:
                    print("Usuario y contraseña correctos. ")
                    Eleccion_rol()
    else:
        print("Usuario no encontrado. Registrese")

#PRODUCTO/AGREGAR/ACTUALIZAR/ELIMINAR
def InventarioProducto():
#AGREGAR
    nombre= input ("Ingrese el nombre del producto : ")
    cantidad= int(input ("Ingrese la cantidad:  "))
    fechaCompra= input ("Ingrese la fecha en que compró el producto: ")
    precio = input ("Ingrese el precio: ")

    Productos = {"Nombre":nombre,
                 "Cantidad":cantidad,
                 "FechaCompra": fechaCompra,
                 "Precio": precio
                }              
    print (Productos)
    CrearProducto.append(Productos)
    print ("El producto ha sido agregado ")
#OPCIONES PRODUCTO
    print("1. Actualizar")
    print("2. Eliminar")
    print("3. Agregar nuevo producto")
    print("4. Regresar al menú principal")
    eleccion=int(input("Escribe tu opción del (1-4)"))
    #ACTUALIZAR
    if eleccion==1:
        nombre= input ("Ingrese el nombre del producto que actualizará: ")
        for Productos in CrearProducto: 
            if Productos["Nombre"] == nombre: 
                cantidad1= int(input ("Ingrese la cantidad:  "))
                fechaCompra1= input ("Ingrese la fecha en que compró el producto: ")
                precio1 = input ("Ingrese el precio: ")

                Productos ["Cantidad"] = cantidad1
                Productos["FechaCompra"]= fechaCompra1
                Productos ["Precio"] = precio1

                print ("El producto ha sido modificado. ")
                print(Productos)
                return
        print ("No se ha encontrado el producto.  ")
#ELIMINAR
    elif eleccion==2:
        Producto = input ("Ingrese el nombre del producto a eliminar: ")

        for Productos in CrearProducto:
            if Productos ["Nombre"] == Producto:
                CrearProducto.remove(Productos)
                print ("El producto ha sido eliminado")
                return 
            print ("No se ha encontrado el producto ")
#AGREGAR PRODUCTO
    elif eleccion==3:
        nombre= input ("Ingrese el nombre del producto : ")
        cantidad= int(input ("Ingrese la cantidad:  "))
        fechaCompra= input ("Ingrese la fecha en que compró el producto: ")
        precio = input ("Ingrese el precio: ")
         

#PROVEEDORES

def InventarioProveedor():
#AGREGAR    
    nombre= input ("Ingrese el nombre del proveedor : ")
    correo= input ("Ingrese el correo del proveedor:  ")
    telefono= input ("Ingrese el número de teléfono del proveedor: ")
    direccion = input ("Ingrese la dirección del proveedor: ")

    Proveedores = {"Nombre":nombre, "Correo":correo, "Telefono": telefono, "Dirección": direccion}

    CrearProveedor.append(Proveedores)
    print ("El proveedor ha sido registrado ")
    print(Proveedores)
    opcion=int(input("¿Desea actualizar o eliminar algún dato? 1=Sí 2=No"))
    if opcion==1:
        print("1=Actualizar 2=Eliminar")
        eleccion=int(input("Escribe tu opción"))
#ACTUALIZAR
        if eleccion==1:
            nombre= input ("Ingrese el nombre del proveedor que actualizará: ")
            for Proveedores in CrearProveedor: 
                if Proveedores["Nombre"] == nombre: 
                    correo1= (input ("Ingrese el correo:  "))
                    Telefono1= int(input ("Ingrese el número de teléfono: "))
                    Direccion1 = input ("Ingrese la dirección: ")

                    Proveedores ["Correo"] = correo1
                    Proveedores["telefono"]= Telefono1
                    Proveedores["direccion"] = Direccion1
                    print ("El proveedor se ha actualizado. ")
                    print(Proveedores)
                    return
            print ("No se ha encontrado el producto.  ")
#ELIMINAR
        elif eleccion==2:
            nombre = input ("Ingrese el nombre del proveedor a eliminar: ")

            for Proveedores in CrearProveedor:
                if Proveedores ["Nombre"] == nombre:
                    CrearProveedor.remove(Proveedores)
                    print ("El proveedor ha sido eliminado")
                    return 
            print ("No se ha encontrado el proveedor ")
    
    #MENÚ ADMINISTRADOR
def menu_administrador():
    print("Bienvenid@ al ménu principal. ")
    print("1. Productos")
    print("2. Proveedores")
    print("3. Cerrar Sesión")
    opcion = int(input("Selecciona una opción (1-3): "))

    if opcion == 1:
        InventarioProducto()
        menu_administrador()
    elif opcion == 2:
        InventarioProveedor()
        menu_administrador()
    elif opcion == 3:
        print ("Cerrando sesión...")
    else:
        print("No existe esa opción.")
  
  #VENTAS

def productos_venta():
    Producto1 = {"Nombre producto":"Maquina de coser",
                 "Cantidad":"5",
                 "Descripción": "Grande, color azul, tiene garantía de un año",
                 "Precio": "800000"
                }
    Producto2 = {"Nombre producto":"Tijeras de tela",
                 "Cantidad":"20",
                 "Descripción": "Buena cálidad, manejables, para sastreria",
                 "Precio": "14000"
                }
    Producto3 = {"Nombre producto":"Piel cremallera para máquina de coser",
                 "Cantidad":"3",
                 "Descripción": "máquina de coser industrial, compatible cualquier marca",
                 "Precio": "11000"
                }
    Productos = { "Producto1": Producto1,"\n"
                  "Producto2": Producto2,"\n"
                  "Producto3": Producto3
                }
    Inventario_Productos.append(Productos)
    for x, y in Productos.items():
        print(x, y)

    venta=int(input("¿Quieres comprar un producto? 1=Sí 2=No"))
    if venta==1:
        print("Cúal de nuestro productos deseas adquirir?")
        print("1. Máquina de coser")
        print("2. Tijeras de tela")
        print("3. Piel cremallera para máquinas de coser")
        opcion=int(input("Escribe tu elección: "))
        if opcion==1:
            cantidad=int(input("¿Cuantos necesitas?"))
            precioTotal1=(cantidad*800000)
            if cantidad>5:
                print("No contamos con ese número de existencias.")
                menu_cliente()
            elif cantidad<=5:
                print(f"Haz realizado la compra del producto máquina de coser que tiene un costo total de {precioTotal1}")
                print("Para más información contacta directamente al número de contacto: 3213451239")
                menu_cliente()
        if opcion==2:
            cantidad=int(input("¿Cuantos necesitas?"))
            precioTotal2= (cantidad*14000)
            if cantidad>20:
                print("No contamos con ese número de existencias.")
                menu_cliente()
            elif cantidad<=20:
                print(f"Haz realizado la compra del producto Tijeras de tela que tiene un costo total de {precioTotal2}.")
                print("Para más información contacta directamente al número de contacto: 3213451239")
                menu_cliente()
        if opcion==3:
            cantidad=int(input("¿Cuantos necesitas?"))
            precioTotal3= (cantidad*11000)
            if cantidad>3:
                print("No contamos con ese número de existencias.")
                menu_cliente()
            elif cantidad<=3:
                print(f"Haz realizado la compra del producto Piel cremallera para máquina de coser que tiene un costo total de {precioTotal3}.")
                print("Para más información contacta directamente al número de contacto: 3213451239")
                menu_cliente()
#CANCELARPEDIDO

def cancelar_Pedido():
    confirmación=int(input("¿Está seguro de que desea cancelar el pedido? 1= Sí 2=No"))
    if confirmación==1:
        motivo=str(input("Por qué desea cancelar su pedido?"))
        print("Pedido cancelado con éxito")
        menu_cliente()
    elif confirmación==2:
        print("Continue con la compra")
        menu_cliente()

#MENÚ CLIENTE
def menu_cliente():
    print("1. Ventas")
    print("2. Cancelar pedido")
    print("3. Cerrar sesión")

    opcion=int(input("Elige una opción (1-3): "))
    if opcion==1:
        productos_venta()
    elif opcion==2:
        cancelar_Pedido()
    elif opcion==3:
        print ("Cerrando sesión")
    else: 
        print("No existe esa opción. Vuelva a elegir.")
        menu_cliente()

  #ROL
def Eleccion_rol():
    print("A continuación elija su rol en el sistema:.")
    print("1. Cliente")
    print("2. Administrador")

    opcion = int(input("Selecciona una opción (1-2): "))
    if opcion == 1:
            menu_cliente()
    elif opcion == 2:
        validacion= int(input("Ingrese el código de confirmación"))
        codigo=123
        if validacion== codigo:
            menu_administrador()
        else:
            print("Opción inválida. Inténtalo de nuevo.")

registrar()