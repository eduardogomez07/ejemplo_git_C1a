conexion_producto = Conexion_BD('Productos_bd.db')
def fun_vender():
  cant_pro = 0
  total = 0
  lista = []
  vender = True
  while vender:
    #item = Productos()
    try:
      codigo = int(input('Ingresar un codigo: '))
    except:
      print("Ingrese un codigo númerico valido!!!")
      vender()
    conexion_producto.consulta(f'SELECT * FROM Productos WHERE id_producto = {codigo}')
    try:
      consulta = conexion_producto.cursor.fetchall()
      if consulta == []:
        raise Exception("El codigo indicado no EXISTE!!!")
    except Exception as e:
      print(e)
      fun_vender()
    conexion_producto.commit()
    print(consulta)
    if consulta[0][2]<0:
      print(f"No tiene disponivulidad de {consulta[0][1]} ")
      break
    else:
      codigo = consulta[0][0]
      nombre = consulta[0][1]
      cantidad_prod = consulta[0][2]
      precio = consulta[0][3]
      categoria = consulta[0][4]
    print("****************Producto****************")
    print(f"{nombre} - ${precio}")
    cantidad = int(input("Ingrese al Cantidad Deseada: "))
    print("****************************************")
    print("***********Lista de Productos***********")
    if cantidad <= cantidad_prod:
      cantidad_prod -=cantidad
      lista.append((codigo,nombre,cantidad,precio,cantidad_prod))
      i = 1
      for item in lista:
        print(f"{i} - {item[2]} - {item[1]} - ${item[3]} - ${item[3] * item[2]}")
        i +=1
      cant_pro += 1
      total += (lista[-1][3] * lista[-1][2])
    else:
      print("Supera la cantidad disponible!!!")
    resp = input("Igresar otro producto? (s/S): ")
    resp = resp.upper()
    if resp != 'S':
      vender = False
    print("****************************************")
  if lista:
    print(f"Monto total = ${total}")
    for item in lista:
      conexion_producto.consulta(f'UPDATE Productos SET cantidad_producto = cantidad_producto - {item[4]} WHERE id_producto = {item[0]}')
      conexion_producto.consulta(f'INSERT INTO Detalle_Venta VALUES(NULL,{item[0]},{item[3]},{item[2]})')
      conexion_producto.commit()
  else:
    print("La venta se CANCELO!!!!")
  


