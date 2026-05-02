from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    ListFlowable,
    ListItem,
    KeepTogether,
)


OUTPUT_PATH = "/Users/marinamr/Downloads/Memoria TFG (2).pdf"


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleCenter",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontName="Helvetica-Bold",
    fontSize=20,
    leading=24,
    spaceAfter=18,
))
styles.add(ParagraphStyle(
    name="Section",
    parent=styles["Heading1"],
    fontName="Helvetica-Bold",
    fontSize=16,
    leading=20,
    spaceBefore=10,
    spaceAfter=10,
    textColor=colors.HexColor("#5A151E"),
))
styles.add(ParagraphStyle(
    name="SubSection",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=12,
    leading=15,
    spaceBefore=8,
    spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="SubSub",
    parent=styles["Heading3"],
    fontName="Helvetica-Bold",
    fontSize=10.5,
    leading=13,
    spaceBefore=6,
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="BodyJ",
    parent=styles["BodyText"],
    alignment=TA_JUSTIFY,
    fontName="Helvetica",
    fontSize=10,
    leading=14,
    spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="Small",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=9,
    leading=12,
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="DiagramTitle",
    parent=styles["Heading3"],
    alignment=TA_CENTER,
    fontName="Helvetica-Bold",
    fontSize=11,
    textColor=colors.HexColor("#5A151E"),
    spaceBefore=8,
    spaceAfter=8,
))


def p(text, style="BodyJ"):
    return Paragraph(text, styles[style])


def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(item, styles["BodyJ"])) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=18,
    )


def add_heading(story, title):
    story.append(p(title, "Section"))


def add_sub(story, title):
    story.append(p(title, "SubSection"))


def add_subsub(story, title):
    story.append(p(title, "SubSub"))


def architecture_diagram():
    d = Drawing(17 * cm, 7 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    boxes = [
        (0.3 * cm, 2.2 * cm, 3.2 * cm, 2 * cm, "Usuario\nAdministrador / Empleado"),
        (4.4 * cm, 2.2 * cm, 4 * cm, 2 * cm, "Frontend Web\nHTML + CSS + JavaScript"),
        (9.3 * cm, 2.2 * cm, 3.4 * cm, 2 * cm, "API REST\nSpring Boot"),
        (13.4 * cm, 2.2 * cm, 3.2 * cm, 2 * cm, "PostgreSQL\nrestaurante_db"),
    ]
    for x, y, w, h, t in boxes:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill, rx=8, ry=8))
        yy = y + h - 0.55 * cm
        for line in t.split("\n"):
            d.add(String(x + w / 2, yy, line, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9))
            yy -= 0.42 * cm
    d.add(Line(3.5 * cm, 3.2 * cm, 4.4 * cm, 3.2 * cm, strokeColor=stroke))
    d.add(Line(8.4 * cm, 3.2 * cm, 9.3 * cm, 3.2 * cm, strokeColor=stroke))
    d.add(Line(12.7 * cm, 3.2 * cm, 13.4 * cm, 3.2 * cm, strokeColor=stroke))
    return d


def backend_layers_diagram():
    d = Drawing(12 * cm, 10 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    layers = [
        (1 * cm, 7.4 * cm, 10 * cm, 1.6 * cm, "Capa Controller\nControladores REST"),
        (1 * cm, 5.2 * cm, 10 * cm, 1.6 * cm, "Capa Service\nLógica de negocio"),
        (1 * cm, 3.0 * cm, 10 * cm, 1.6 * cm, "Capa Repository\nPersistencia JPA"),
        (1 * cm, 0.8 * cm, 10 * cm, 1.6 * cm, "Base de datos\nPostgreSQL"),
    ]
    for x, y, w, h, t in layers:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill, rx=8, ry=8))
        yy = y + h - 0.55 * cm
        for line in t.split("\n"):
            d.add(String(x + w / 2, yy, line, textAnchor="middle", fontName="Helvetica-Bold", fontSize=10))
            yy -= 0.45 * cm
    for y1, y2 in [(7.4, 6.8), (5.2, 4.6), (3.0, 2.4)]:
        d.add(Line(6 * cm, y1 * cm, 6 * cm, y2 * cm, strokeColor=stroke))
    return d


def use_case_diagram():
    d = Drawing(17 * cm, 9 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    d.add(Circle(1.6 * cm, 6.8 * cm, 0.45 * cm, strokeColor=stroke))
    d.add(String(1.6 * cm, 5.9 * cm, "Administrador", textAnchor="middle", fontName="Helvetica", fontSize=9))
    d.add(Circle(1.6 * cm, 2.4 * cm, 0.45 * cm, strokeColor=stroke))
    d.add(String(1.6 * cm, 1.5 * cm, "Empleado", textAnchor="middle", fontName="Helvetica", fontSize=9))
    use_cases = [
        (6.6 * cm, 7.2 * cm, 4.9 * cm, 1 * cm, "Iniciar sesión"),
        (6.6 * cm, 5.8 * cm, 4.9 * cm, 1 * cm, "Ver sala"),
        (6.6 * cm, 4.4 * cm, 4.9 * cm, 1 * cm, "Gestionar comanda"),
        (6.6 * cm, 3.0 * cm, 4.9 * cm, 1 * cm, "Gestionar productos"),
        (6.6 * cm, 1.6 * cm, 4.9 * cm, 1 * cm, "Consultar informes"),
        (12.2 * cm, 4.4 * cm, 3.7 * cm, 1 * cm, "Gestionar usuarios"),
        (12.2 * cm, 3.0 * cm, 3.7 * cm, 1 * cm, "Editar sala"),
    ]
    for x, y, w, h, t in use_cases:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill, rx=8, ry=8))
        d.add(String(x + w / 2, y + 0.38 * cm, t, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9))
    for target_y in [7.7, 6.3, 4.9, 3.5, 2.1]:
        d.add(Line(2.05 * cm, 6.8 * cm, 6.6 * cm, target_y * cm, strokeColor=stroke))
    for target_y in [7.7, 6.3, 4.9, 3.5]:
        d.add(Line(2.05 * cm, 2.4 * cm, 6.6 * cm, target_y * cm, strokeColor=stroke))
    d.add(Line(2.05 * cm, 6.8 * cm, 12.2 * cm, 4.9 * cm, strokeColor=stroke))
    d.add(Line(2.05 * cm, 6.8 * cm, 12.2 * cm, 3.5 * cm, strokeColor=stroke))
    return d


def class_diagram():
    d = Drawing(18 * cm, 11 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    classes = [
        (0.5 * cm, 8.2 * cm, 3.4 * cm, 2.2 * cm, "Usuario\nid\nnombre\nemail\npassword\nrol"),
        (4.5 * cm, 8.2 * cm, 3.4 * cm, 2.2 * cm, "Mesa\nid\nnumero\ncapacidad\nestado\nx,y"),
        (8.5 * cm, 8.2 * cm, 3.4 * cm, 2.2 * cm, "Categoria\nid\nnombre"),
        (12.5 * cm, 8.2 * cm, 4.2 * cm, 2.2 * cm, "Producto\nid\nnombre\nprecio\ncategoria"),
        (4.5 * cm, 4.2 * cm, 3.8 * cm, 2.5 * cm, "Comanda\nid\nestado\nfecha\nmesa\nlineas"),
        (9.0 * cm, 4.2 * cm, 4.4 * cm, 2.5 * cm, "LineaComanda\nid\ncantidad\nnombre\nprecio\ncategoria\nproducto"),
        (14.0 * cm, 4.2 * cm, 3.4 * cm, 2.0 * cm, "Venta\nid\nfecha\ntotal\nlineas"),
    ]
    for x, y, w, h, t in classes:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill))
        yy = y + h - 0.42 * cm
        for idx, line in enumerate(t.split("\n")):
            d.add(String(x + (w / 2 if idx == 0 else 0.12 * cm), yy, line, textAnchor="middle" if idx == 0 else "start", fontName="Helvetica-Bold" if idx == 0 else "Helvetica", fontSize=8))
            yy -= 0.32 * cm
    for x1, y1, x2, y2 in [
        (11.9, 9.3, 12.5, 9.3),
        (6.2, 8.2, 6.2, 6.7),
        (10.6, 8.2, 10.6, 6.7),
        (8.3, 5.5, 9.0, 5.5),
        (13.4, 5.2, 14.0, 5.2),
    ]:
        d.add(Line(x1 * cm, y1 * cm, x2 * cm, y2 * cm, strokeColor=stroke))
    return d


def er_diagram():
    d = Drawing(18 * cm, 10.5 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    entities = [
        (0.7 * cm, 7.9 * cm, 3.1 * cm, 1.4 * cm, "USUARIO"),
        (4.5 * cm, 7.9 * cm, 3.1 * cm, 1.4 * cm, "MESA"),
        (8.3 * cm, 7.9 * cm, 3.1 * cm, 1.4 * cm, "CATEGORIA"),
        (12.1 * cm, 7.9 * cm, 3.6 * cm, 1.4 * cm, "PRODUCTO"),
        (4.5 * cm, 4.2 * cm, 3.1 * cm, 1.4 * cm, "COMANDA"),
        (8.3 * cm, 4.2 * cm, 3.8 * cm, 1.4 * cm, "LINEA_COMANDA"),
        (12.8 * cm, 4.2 * cm, 2.9 * cm, 1.4 * cm, "VENTA"),
    ]
    for x, y, w, h, t in entities:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill))
        d.add(String(x + w / 2, y + 0.48 * cm, t, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9))
    for x1, y1, x2, y2 in [
        (11.4, 8.6, 12.1, 8.6),
        (6.0, 7.9, 6.0, 5.6),
        (10.1, 7.9, 10.1, 5.6),
        (7.6, 4.9, 8.3, 4.9),
        (12.1, 4.9, 12.8, 4.9),
    ]:
        d.add(Line(x1 * cm, y1 * cm, x2 * cm, y2 * cm, strokeColor=stroke))
    return d


def nav_diagram():
    d = Drawing(16 * cm, 8.5 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    pages = [
        (6 * cm, 6.9 * cm, 4 * cm, 1.2 * cm, "login.html"),
        (6 * cm, 4.8 * cm, 4 * cm, 1.2 * cm, "sala.html"),
        (0.9 * cm, 2.2 * cm, 4 * cm, 1.2 * cm, "comanda.html"),
        (6 * cm, 2.2 * cm, 4 * cm, 1.2 * cm, "productos.html"),
        (11.1 * cm, 2.2 * cm, 4 * cm, 1.2 * cm, "informes / usuarios"),
    ]
    for x, y, w, h, t in pages:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill, rx=8, ry=8))
        d.add(String(x + w / 2, y + 0.42 * cm, t, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9))
    d.add(Line(8 * cm, 6.9 * cm, 8 * cm, 6.0 * cm, strokeColor=stroke))
    d.add(Line(8 * cm, 4.8 * cm, 2.9 * cm, 3.4 * cm, strokeColor=stroke))
    d.add(Line(8 * cm, 4.8 * cm, 8 * cm, 3.4 * cm, strokeColor=stroke))
    d.add(Line(8 * cm, 4.8 * cm, 13.1 * cm, 3.4 * cm, strokeColor=stroke))
    return d


