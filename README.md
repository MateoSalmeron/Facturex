# Facturex

Facturex es una aplicación que generara facturas de unos determinados clientes guardados previamnente en un repositorio (por determinar), las facturas serán generadas en pdf y descargadas a una carpeta para que el/la usuario/a de la apicación pueda hacer lo que quiera con ellas.

Este petproyect ha salido por un problema que me comento un amiga, ella es autonoma y necesita generar la factura a mano una a una y luego pasarla por el sistema de autofirma.
En la primera versión no va a haber integración con autofirma.

Se va a intentar seguir una arquitectura exagonal, hacer el desarrollo con TDD y buenas practicas pero eso habrá que verlo  :) 

EL MVP simplmente generara facturas en pdf de unos datos dados y previamente añadidos a la base de datos, no tendrá interfaz grafica simplemente una ejecución del programa y nada mas.
En futuras iteraciones si vemos que el programa da para mas se integrará con autofirma y posteriormente se le podrá añadir una UI o algo similar.


Para gnerar PDF usaremos reportLab una libreria opensource para python
Para testing usaremos Mamba

Requisitos MVP:
- Numeración de Facturas
- Generar factura por clinte y guardar en pdf en una carpeta.
- calcular el precio de la factura en función del precio y numero de sesiones

Datos del profesional: 
- Nombre y apellidos
- DNI
- dirección?

Datos necesarios por clinte: 
- Nombre y apellidos
- DNI/NIF
- Numero sesiones
- Precio por sesion



