# Diagrama de estados

![Diagrama de estados](Imagenes/Diagrama_de_estados.png)

En este ejemplo, los estados son los siguientes:

- **Pendiente:** Representa el estado inicial de una reserva de habitación. La reserva ha sido creada, pero el huésped aún no ha realizado el check-in.
- **Ocupada:** Después del check-in, la reserva pasa al estado de "Ocupada". En este estado, la habitación está ocupada por el huésped.
- **Cancelada:** Si se cancela la reserva antes del check-in, pasa al estado de "Cancelada". La reserva se considera cancelada y ya no es válida.
- **Finalizada:** Después del check-out, la reserva se marca como "Finalizada". En este estado, el huésped ha dejado la habitación y la reserva ha concluido.