def security_diagram():
    d = Drawing(17 * cm, 8 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    labels = [
        (0.2 * cm, 5.6 * cm, 2.8 * cm, 1.2 * cm, "Cliente"),
        (3.5 * cm, 5.6 * cm, 3.2 * cm, 1.2 * cm, "Frontend"),
        (7.2 * cm, 5.6 * cm, 3.2 * cm, 1.2 * cm, "AuthController"),
        (10.9 * cm, 5.6 * cm, 2.8 * cm, 1.2 * cm, "Spring Security"),
        (14.2 * cm, 5.6 * cm, 2.4 * cm, 1.2 * cm, "DB"),
    ]
    for x, y, w, h, t in labels:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill, rx=6, ry=6))
        d.add(String(x + w / 2, y + 0.42 * cm, t, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9))
    for x in [1.6, 5.1, 8.8, 12.3, 15.4]:
        d.add(Line(x * cm, 5.6 * cm, x * cm, 0.9 * cm, strokeColor=colors.grey))
    for x1, y1, x2, y2, txt in [
        (1.6, 4.7, 5.1, 4.7, "Introducción de credenciales"),
        (5.1, 4.0, 8.8, 4.0, "POST /auth/login"),
        (8.8, 3.3, 12.3, 3.3, "AuthenticationManager"),
        (12.3, 2.6, 15.4, 2.6, "Buscar usuario"),
        (12.3, 1.9, 5.1, 1.9, "Respuesta autenticada"),
    ]:
        d.add(Line(x1 * cm, y1 * cm, x2 * cm, y2 * cm, strokeColor=stroke))
        d.add(String(((x1 + x2) / 2) * cm, (y1 + 0.1) * cm, txt, textAnchor="middle", fontName="Helvetica", fontSize=8))
    return d


def db_design_diagram():
    d = Drawing(15 * cm, 8 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    tables = [
        (0.5 * cm, 5.3 * cm, 3.2 * cm, 1.1 * cm, "usuario"),
        (4.1 * cm, 5.3 * cm, 3.2 * cm, 1.1 * cm, "mesa"),
        (7.7 * cm, 5.3 * cm, 3.2 * cm, 1.1 * cm, "categoria"),
        (11.3 * cm, 5.3 * cm, 3.2 * cm, 1.1 * cm, "producto"),
        (4.1 * cm, 2.4 * cm, 3.2 * cm, 1.1 * cm, "comanda"),
        (7.7 * cm, 2.4 * cm, 3.2 * cm, 1.1 * cm, "linea_comanda"),
        (11.3 * cm, 2.4 * cm, 3.2 * cm, 1.1 * cm, "venta"),
    ]
    for x, y, w, h, t in tables:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill))
        d.add(String(x + w / 2, y + 0.36 * cm, t, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9))
    for x1, y1, x2, y2 in [
        (10.9, 5.85, 11.3, 5.85),
        (5.7, 5.3, 5.7, 3.5),
        (9.3, 5.3, 9.3, 3.5),
        (7.3, 2.95, 7.7, 2.95),
        (10.9, 2.95, 11.3, 2.95),
    ]:
        d.add(Line(x1 * cm, y1 * cm, x2 * cm, y2 * cm, strokeColor=stroke))
    return d


def repeated_paragraphs(base_texts):
    flow = []
    for t in base_texts:
        flow.append(p(t, "BodyJ"))
    return flow


