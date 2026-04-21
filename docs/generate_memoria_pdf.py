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
)


OUTPUT_PATH = "/Users/marinamr/Downloads/Memoria TFG (1).pdf"


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleCenter",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontName="Helvetica-Bold",
    fontSize=20,
    leading=24,
    spaceAfter=16,
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


def bullet_list(items):
    flow = []
    for item in items:
        flow.append(ListItem(Paragraph(item, styles["BodyJ"])))
    return ListFlowable(flow, bulletType="bullet", start="circle", leftIndent=18)


def box(x, y, w, h, text, fill="#F5EFEA"):
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, strokeColor=colors.HexColor("#5A151E"), fillColor=colors.HexColor(fill), rx=8, ry=8))
    lines = text.split("\n")
    yy = h - 18
    for line in lines:
        d.add(String(w / 2, yy, line, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9, fillColor=colors.HexColor("#2C2C2C")))
        yy -= 12
    return d


def arquitectura_sistema():
    d = Drawing(17 * cm, 7 * cm)
    fill = colors.HexColor("#F5EFEA")
    stroke = colors.HexColor("#5A151E")
    text = colors.HexColor("#2C2C2C")
    boxes = [
        (0.3 * cm, 2.2 * cm, 3.2 * cm, 2 * cm, "Usuario\nAdmin / Empleado"),
        (4.4 * cm, 2.2 * cm, 4 * cm, 2 * cm, "Frontend Web\nHTML + CSS + JS"),
        (9.3 * cm, 2.2 * cm, 3.4 * cm, 2 * cm, "API REST\nSpring Boot"),
        (13.4 * cm, 2.2 * cm, 3.2 * cm, 2 * cm, "PostgreSQL\nrestaurante_db"),
    ]
    for x, y, w, h, t in boxes:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill, rx=8, ry=8))
        yy = y + h - 0.6 * cm
        for line in t.split("\n"):
            d.add(String(x + w / 2, yy, line, textAnchor="middle", fontName="Helvetica-Bold", fontSize=10, fillColor=text))
            yy -= 0.45 * cm
    d.add(Line(3.5 * cm, 3.2 * cm, 4.4 * cm, 3.2 * cm, strokeColor=stroke, strokeWidth=1.5))
    d.add(Line(8.4 * cm, 3.2 * cm, 9.3 * cm, 3.2 * cm, strokeColor=stroke, strokeWidth=1.5))
    d.add(Line(12.7 * cm, 3.2 * cm, 13.4 * cm, 3.2 * cm, strokeColor=stroke, strokeWidth=1.5))
    return d


def capas_backend():
    d = Drawing(12 * cm, 10 * cm)
    fill = colors.HexColor("#F5EFEA")
    stroke = colors.HexColor("#5A151E")
    layers = [
        (1 * cm, 7.4 * cm, 10 * cm, 1.6 * cm, "Capa de presentación\nControllers REST"),
        (1 * cm, 5.2 * cm, 10 * cm, 1.6 * cm, "Capa de lógica\nServices y reglas de negocio"),
        (1 * cm, 3.0 * cm, 10 * cm, 1.6 * cm, "Capa de persistencia\nRepositories JPA"),
        (1 * cm, 0.8 * cm, 10 * cm, 1.6 * cm, "Base de datos\nPostgreSQL"),
    ]
    for x, y, w, h, t in layers:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill, rx=8, ry=8))
        yy = y + h - 0.55 * cm
        for line in t.split("\n"):
            d.add(String(x + w / 2, yy, line, textAnchor="middle", fontName="Helvetica-Bold", fontSize=10))
            yy -= 0.45 * cm
    for y1, y2 in [(7.4, 6.8), (5.2, 4.6), (3.0, 2.4)]:
        d.add(Line(6 * cm, y1 * cm, 6 * cm, y2 * cm, strokeColor=stroke, strokeWidth=1.5))
    return d


