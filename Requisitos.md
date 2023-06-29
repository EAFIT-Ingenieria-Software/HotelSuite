# Requisitos <!-- omit in toc -->

- [Requisito de negocio](#requisito-de-negocio)
- [Regla de negocio](#regla-de-negocio)
- [Requisito de interesado](#requisito-de-interesado)
- [Atributo de calidad](#atributo-de-calidad)
- [Requisito funcional](#requisito-funcional)
- [Requisito no funcional](#requisito-no-funcional)
- [Restricción](#restricción)
- [Interfaz externa](#interfaz-externa)

## Requisito de negocio

- **RB1:** El sistema debe permitir a los clientes realizar reservas en línea de habitaciones y servicios adicionales.

  - Descripción: Los clientes deben poder acceder al sistema HotelSuite a través de una interfaz intuitiva y realizar reservas de habitaciones y servicios adicionales, como comidas o actividades.
  - Criterios de aceptación:
    - Los clientes pueden buscar y seleccionar fechas de reserva deseadas.
    - Los clientes pueden ver la disponibilidad en tiempo real de las habitaciones y servicios.
    - Los clientes pueden seleccionar y reservar habitaciones y servicios adicionales.
    - Los clientes reciben una confirmación de reserva por correo electrónico.

- **RB2:** El sistema debe generar facturas detalladas y precisas para los huéspedes.

  - Descripción: El sistema debe generar automáticamente facturas detalladas para los huéspedes, incluyendo los cargos por habitación, servicios adicionales y los impuestos aplicables.
  - Criterios de aceptación:
    - Las facturas deben incluir un desglose claro de los cargos por habitación y servicios.
    - Las facturas deben mostrar los impuestos aplicables de acuerdo con las regulaciones locales.
    - Las facturas deben ser precisas y reflejar correctamente los cargos realizados durante la estancia.
    - Las facturas deben poder ser impresas o enviadas por correo electrónico a los huéspedes.

- **RB3:** El sistema debe proporcionar informes financieros y de rendimiento del hotel.

  - Descripción: El sistema debe generar informes financieros y de rendimiento del hotel, proporcionando información sobre ingresos, gastos y ocupación.
  - Criterios de aceptación:
    - Los informes deben mostrar los ingresos generados por habitación, servicios y otros conceptos.
    - Los informes deben mostrar los gastos asociados con la operación del hotel.
    - Los informes deben incluir datos sobre la ocupación y el rendimiento del hotel.
    - Los informes deben ser generados en formatos legibles y exportables.

## Regla de negocio

- **RN1:** El sistema debe aplicar reglas de cancelación y políticas de tarifas según las políticas específicas de cada hotel.

  - Descripción: El sistema debe permitir configurar y aplicar reglas de cancelación y políticas de tarifas según las políticas y reglas establecidas por cada hotel en particular.

  - Criterios de aceptación:
    - El sistema permite configurar diferentes políticas de cancelación y tarifas para habitaciones y servicios.
    - El sistema aplica automáticamente las reglas de cancelación y tarifas configuradas durante el proceso de reserva.
    - El sistema muestra claramente las políticas de cancelación y tarifas aplicables durante el proceso de reserva.

- **RN2:** El sistema debe verificar la disponibilidad de habitaciones y servicios en tiempo real al realizar una reserva.

  - Descripción: El sistema debe realizar una verificación en tiempo real de la disponibilidad de habitaciones y servicios al recibir una solicitud de reserva, evitando la sobreventa y garantizando la precisión de las reservas.

  - Criterios de aceptación:
    - El sistema muestra la disponibilidad actualizada de habitaciones y servicios durante el proceso de reserva.
    - El sistema bloquea automáticamente las habitaciones y servicios seleccionados para evitar reservas duplicadas.
    - El sistema muestra un mensaje de error si no hay disponibilidad para las fechas solicitadas.

- **RN3:** El sistema debe aplicar impuestos y cargos adicionales según las regulaciones y políticas locales.

  - Descripción: El sistema debe aplicar automáticamente los impuestos y cargos adicionales correspondientes de acuerdo con las regulaciones y políticas locales establecidas para el hotel.

  - Criterios de aceptación:
    - El sistema aplica los impuestos y cargos adicionales correspondientes a las reservas y servicios.
    - Los impuestos y cargos adicionales se calculan correctamente según las regulaciones y políticas locales.
    - El sistema muestra el desglose de los impuestos y cargos adicionales en las facturas generadas.

## Requisito de interesado

- **RI1:** El sistema debe permitir a los propietarios y gerentes del hotel acceder a información financiera en tiempo real.

  - Descripción: Los propietarios y gerentes del hotel deben poder acceder a informes y datos financieros actualizados en tiempo real para monitorear el desempeño y tomar decisiones informadas.

  - Criterios de aceptación:
    - Los propietarios y gerentes pueden acceder a informes financieros en tiempo real a través de una interfaz segura.
    - Los informes financieros incluyen datos actualizados sobre ingresos, gastos y rentabilidad del hotel.
    - Los informes financieros se pueden personalizar y generar según los requisitos específicos de los propietarios y gerentes.

- **RI2:** El sistema debe ofrecer una interfaz intuitiva y fácil de usar para el personal del hotel.

  - Descripción: El sistema debe contar con una interfaz de usuario intuitiva y amigable para que el personal del hotel pueda realizar tareas de manera eficiente y sin dificultades.

- Criterios de aceptación:

  - La interfaz del sistema es fácil de navegar y entender para el personal del hotel.
  - Las funciones y características del sistema se presentan de forma clara y accesible.
  - El sistema proporciona instrucciones y ayuda contextual para facilitar la realización de tareas.

- **RI3:** El sistema debe proporcionar una experiencia de reserva personalizada para los huéspedes.

  - Descripción: El sistema debe permitir la personalización de la experiencia de reserva para los huéspedes, teniendo en cuenta sus preferencias y necesidades individuales.

  - Criterios de aceptación:
    - Los huéspedes pueden seleccionar y personalizar opciones adicionales, como servicios especiales o preferencias de habitación.
    - El sistema registra y almacena las preferencias de los huéspedes para futuras estancias.
    - El sistema muestra recomendaciones y ofertas personalizadas basadas en las preferencias de los huéspedes.

## Atributo de calidad

- **AC1:** El sistema debe ser seguro y proteger la información confidencial de los huéspedes.

  - Descripción: El sistema debe implementar medidas de seguridad adecuadas para proteger la información personal y confidencial de los huéspedes, como datos de tarjetas de crédito y datos de identificación.

  - Criterios de aceptación:
    - El sistema utiliza protocolos de seguridad para proteger la transmisión de datos sensibles.
    - La información personal y financiera de los huéspedes se almacena de forma segura y encriptada.
    - El acceso al sistema está restringido a usuarios autorizados a través de autenticación segura.

- **AC2:** El sistema debe tener un alto rendimiento y responder rápidamente a las solicitudes de los usuarios.

  - Descripción: El sistema debe ser capaz de manejar un alto volumen de solicitudes de usuarios y proporcionar respuestas rápidas y eficientes en todo momento.

  - Criterios de aceptación:
    - El sistema responde a las solicitudes de reserva y consultas de los usuarios en un tiempo aceptable.
    - El sistema mantiene un rendimiento óptimo incluso en momentos de alta demanda.
    - El tiempo de carga de la interfaz del sistema es rápido y no genera retrasos significativos para los usuarios.

- **AC3:** El sistema debe ser confiable y estar disponible las 24 horas del día, los 7 días de la semana.

  - Descripción: El sistema debe ser confiable y estar disponible continuamente para garantizar el acceso y la funcionalidad ininterrumpida para los usuarios.

  - Criterios de aceptación:

    - El sistema tiene una alta disponibilidad, con un tiempo de inactividad mínimo planificado.
    - Se realizan copias de seguridad periódicas de los datos del sistema para garantizar su integridad y recuperación en caso de fallos.
    - El sistema es capaz de recuperarse rápidamente de errores o fallas sin perder datos críticos.

## Requisito funcional

- **RF1:** El sistema debe permitir a los usuarios realizar búsquedas de disponibilidad de habitaciones por fechas y otros criterios.

  - Descripción: Los usuarios deben poder realizar búsquedas de disponibilidad de habitaciones según las fechas deseadas y otros criterios, como tipo de habitación o número de huéspedes.

  - Criterios de aceptación:
    - Los usuarios pueden seleccionar fechas de check-in y check-out deseadas.
    - Los usuarios pueden aplicar filtros adicionales, como tipo de habitación, categoría o comodidades.
    - El sistema muestra los resultados de disponibilidad de habitaciones según los criterios de búsqueda ingresados.

- **RF2:** El sistema debe enviar notificaciones automáticas de confirmación de reserva a los huéspedes y al personal del hotel.

  - Descripción: El sistema debe enviar automáticamente notificaciones de confirmación de reserva a los huéspedes que hayan realizado una reserva exitosa, así como a los miembros del personal del hotel encargados de gestionar las reservas.

  - Criterios de aceptación:
    - Los huéspedes reciben una notificación automática de confirmación por correo electrónico después de realizar una reserva.
    - El personal del hotel recibe notificaciones automáticas de nuevas reservas realizadas por los huéspedes.
    - Las notificaciones incluyen detalles de la reserva, como fechas, tipo de habitación y servicios adicionales seleccionados.

- **RF3:** El sistema debe generar informes financieros periódicos sobre ingresos, gastos y rendimiento del hotel.

  - Descripción: El sistema debe ser capaz de generar informes financieros periódicos que proporcionen información sobre los ingresos generados, los gastos incurridos y el rendimiento general del hotel.

  - Criterios de aceptación:
    - El sistema permite generar informes financieros periódicos, como informes mensuales, trimestrales o anuales.
    - Los informes financieros incluyen información detallada sobre los ingresos por habitación, servicios y otras fuentes.
    - Los informes muestran un análisis comparativo de los gastos y los ingresos, así como métricas de rendimiento clave.

## Requisito no funcional

- **RNF1:** El sistema debe ser compatible con diferentes navegadores web y dispositivos móviles.

  - Descripción: El sistema debe ser compatible y funcionar correctamente en una variedad de navegadores web populares y dispositivos móviles, garantizando una experiencia consistente para los usuarios.

  - Criterios de aceptación:
    - El sistema se prueba y es compatible con navegadores web comunes, como Google Chrome, Mozilla Firefox, Safari y Microsoft Edge.
  - El sistema se adapta y muestra correctamente en diferentes tamaños de pantalla y resoluciones en dispositivos móviles.

- **RNF2:** El sistema debe cumplir con los estándares de accesibilidad web para garantizar su uso por personas con discapacidades.

  - Descripción: El sistema debe responder a las operaciones principales, como la realización de una reserva o la generación de una factura, en un tiempo aceptable para proporcionar una experiencia de usuario fluida.

  - Criterios de aceptación:
    - El sistema completa las operaciones principales, como reservas y facturación, en un tiempo máximo de X segundos.
    - Las acciones del sistema, como cargar una página o procesar una solicitud, no generan demoras significativas.

- **RNF3:** El sistema debe tener una interfaz multilingüe para atender a huéspedes internacionales.

  - Descripción: El sistema debe ofrecer una interfaz de usuario que admita múltiples idiomas, permitiendo a los huéspedes utilizar el sistema en su idioma preferido.

  - Criterios de aceptación:
    - El sistema proporciona una opción para que los usuarios seleccionen su idioma preferido.
    - La interfaz del sistema se traduce y muestra correctamente en los idiomas seleccionados.
    - Los mensajes y notificaciones generados por el sistema se envían en el idioma seleccionado por el huésped.

## Restricción

- **RE1:** El sistema debe estar disponible para su uso en múltiples hoteles simultáneamente.

  - Descripción: El sistema debe tener la capacidad de ser utilizado de manera concurrente por varios hoteles, permitiendo que cada hotel gestione sus propias operaciones de manera independiente.

  - Criterios de aceptación:

    - El sistema puede admitir la creación y gestión de múltiples instancias de hotel dentro de una sola plataforma.
    - Cada hotel puede acceder y utilizar el sistema de forma independiente, sin interferir con otras propiedades hoteleras.
    - La configuración y personalización del sistema se pueden realizar de manera individualizada para cada hotel.

- **RE2:** El sistema debe cumplir con las regulaciones de protección de datos y privacidad.

  - Descripción: El sistema debe cumplir con las leyes y regulaciones aplicables relacionadas con la protección de datos y la privacidad de los huéspedes, garantizando un tratamiento adecuado y seguro de la información personal.

  - Criterios de aceptación:
    - El sistema cumple con las regulaciones locales y regionales de protección de datos, como el GDPR en la Unión Europea.
    - Los huéspedes tienen la opción de otorgar su consentimiento para el procesamiento de sus datos personales.
    - Se implementan medidas técnicas y organizativas para proteger los datos personales de accesos no autorizados o uso indebido.

- **RE3:** El sistema debe estar basado en la nube para permitir un acceso fácil y una escalabilidad flexible.

  - Descripción: El sistema debe estar alojado en la nube, lo que permite un acceso conveniente desde cualquier ubicación y facilita la capacidad de escalar recursos según las necesidades del hotel.

  - Criterios de aceptación:

    - El sistema se encuentra alojado en una plataforma de computación en la nube confiable y segura.
    - Los usuarios pueden acceder al sistema a través de un navegador web o una aplicación móvil con conexión a Internet.
    - El sistema puede adaptarse a la demanda y manejar un aumento en el número de usuarios o transacciones sin afectar el rendimiento.

## Interfaz externa

- **IE1:** El sistema debe integrarse con pasarelas de pago externas para procesar transacciones seguras.
  -Descripción: El sistema debe ser capaz de integrarse con un sistema de pago en línea, como PayPal o una pasarela de pago, para procesar transacciones y cobrar a los huéspedes por las reservas y servicios.

  - Criterios de aceptación:

    - El sistema permite a los usuarios realizar pagos en línea de forma segura.
    - El sistema registra y actualiza automáticamente los pagos realizados por los huéspedes en la base de datos del sistema.
    - Los datos de pago del huésped se mantienen seguros y no se almacenan en el sistema HotelSuite.

- **IE2:** El sistema debe integrarse con proveedores externos de servicios turísticos para ofrecer opciones adicionales a los huéspedes.

  - Descripción: El sistema debe permitir la integración con proveedores externos de servicios turísticos, como agencias de viajes en línea, para proporcionar a los huéspedes opciones adicionales, como tours, actividades o alquiler de automóviles.

  - Criterios de aceptación:

    - El sistema puede intercambiar datos de disponibilidad y precios con los proveedores externos.
    - Los huéspedes pueden acceder y reservar servicios adicionales a través del sistema.
    - La disponibilidad y los detalles de los servicios externos se actualizan en tiempo real en el sistema.

- **IE3:** El sistema debe integrarse con sistemas de contabilidad externos para facilitar la gestión financiera del hotel.

  - Descripción: El sistema debe tener la capacidad de integrarse con sistemas de contabilidad externos, como software de contabilidad, para simplificar la gestión financiera y el seguimiento de las transacciones del hotel.

  - Criterios de aceptación:

    - El sistema puede exportar datos financieros relevantes, como ingresos y gastos, en un formato compatible con los sistemas de contabilidad.
    - Los datos financieros se transfieren de manera segura y precisa al sistema de contabilidad externo.
    - Los informes financieros generados por el sistema se basan en datos precisos y actualizados provenientes del sistema de contabilidad.
