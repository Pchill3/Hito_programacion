#necesitamos un registro de cliente en la clase cliente
#el cual tendra que constar de nombre, pais (importante porque tendremos que hacer que le cobren gastos de envio), telefono y dni
#aqui creamos la clase cliente
class cliente:
#aqui creamos la funcion
    def __init__(self,nombre,pais,direccion,telefono,dni,email):
        self.nombre=nombre
        self.pais=pais
        self.direccion=direccion
        self.telefono=telefono
        self.dni=dni
        self.email=email
#aqui creamos la funcion de mostrar el cliente
    def consultarcliente(self):
        print((f'Cliente: [nombre: {self.nombre}, pais: {self.pais}, direccion: {self.direccion}, telefono: {self.telefono}, dni: {self.dni}, email:{self.email}]'))
#aqui creamos una funcion que te dice cuanto debes pagar de gastos de envio si eres de fuera de españa
    def eresdefueradeespaña(self):
        if self.pais.lower()!='españa':
            print(f'los gastos de envio son 20 euros')
        else:
            print('no tienes gastos de envio porque resides en españa')

#aqui llamamos a las variable y hacemos un input el cual te permite introducir los datos de cada cliente que quieras crear
cliente1=cliente(input('dime tu nombre: '), input('dime tu pais: '), input('dime tu direccion: ' ), input('dime tu telefono: '), input('dime tu dni: '), input('dime tu email: '))
cliente1.eresdefueradeespaña()
cliente1.consultarcliente()