def casos_uso():
    d = Drawing(17 * cm, 9 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    d.add(Circle(1.6 * cm, 6.8 * cm, 0.45 * cm, strokeColor=stroke))
    d.add(String(1.6 * cm, 5.9 * cm, "Administrador", textAnchor="middle", fontName="Helvetica", fontSize=9))
    d.add(Circle(1.6 * cm, 2.4 * cm, 0.45 * cm, strokeColor=stroke))
    d.add(String(1.6 * cm, 1.5 * cm, "Empleado", textAnchor="middle", fontName="Helvetica", fontSize=9))
    use_cases = [
        (7 * cm, 7.2 * cm, 4.5 * cm, 1 * cm, "Iniciar sesión"),
        (7 * cm, 5.8 * cm, 4.5 * cm, 1 * cm, "Ver sala"),
        (7 * cm, 4.4 * cm, 4.5 * cm, 1 * cm, "Gestionar comanda"),
        (7 * cm, 3.0 * cm, 4.5 * cm, 1 * cm, "Gestionar productos"),
        (7 * cm, 1.6 * cm, 4.5 * cm, 1 * cm, "Consultar informes"),
        (12 * cm, 4.4 * cm, 4.2 * cm, 1 * cm, "Gestionar usuarios"),
    ]
    for x, y, w, h, t in use_cases:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill, rx=10, ry=10))
        d.add(String(x + w / 2, y + 0.38 * cm, t, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9))
    for target_y in [7.7, 6.3, 4.9, 3.5, 2.1]:
        d.add(Line(2.05 * cm, 6.8 * cm, 7 * cm, target_y * cm, strokeColor=stroke))
    for target_y in [7.7, 6.3, 4.9]:
        d.add(Line(2.05 * cm, 2.4 * cm, 7 * cm, target_y * cm, strokeColor=stroke))
    d.add(Line(2.05 * cm, 6.8 * cm, 12 * cm, 4.9 * cm, strokeColor=stroke))
    return d


def diagrama_clases():
    d = Drawing(18 * cm, 11 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    classes = [
        (0.5 * cm, 8.2 * cm, 3.5 * cm, 2.2 * cm, "Usuario\nid\nnombre\nemail\npassword\nrol"),
        (4.6 * cm, 8.2 * cm, 3.5 * cm, 2.2 * cm, "Mesa\nid\nnumero\ncapacidad\nestado\nx,y"),
        (8.7 * cm, 8.2 * cm, 3.5 * cm, 2.2 * cm, "Categoria\nid\nnombre"),
        (12.8 * cm, 8.2 * cm, 4 * cm, 2.2 * cm, "Producto\nid\nnombre\nprecio\ncategoria"),
        (4.6 * cm, 4.4 * cm, 3.7 * cm, 2.4 * cm, "Comanda\nid\nfecha\nestado\nmesa"),
        (9.2 * cm, 4.4 * cm, 4.2 * cm, 2.4 * cm, "LineaComanda\nid\ncantidad\nnombre\nprecio\ncategoria"),
        (14.2 * cm, 4.4 * cm, 3.3 * cm, 2.0 * cm, "Venta\nid\nfecha\ntotal"),
    ]
    for x, y, w, h, t in classes:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill))
        yy = y + h - 0.45 * cm
        for i, line in enumerate(t.split("\n")):
            d.add(String(x + 0.15 * cm if i else x + w / 2, yy, line, textAnchor="middle" if i == 0 else "start", fontName="Helvetica-Bold" if i == 0 else "Helvetica", fontSize=8))
            yy -= 0.33 * cm
    lines = [
        ((12.8, 9.3), (12.2, 9.3)),
        ((10.5, 8.2), (10.5, 6.8)),
        ((6.4, 8.2), (6.4, 6.8)),
        ((8.3, 5.6), (9.2, 5.6)),
        ((13.4, 5.6), (14.2, 5.6)),
    ]
    for (x1, y1), (x2, y2) in lines:
        d.add(Line(x1 * cm, y1 * cm, x2 * cm, y2 * cm, strokeColor=stroke))
    return d


