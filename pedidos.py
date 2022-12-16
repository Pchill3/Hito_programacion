#en pedidos tenemos que poner factuas importes totales y tenemos que hacer el calculo de gastos de envios
#aqui importamos clases
import Cliente
import productos
from Cliente import cliente
from productos import producto

#aqui creamos las variables
class pedido:
    def __init__(self,id,fecha_pedido,id_cliente,id_producto,unidades,importetotal):
        self.id=id
        self.fecha_pedido=fecha_pedido
        self.id_cliente=id_cliente
        self.id_producto=id_producto
        self.unidades=unidades
        self.importetotal=importetotal
#esta es la funcion de gastos de envio de españa la cual hace que si no eres de españa te cobren 20 euros de gastos de envio
    def compra(self):
        if Cliente.cliente1.pais.lower()!='españa':
            total=self.importetotal+20
            print(f'tu total del pediddo con los 20 euros de envio es: {total}')
        else:
            self.importetotal
#esta es la funcion de enviar sms
    def enviarsms(self):
        print('envio sms')
# esta es la funcion de enviar pdf
    def enviarpdf(self):
        print(f'envio pdf de {self.id_cliente}')
# esta es la funcion de enseñar los pedidos
    def enseñarpedido(self):
        print(f'id: {self.id}')
        print(f'fecha: {self.fecha_pedido}')
        print(f'cliente: {self.id_cliente}')
        print(f'producto: {self.id_producto}')
        print(f'unidades: {self.unidades}')
        print(f'importetotal: {self.importetotal}')

#aqui llamamos a las funciones
pedido1=pedido('A1','11/05/2022',Cliente.cliente1.nombre,productos.producto3.nombre,7,productos.producto3.precio*7)
pedido1.enseñarpedido()
pedido1.compra()