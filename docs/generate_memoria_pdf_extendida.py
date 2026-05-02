from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Spacer, PageBreak

import generate_memoria_pdf as base


OUTPUT_PATH = "/Users/marinamr/Downloads/Memoria TFG (1).pdf"
p = base.p
bullet_list = base.bullet_list
add_heading = base.add_heading
add_sub = base.add_sub


def req_block(code, title, funcionalidad, tareas, pruebas):
    flow = []
    flow.append(p(f"<b>{code}</b> - {title}", "SubSection"))
    flow.append(p(funcionalidad, "BodyJ"))
    if tareas:
        flow.append(p("<b>Tareas de implementación</b>", "Small"))
        flow.append(bullet_list(tareas))
    if pruebas:
        flow.append(p("<b>Pruebas asociadas</b>", "Small"))
        flow.append(bullet_list(pruebas))
    return flow


def story_extendida():
    story = []

    story.append(Spacer(1, 3.2 * cm))
    story.append(p("Desarrollo de una web multiplataforma para la gestión de comandas de un restaurante", "TitleCenter"))
    story.append(p("2º Desarrollo de Aplicaciones Multiplataforma", "SubSection"))
    story.append(Spacer(1, 1 * cm))
    story.append(p("Marina Moreno Rodríguez", "SubSection"))
    story.append(p("Memoria técnica desarrollada y adaptada al proyecto Orsy", "BodyJ"))
    story.append(PageBreak())

    add_heading(story, "DEDICATORIA (OPCIONAL)")
    story.append(p(
        "A mi familia, por el apoyo constante durante todo el proceso de aprendizaje y desarrollo, y a las personas que me han acompañado en este proyecto.",
        "BodyJ",
    ))
    story.append(PageBreak())

    add_heading(story, "ÍNDICES")
    story.append(bullet_list([
        "Abstract",
        "Justificación del proyecto",
        "Introducción",
        "Objetivos",
        "Requisitos funcionales y técnicos del proyecto",
        "Descripción",
        "Arquitectura del sistema",
        "Arquitectura en capas del backend",
        "Casos de uso",
        "Diagrama de clases",
        "Diagrama entidad-relación",
        "Diseño de la base de datos",
        "Diagrama de navegación",
        "Seguridad del sistema",
        "Tecnología",
        "Metodología",
        "Presupuesto",
        "Control de versiones",
        "Trabajos futuros",
        "Valor funcional del sistema",
        "Conclusiones",
        "Referencias",
    ]))
    story.append(PageBreak())

    add_heading(story, "ABSTRACT")
    story.append(p(
        "Este proyecto consiste en el desarrollo de una aplicación web para la gestión de comandas en un restaurante. "
        "La solución está pensada para digitalizar el trabajo diario del personal de sala, permitiendo controlar el estado de las mesas, "
        "abrir comandas, añadir productos, cerrar pedidos y consultar informes de ventas. El sistema incorpora además un módulo de administración "
        "para gestionar usuarios, productos, categorías y el plano de sala.",
        "BodyJ",
    ))
    story.append(p(
        "A nivel técnico, la aplicación sigue una arquitectura cliente-servidor. El frontend está desarrollado con HTML, CSS y JavaScript, "
        "mientras que el backend se implementa mediante Spring Boot como una API REST. La seguridad se apoya en Spring Security y el almacenamiento "
        "de la información se realiza en PostgreSQL. El acceso se organiza mediante roles diferenciados, y la autenticación utiliza PIN de 4 dígitos, "
        "adecuado para un entorno de uso rápido como el de un restaurante.",
        "BodyJ",
    ))
    story.append(p(
        "El objetivo principal del proyecto es mejorar la eficiencia de la operativa diaria, reducir errores en la toma y gestión de comandas "
        "y ofrecer una herramienta sencilla, usable y adaptable a dispositivos de escritorio, tablet y móvil.",
        "BodyJ",
    ))
    story.append(p(
        "This project consists of developing a web application for restaurant order management. The system allows staff to control tables, create "
        "and update orders, manage products, and generate sales reports. The frontend is built with HTML, CSS and JavaScript, while the backend "
        "is implemented as a Spring Boot REST API connected to PostgreSQL. Authentication and authorization are handled through Spring Security, "
        "using four-digit PIN credentials suitable for fast use in a real restaurant environment.",
        "BodyJ",
    ))
    story.append(PageBreak())

    add_heading(story, "JUSTIFICACIÓN DEL PROYECTO")
    story.append(p(
        "La idea de este proyecto surge de una situación habitual en muchos restaurantes pequeños y medianos: la gestión de mesas y comandas "
        "todavía se realiza con papel, libretas o soluciones poco integradas. Esto provoca errores frecuentes, dificultad para mantener un control "
        "claro del estado de la sala y poca capacidad para analizar posteriormente las ventas realizadas.",
        "BodyJ",
    ))
    story.append(p(
        "En un contexto de servicio real, la rapidez y la claridad son fundamentales. Un camarero necesita saber en pocos segundos qué mesas están libres, "
        "cuáles tienen una comanda abierta y qué productos se han registrado en cada una. Al mismo tiempo, el responsable del establecimiento necesita "
        "poder mantener actualizado el catálogo de productos, controlar los usuarios con acceso al sistema y consultar un resumen de la actividad del negocio.",
        "BodyJ",
    ))
    story.append(p(
        "Aunque existen soluciones comerciales para este tipo de necesidades, muchas de ellas presentan inconvenientes para pequeños negocios: "
        "coste elevado, complejidad de uso, dependencias con hardware específico o dificultad para adaptar la herramienta a flujos de trabajo concretos. "
        "Por ello, Orsy se plantea como una alternativa propia, modular y comprensible, pensada para cubrir las necesidades reales de un restaurante sin "
        "sobrecargar al usuario con funciones innecesarias.",
        "BodyJ",
    ))
    story.append(p(
        "La aplicación también tiene valor académico, ya que permite integrar en un mismo proyecto conocimientos de análisis, diseño de bases de datos, "
        "desarrollo frontend, desarrollo backend, seguridad, arquitectura software y documentación técnica.",
        "BodyJ",
    ))
    story.append(PageBreak())

    add_heading(story, "INTRODUCCIÓN")
    story.append(p(
        "Orsy es una aplicación web destinada a la gestión integral del flujo de trabajo de un restaurante. El sistema se centra en la operativa de sala, "
        "pero no se limita a la toma de pedidos: también aborda la administración de productos, la organización del plano de mesas, el control de usuarios "
        "y la generación de informes a partir de la actividad registrada.",
        "BodyJ",
    ))
    story.append(p(
        "Desde el punto de vista del usuario, la aplicación ofrece diferentes vistas según el rol y el dispositivo. En escritorio se mantiene una navegación "
        "completa para administradores, mientras que en tablet y móvil la experiencia está simplificada para favorecer un uso más rápido durante el servicio. "
        "Esto permite adaptar la herramienta a distintos contextos de trabajo sin cambiar la lógica central del sistema.",
        "BodyJ",
    ))
    story.append(p(
        "Desde el punto de vista técnico, el proyecto adopta una arquitectura cliente-servidor con separación clara de responsabilidades. "
        "El frontend renderiza la interfaz y consume datos desde el backend. El backend aplica autenticación, permisos, validaciones y persistencia. "
        "La base de datos mantiene el estado del sistema de forma consistente entre sesiones y dispositivos.",
        "BodyJ",
    ))
    story.append(PageBreak())

    add_heading(story, "OBJETIVOS")
    story.append(p("El objetivo general del proyecto es desarrollar una aplicación web que permita gestionar de forma eficiente las comandas y mesas de un restaurante.", "BodyJ"))
    story.append(p("A partir de este objetivo general se definen los siguientes objetivos específicos:", "BodyJ"))
    story.append(bullet_list([
        "Diseñar una aplicación web intuitiva para la visualización de la sala.",
        "Permitir la creación, seguimiento y cierre de comandas asociadas a cada mesa.",
        "Desarrollar un sistema de gestión de productos y categorías.",
        "Implementar autenticación con roles diferenciados entre administrador y empleado.",
        "Facilitar el acceso rápido mediante PIN de 4 dígitos.",
        "Desarrollar un módulo de informes que permita analizar la actividad del restaurante.",
        "Implementar una arquitectura modular y mantenible basada en frontend, backend y base de datos.",
        "Adaptar la interfaz a escritorio, tablet y móvil.",
    ]))
    story.append(PageBreak())

    add_heading(story, "REQUISITOS FUNCIONALES Y TÉCNICOS DEL PROYECTO")
    story.append(p(
        "En esta sección se describen los requisitos del sistema organizados por bloques funcionales. Se mantienen numerados para facilitar la "
        "trazabilidad entre análisis, implementación y pruebas.",
        "BodyJ",
    ))

    for block in req_block(
        "R01",
        "El sistema debe permitir el registro y la autenticación de usuarios con roles diferenciados",
        "El sistema debe permitir crear usuarios, autenticar credenciales y restringir el acceso a determinadas funcionalidades en función del rol asignado.",
        [
            "Crear la entidad `Usuario` con los campos id, nombre, email, password y rol.",
            "Imponer `email` como campo único y obligatorio.",
            "Implementar cifrado del PIN con BCrypt en backend.",
            "Configurar `AuthController` con login por email+PIN y por PIN en dispositivos.",
            "Configurar Spring Security para proteger endpoints sensibles.",
            "Ocultar acciones de administrador en el frontend cuando el usuario autenticado es empleado.",
        ],
        [
            "Login correcto con credenciales válidas.",
            "Login incorrecto con credenciales erróneas.",
            "Acceso denegado a endpoints de administración cuando el usuario es EMPLEADO.",
            "Persistencia correcta de la sesión en frontend.",
        ],
    ):
        story.append(block)

    for block in req_block(
        "R02",
        "El sistema debe permitir gestionar productos y categorías",
        "El sistema debe ofrecer un catálogo de productos clasificados por categorías, editable por el administrador y consultable por el empleado durante la creación de comandas.",
        [
            "Crear las entidades `Producto` y `Categoria` y su relación ManyToOne.",
            "Implementar `ProductoController` y `CategoriaController` con operaciones CRUD.",
            "Construir la vista `productos.html` con filtros y agrupación por categorías.",
            "Implementar validación de precio y asociación con categoría existente.",
        ],
        [
            "Creación de categoría y producto.",
            "Edición de precio o categoría.",
            "Borrado de un producto.",
            "Visualización correcta del catálogo en la pantalla de comanda.",
        ],
    ):
        story.append(block)

    for block in req_block(
        "R03",
        "El sistema debe permitir gestionar mesas y plano de sala",
        "El sistema debe representar visualmente las mesas del restaurante y conservar su estado y posición dentro del plano.",
        [
            "Crear la entidad `Mesa` con número, capacidad, estado y coordenadas `x`,`y`.",
            "Construir la vista `sala.html` para dibujar el plano.",
            "Implementar operaciones CRUD de mesas en `MesaController`.",
            "Permitir al administrador arrastrar mesas y guardar coordenadas actualizadas.",
            "Actualizar el estado visual de la mesa según esté libre, ocupada o pendiente.",
        ],
        [
            "Persistencia de posición tras recargar la página.",
            "Cambio de estado tras enviar o cobrar una comanda.",
            "Restricción de edición del plano solo para ADMIN.",
        ],
    ):
        story.append(block)

    for block in req_block(
        "R04",
        "El sistema debe permitir gestionar comandas",
        "La aplicación debe soportar la creación de comandas asociadas a una mesa, la adición de productos, el cálculo del total y la actualización del estado del pedido.",
        [
            "Crear las entidades `Comanda`, `LineaComanda` y los DTO asociados.",
            "Implementar `ComandaController` para creación, consulta, actualización y borrado.",
            "Permitir cargar una comanda activa por mesa.",
            "Reflejar el total del ticket de forma automática en frontend.",
            "Cambiar el estado de la mesa al enviar, cerrar o cobrar una comanda.",
        ],
        [
            "Creación correcta de comanda con líneas.",
            "Recuperación de una comanda abierta por mesa.",
            "Actualización de estado a CERRADA o COBRADA.",
            "Recalculado correcto del total a partir de la cantidad y el precio de cada línea.",
        ],
    ):
        story.append(block)

    for block in req_block(
        "R05",
        "El sistema debe permitir generar informes de ventas",
        "El sistema debe ofrecer un resumen visual de la actividad económica del restaurante basado en las comandas cobradas.",
        [
            "Crear la vista `informes.html` accesible solo por administradores.",
            "Consultar las comandas cobradas desde el backend.",
            "Calcular total facturado, número de tickets, ticket medio y producto estrella.",
            "Representar la información mediante Chart.js en formato de barras y doughnut.",
        ],
        [
            "Cálculo correcto de indicadores.",
            "Exclusión de comandas no cobradas en los informes.",
            "Visualización correcta de gráficos.",
        ],
    ):
        story.append(block)

    for block in req_block(
        "R06",
        "El sistema debe ser accesible vía web y usable en varios dispositivos",
        "La aplicación debe poder utilizarse desde navegador y adaptarse a escritorio, tablet y móvil.",
        [
            "Implementar frontend web con HTML, CSS y JavaScript.",
            "Crear estilos responsive en `styles.css`.",
            "Limitar navegación en dispositivos a las pantallas necesarias para el servicio.",
            "Simplificar el login en tablet y móvil con teclado PIN.",
        ],
        [
            "Carga correcta de la interfaz en escritorio.",
            "Adaptación visual a tablet.",
            "Adaptación visual a móvil.",
            "Acceso funcional mediante PIN en dispositivos.",
        ],
    ):
        story.append(block)

    story.append(PageBreak())

    add_heading(story, "DESCRIPCIÓN")
    add_sub(story, "Descripción funcional del sistema")
    story.append(p(
        "La aplicación está diseñada para seguir el flujo natural de trabajo de un restaurante. El punto de entrada del sistema es el módulo de autenticación. "
        "Una vez validado, el usuario accede a la sala, donde visualiza el estado de las mesas. Desde allí puede entrar en una mesa concreta, abrir una comanda, "
        "añadir productos, cerrar el pedido o proceder al cobro.",
        "BodyJ",
    ))
    story.append(p(
        "En el caso de un administrador, el sistema también permite crear mesas, modificar su posición, gestionar usuarios, mantener actualizado el catálogo de "
        "productos y categorías y consultar informes globales. En el caso de un empleado, el uso se centra en la operativa de sala y comandas.",
        "BodyJ",
    ))
    add_sub(story, "Funcionamiento paso por paso")
    for txt in [
        "1. El usuario accede a la aplicación y se autentica.",
        "2. El frontend almacena la sesión y el perfil del usuario.",
        "3. La pantalla de sala consulta las mesas disponibles y su estado.",
        "4. Si se selecciona una mesa libre, se registra el número de clientes.",
        "5. Se accede a la pantalla de comanda con el identificador de la mesa.",
        "6. La pantalla de comanda consulta productos y la posible comanda abierta.",
        "7. El usuario añade productos, generando o ampliando líneas del ticket.",
        "8. La comanda se envía al backend para persistirla.",
        "9. El estado de la mesa cambia según la operativa: libre, ocupada o pendiente.",
        "10. Si la comanda se cobra, pasa a formar parte de la información usada en informes.",
    ]:
        story.append(p(txt, "BodyJ"))
    add_sub(story, "Pantallas del sistema")
    story.append(bullet_list([
        "login.html: autenticación de usuarios.",
        "sala.html: visualización del plano de mesas.",
        "comanda.html: creación y actualización del pedido de una mesa.",
        "productos.html: gestión del catálogo.",
        "informes.html: visualización de estadísticas de venta.",
        "usuarios.html: gestión de usuarios del sistema.",
    ]))
    story.append(PageBreak())

    add_heading(story, "Arquitectura del sistema")
    story.append(p(
        "La solución sigue una arquitectura cliente-servidor. El frontend se ejecuta en el navegador y delega toda la lógica de persistencia y seguridad en el backend. "
        "El backend expone una API REST, protegida con Spring Security, y utiliza PostgreSQL como sistema de almacenamiento permanente.",
        "BodyJ",
    ))
    story.append(p("Diagrama de arquitectura del sistema", "DiagramTitle"))
    story.append(base.arquitectura_sistema())
    story.append(PageBreak())

    add_heading(story, "Arquitectura en capas del backend")
    story.append(p(
        "El backend adopta una separación en capas para mejorar la claridad del código. Los controladores actúan como punto de entrada HTTP, "
        "los servicios centralizan las reglas de negocio y los repositorios encapsulan el acceso a base de datos. Las entidades representan el modelo de dominio "
        "y los DTO sirven para transportar información entre cliente y servidor cuando es necesario adaptar el formato.",
        "BodyJ",
    ))
    story.append(p("Diagrama de arquitectura en capas del backend", "DiagramTitle"))
    story.append(base.capas_backend())
    story.append(PageBreak())

    add_heading(story, "Casos de uso")
    story.append(p(
        "Los actores principales del sistema son administrador y empleado. Ambos comparten el flujo de autenticación y el trabajo operativo sobre la sala, "
        "pero solo el administrador dispone de funciones de configuración y explotación de datos.",
        "BodyJ",
    ))
    story.append(p("Diagrama de casos de uso", "DiagramTitle"))
    story.append(base.casos_uso())
    story.append(PageBreak())

    add_heading(story, "Diagrama de clases")
    story.append(p(
        "El modelo de clases está formado por las entidades que estructuran el dominio del problema. `Usuario` representa a los actores del sistema, `Mesa` "
        "la organización física del restaurante, `Categoria` y `Producto` el catálogo comercial, `Comanda` el pedido realizado en una mesa, `LineaComanda` "
        "el detalle de los productos servidos y `Venta` una entidad preparada para futuras ampliaciones orientadas a cierre contable independiente.",
        "BodyJ",
    ))
    story.append(p("Diagrama de clases del dominio", "DiagramTitle"))
    story.append(base.diagrama_clases())
    story.append(PageBreak())

    add_heading(story, "Diagrama entidad-relación")
    story.append(p(
        "La base de datos se modela como un conjunto de entidades relacionadas. La relación entre categoría y producto es de uno a muchos, mientras que una mesa "
        "puede tener múltiples comandas a lo largo del tiempo. Cada comanda contiene múltiples líneas, y cada línea referencia un producto. Esta estructura evita "
        "redundancias innecesarias y permite mantener la integridad del dominio.",
        "BodyJ",
    ))
    story.append(p("Diagrama entidad-relación", "DiagramTitle"))
    story.append(base.entidad_relacion())
    story.append(PageBreak())

    add_heading(story, "Diseño de la base de datos")
    story.append(p(
        "El diseño de la base de datos se ha realizado siguiendo una aproximación relacional y atendiendo a criterios de integridad, consistencia y simplicidad. "
        "Cada tabla posee una clave primaria autogenerada y las relaciones entre tablas se representan mediante claves foráneas. En el caso de usuarios, el email "
        "está restringido como único; en el caso de mesas, la posición del plano se conserva mediante coordenadas `x` e `y`; y en el caso de comandas, el estado se "
        "expresa mediante un enum que representa el flujo operativo del pedido.",
        "BodyJ",
    ))
    story.append(p(
        "La tabla `linea_comanda` duplica ciertos datos del producto, como nombre, precio y categoría, con el objetivo de preservar el valor histórico del pedido "
        "en el momento de la compra. Esta decisión evita inconsistencias si posteriormente cambia el catálogo.",
        "BodyJ",
    ))
    story.append(p("Diseño lógico de tablas", "DiagramTitle"))
    story.append(base.diseno_bd())
    story.append(PageBreak())

    add_heading(story, "Diagrama de navegación")
    story.append(p(
        "La navegación general del sistema está centrada en la sala. Después del login, el usuario accede a la pantalla principal del restaurante. Desde ella se entra "
        "en comandas, y dependiendo del rol también puede acceder a productos, informes y usuarios. En dispositivos más pequeños, la navegación se simplifica para "
        "favorecer el uso rápido durante el servicio.",
        "BodyJ",
    ))
    story.append(p("Diagrama de navegación", "DiagramTitle"))
    story.append(base.navegacion())
    story.append(PageBreak())

    add_heading(story, "Seguridad del sistema")
    story.append(p(
        "La seguridad del sistema se apoya en varios mecanismos. En primer lugar, los PIN de los usuarios no se almacenan en texto plano, sino cifrados con BCrypt. "
        "En segundo lugar, el backend protege los endpoints mediante Spring Security y anotaciones `@PreAuthorize`. En tercer lugar, el frontend adapta la interfaz "
        "a los permisos del usuario ocultando opciones que no le corresponden.",
        "BodyJ",
    ))
    story.append(p(
        "Las rutas de autenticación `/auth/login` y `/auth/pin-login` quedan abiertas para permitir el acceso inicial, pero el resto de recursos requieren autenticación. "
        "Las operaciones de administración de productos, categorías, usuarios y edición del plano están restringidas al rol `ADMIN`, mientras que `EMPLEADO` puede operar "
        "sobre sala y comandas.",
        "BodyJ",
    ))
    story.append(p("Diagrama de seguridad del sistema", "DiagramTitle"))
    story.append(base.seguridad())
    story.append(PageBreak())

    add_heading(story, "TECNOLOGÍA")
    add_sub(story, "HTML")
    story.append(p("Se utiliza para estructurar las páginas del sistema: login, sala, comanda, productos, informes y usuarios.", "BodyJ"))
    add_sub(story, "CSS")
    story.append(p("Define la apariencia visual de la aplicación y el comportamiento responsive adaptado a escritorio, tablet y móvil.", "BodyJ"))
    add_sub(story, "JavaScript")
    story.append(p("Gestiona la interacción del usuario, el consumo de la API y la actualización dinámica del DOM en cada pantalla.", "BodyJ"))
    add_sub(story, "Spring Boot")
    story.append(p("Se utiliza como framework principal del backend para construir la API REST y organizar el proyecto en controladores, servicios y repositorios.", "BodyJ"))
    add_sub(story, "Spring Security")
    story.append(p("Permite implementar autenticación, autorización por roles y protección de endpoints.", "BodyJ"))
    add_sub(story, "PostgreSQL")
    story.append(p("Se utiliza como sistema gestor de base de datos relacional para almacenar la información persistente del sistema.", "BodyJ"))
    add_sub(story, "Chart.js")
    story.append(p("Se integra en el módulo de informes para representar visualmente los datos de ventas.", "BodyJ"))
    story.append(PageBreak())

    add_heading(story, "METODOLOGÍA")
    story.append(p(
        "El desarrollo del proyecto se ha organizado en fases consecutivas, aunque con iteraciones parciales para refinar funcionalidades ya implementadas. "
        "El proceso puede resumirse en análisis, diseño, implementación, integración, pruebas y documentación.",
        "BodyJ",
    ))
    story.append(bullet_list([
        "Análisis del problema y de las necesidades del restaurante.",
        "Modelado inicial de entidades y relaciones.",
        "Diseño de pantallas principales.",
        "Implementación del backend y de la base de datos.",
        "Implementación del frontend y conexión con la API.",
        "Aplicación de seguridad y control de permisos.",
        "Adaptación responsive y revisión funcional.",
        "Redacción de la memoria final.",
    ]))
    story.append(PageBreak())

    add_heading(story, "PRESUPUESTO")
    story.append(p(
        "Tomando como referencia una dedicación estimada de 100 horas de trabajo entre análisis, desarrollo, pruebas y documentación, y valorando la hora de trabajo "
        "en 20 €, el coste orientativo del proyecto se sitúa en 2.000 €. Esta cifra se presenta como una estimación académica y no como presupuesto cerrado.",
        "BodyJ",
    ))
    add_heading(story, "CONTROL DE VERSIONES")
    story.append(p(
        "El proyecto se ha gestionado con Git, lo que permite registrar la evolución del código, mantener trazabilidad sobre las modificaciones realizadas y recuperar "
        "versiones anteriores del sistema en caso necesario.",
        "BodyJ",
    ))
    story.append(PageBreak())

    add_heading(story, "TRABAJOS FUTUROS")
    story.append(bullet_list([
        "Sincronización en tiempo real entre varios dispositivos.",
        "Impresión automática de comandas en cocina.",
        "Integración con TPV o pasarelas de pago.",
        "Reserva de mesas y planificación previa.",
        "Módulo de inventario.",
        "Informes más avanzados por franjas horarias o familias de productos.",
        "Panel de administración más completo y visual.",
    ]))
    story.append(PageBreak())

    add_heading(story, "VALOR FUNCIONAL DEL SISTEMA")
    story.append(p(
        "El sistema desarrollado tiene un valor funcional claro porque responde a una necesidad concreta de negocio. No se trata de una práctica aislada, sino de una "
        "herramienta que reproduce un flujo de trabajo real: apertura de mesas, gestión de pedidos, control de usuarios y análisis de ventas. La interfaz visual y la "
        "separación por roles hacen que la aplicación sea comprensible, defendible y usable en un entorno de restauración.",
        "BodyJ",
    ))
    story.append(PageBreak())

    add_heading(story, "CONCLUSIONES")
    story.append(p(
        "El proyecto ha permitido desarrollar una aplicación web completa integrando frontend, backend, seguridad y base de datos. Además de cumplir con los objetivos "
        "planteados, ha servido para aplicar de forma práctica conocimientos de arquitectura cliente-servidor, modelado relacional, autenticación y diseño de interfaces.",
        "BodyJ",
    ))
    story.append(p(
        "Uno de los aspectos más relevantes ha sido la construcción de una lógica de negocio coherente con el contexto de un restaurante, especialmente en la gestión "
        "del ciclo de vida de las comandas y en el control del estado de las mesas. También ha sido importante la adaptación responsive, ya que la aplicación debe poder "
        "utilizarse tanto en escritorio como en dispositivos táctiles.",
        "BodyJ",
    ))
    story.append(p(
        "En conjunto, Orsy constituye una solución funcional y técnicamente sólida, alineada con un caso real de negocio y suficientemente modular como para admitir "
        "ampliaciones futuras.",
        "BodyJ",
    ))
    story.append(PageBreak())

    add_heading(story, "REFERENCIAS")
    story.append(bullet_list([
        "Spring Boot Documentation: https://spring.io/projects/spring-boot",
        "Spring Security Documentation: https://spring.io/projects/spring-security",
        "PostgreSQL Documentation: https://www.postgresql.org/docs/",
        "Chart.js Documentation: https://www.chartjs.org/",
        "MDN Web Docs (HTML, CSS, JavaScript): https://developer.mozilla.org/",
        "REST API Tutorial: https://restfulapi.net/",
    ]))

    return story


def add_page_number(canvas, doc):
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#5A151E"))
    canvas.drawRightString(19.2 * cm, 1.2 * cm, f"{doc.page}")


def main():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=1.8 * cm,
        title="Memoria TFG Orsy extendida",
        author="Marina Moreno Rodríguez",
    )
    doc.build(story_extendida(), onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    main()