def entidad_relacion():
    d = Drawing(18 * cm, 11 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    entities = [
        (0.6 * cm, 8.5 * cm, 3.4 * cm, 1.6 * cm, "USUARIO"),
        (4.8 * cm, 8.5 * cm, 3.4 * cm, 1.6 * cm, "MESA"),
        (9.0 * cm, 8.5 * cm, 3.4 * cm, 1.6 * cm, "CATEGORIA"),
        (13.2 * cm, 8.5 * cm, 3.4 * cm, 1.6 * cm, "PRODUCTO"),
        (4.8 * cm, 4.8 * cm, 3.4 * cm, 1.6 * cm, "COMANDA"),
        (9.0 * cm, 4.8 * cm, 3.8 * cm, 1.6 * cm, "LINEA_COMANDA"),
        (13.6 * cm, 4.8 * cm, 2.9 * cm, 1.6 * cm, "VENTA"),
    ]
    for x, y, w, h, t in entities:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill))
        d.add(String(x + w / 2, y + 0.6 * cm, t, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9))
    for x1, y1, x2, y2 in [
        (12.4, 9.3, 13.2, 9.3),
        (6.5, 8.5, 6.5, 6.4),
        (10.9, 8.5, 10.9, 6.4),
        (8.2, 5.6, 9.0, 5.6),
        (12.8, 5.6, 13.6, 5.6),
    ]:
        d.add(Line(x1 * cm, y1 * cm, x2 * cm, y2 * cm, strokeColor=stroke))
    return d


def navegacion():
    d = Drawing(16 * cm, 9 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    pages = [
        (6 * cm, 7.2 * cm, 4 * cm, 1.2 * cm, "login.html"),
        (6 * cm, 5.2 * cm, 4 * cm, 1.2 * cm, "sala.html"),
        (1.0 * cm, 2.6 * cm, 4 * cm, 1.2 * cm, "comanda.html"),
        (6.0 * cm, 2.6 * cm, 4 * cm, 1.2 * cm, "productos.html"),
        (11.0 * cm, 2.6 * cm, 4 * cm, 1.2 * cm, "informes.html / usuarios.html"),
    ]
    for x, y, w, h, t in pages:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill, rx=8, ry=8))
        d.add(String(x + w / 2, y + 0.45 * cm, t, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9))
    d.add(Line(8 * cm, 7.2 * cm, 8 * cm, 6.4 * cm, strokeColor=stroke))
    d.add(Line(8 * cm, 5.2 * cm, 3 * cm, 3.8 * cm, strokeColor=stroke))
    d.add(Line(8 * cm, 5.2 * cm, 8 * cm, 3.8 * cm, strokeColor=stroke))
    d.add(Line(8 * cm, 5.2 * cm, 13 * cm, 3.8 * cm, strokeColor=stroke))
    return d


def seguridad():
    d = Drawing(17 * cm, 8 * cm)
    stroke = colors.HexColor("#5A151E")
    fill = colors.HexColor("#F5EFEA")
    labels = [
        (0.2 * cm, 5.5 * cm, 2.8 * cm, 1.2 * cm, "Cliente"),
        (3.5 * cm, 5.5 * cm, 3.2 * cm, 1.2 * cm, "Frontend"),
        (7.2 * cm, 5.5 * cm, 3.2 * cm, 1.2 * cm, "AuthController"),
        (10.9 * cm, 5.5 * cm, 2.8 * cm, 1.2 * cm, "Security"),
        (14.2 * cm, 5.5 * cm, 2.4 * cm, 1.2 * cm, "DB"),
    ]
    for x, y, w, h, t in labels:
        d.add(Rect(x, y, w, h, strokeColor=stroke, fillColor=fill, rx=6, ry=6))
        d.add(String(x + w / 2, y + 0.42 * cm, t, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9))
    for x in [1.6, 5.1, 8.8, 12.3, 15.4]:
        d.add(Line(x * cm, 5.5 * cm, x * cm, 0.9 * cm, strokeColor=colors.grey))
    arrows = [
        (1.6, 4.7, 5.1, 4.7, "Credenciales"),
        (5.1, 4.0, 8.8, 4.0, "POST /auth/login"),
        (8.8, 3.3, 12.3, 3.3, "Autenticación"),
        (12.3, 2.6, 15.4, 2.6, "Buscar usuario"),
        (12.3, 1.9, 5.1, 1.9, "AuthResponse + sesión"),
    ]
    for x1, y1, x2, y2, txt in arrows:
        d.add(Line(x1 * cm, y1 * cm, x2 * cm, y2 * cm, strokeColor=stroke))
        d.add(String(((x1 + x2) / 2) * cm, (y1 + 0.12) * cm, txt, textAnchor="middle", fontName="Helvetica", fontSize=8))
    return d