def build_story():
    story = []

    story.append(Spacer(1, 3.6 * cm))
    story.append(p("Desarrollo de una web multiplataforma para la gestión de comandas de un restaurante", "TitleCenter"))
    story.append(p("2º Desarrollo de Aplicaciones Multiplataforma", "SubSection"))
    story.append(Spacer(1, 1.2 * cm))
    story.append(p("Marina Moreno Rodríguez", "SubSection"))
    story.append(p("Memoria técnica final del proyecto Orsy", "BodyJ"))
    story.append(Spacer(1, 3.8 * cm))
    story.append(p("Tutor: José Manuel", "Small"))
    story.append(PageBreak())

    story.append(PageBreak())

    add_heading(story, "ÍNDICE")
    story.append(bullets([
        "Abstract",
        "Resumen y objetivos",
        "Antecedentes",
        "Análisis de requisitos",
        "Propuesta de solución",
        "Plan de trabajo",
        "Desarrollo",
        "Despliegue e instalación",
        "Evolución / trabajo futuro",
        "Conclusiones",
        "Bibliografía (APA)",
    ]))
    story.append(p(
        "Aunque en un procesador de texto el índice automático es la opción más recomendable, en esta memoria se mantiene una estructura clara y jerarquizada "
        "para que todos los apartados solicitados resulten localizables con facilidad.",
        "BodyJ",
    ))
    story.append(PageBreak())

    add_heading(story, "ABSTRACT")
    story.extend(repeated_paragraphs([
        "This project presents the design and implementation of a multiplatform web application for restaurant order management. The aim of the system is to simplify "
        "the operational workflow of a restaurant by providing tools for table control, order creation, product management, user administration and sales reporting.",
        "The application follows a client-server architecture. The frontend is implemented with HTML, CSS and JavaScript and is responsible for user interaction, "
        "screen rendering and communication with the backend. The backend is implemented in Java using Spring Boot and exposes a REST API protected with Spring Security. "
        "Persistent data is stored in PostgreSQL through Spring Data JPA.",
        "From a functional perspective, the system supports several restaurant processes: user authentication, visual table management, creation and update of orders, "
        "product and category administration, basic sales reporting and role-based access control. The user experience has also been adapted to different devices, "
        "including desktop, tablet and mobile contexts.",
        "The project is relevant because it addresses a realistic business need. Many small and medium-sized restaurants still manage orders manually or with partially "
        "digitalized workflows. Orsy proposes a lighter and more accessible alternative focused on usability, consistency of business rules and maintainability of the code base.",
        "The resulting application is not only a technical exercise but also a practical solution with potential applicability in real hospitality environments. "
        "It also demonstrates the integration of database design, backend architecture, frontend development, security and documentation within a single academic project.",
    ]))
    story.append(PageBreak())

    add_heading(story, "RESUMEN Y OBJETIVOS")
    add_sub(story, "Resumen")
    story.extend(repeated_paragraphs([
        "Orsy es una aplicación web orientada a la gestión de comandas de un restaurante. La idea principal del sistema es centralizar en una única herramienta "
        "las tareas más repetitivas del servicio: consultar el estado de las mesas, abrir comandas, añadir productos, cobrar pedidos y disponer de una visión "
        "general de la actividad del local.",
        "La aplicación está pensada para entornos donde el ritmo de trabajo es alto y los errores manuales tienen un impacto inmediato. En un restaurante, "
        "una comanda mal registrada, una mesa cobrada por duplicado o una descoordinación entre el estado real de la sala y el sistema puede generar retrasos, "
        "mal servicio al cliente y pérdida de control sobre las ventas. Por ello, el proyecto pone el foco en la rapidez de interacción y en la claridad visual.",
        "El sistema diferencia claramente entre dos perfiles de uso. El empleado se centra en la operativa de sala y la gestión de comandas, mientras que el administrador "
        "dispone además de funciones de configuración: usuarios, productos, categorías, edición del plano de mesas e informes. Esta separación permite mantener "
        "un control de permisos coherente con el trabajo real del establecimiento.",
        "A nivel técnico, Orsy se articula como una arquitectura cliente-servidor. El frontend ejecutado en navegador consume una API REST que gestiona autenticación, "
        "reglas de negocio y acceso a datos. La información queda almacenada en PostgreSQL, permitiendo mantener persistencia del estado del sistema entre sesiones "
        "y dispositivos.",
    ]))
    add_sub(story, "Objetivo general")
    story.append(p(
        "Desarrollar una aplicación web multiplataforma que permita gestionar de forma eficiente las comandas y mesas de un restaurante, integrando autenticación, "
        "control de usuarios, persistencia de datos y visualización de información operativa.",
        "BodyJ",
    ))
    add_sub(story, "Objetivos específicos")
    story.append(bullets([
        "Diseñar una interfaz visual para representar la sala del restaurante.",
        "Permitir abrir, actualizar, cerrar y cobrar comandas asociadas a cada mesa.",
        "Mantener un catálogo de productos y categorías editable por el administrador.",
        "Implementar un sistema de usuarios con roles diferenciados.",
        "Desarrollar un acceso ágil mediante PIN de 4 dígitos para contextos de servicio rápido.",
        "Generar informes de ventas a partir de las comandas cobradas.",
        "Separar frontend, backend y base de datos para facilitar mantenimiento y escalabilidad.",
        "Adaptar la interfaz a escritorio, tablet y móvil.",
    ]))
    story.append(PageBreak())

    add_heading(story, "ANTECEDENTES")
    story.extend(repeated_paragraphs([
        "La digitalización de procesos en restauración se ha convertido en una necesidad frecuente incluso en negocios de pequeño tamaño. Aunque los grandes sistemas de "
        "TPV y gestión hostelera ofrecen soluciones muy completas, no siempre encajan con las necesidades reales de establecimientos con estructuras reducidas, equipos "
        "pequeños o presupuestos limitados.",
        "En muchos restaurantes sigue existiendo una mezcla de procedimientos manuales y herramientas digitales parciales. Por ejemplo, es habitual anotar los pedidos "
        "en papel, trasladarlos manualmente a cocina y posteriormente registrar el cobro en otra herramienta distinta. Esta fragmentación del proceso introduce errores "
        "y dificulta la trazabilidad de lo ocurrido durante el servicio.",
        "Desde el punto de vista de la ingeniería del software, este contexto constituye un caso de estudio especialmente adecuado. El dominio del problema es comprensible, "
        "los usuarios y roles están claramente diferenciados y la lógica de negocio exige mantener consistencia entre varias entidades: mesas, comandas, productos y usuarios.",
        "Además, la gestión de comandas encaja bien con una arquitectura web moderna. Un frontend ligero puede encargarse de la interacción con el personal de sala, mientras "
        "que un backend centraliza autenticación, reglas de negocio y persistencia. La separación entre capas también facilita la evolución del sistema y la incorporación "
        "de nuevos dispositivos o integraciones futuras.",
        "En cuanto a proyectos similares, existen aplicaciones comerciales orientadas a la hostelería que incluyen reservas, inventario, caja, facturación, integración con "
        "pasarelas de pago y otras utilidades. Sin embargo, gran parte de esas soluciones están sobredimensionadas para el alcance de este proyecto o dependen de licencias, "
        "hardware específico o modelos de suscripción que dificultan su adopción en pequeños negocios.",
        "Orsy parte de un planteamiento diferente: construir una herramienta más simple, modular y entendible, centrada en resolver bien el flujo principal del servicio. "
        "No pretende competir con soluciones empresariales masivas, sino demostrar que con una base tecnológica adecuada es posible cubrir las necesidades fundamentales de un restaurante.",
        "Otro antecedente relevante es la evolución del acceso desde dispositivos. En entornos reales, no siempre resulta práctico obligar al usuario a introducir email y "
        "contraseña completa. Por ello, el sistema incorpora la posibilidad de autenticación mediante PIN de 4 dígitos, manteniendo seguridad razonable y rapidez de uso.",
        "Por último, el proyecto también se apoya en antecedentes académicos ligados al desarrollo de aplicaciones full stack. Integra modelado de bases de datos, arquitectura "
        "en capas, seguridad basada en roles, consumo de APIs REST, generación de informes y documentación técnica extensa, por lo que constituye un ejemplo completo de proyecto de fin de ciclo.",
        "Si se observa la evolución reciente de la restauración, puede verse una tendencia clara hacia sistemas cada vez más conectados. Ya no se espera únicamente que una herramienta "
        "registre un pedido, sino que sea capaz de integrarse con cocina, caja, informes, dispositivos móviles y, en muchos casos, con canales externos como reparto a domicilio. "
        "Aunque Orsy no pretende cubrir todo ese ecosistema, sí nace dentro de esa misma lógica de modernización operativa.",
        "También debe considerarse como antecedente la proliferación de aplicaciones web internas frente a programas de escritorio tradicionales. Las soluciones web ofrecen ventajas "
        "importantes en términos de despliegue, mantenimiento y portabilidad. En lugar de instalar software distinto en cada equipo, basta con disponer de un navegador y de acceso "
        "a un servidor. Esta característica encaja especialmente bien con restaurantes que usan ordenadores de caja, tablets para sala o incluso teléfonos móviles de apoyo.",
        "Desde la perspectiva del usuario final, otro antecedente relevante es la necesidad de rapidez cognitiva. En plena hora punta, el personal no dispone de tiempo para navegar "
        "por menús complejos ni para interpretar interfaces ambiguas. Por ello, la ergonomía del software hostelero ha evolucionado hacia pantallas directas, acciones rápidas y reducción "
        "de pasos intermedios. El presente proyecto adopta esa filosofía intentando que la mayoría de operaciones se resuelvan en muy pocos gestos.",
        "A nivel de ingeniería, el proyecto también se relaciona con la práctica consolidada de separar claramente presentación, negocio y persistencia. Esta organización no solo responde "
        "a criterios de orden interno, sino que facilita tareas futuras como la sustitución de la interfaz, la ampliación de módulos o la integración con nuevas fuentes de datos.",
        "En conjunto, estos antecedentes muestran que Orsy no surge como un desarrollo aislado, sino como una respuesta concreta a tendencias reales del sector hostelero y a principios "
        "técnicos ampliamente utilizados en el desarrollo de aplicaciones empresariales modernas.",
    ]))
    story.append(PageBreak())

    add_heading(story, "ANÁLISIS DE REQUISITOS")
    story.append(p(
        "El análisis de requisitos se ha realizado identificando primero las necesidades del restaurante y después transformándolas en bloques funcionales. "
        "Cada bloque se ha descompuesto en funcionalidades, tareas de implementación y pruebas asociadas, de forma similar a una matriz de trazabilidad.",
        "BodyJ",
    ))
    add_sub(story, "R01. Autenticación, usuarios y control de acceso")
    story.extend(repeated_paragraphs([
        "El sistema debe distinguir entre usuarios con rol administrador y empleado. Esta diferenciación no es solo visual, sino funcional: determina qué endpoints pueden "
        "consumirse y qué acciones deben aparecer disponibles en la interfaz.",
        "Cada usuario dispone de nombre, email, PIN y rol. En escritorio el acceso se realiza mediante email y PIN. En tablet y móvil se prioriza un acceso simplificado "
        "basado únicamente en PIN, manteniendo la posibilidad de identificar unívocamente al usuario dentro del sistema.",
        "El backend debe evitar almacenar credenciales en texto plano. Por este motivo, el PIN se cifra utilizando BCrypt antes de persistirse. Spring Security se encarga "
        "de la autenticación y de la protección de rutas mediante control por roles.",
    ]))
    story.append(bullets([
        "Creación de la entidad `Usuario` y su repositorio.",
        "Restricción `UNIQUE` sobre el email.",
        "Validación del PIN como cadena numérica de cuatro dígitos.",
        "Autenticación mediante `AuthController`.",
        "Protección de endpoints con `@PreAuthorize`.",
        "Ocultación de elementos de administración en el frontend cuando el usuario es empleado.",
    ]))
    add_sub(story, "R02. Gestión de productos y categorías")
    story.extend(repeated_paragraphs([
        "El catálogo de productos es una parte esencial del sistema porque se reutiliza tanto en la pantalla de gestión de productos como en la pantalla de comanda. "
        "Cada producto necesita una categoría, un nombre y un precio, y el administrador debe poder mantener estos datos actualizados.",
        "El análisis funcional determina que el empleado puede consultar productos, pero no modificarlos. En cambio, el administrador puede crear nuevos productos, "
        "asignarlos a categorías, modificar su precio o eliminarlos si dejan de estar disponibles.",
    ]))
    story.append(bullets([
        "Entidad `Categoria` con lista de productos asociada.",
        "Entidad `Producto` con relación ManyToOne hacia categoría.",
        "Controladores específicos para productos y categorías.",
        "DTO de producto para adaptar la salida al frontend.",
        "Pantalla `productos.html` con filtro por categorías.",
    ]))
    add_sub(story, "R03. Gestión de mesas y plano de sala")
    story.extend(repeated_paragraphs([
        "La sala del restaurante debe representarse de forma visual. No basta con una lista de mesas: el usuario necesita ver el plano para identificar rápidamente "
        "la distribución del local y el estado operativo de cada mesa.",
        "Cada mesa almacena número, capacidad, estado y coordenadas del plano. Las coordenadas permiten mantener una disposición estable incluso después de cerrar la sesión "
        "o recargar la aplicación. El administrador debe poder crear mesas, modificar sus datos y recolocarlas arrastrándolas sobre el plano.",
    ]))
    story.append(bullets([
        "Entidad `Mesa` con `x` e `y` persistentes.",
        "Estados de mesa gestionados mediante enum.",
        "CRUD de mesas en backend.",
        "Pantalla de sala con renderizado absoluto de posiciones.",
        "Actualización del estado de mesa según la comanda.",
    ]))
    add_sub(story, "R04. Gestión de comandas")
    story.extend(repeated_paragraphs([
        "La comanda es la entidad central del sistema. Debe poder asociarse a una mesa, contener varias líneas y pasar por diferentes estados a lo largo del servicio. "
        "Además, el sistema debe poder recuperar la comanda abierta de una mesa para continuar un pedido ya iniciado.",
        "Cada línea de comanda almacena tanto la referencia al producto como una copia de nombre, precio y categoría. Esta decisión se toma para preservar el valor histórico "
        "del pedido aunque el producto cambie posteriormente en el catálogo.",
    ]))
    story.append(bullets([
        "Entidad `Comanda` con estado, fecha, mesa y líneas.",
        "Entidad `LineaComanda` con cantidad y copia de datos de producto.",
        "DTO `ComandaDTO` para creación y actualización desde frontend.",
        "Carga de comanda activa por mesa.",
        "Cambio de estado de mesa asociado al ciclo de la comanda.",
    ]))
    add_sub(story, "R05. Informes")
    story.extend(repeated_paragraphs([
        "La aplicación necesita un módulo de informes sencillo pero útil. En lugar de construir un sistema completo de inteligencia de negocio, se prioriza la obtención "
        "de indicadores fáciles de interpretar: total facturado, tickets, media por ticket, producto estrella y representación gráfica de ventas.",
        "Los informes deben basarse solo en comandas cobradas, ya que son las que representan ventas cerradas y consistentes desde el punto de vista del negocio.",
    ]))
    add_sub(story, "R06. Requisitos técnicos")
    story.append(bullets([
        "Backend en Java 17 con Spring Boot.",
        "Persistencia relacional en PostgreSQL.",
        "Frontend con HTML, CSS y JavaScript vanilla.",
        "Seguridad con Spring Security y BCrypt.",
        "Comunicación entre capas mediante API REST JSON.",
        "Adaptación responsive para varios tamaños de pantalla.",
    ]))
    add_sub(story, "R07. Requisitos no funcionales")
    story.extend(repeated_paragraphs([
        "Además de los requisitos funcionales, el sistema necesita cumplir una serie de condiciones de calidad que determinan su utilidad real. Un sistema que permita abrir comandas "
        "pero resulte lento, confuso o inseguro no sería válido en un entorno de restauración.",
        "El primer requisito no funcional relevante es la usabilidad. La interfaz debe ser comprensible con un periodo de aprendizaje reducido y debe favorecer que el usuario complete "
        "acciones frecuentes de manera rápida. Esto afecta a la disposición visual de botones, la legibilidad de los estados de mesa, el contraste cromático y la simplificación del flujo de acceso.",
        "El segundo requisito es la mantenibilidad. El proyecto debe estar organizado de forma que una futura persona desarrolladora pueda localizar con facilidad la lógica del login, "
        "los endpoints de cada módulo o las reglas que afectan a la gestión de comandas. Por ello se ha optado por una división clara en paquetes y ficheros especializados.",
        "También se considera esencial la seguridad. Aunque se trata de una aplicación académica, debe proteger credenciales, restringir acciones según rol y evitar que un empleado "
        "acceda a opciones exclusivas de administración. La elección de Spring Security y el cifrado con BCrypt responden directamente a este requisito.",
        "Otro aspecto importante es la fiabilidad. El sistema debe conservar correctamente la información de mesas, usuarios y pedidos incluso después de reinicios o recargas. "
        "La persistencia en PostgreSQL y la representación de las mesas mediante coordenadas guardadas contribuyen a este objetivo.",
        "Finalmente, la portabilidad constituye un requisito central del proyecto. La aplicación debe poder utilizarse desde ordenador, tablet o móvil sin necesidad de desarrollar "
        "clientes separados. Esta exigencia condiciona tanto la capa visual como determinadas decisiones de interacción, como el acceso simplificado mediante PIN.",
    ]))
    add_sub(story, "Historias de usuario representativas")
    story.append(bullets([
        "Como empleado, quiero identificarme rápidamente con un PIN para comenzar a trabajar sin perder tiempo en el inicio de turno.",
        "Como empleado, quiero ver de un vistazo qué mesas están libres u ocupadas para poder actuar con rapidez durante el servicio.",
        "Como empleado, quiero abrir la comanda de una mesa y añadir productos sin rehacer el pedido si tengo que volver más tarde.",
        "Como administrador, quiero gestionar usuarios y sus PIN para controlar quién accede al sistema.",
        "Como administrador, quiero modificar el catálogo de productos para reflejar cambios de carta o precio.",
        "Como administrador, quiero consultar informes básicos de ventas para obtener una visión rápida de la actividad del local.",
        "Como administrador, quiero recolocar mesas en el plano para adaptar la sala a la distribución real del restaurante.",
    ]))
    add_sub(story, "Criterios de aceptación")
    story.extend(repeated_paragraphs([
        "Para considerar que el login funciona correctamente, el sistema debe permitir el acceso a usuarios válidos y bloquear credenciales incorrectas. Además, debe reflejar en la interfaz "
        "el rol autenticado y ocultar las opciones que no correspondan a dicho perfil.",
        "Para considerar válida la gestión de sala, una mesa debe mantener su número, su estado y su posición después de recargar la aplicación. Si una comanda se abre o se cobra, "
        "el estado visual de la mesa debe actualizarse de manera coherente.",
        "Para validar la gestión de productos, el administrador debe poder crear, editar y eliminar registros, y dichos cambios deben verse reflejados tanto en la pantalla de catálogo "
        "como en la selección de productos dentro de la comanda.",
        "En el módulo de informes, el criterio de aceptación principal es que los datos agregados coincidan con las comandas cobradas existentes en la base de datos. "
        "No se trata solo de mostrar gráficos, sino de asegurar consistencia entre operación y análisis.",
    ]))
    story.append(PageBreak())

    add_heading(story, "PROPUESTA DE SOLUCIÓN")
    story.extend(repeated_paragraphs([
        "La solución propuesta consiste en una aplicación web cliente-servidor dividida en dos proyectos cooperantes: un backend Spring Boot y un frontend estático ligero. "
        "Esta elección permite mantener la interfaz desacoplada de la lógica de negocio y facilita tanto el mantenimiento como posibles despliegues independientes.",
        "El backend actúa como núcleo del sistema. Gestiona autenticación, seguridad, validación de datos, acceso a base de datos y reglas de negocio. Los controladores REST "
        "exponen los recursos principales del dominio: mesas, productos, categorías, comandas, usuarios y ventas. Las reglas de autorización se aplican en los endpoints.",
        "El frontend, por su parte, está diseñado para ser sencillo de desplegar y rápido de ejecutar. Se apoya en HTML, CSS y JavaScript puro, sin frameworks complejos, "
        "lo que simplifica el proyecto y reduce dependencias innecesarias. Cada pantalla se corresponde con una necesidad funcional concreta: login, sala, comanda, productos, informes y usuarios.",
        "La propuesta también introduce una adaptación por dispositivo. En escritorio se mantiene una experiencia más completa, apropiada para administración. En tablet y móvil, "
        "la navegación se simplifica para favorecer el uso operativo durante el servicio, priorizando la sala y la comanda frente a tareas de configuración.",
        "Desde el punto de vista de los datos, PostgreSQL se utiliza como motor relacional porque ofrece consistencia, soporte robusto para transacciones y una integración adecuada con JPA. "
        "El modelo de datos está pensado para representar con claridad el dominio del restaurante sin introducir entidades innecesarias.",
        "La propuesta de solución no se limita a una simple suma de tecnologías. Se basa en una distribución consciente de responsabilidades. El navegador se ocupa de la interacción "
        "inmediata con el usuario, mientras que el servidor aplica validaciones, controla permisos y garantiza la coherencia del dato. Esta separación es especialmente importante en un "
        "sistema con diferentes tipos de usuario y con operaciones que afectan al estado del negocio.",
        "Otro aspecto clave de la propuesta es su escalabilidad conceptual. Aunque el alcance del proyecto es académico, la estructura adoptada permitiría añadir nuevos módulos de forma "
        "progresiva. Por ejemplo, podrían incorporarse reservas, control de stock, integración con cocina o un módulo específico de caja sin necesidad de rediseñar la arquitectura completa.",
        "También se ha buscado una solución equilibrada en términos de complejidad. En vez de introducir un framework pesado de frontend o mecanismos avanzados de autenticación que excedieran "
        "el objetivo del proyecto, se ha optado por tecnologías suficientemente robustas y a la vez comprensibles. Esta decisión mejora la mantenibilidad y refuerza el valor formativo del trabajo.",
    ]))
    add_sub(story, "Justificación de decisiones técnicas")
    story.append(bullets([
        "Spring Boot acelera la construcción de la API y favorece una organización modular.",
        "Spring Security permite resolver autenticación y roles sin implementar mecanismos propios inseguros.",
        "PostgreSQL aporta robustez y persistencia real del sistema.",
        "JavaScript vanilla reduce complejidad en el frontend y facilita la comprensión del proyecto.",
        "Chart.js permite incorporar visualización gráfica con poco coste técnico.",
    ]))
    add_sub(story, "Alternativas valoradas")
    story.extend(repeated_paragraphs([
        "Una posible alternativa habría sido desarrollar toda la aplicación dentro de un único proyecto monolítico con plantillas del lado del servidor. Esa opción podría simplificar "
        "algunos aspectos iniciales, pero también dificultaría la evolución independiente del frontend y del backend, además de limitar la posibilidad de reutilizar la API desde otros clientes.",
        "Otra alternativa era utilizar un framework de frontend como React o Vue. Sin embargo, para el alcance del proyecto se ha considerado más razonable una solución con JavaScript puro, "
        "ya que reduce la sobrecarga de herramientas, acelera el desarrollo inicial y hace que la memoria pueda explicar de forma más transparente el funcionamiento interno del sistema.",
        "También podría haberse utilizado una base de datos no relacional. No obstante, el dominio del problema presenta relaciones bien definidas entre usuarios, mesas, comandas, líneas y productos, "
        "por lo que un modelo relacional resulta más natural y más seguro para preservar integridad.",
    ]))
    add_sub(story, "Flujo general de la solución")
    story.extend(repeated_paragraphs([
        "El flujo comienza cuando el usuario accede al frontend y se autentica. A partir de ese momento, la aplicación conserva la sesión y utiliza las credenciales en cada petición protegida. "
        "La sala se obtiene del backend y se representa en el navegador con el estado actualizado de cada mesa.",
        "Cuando el usuario selecciona una mesa, el sistema navega al módulo de comanda, donde recupera el catálogo de productos y la comanda activa, si existe. Cualquier modificación del ticket "
        "se prepara en el frontend y finalmente se envía al backend para persistirse de forma consistente.",
        "Si la comanda se cierra o se cobra, la lógica del servidor actualiza tanto el pedido como el estado de la mesa. Más tarde, esos mismos datos son reutilizados por el módulo de informes, "
        "que transforma la actividad operativa en indicadores de negocio. Este flujo muestra cómo toda la aplicación comparte una base de datos común y reglas centralizadas.",
    ]))
    story.append(p("Diagrama de arquitectura del sistema", "DiagramTitle"))
    story.append(architecture_diagram())
    story.extend(repeated_paragraphs([
        "El diagrama anterior sintetiza la organización del sistema. El usuario interactúa exclusivamente con el frontend, que actúa como capa de presentación. Este, a su vez, delega "
        "en la API las decisiones críticas y la validación de datos. Finalmente, PostgreSQL garantiza la persistencia de la información y permite que las decisiones tomadas en un dispositivo "
        "queden disponibles para el resto del sistema.",
        "Este modelo aporta una ventaja importante: cualquier cambio de interfaz no obliga a rediseñar la lógica central. Del mismo modo, si en el futuro se quisiera desarrollar una aplicación "
        "móvil nativa o una interfaz para cocina, podría reutilizarse buena parte del backend existente.",
    ]))
    story.append(PageBreak())

    add_heading(story, "PLAN DE TRABAJO")
    story.extend(repeated_paragraphs([
        "El proyecto se ha planteado en varias fases lógicas, aunque con iteraciones de revisión y mejora sobre módulos ya desarrollados. Este enfoque permite avanzar de manera "
        "ordenada sin perder flexibilidad ante cambios detectados durante la implementación.",
        "La primera fase corresponde al análisis del problema y la identificación de requisitos. En esta etapa se determina qué procesos del restaurante deben digitalizarse, "
        "qué roles participan y qué entidades son necesarias para modelar el sistema.",
        "La segunda fase se centra en el diseño: estructura de la base de datos, modelo de clases, definición de endpoints REST y bosquejo inicial de pantallas. "
        "Se toma la decisión de separar claramente backend y frontend y de representar la sala mediante coordenadas persistentes.",
        "La tercera fase es la implementación del backend. En ella se crean entidades, repositorios, controladores, servicios y configuración de seguridad. "
        "Una vez disponible la API, se procede a la implementación del frontend y a la conexión entre ambas partes.",
        "La cuarta fase engloba la integración y las pruebas. Aquí se revisa el funcionamiento de las pantallas sobre datos reales, se corrigen incoherencias y se valida el flujo "
        "de apertura, actualización y cobro de comandas.",
        "Finalmente, se dedica una fase específica a la adaptación responsive, la mejora de la experiencia en móvil y tablet, y la documentación final del proyecto.",
        "En la práctica, el plan de trabajo no ha sido estrictamente lineal. Algunas decisiones de diseño se revisaron cuando la implementación reveló necesidades no detectadas en el análisis inicial. "
        "Por ejemplo, la adaptación del login a PIN y la simplificación del acceso desde dispositivos táctiles requirieron modificar tanto la interfaz como el backend y el modelo de credenciales.",
        "Este comportamiento iterativo es habitual en proyectos reales. Lejos de considerarse un problema, ha permitido refinar la solución a partir de pruebas de uso y convertir requisitos implícitos "
        "en decisiones explícitas de diseño e implementación.",
    ]))
    add_sub(story, "Fases resumidas")
    story.append(bullets([
        "Fase 1. Análisis del problema y definición de requisitos.",
        "Fase 2. Diseño de base de datos, arquitectura y pantallas.",
        "Fase 3. Implementación del backend.",
        "Fase 4. Implementación del frontend.",
        "Fase 5. Integración y pruebas.",
        "Fase 6. Seguridad y adaptación responsive.",
        "Fase 7. Documentación y revisión final.",
    ]))
    add_sub(story, "Cronograma orientativo")
    story.extend(repeated_paragraphs([
        "En una planificación temporal aproximada, las primeras semanas se dedicarían al estudio del problema y la definición de requisitos. A continuación, se reservaría un bloque específico "
        "para el modelado de datos y el diseño de la arquitectura. Esta fase de preparación resulta fundamental porque condiciona buena parte de la consistencia posterior del sistema.",
        "Las siguientes semanas se centrarían en el desarrollo del backend, comenzando por usuarios y autenticación, continuando con productos y categorías y finalizando con mesas y comandas. "
        "Una vez disponible la API principal, el trabajo se desplazaría al frontend, priorizando primero el login y la sala, después la comanda y finalmente los módulos administrativos.",
        "En la parte final del proyecto se concentrarían las pruebas, la corrección de errores, la adaptación responsive, la generación de diagramas y la redacción de la memoria. "
        "Este orden es coherente con la necesidad de documentar una solución ya suficientemente estable.",
    ]))
    add_sub(story, "Riesgos y medidas de mitigación")
    story.append(bullets([
        "Riesgo de incoherencia entre estado de mesa y comanda: se mitiga actualizando ambas entidades dentro del mismo flujo de negocio.",
        "Riesgo de dificultad de uso en dispositivos táctiles: se mitiga mediante login por PIN y simplificación de navegación.",
        "Riesgo de crecimiento desordenado del código: se mitiga separando responsabilidades por paquetes y módulos.",
        "Riesgo de pérdida de datos por errores manuales: se mitiga usando persistencia relacional y validaciones en backend.",
        "Riesgo de accesos indebidos: se mitiga con roles, cifrado de credenciales y control de rutas protegidas.",
    ]))
    story.append(PageBreak())

    add_heading(story, "DESARROLLO")
    add_sub(story, "1. Desarrollo del frontend")
    story.extend(repeated_paragraphs([
        "El frontend del proyecto se ha estructurado en páginas HTML independientes reforzadas con ficheros JavaScript específicos por módulo. Esta organización facilita la comprensión "
        "de la aplicación y permite que cada pantalla concentre únicamente la lógica necesaria para su funcionalidad principal.",
        "El archivo `styles.css` centraliza toda la presentación visual del sistema. En él se define la estructura general de dashboard, la barra superior, la barra lateral, "
        "la presentación de tarjetas, los estilos del plano de sala, los productos, el ticket de comanda y el login. También incorpora media queries para adaptar la interfaz "
        "a escritorio, tablet y móvil.",
    ]))
    add_subsub(story, "1.1. Login")
    story.extend(repeated_paragraphs([
        "La pantalla `login.html` se ha diseñado para adaptarse al tipo de dispositivo. En escritorio se solicita email y PIN, mientras que en tablet y móvil se muestra una interfaz "
        "de PIN simplificada con teclado numérico visual. Esta decisión busca reducir fricción durante el acceso desde dispositivos usados en sala.",
        "La lógica asociada al login se concentra en `auth.js`. Este fichero gestiona la sesión, los encabezados de autenticación, la actualización de la barra superior, la detección "
        "de rol y la simplificación de navegación en dispositivos pequeños. También centraliza las peticiones autenticadas mediante `apiFetch`, evitando duplicar código.",
    ]))
    add_subsub(story, "1.2. Sala")
    story.extend(repeated_paragraphs([
        "La pantalla `sala.html` es el núcleo visual del sistema. A través de `app.js`, consulta las mesas al backend y las representa en un contenedor con posicionamiento absoluto. "
        "Cada mesa se pinta según su estado y número, y el administrador puede moverlas en modo edición para ajustar el plano del restaurante.",
        "La conservación de coordenadas en base de datos permite que la disposición del plano sea persistente. Esto significa que una modificación hecha por un administrador se mantiene "
        "después de recargar la página o iniciar una nueva sesión.",
    ]))
    add_subsub(story, "1.3. Comanda")
    story.extend(repeated_paragraphs([
        "La pantalla `comanda.html` recibe el identificador de la mesa mediante parámetro en la URL. A partir de ese dato consulta la mesa, recupera la comanda abierta si existe y "
        "muestra el catálogo de productos agrupado por categorías. El usuario puede añadir productos al ticket, y el sistema recalcula el total de manera inmediata.",
        "La lógica de comanda soporta tanto la creación de un pedido nuevo como la continuidad de una comanda ya abierta, lo que evita perder información en contextos de servicio reales.",
    ]))
    add_subsub(story, "1.4. Productos, informes y usuarios")
    story.extend(repeated_paragraphs([
        "`productos.html` permite al administrador mantener el catálogo, mientras que `informes.html` representa información de negocio usando Chart.js. `usuarios.html` centraliza "
        "la gestión de cuentas del sistema. En los tres casos, la interfaz se apoya en la sesión cargada por `auth.js` y en la respuesta del backend según permisos.",
        "La modularización por pantalla evita que el proyecto derive hacia un único script inmanejable. Cada página aborda un problema concreto y el código asociado se mantiene relativamente "
        "próximo a la necesidad funcional que resuelve. Esto facilita tanto la depuración como la explicación académica del sistema.",
    ]))
    add_sub(story, "1.5. Explicación paso a paso del flujo de uso")
    story.extend(repeated_paragraphs([
        "El flujo típico de trabajo comienza con la autenticación. Tras validar las credenciales, el sistema redirige al usuario a la sala y carga la información persistida de mesas. "
        "La pantalla principal muestra de forma inmediata el número de mesa, su estado y, de forma implícita, la disponibilidad del local.",
        "Si el usuario pulsa una mesa libre, la aplicación solicita el número de comensales y genera una comanda inicial. Si la mesa ya se encontraba ocupada, se recupera la comanda activa "
        "para permitir continuar la toma del pedido. Este comportamiento evita duplicidades y se ajusta a la operativa habitual del restaurante.",
        "En el módulo de comanda, el usuario va seleccionando productos del catálogo. Cada selección se traduce en una línea del ticket con su cantidad e importe acumulado. "
        "El total visible se recalcula constantemente para ofrecer retroalimentación inmediata al personal.",
        "Cuando la comanda se envía, el backend persiste la información y la mesa queda vinculada a ese pedido. Posteriormente, el usuario puede volver a entrar, añadir nuevos productos, "
        "cerrar la comanda o marcarla como cobrada. Esta secuencia resume el núcleo funcional del proyecto y explica por qué la relación entre sala y comanda es tan importante.",
    ]))
    story.append(PageBreak())

    add_sub(story, "2. Desarrollo del backend")
    story.extend(repeated_paragraphs([
        "El backend se ha construido con Spring Boot 4 sobre Java 17. La organización en paquetes facilita la separación de responsabilidades: `controller` para la exposición REST, "
        "`model` para el dominio, `repository` para la persistencia, `service` para la lógica de negocio y `security` para autenticación y autorización.",
        "La aplicación principal se arranca desde `OrsyApplication`, mientras que `UsuarioInitializer` ejecuta tareas de inicialización sobre usuarios, como migración de credenciales "
        "sin cifrar y creación del administrador por defecto.",
    ]))
    add_subsub(story, "2.1. Controladores")
    story.extend(repeated_paragraphs([
        "`AuthController` gestiona la autenticación por email+PIN y por PIN. `MesaController` administra la consulta y edición de mesas. `ProductoController` y `CategoriaController` "
        "resuelven el catálogo. `ComandaController` concentra la creación, consulta y actualización del pedido, mientras que `UsuarioController` y `VentaController` cubren las tareas "
        "administrativas restantes.",
        "Cada controlador trabaja con rutas REST claras y devuelve datos en formato JSON, lo que hace sencillo el consumo desde el frontend.",
    ]))
    add_subsub(story, "2.2. Servicios")
    story.extend(repeated_paragraphs([
        "Actualmente la lógica de servicio está más desarrollada en `UsuarioService`, encargado de validar y cifrar el PIN de usuario, normalizar emails y localizar usuarios para login por PIN. "
        "Aunque otras operaciones del sistema residen directamente en controladores, la estructura del proyecto permitiría extraer más lógica a servicios si el sistema siguiera creciendo.",
    ]))
    add_subsub(story, "2.3. Seguridad")
    story.extend(repeated_paragraphs([
        "`SecurityConfig` configura Spring Security en modo sin estado, con CORS habilitado y CSRF desactivado. Las rutas de autenticación quedan abiertas y el resto requiere validación. "
        "Además, `CustomUserDetailsService` carga los usuarios desde base de datos y transforma el rol de negocio en autoridades de Spring Security.",
        "La autorización a nivel de endpoint se completa con `@PreAuthorize`, lo que permite expresar reglas como `hasRole('ADMIN')` o `hasAnyRole('ADMIN','EMPLEADO')` de forma explícita.",
        "Esta configuración persigue un equilibrio entre sencillez y corrección técnica. El proyecto no necesita mecanismos complejos como OAuth2 o JWT para cumplir sus objetivos, "
        "pero sí requiere una base de seguridad seria que evite credenciales en claro y accesos indiscriminados.",
    ]))
    story.append(p("Diagrama de capas del backend", "DiagramTitle"))
    story.append(backend_layers_diagram())
    story.extend(repeated_paragraphs([
        "El backend se ha organizado siguiendo una arquitectura en capas porque este patrón favorece una separación limpia entre exposición, negocio y persistencia. "
        "Cada capa depende de la inmediatamente inferior, lo que reduce acoplamiento y hace más fácil localizar la responsabilidad de cada fragmento de código.",
        "La capa de controladores se orienta al protocolo HTTP y al intercambio de datos con el frontend. La capa de servicios recoge validaciones y decisiones de negocio. "
        "Los repositorios encapsulan el acceso a datos y permiten trabajar con operaciones de alto nivel sin escribir consultas repetitivas para cada entidad.",
    ]))
    story.append(PageBreak())

    add_sub(story, "3. Desarrollo del modelo de datos")
    story.extend(repeated_paragraphs([
        "La base del modelo de datos la forman las entidades `Usuario`, `Mesa`, `Categoria`, `Producto`, `Comanda`, `LineaComanda` y `Venta`. "
        "El diseño busca reflejar fielmente el dominio del restaurante sin introducir una sobrecarga innecesaria de tablas o relaciones.",
        "`Mesa` conserva no solo su identidad y capacidad, sino también la posición `x` e `y` del plano. `Producto` depende de una `Categoria`. `Comanda` se asocia a una `Mesa` y "
        "contiene una colección de `LineaComanda`. La línea, a su vez, referencia el producto y mantiene una copia de información descriptiva y económica.",
        "La entidad `Venta` existe como base de expansión futura. En el estado actual del sistema, los informes se alimentan principalmente de comandas con estado `COBRADA`, "
        "pero la presencia de `Venta` anticipa una posible separación entre pedido operativo y registro económico final.",
        "Esta selección de entidades responde a un criterio de mínima complejidad suficiente. En lugar de incorporar tablas auxiliares para cada pequeño detalle, se han modelado "
        "solo aquellos conceptos que tienen una responsabilidad clara dentro del negocio. De este modo, el diseño conserva expresividad sin volverse innecesariamente difícil de mantener.",
    ]))
    story.append(p("Diagrama de clases", "DiagramTitle"))
    story.append(class_diagram())
    story.extend(repeated_paragraphs([
        "El diagrama de clases permite observar de forma directa cuáles son los elementos permanentes del sistema y cómo se relacionan entre sí. Destaca especialmente la centralidad de `Comanda`, "
        "que actúa como nexo entre la sala, los productos consumidos y la futura información de ventas.",
        "También se aprecia la importancia de `LineaComanda` como entidad intermedia. En muchos desarrollos esta clase se infravalora, pero aquí resulta esencial porque es la que materializa "
        "el contenido real de cada pedido y permite conservar una fotografía del ticket en el momento de la venta.",
    ]))
    story.append(PageBreak())

    add_sub(story, "4. Desarrollo de la base de datos")
    story.extend(repeated_paragraphs([
        "PostgreSQL se utiliza como base de datos relacional del sistema. La configuración se encuentra en `application.properties`, donde se define la URL, el usuario, la contraseña "
        "y el comportamiento de Hibernate mediante `ddl-auto=update`. Esta configuración permite que la estructura evolucione durante el desarrollo sin necesidad de recrear manualmente "
        "todo el esquema en cada ejecución.",
        "La integridad del modelo se apoya en claves primarias autogeneradas, relaciones con claves foráneas y restricciones como `nullable = false` o `unique = true`. "
        "Este enfoque reduce errores y asegura consistencia en la información almacenada.",
        "La elección de PostgreSQL también se justifica por su fiabilidad y por su buena integración con herramientas del ecosistema Java. Para un sistema que debe conservar con precisión "
        "pedidos, usuarios y precios, disponer de un motor maduro y ampliamente documentado supone una ventaja importante.",
        "Desde el punto de vista académico, el uso de una base de datos relacional permite además explicar con claridad las relaciones uno a muchos y muchos a uno que aparecen en el problema. "
        "Esto refuerza el valor didáctico del proyecto y facilita su exposición en una memoria técnica.",
    ]))
    story.append(p("Diagrama entidad-relación", "DiagramTitle"))
    story.append(er_diagram())
    story.extend(repeated_paragraphs([
        "El diagrama entidad-relación resume la estructura persistente del proyecto. Se observa que `Categoria` agrupa productos, `Mesa` agrupa comandas en distintos momentos del tiempo "
        "y `Comanda` agrupa líneas que representan productos concretos consumidos por los clientes.",
        "Este modelo asegura que la información quede normalizada en un nivel suficiente para evitar redundancia innecesaria, aunque se aceptan duplicaciones controladas en `LineaComanda` "
        "para preservar el histórico económico del pedido.",
    ]))
    story.append(PageBreak())

    add_sub(story, "5. Desarrollo de la lógica de negocio")
    story.extend(repeated_paragraphs([
        "La lógica de negocio más crítica se concentra en la gestión de comandas y el estado de mesas. Cuando el usuario abre una mesa libre, el sistema solicita el número de clientes. "
        "Después, la comanda puede recibir productos y cantidades. Al enviarse, el backend genera una entidad `Comanda` con sus líneas y el frontend actualiza la mesa a estado ocupada.",
        "Cuando la comanda se cierra o se cobra, se actualiza el estado del pedido y simultáneamente se modifica el estado de la mesa. Este acoplamiento funcional es importante para reflejar "
        "el comportamiento real del restaurante y evitar incoherencias entre lo que ve el usuario y la situación almacenada en base de datos.",
        "El cálculo del total del ticket se realiza a partir de las líneas de comanda. En el módulo de informes, las comandas cobradas se recorren para agregar importes, contar tickets y "
        "extraer información agregada por producto o categoría.",
    ]))
    add_sub(story, "6. Integración frontend-backend")
    story.extend(repeated_paragraphs([
        "La integración entre ambas partes del sistema se realiza mediante peticiones HTTP con `fetch`. El fichero `auth.js` unifica la lógica de autenticación y añade automáticamente "
        "la cabecera `Authorization` a las llamadas protegidas. Esto simplifica el resto del frontend y evita duplicidad de código.",
        "La respuesta del backend se consume en formato JSON. Cada pantalla transforma esos datos en elementos del DOM, de modo que la interfaz se mantiene sincronizada con el estado real del sistema.",
    ]))
    add_sub(story, "7. Diseño responsive")
    story.extend(repeated_paragraphs([
        "La adaptación responsive no se limita a cambiar tamaños de fuente o reorganizar cajas. En Orsy implica también modificar la forma de interacción. En dispositivos pequeños, "
        "la navegación se simplifica y el login se reduce a PIN, priorizando rapidez y facilidad de uso sobre amplitud funcional.",
        "En la sala, el plano mantiene las posiciones originales de las mesas y utiliza scroll en lugar de reescalar agresivamente su ubicación. Esto preserva la referencia espacial del usuario, "
        "algo importante cuando la distribución física del local ya es conocida por el personal.",
    ]))
    add_sub(story, "8. Pruebas realizadas")
    story.extend(repeated_paragraphs([
        "Durante el desarrollo se han realizado pruebas funcionales manuales sobre el flujo principal: login, acceso a sala, apertura de comanda, envío de pedido, cambio de estado de mesa, "
        "cobro y generación de informes. También se han ejecutado pruebas automatizadas básicas mediante Gradle para verificar que el backend compila y mantiene el comportamiento esperado.",
        "Además, se ha revisado el comportamiento responsive en distintos anchos de pantalla, así como la persistencia correcta de coordenadas y datos entre refrescos.",
    ]))
    add_sub(story, "8.1. Casos de prueba representativos")
    story.extend(repeated_paragraphs([
        "Uno de los casos de prueba más importantes consiste en crear una mesa, abrir una comanda, añadir varios productos, salir de la pantalla y volver a entrar. "
        "El resultado esperado es que el pedido permanezca disponible y que la mesa continúe marcada como ocupada.",
        "Otro caso fundamental es la modificación del catálogo. Tras actualizar el precio de un producto, las nuevas comandas deben utilizar el precio actualizado, mientras que las líneas "
        "ya registradas deben conservar su valor previo si se almacenó en la línea de pedido. Esta comprobación valida la decisión de copiar determinados datos al crear la comanda.",
        "También se ha considerado el caso de inicio de sesión desde distintos tamaños de pantalla. En escritorio deben aparecer email y PIN; en tablet y móvil, solo el PIN con teclado numérico. "
        "Con ello se valida que la adaptación responsive no sea únicamente estética, sino también funcional.",
    ]))
    add_sub(story, "9. Desarrollo detallado del backend")
    add_subsub(story, "9.1. Entidades del modelo")
    story.extend(repeated_paragraphs([
        "La entidad `Usuario` representa a los actores del sistema. Contiene nombre, email, PIN cifrado y rol. El email sirve como identificador estable en escritorio, mientras que el PIN "
        "se usa como credencial rápida para acceso y autenticación. La presencia del rol hace posible separar funciones de administración y operativa.",
        "La entidad `Mesa` describe la representación física y lógica de una mesa del restaurante. No solo almacena número y capacidad, sino también su estado operativo y sus coordenadas "
        "dentro del plano de sala. Esto permite que la interfaz visual esté directamente respaldada por datos persistentes.",
        "La entidad `Categoria` agrupa productos de manera conceptual. Aunque su estructura es sencilla, tiene un papel importante porque ordena el catálogo y permite que el frontend "
        "filtre y presente los productos de forma más clara durante la toma de pedidos.",
        "La entidad `Producto` almacena el nombre, el precio y la categoría a la que pertenece. Esta información se utiliza en la gestión administrativa del catálogo y en la pantalla "
        "de comanda, donde el camarero selecciona los productos a servir.",
        "La entidad `Comanda` es el elemento central del dominio. Se asocia a una mesa, tiene una fecha de apertura y un estado, y contiene una lista de líneas. Su ciclo de vida "
        "marca una parte esencial de la lógica del sistema, ya que determina el comportamiento del estado de la mesa y la información que posteriormente se utilizará para informes.",
        "La entidad `LineaComanda` representa cada producto concreto que forma parte del pedido. Además de la referencia al producto, almacena nombre, precio y categoría copiados, "
        "de modo que el sistema preserve la información histórica incluso si posteriormente el catálogo cambia.",
        "La entidad `Venta` aparece como base para una posible evolución futura. Aunque la versión actual calcula los informes desde las comandas cobradas, la existencia de esta entidad "
        "permite contemplar una futura separación entre pedido operativo y registro económico final.",
    ]))
    add_subsub(story, "9.2. Controladores REST")
    story.extend(repeated_paragraphs([
        "`AuthController` resuelve la autenticación. En el método de login por email y PIN delega la verificación real en el `AuthenticationManager` de Spring Security. "
        "En el login por PIN, localiza al usuario a través del servicio y devuelve la respuesta adaptada al frontend. Este controlador es el punto de entrada del sistema para la gestión de sesiones.",
        "`MesaController` se encarga de todas las operaciones relacionadas con las mesas. Permite listar todas las mesas, consultar una mesa concreta, crear nuevas mesas, "
        "actualizar sus datos, modificar su estado y borrarlas. La protección por rol asegura que la edición del plano solo esté disponible para administradores.",
        "`ProductoController` devuelve productos en formato DTO para que el frontend reciba exactamente los datos que necesita. También soporta la creación, actualización y borrado de productos. "
        "La relación con categoría se resuelve consultando el repositorio de categorías antes de persistir.",
        "`CategoriaController` ofrece operaciones de consulta y mantenimiento sobre las categorías. Aunque es uno de los módulos más simples, resulta clave para organizar el catálogo del sistema.",
        "`ComandaController` concentra la lógica de creación y actualización de pedidos. Al recibir un `ComandaDTO`, busca la mesa correspondiente, crea una comanda nueva, recorre todas las líneas "
        "solicitadas por el cliente y asocia cada una con el producto adecuado. Gracias al mapeo en cascada, la comanda y sus líneas se guardan de forma conjunta.",
        "`UsuarioController` expone la gestión de usuarios al rol administrador. Su responsabilidad es delegar la creación, actualización y borrado en `UsuarioService`, donde se centralizan "
        "las validaciones del PIN y la normalización del email.",
        "`VentaController` ofrece un soporte sencillo sobre la entidad de ventas. Aunque la funcionalidad económica del sistema aún se apoya sobre las comandas cobradas, este controlador deja abierta "
        "una línea de evolución para posteriores ampliaciones del módulo de facturación.",
    ]))
    add_subsub(story, "9.3. Repositorios y persistencia")
    story.extend(repeated_paragraphs([
        "Los repositorios del sistema heredan de `JpaRepository`, lo que permite reutilizar una gran cantidad de operaciones comunes sin implementarlas manualmente. "
        "Este enfoque acelera el desarrollo y reduce código repetitivo en operaciones CRUD.",
        "`UsuarioRepository` se utiliza principalmente para recuperar usuarios por email, operación esencial para el login y para el control de unicidad de cuentas. "
        "`MesaRepository`, `ProductoRepository`, `CategoriaRepository`, `ComandaRepository` y `VentaRepository` resuelven la persistencia específica de cada entidad.",
        "La combinación de Hibernate y JPA facilita el mapeo objeto-relacional del sistema. Gracias a ello, el desarrollador puede trabajar con objetos Java mientras la capa de persistencia "
        "se encarga de traducir operaciones al modelo relacional de PostgreSQL.",
    ]))
    add_subsub(story, "9.4. Seguridad y autenticación")
    story.extend(repeated_paragraphs([
        "La seguridad se basa en un modelo sin estado. Cada petición relevante incorpora credenciales en cabecera y el backend valida el acceso sin apoyarse en sesión de servidor clásica. "
        "Esto simplifica el despliegue y se adapta bien a una API REST.",
        "El uso de BCrypt garantiza que el PIN nunca se almacena en texto plano. Incluso aunque dos usuarios eligieran el mismo PIN, el hash resultante podría variar debido al uso de sal. "
        "Esto supone una mejora fundamental respecto a soluciones inseguras basadas en almacenamiento directo.",
        "Spring Security se configura para permitir únicamente los endpoints necesarios antes de la autenticación, mientras que el resto del sistema queda protegido. "
        "Las anotaciones `@PreAuthorize` funcionan como una segunda capa de control, expresando de forma clara qué operaciones son exclusivas de administración.",
    ]))
    add_subsub(story, "9.5. Endpoints principales")
    story.append(bullets([
        "`POST /auth/login`: autenticación por email y PIN.",
        "`POST /auth/pin-login`: autenticación simplificada por PIN en dispositivos.",
        "`GET /mesas`: listado de mesas.",
        "`GET /mesas/{id}`: detalle de una mesa.",
        "`PUT /mesas/{id}/estado`: cambio de estado de mesa.",
        "`POST /comandas`: creación de comanda.",
        "`GET /comandas/mesa/{mesaId}`: recuperación de comanda activa.",
        "`PUT /comandas/{id}`: actualización de estado de comanda.",
        "`GET /productos`: catálogo de productos.",
        "`GET /categorias`: listado de categorías.",
        "`GET /usuarios`: listado de usuarios.",
        "`GET /ventas`: consulta de ventas.",
    ]))
    add_sub(story, "10. Desarrollo detallado del frontend")
    add_subsub(story, "10.1. auth.js")
    story.extend(repeated_paragraphs([
        "El archivo `auth.js` actúa como módulo transversal del frontend. En él se concentran la lectura y escritura de la sesión, la obtención del usuario autenticado, la detección de rol, "
        "la construcción de la cabecera Basic Auth y la lógica de redirección cuando una petición devuelve error 401.",
        "La función `requireAuth()` se utiliza como guardia de acceso en varias pantallas. Si no existe sesión válida, evita la carga del resto de la lógica y redirige a login. "
        "De este modo se mantiene una validación homogénea en toda la interfaz.",
        "La función `apiFetch()` encapsula `fetch` y añade credenciales automáticamente. Esta abstracción reduce repetición y centraliza el tratamiento del caso `Sesión expirada`.",
        "El mismo fichero detecta el tamaño de pantalla para adaptar el login. En escritorio se mantiene email y PIN, mientras que en dispositivos se muestra una interfaz basada en teclado numérico "
        "y puntos visuales, lo que mejora la experiencia de uso en contextos táctiles.",
    ]))
    add_subsub(story, "10.2. app.js")
    story.extend(repeated_paragraphs([
        "`app.js` reúne la lógica de sala y comanda. En la parte de sala, obtiene las mesas desde el backend, las transforma a un formato adecuado para el frontend y las dibuja dentro del plano. "
        "Además, gestiona el modo edición para administradores, el arrastre de mesas y el guardado de coordenadas.",
        "En la parte de comanda, el archivo obtiene productos y categorías, carga la comanda activa si existe, actualiza el ticket, calcula importes y ejecuta operaciones de envío, cierre y cobro. "
        "La estructura del archivo refleja el flujo principal del sistema y por eso concentra una porción importante de la lógica del proyecto.",
    ]))
    add_subsub(story, "10.3. productos.js")
    story.extend(repeated_paragraphs([
        "El módulo `productos.js` se ocupa de cargar productos y categorías, construir filtros y agrupar visualmente los productos por categoría. "
        "La lógica está pensada para que el administrador pueda mantener el catálogo mediante acciones sencillas como crear, editar o borrar productos.",
        "También incluye funciones auxiliares como `normalizarCategorias()`, que evita categorías inválidas o duplicadas, y `promptCategoria()`, que simplifica la selección de categoría en operaciones de creación o edición.",
    ]))
    add_subsub(story, "10.4. informes.js")
    story.extend(repeated_paragraphs([
        "`informes.js` consulta el conjunto de comandas y filtra las que se encuentran cobradas. A partir de ahí calcula totales y genera tres visualizaciones: resumen diario, top productos "
        "y ventas por categoría. Aunque el módulo es corto, concentra un trabajo de agregación de datos que transforma operaciones del día a día en información de análisis.",
    ]))
    add_subsub(story, "10.5. usuarios.js")
    story.extend(repeated_paragraphs([
        "El archivo `usuarios.js` implementa la gestión administrativa de cuentas. Su flujo se basa en recuperar todos los usuarios, renderizarlos como tarjetas e invocar operaciones de creación, edición y borrado. "
        "La introducción del PIN como credencial de 4 dígitos hace que este módulo también tenga un papel importante desde el punto de vista de seguridad y administración de accesos.",
    ]))
    add_subsub(story, "10.6. styles.css")
    story.extend(repeated_paragraphs([
        "`styles.css` organiza visualmente el sistema. Se encarga del layout general, el aspecto de la sidebar, la topbar, las tarjetas, la sala, el ticket y el login. "
        "Una parte significativa del trabajo responsive se ha implementado aquí mediante media queries, reorganizando elementos según el ancho de pantalla.",
        "El diseño del login con teclado PIN redondo también depende de esta hoja de estilos, que busca transmitir una interacción clara y táctil en dispositivos móviles y tablets.",
    ]))
    add_sub(story, "11. Diccionario de datos y clases")
    story.extend(repeated_paragraphs([
        "Como apoyo a la comprensión del sistema, puede elaborarse un diccionario de datos resumido. En él, cada entidad del dominio se relaciona con su función dentro de la aplicación, "
        "los campos más relevantes y las restricciones principales. Este tipo de documentación resulta especialmente útil cuando el sistema va a ser mantenido por terceros.",
        "En el caso de `Usuario`, los campos críticos son email y password cifrada. En `Mesa`, los más relevantes son estado y coordenadas. En `Comanda`, el estado y la relación con `Mesa` "
        "determinan su papel dentro del flujo. En `LineaComanda`, la cantidad y el precio copiado garantizan la consistencia del ticket.",
    ]))
    add_sub(story, "11.1. Explicación funcional de clases y funciones usadas")
    story.extend(repeated_paragraphs([
        "Una parte importante de esta memoria consiste en explicar no solo qué componentes existen, sino para qué sirven dentro del programa. Por ejemplo, `UsuarioService` no es simplemente "
        "una clase auxiliar, sino el punto donde se centralizan validaciones de credenciales, normalización de email y cifrado del PIN antes de guardar usuarios.",
        "De forma similar, `CustomUserDetailsService` funciona como puente entre el modelo de negocio y Spring Security. Su misión es traducir un `Usuario` persistido a la estructura que la "
        "biblioteca de seguridad necesita para autenticar y autorizar peticiones.",
        "En el frontend, funciones como `requireAuth`, `apiFetch`, `renderMesas`, `renderTicket`, `cargarProductos`, `guardarUsuario` o `cargarInforme` no deben entenderse como simples nombres "
        "aislados, sino como piezas de una cadena operativa. Unas garantizan seguridad, otras coordinan la comunicación con el backend y otras transforman datos en representación visual.",
        "Esta forma de documentar el código resulta especialmente valiosa en un proyecto académico porque demuestra comprensión profunda del programa, no solo capacidad de implementación.",
    ]))
    add_sub(story, "12. Flujos de uso reales")
    story.extend(repeated_paragraphs([
        "Un ejemplo de flujo real es el de un empleado que inicia turno, accede mediante PIN en tablet, consulta la sala y ve que la mesa 4 está libre. Al pulsarla, introduce el número de clientes, "
        "abre la comanda y añade varios productos. Después envía el pedido y la mesa pasa a ocupada.",
        "Otro flujo corresponde a un administrador que, antes de abrir el local, edita el plano de sala, crea una nueva mesa y corrige el precio de varios productos. Más tarde, al finalizar el día, "
        "consulta el módulo de informes para revisar el total facturado y el producto más vendido.",
        "Estos ejemplos muestran que el valor del sistema no reside solo en su estructura técnica, sino también en cómo esa estructura se traduce en operaciones concretas del negocio.",
    ]))
    add_sub(story, "13. Diagramas de análisis y diseño")
    story.append(p("Diagrama de casos de uso", "DiagramTitle"))
    story.append(use_case_diagram())
    story.extend(repeated_paragraphs([
        "El diagrama de casos de uso resume la relación entre actores y funcionalidades. Se aprecia que tanto administrador como empleado comparten el núcleo operativo del sistema, "
        "mientras que el rol administrador amplía sus permisos hacia configuración y supervisión.",
        "Esta diferencia es importante porque evita que el sistema trate a todos los usuarios como equivalentes. En un entorno real, limitar funciones reduce errores y mejora la seguridad organizativa.",
    ]))
    story.append(p("Diagrama de navegación", "DiagramTitle"))
    story.append(nav_diagram())
    story.extend(repeated_paragraphs([
        "El diagrama de navegación representa el recorrido principal entre pantallas. Login actúa como puerta de entrada, sala como centro operativo y comanda como pantalla de detalle del servicio. "
        "Las secciones de productos, informes y usuarios dependen más del trabajo administrativo, aunque siguen formando parte del mismo ecosistema de navegación.",
    ]))
    story.append(p("Diagrama de seguridad del sistema", "DiagramTitle"))
    story.append(security_diagram())
    story.extend(repeated_paragraphs([
        "El diagrama de seguridad resume el trayecto de autenticación desde el cliente hasta la base de datos. Aunque visualmente sea simple, concentra una de las decisiones clave del proyecto: "
        "la validación de credenciales no se resuelve en el navegador, sino en el backend, y además se apoya en mecanismos estándar del ecosistema Spring.",
    ]))
    story.append(p("Diagrama de diseño de base de datos", "DiagramTitle"))
    story.append(db_design_diagram())
    story.extend(repeated_paragraphs([
        "Este último esquema ofrece una visión simplificada del diseño relacional y complementa al diagrama entidad-relación. Su función es especialmente útil cuando se quiere explicar "
        "rápidamente al lector qué tablas forman el núcleo de la persistencia y cómo se conectan entre sí.",
    ]))
    story.append(PageBreak())

    add_heading(story, "DESPLIEGUE E INSTALACIÓN")
    story.extend(repeated_paragraphs([
        "Para ejecutar el sistema en entorno local se necesitan dos elementos: el backend Spring Boot y el frontend web. El backend requiere Java 17, Gradle y acceso a una base de datos PostgreSQL. "
        "El frontend puede abrirse desde navegador o servirse mediante un servidor estático sencillo.",
        "El primer paso consiste en preparar PostgreSQL y crear la base de datos `restaurante_db`. Después debe revisarse el archivo `application.properties` para verificar la URL, el usuario y la contraseña. "
        "Una vez hecho esto, se puede arrancar el backend con Gradle. Al iniciarse, Hibernate actualiza el esquema y el inicializador de usuarios crea o actualiza el administrador por defecto.",
        "En segundo lugar, se abre el frontend del proyecto `Orsy_TFG`. La interfaz realiza peticiones hacia `http://localhost:8080`, por lo que el backend debe permanecer activo durante el uso del sistema.",
        "El despliegue en un entorno remoto seguiría una lógica similar: backend desplegado como servicio Java, base de datos PostgreSQL accesible por red y frontend publicado como sitio estático.",
        "Desde el punto de vista operativo, conviene diferenciar claramente entre entorno de desarrollo y entorno de explotación. En desarrollo se prioriza la facilidad para probar cambios, "
        "por lo que puede ser aceptable usar `ddl-auto=update` y credenciales de prueba. En un despliegue real, en cambio, conviene endurecer la configuración, fijar copias de seguridad y controlar mejor la exposición de servicios.",
    ]))
    add_sub(story, "Pasos de instalación local")
    story.append(bullets([
        "Instalar Java 17.",
        "Instalar PostgreSQL.",
        "Crear la base de datos `restaurante_db`.",
        "Configurar credenciales en `src/main/resources/application.properties`.",
        "Ejecutar el backend con `./gradlew bootRun` o desde el IDE.",
        "Abrir el frontend de `Orsy_TFG` en navegador.",
        "Acceder con las credenciales o PIN configurados en el sistema.",
    ]))
    add_sub(story, "Consideraciones de despliegue")
    story.append(bullets([
        "Mantener la configuración de base de datos fuera del código en un despliegue real.",
        "Revisar los orígenes permitidos por CORS si el frontend se sirve desde otro dominio.",
        "Configurar HTTPS en producción.",
        "Establecer una estrategia de copias de seguridad sobre PostgreSQL.",
    ]))
    add_sub(story, "Secuencia de arranque recomendada")
    story.extend(repeated_paragraphs([
        "La secuencia de arranque recomendada comienza por la base de datos, continúa con el backend y finaliza con el frontend. Este orden evita errores de conexión iniciales "
        "y permite que el backend aplique actualizaciones de esquema antes de que el usuario interactúe con la aplicación.",
        "Una vez levantado el backend, es aconsejable revisar que el endpoint de autenticación responde correctamente y que el usuario administrador por defecto ha sido creado o actualizado. "
        "Solo después de esa verificación tiene sentido abrir la interfaz y comenzar las pruebas funcionales.",
    ]))
    add_sub(story, "Mantenimiento e incidencias")
    story.extend(repeated_paragraphs([
        "En caso de incidencias, una de las primeras comprobaciones debe ser la conectividad entre frontend y backend. Si el navegador no logra acceder a `localhost:8080`, el problema no suele "
        "estar en la lógica de la interfaz sino en que el servidor no está levantado o la configuración de red no coincide.",
        "Otra fuente de incidencias habitual es la base de datos. Credenciales incorrectas, esquemas no creados o cambios incompatibles en entidades pueden impedir el arranque del backend. "
        "Por ello, el despliegue debe acompañarse de una revisión periódica de logs y de una política clara de copia de seguridad.",
        "Desde un punto de vista de mantenimiento evolutivo, la organización modular del sistema ayuda a que las futuras modificaciones se concentren en áreas concretas. "
        "Un cambio en el catálogo afectará sobre todo a `Producto` y sus controladores; un cambio en autenticación se centrará en `AuthController`, `UsuarioService` y la configuración de seguridad.",
    ]))
    story.append(PageBreak())

    add_heading(story, "EVOLUCIÓN / TRABAJO FUTURO")
    story.extend(repeated_paragraphs([
        "Aunque Orsy cubre el flujo principal de un restaurante, existen múltiples líneas de evolución razonables. La primera es la sincronización en tiempo real entre dispositivos, "
        "de forma que un cambio en el estado de la sala se refleje instantáneamente sin necesidad de recargar la página.",
        "Otra mejora relevante sería la integración con impresoras de cocina o sistemas de ticketing. Esto permitiría que el envío de una comanda se tradujera automáticamente en un documento "
        "físico o digital para la preparación del pedido.",
        "También resultaría útil incorporar un módulo de inventario y stock, de modo que el catálogo no solo almacenase nombre y precio de producto, sino también disponibilidad y alertas. "
        "En paralelo, el módulo de informes podría ampliarse con filtros temporales, comparativas históricas, desglose por categorías o franjas horarias.",
        "Desde el punto de vista de la experiencia de usuario, sería interesante sustituir algunos formularios basados en `prompt` por modales más trabajados, introducir validaciones visuales "
        "más ricas y mejorar el flujo de edición de usuarios y productos.",
        "Finalmente, una evolución natural del proyecto sería la incorporación de pagos, reservas o incluso una versión móvil específica para camareros. Todas estas líneas de trabajo son viables "
        "gracias a la separación en capas y a la estructura modular conseguida en la versión actual.",
        "Otra evolución interesante sería la incorporación de auditoría de acciones. Registrar qué usuario creó o cobró una comanda, o quién modificó un producto, añadiría trazabilidad y "
        "resultaría útil tanto para gestión como para depuración de incidencias.",
        "También podría plantearse una mejora de internacionalización y parametrización. En un sistema más maduro, ciertos textos, impuestos o configuraciones del local deberían externalizarse "
        "para adaptar la aplicación a distintos contextos sin necesidad de modificar código.",
    ]))
    story.append(PageBreak())

    add_heading(story, "CONCLUSIONES")
    story.extend(repeated_paragraphs([
        "El desarrollo de Orsy ha permitido construir una aplicación completa a partir de un problema real de negocio. A lo largo del proyecto se han integrado conocimientos de diseño de bases "
        "de datos, desarrollo backend, frontend web, seguridad y documentación técnica en una solución coherente y funcional.",
        "Uno de los aspectos más importantes del proyecto ha sido la construcción de una lógica de negocio alineada con la operativa real del restaurante. La relación entre mesas, comandas, productos "
        "y roles no se ha tratado como un simple CRUD, sino como un flujo con estados y restricciones que deben mantenerse consistentes.",
        "También ha resultado especialmente relevante la separación entre frontend y backend. Esta arquitectura facilita la comprensión del sistema, hace más sencillo su mantenimiento y prepara el terreno "
        "para futuras ampliaciones o nuevos clientes de la API.",
        "En conjunto, el proyecto no solo cumple sus objetivos técnicos y funcionales, sino que además constituye una base sólida para seguir evolucionando. Por ello, puede considerarse un resultado adecuado "
        "tanto desde el punto de vista académico como desde el punto de vista práctico.",
    ]))
    story.append(PageBreak())

    add_heading(story, "BIBLIOGRAFÍA (APA)")
    story.extend(repeated_paragraphs([
        "Chart.js. (2026). <i>Chart.js documentation</i>. https://www.chartjs.org/",
        "Fielding, R. T. (2000). <i>Architectural styles and the design of network-based software architectures</i> (Doctoral dissertation, University of California, Irvine).",
        "MDN Web Docs. (2026). <i>HTML: HyperText Markup Language</i>. Mozilla. https://developer.mozilla.org/",
        "MDN Web Docs. (2026). <i>CSS: Cascading Style Sheets</i>. Mozilla. https://developer.mozilla.org/",
        "MDN Web Docs. (2026). <i>JavaScript</i>. Mozilla. https://developer.mozilla.org/",
        "PostgreSQL Global Development Group. (2026). <i>PostgreSQL documentation</i>. https://www.postgresql.org/docs/",
        "Spring. (2026). <i>Spring Boot reference documentation</i>. https://spring.io/projects/spring-boot",
        "Spring. (2026). <i>Spring Security reference documentation</i>. https://spring.io/projects/spring-security",
        "Richardson, L., & Ruby, S. (2007). <i>RESTful web services</i>. O'Reilly Media.",
        "Wikipedia contributors. (2026). <i>Bcrypt</i>. Wikipedia. https://en.wikipedia.org/wiki/Bcrypt",
    ]))
    return story


def add_page_number(canvas, doc):
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#5A151E"))
    canvas.drawRightString(19.1 * cm, 1.2 * cm, f"{doc.page}")


def main():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=1.8 * cm,
        title="Memoria TFG Orsy",
        author="Marina Moreno Rodríguez",
    )
    doc.build(build_story(), onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    main()