def diseno_bd():
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
        d.add(String(x + w / 2, y + 0.38 * cm, t, textAnchor="middle", fontName="Helvetica-Bold", fontSize=9))
    for x1, y1, x2, y2 in [
        (10.9, 5.85, 11.3, 5.85),
        (5.7, 5.3, 5.7, 3.5),
        (9.3, 5.3, 9.3, 3.5),
        (7.3, 2.95, 7.7, 2.95),
        (10.9, 2.95, 11.3, 2.95),
    ]:
        d.add(Line(x1 * cm, y1 * cm, x2 * cm, y2 * cm, strokeColor=stroke))
    return d


def add_heading(story, title):
    story.append(p(title, "Section"))


def add_sub(story, title):
    story.append(p(title, "SubSection"))


def build_story():
    story = []
    story.append(Spacer(1, 3.5 * cm))
    story.append(p("Desarrollo de una web multiplataforma para la gestión de comandas de un restaurante", "TitleCenter"))
    story.append(p("2º Desarrollo de Aplicaciones Multiplataforma", "SubSection"))
    story.append(Spacer(1, 1.2 * cm))
    story.append(p("Marina Moreno Rodríguez", "SubSection"))
    story.append(p("Memoria adaptada al estado actual del proyecto Orsy", "BodyJ"))
    story.append(PageBreak())

    add_heading(story, "DEDICATORIA (OPCIONAL)")
    story.append(p("A mi familia y a todas las personas que me han acompañado durante el desarrollo de este proyecto.", "BodyJ"))
    story.append(PageBreak())

    add_heading(story, "ÍNDICES")
    story.append(bullet_list([
        "Abstract",
        "Justificación del proyecto",
        "Introducción",
        "Objetivos",
        "Requisitos funcionales y técnicos",
        "Descripción del sistema",
        "Arquitectura del sistema",
        "Arquitectura en capas del backend",
        "Casos de uso",
        "Diagrama de clases",
        "Diagrama entidad-relación",
        "Diseño de la base de datos",
        "Diagrama de navegación",
        "Seguridad del sistema",
        "Tecnologías utilizadas",
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
        "La solución permite controlar mesas, crear comandas, añadir productos, gestionar usuarios y consultar informes de ventas. "
        "La aplicación se divide en un frontend web construido con HTML, CSS y JavaScript y un backend desarrollado con Spring Boot "
        "que expone una API REST protegida con Spring Security. La información se almacena en PostgreSQL. "
        "El objetivo principal es digitalizar el proceso de servicio, reducir errores y mejorar la organización del trabajo en sala.",
        "BodyJ"
    ))
    story.append(p(
        "This project consists of the development of a web application for restaurant order management. "
        "The system allows table control, order creation, product management, user administration and sales reporting. "
        "The solution is divided into a web frontend built with HTML, CSS and JavaScript and a backend implemented with Spring Boot "
        "as a secured REST API. Data is stored in PostgreSQL. The main goal is to digitalize restaurant operations, reduce mistakes "
        "and improve workflow efficiency.",
        "BodyJ"
    ))
    story.append(PageBreak())

    add_heading(story, "JUSTIFICACIÓN DEL PROYECTO")
    story.append(p(
        "La necesidad de este proyecto aparece en el contexto de pequeños y medianos restaurantes que todavía gestionan mesas y pedidos "
        "con métodos manuales o con soluciones poco flexibles. En estos entornos es habitual encontrar problemas como pérdida de pedidos, "
        "errores al cobrar, dificultad para conocer el estado real de la sala y falta de visibilidad sobre las ventas.",
        "BodyJ"
    ))
    story.append(p(
        "Orsy se plantea como una solución web accesible desde navegador, con una interfaz sencilla y un modelo de permisos claro. "
        "El sistema diferencia entre administradores y empleados, incorpora un plano visual de mesas y facilita la creación y seguimiento "
        "de comandas de manera rápida. Además, permite mantener un catálogo de productos y categorías y generar informes básicos de negocio.",
        "BodyJ"
    ))
    story.append(PageBreak())

    add_heading(story, "INTRODUCCIÓN")
    story.append(p(
        "Orsy es una aplicación web orientada a la gestión diaria de un restaurante. El flujo principal comienza con la autenticación del usuario, "
        "continúa con la visualización de la sala y permite abrir una mesa, añadir productos a una comanda, cerrarla o cobrarla y volver a dejar "
        "la mesa disponible. Sobre esa base se añaden módulos complementarios como productos, usuarios e informes.",
        "BodyJ"
    ))
    story.append(p(
        "A nivel técnico, el sistema adopta una arquitectura cliente-servidor. El frontend se encarga de la interacción con el usuario y consume "
        "la API REST del backend. El backend centraliza la lógica de negocio, la seguridad y el acceso a datos. Esta separación favorece la "
        "mantenibilidad del sistema y su evolución futura.",
        "BodyJ"
    ))
    story.append(PageBreak())

    add_heading(story, "OBJETIVOS")
    story.append(p("El objetivo general del proyecto es desarrollar una aplicación web para la gestión eficiente de comandas de un restaurante.", "BodyJ"))
    story.append(bullet_list([
        "Diseñar una interfaz visual para representar el plano de mesas.",
        "Permitir la apertura, edición y cierre de comandas asociadas a cada mesa.",
        "Gestionar el catálogo de productos y categorías.",
        "Diferenciar funcionalidades entre administrador y empleado.",
        "Incorporar autenticación segura mediante PIN de 4 dígitos.",
        "Generar informes de ventas a partir de las comandas cobradas.",
        "Separar claramente frontend, backend y base de datos dentro de una arquitectura cliente-servidor.",
    ]))
    story.append(PageBreak())

    add_heading(story, "REQUISITOS FUNCIONALES Y TÉCNICOS DEL PROYECTO")
    add_sub(story, "R01. Autenticación y control de acceso")
    story.append(bullet_list([
        "El sistema debe permitir iniciar sesión como administrador o empleado.",
        "El backend debe cifrar el PIN mediante BCrypt.",
        "Los endpoints deben restringirse por rol con Spring Security.",
        "En móvil y tablet debe permitirse login solo con PIN.",
    ]))
    add_sub(story, "R02. Gestión de productos y categorías")
    story.append(bullet_list([
        "El administrador puede crear, editar y borrar productos.",
        "El administrador puede crear, editar y borrar categorías.",
        "El empleado puede consultar el catálogo para añadir productos a una comanda.",
    ]))
    add_sub(story, "R03. Gestión de mesas y sala")
    story.append(bullet_list([
        "La aplicación debe mostrar un plano de mesas.",
        "Cada mesa debe almacenar coordenadas x e y en base de datos.",
        "El administrador puede editar el plano y mover las mesas.",
        "La mesa debe cambiar de estado según la comanda.",
    ]))
    add_sub(story, "R04. Gestión de comandas")
    story.append(bullet_list([
        "Se debe poder abrir una comanda por mesa.",
        "Se deben poder añadir líneas con producto y cantidad.",
        "La comanda debe pasar por estados ABIERTA, CERRADA y COBRADA.",
        "El total debe calcularse a partir de las líneas.",
    ]))
    add_sub(story, "R05. Informes")
    story.append(bullet_list([
        "El sistema debe mostrar total facturado, número de tickets, ticket medio y producto estrella.",
        "Debe representar la información en gráficos mediante Chart.js.",
    ]))
    story.append(PageBreak())

    add_heading(story, "DESCRIPCIÓN")
    add_sub(story, "Funcionamiento general paso por paso")
    for text in [
        "1. El usuario accede a la aplicación desde el navegador.",
        "2. Se autentica con email y PIN en escritorio, o con PIN único en móvil y tablet.",
        "3. El frontend guarda la sesión y muestra la sala.",
        "4. La pantalla de sala solicita al backend la lista de mesas y las dibuja según sus coordenadas.",
        "5. Al pulsar una mesa libre, se solicita el número de clientes y se abre la pantalla de comanda.",
        "6. La pantalla de comanda consulta los productos y la posible comanda activa de la mesa.",
        "7. El usuario añade productos, envía la comanda o la cobra.",
        "8. Al enviar o cobrar, el backend actualiza la comanda y el estado de la mesa.",
        "9. El administrador dispone además de productos, usuarios e informes.",
    ]:
        story.append(p(text, "BodyJ"))
    add_sub(story, "Descripción de módulos")
    story.append(bullet_list([
        "Login: controla autenticación, sesión y adaptación por dispositivo.",
        "Sala: representa el plano de mesas y su estado operativo.",
        "Comanda: permite añadir productos, recalcular ticket y persistir el pedido.",
        "Productos: administra el catálogo de productos y categorías.",
        "Usuarios: permite crear y editar usuarios con rol y PIN.",
        "Informes: resume las ventas a partir de comandas cobradas.",
    ]))
    story.append(PageBreak())

    add_heading(story, "ARQUITECTURA DEL SISTEMA")
    story.append(p("El sistema está dividido en frontend, backend y base de datos, conectados mediante una API REST.", "BodyJ"))
    story.append(p("Diagrama de arquitectura del sistema", "DiagramTitle"))
    story.append(arquitectura_sistema())
    story.append(PageBreak())

    add_heading(story, "ARQUITECTURA EN CAPAS DEL BACKEND")
    story.append(p(
        "El backend se organiza en capas diferenciadas. Los controladores gestionan la comunicación HTTP, los servicios concentran la lógica "
        "de negocio y los repositorios encapsulan el acceso a PostgreSQL mediante JPA.",
        "BodyJ"
    ))
    story.append(p("Diagrama de arquitectura en capas", "DiagramTitle"))
    story.append(capas_backend())
    story.append(PageBreak())

    add_heading(story, "CASOS DE USO")
    story.append(p(
        "Los actores del sistema son administrador y empleado. Ambos pueden operar sobre sala y comandas, mientras que la gestión avanzada "
        "queda reservada al administrador.",
        "BodyJ"
    ))
    story.append(p("Diagrama de casos de uso", "DiagramTitle"))
    story.append(casos_uso())
    story.append(PageBreak())

    add_heading(story, "DIAGRAMA DE CLASES")
    story.append(p(
        "Las clases principales del dominio son Usuario, Mesa, Categoria, Producto, Comanda, LineaComanda y Venta. "
        "Comanda actúa como núcleo del proceso operativo y se relaciona con Mesa y con sus líneas.",
        "BodyJ"
    ))
    story.append(p("Diagrama de clases", "DiagramTitle"))
    story.append(diagrama_clases())
    story.append(PageBreak())

    add_heading(story, "DIAGRAMA ENTIDAD-RELACIÓN")
    story.append(p(
        "La base de datos del sistema es relacional. Las relaciones más relevantes son Categoria-Producto, Mesa-Comanda y Comanda-LineaComanda. "
        "LineaComanda resuelve la relación entre una comanda y los productos que contiene.",
        "BodyJ"
    ))
    story.append(p("Diagrama entidad-relación", "DiagramTitle"))
    story.append(entidad_relacion())
    story.append(PageBreak())

    add_heading(story, "DISEÑO DE LA BASE DE DATOS")
    story.append(p(
        "La tabla usuario almacena nombre, email, PIN cifrado y rol. La tabla mesa conserva el número, capacidad, estado y coordenadas del plano. "
        "Producto se vincula con categoria, comanda se vincula con mesa y linea_comanda almacena cada línea de pedido con cantidad y copia de datos "
        "del producto. Venta existe como entidad adicional para evolución futura.",
        "BodyJ"
    ))
    story.append(p("Esquema lógico de tablas", "DiagramTitle"))
    story.append(diseno_bd())
    story.append(PageBreak())

    add_heading(story, "DIAGRAMA DE NAVEGACIÓN")
    story.append(p(
        "La navegación principal parte del login y conduce a sala. Desde sala se accede a comanda y, en escritorio o con permisos adecuados, "
        "a productos, informes y usuarios.",
        "BodyJ"
    ))
    story.append(p("Diagrama de navegación", "DiagramTitle"))
    story.append(navegacion())
    story.append(PageBreak())

    add_heading(story, "SEGURIDAD DEL SISTEMA")
    story.append(p(
        "El sistema utiliza Spring Security, autenticación basada en credenciales, contraseñas cifradas con BCrypt y autorización por roles. "
        "Los endpoints de administración exigen rol ADMIN, mientras que empleados y administradores comparten acceso a sala y comandas.",
        "BodyJ"
    ))
    story.append(p("Diagrama del flujo de seguridad", "DiagramTitle"))
    story.append(seguridad())
    story.append(PageBreak())

    add_heading(story, "TECNOLOGÍA")
    story.append(bullet_list([
        "HTML: estructura de las páginas del frontend.",
        "CSS: estilos visuales y adaptación responsive.",
        "JavaScript: lógica del cliente, consumo de API y renderizado dinámico.",
        "Spring Boot: framework principal del backend.",
        "Spring Security: autenticación y autorización.",
        "Spring Data JPA: persistencia sobre base de datos.",
        "PostgreSQL: almacenamiento relacional.",
        "Chart.js: generación de gráficos en informes.",
    ]))
    story.append(PageBreak())

    add_heading(story, "METODOLOGÍA")
    story.append(p(
        "El desarrollo del proyecto se ha organizado en fases: análisis del problema, diseño de datos y pantallas, implementación del frontend, "
        "desarrollo del backend, integración entre capas, incorporación de seguridad, adaptación responsive y documentación final.",
        "BodyJ"
    ))
    story.append(bullet_list([
        "Análisis de necesidades del restaurante.",
        "Definición de entidades, relaciones y roles.",
        "Construcción del frontend por pantallas.",
        "Implementación de API REST y seguridad.",
        "Integración con PostgreSQL.",
        "Pruebas funcionales y mejoras responsive.",
        "Documentación técnica y funcional.",
    ]))
    story.append(PageBreak())

    add_heading(story, "PRESUPUESTO")
    story.append(p(
        "Se estima una dedicación aproximada de 100 horas de desarrollo para análisis, diseño, implementación, pruebas y documentación. "
        "Tomando como referencia un coste de 20 € por hora, el coste orientativo del proyecto es de 2.000 €.",
        "BodyJ"
    ))
    add_heading(story, "CONTROL DE VERSIONES")
    story.append(p(
        "El proyecto se gestiona con Git, lo que permite mantener histórico de cambios, facilitar la recuperación de versiones y trabajar de forma ordenada sobre el código.",
        "BodyJ"
    ))
    story.append(PageBreak())

    add_heading(story, "TRABAJOS FUTUROS")
    story.append(bullet_list([
        "Sincronización en tiempo real entre dispositivos.",
        "Integración con impresoras de cocina.",
        "Gestión de reservas.",
        "Informes más avanzados por periodo y categoría.",
        "Módulo de inventario.",
        "Gestión de pagos integrada.",
    ]))
    story.append(PageBreak())

    add_heading(story, "VALOR FUNCIONAL DEL SISTEMA")
    story.append(p(
        "Orsy resuelve un caso de uso real y claramente defendible: la gestión de comandas en restauración. "
        "El sistema integra autenticación, control de sala, creación de comandas, administración de catálogo y análisis de ventas. "
        "Su valor reside en la claridad de uso y en su aplicabilidad a pequeños negocios que necesitan una herramienta práctica y accesible.",
        "BodyJ"
    ))
    story.append(PageBreak())

    add_heading(story, "CONCLUSIONES")
    story.append(p(
        "El proyecto ha permitido aplicar conocimientos de frontend, backend, seguridad y bases de datos en una solución completa y orientada a negocio. "
        "A lo largo del desarrollo se ha construido una arquitectura separada, mantenible y extensible, capaz de representar el flujo de trabajo real "
        "de un restaurante. El resultado es una aplicación funcional que cubre las necesidades principales del servicio y que puede seguir evolucionando.",
        "BodyJ"
    ))
    story.append(PageBreak())

    add_heading(story, "REFERENCIAS")
    story.append(bullet_list([
        "Spring Boot Documentation: https://spring.io/projects/spring-boot",
        "Spring Security Reference: https://spring.io/projects/spring-security",
        "PostgreSQL Documentation: https://www.postgresql.org/docs/",
        "Chart.js Documentation: https://www.chartjs.org/",
        "MDN Web Docs: https://developer.mozilla.org/",
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
        title="Memoria TFG Orsy",
        author="Marina Moreno Rodríguez",
    )
    doc.build(build_story(), onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    main()
