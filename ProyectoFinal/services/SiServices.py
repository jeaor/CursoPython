from rich.console import Console
from rich.prompt import Prompt
from sqlite3 import Connection
from config.email import EmailService
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

def SistInmobiliaria(conn:Connection):
    console.clear()
    console.print("[bold blue]===Sistema Inmobiliaria===[/bold blue]")
    
    console.print("[bold red]1. Ver todos los Productos[/bold red]")
    console.print("[bold white]2. Ver Producto(Especifico)[/bold white]")
    console.print("[bold green]3. Salir[/bold green]")
    
    opcion = Prompt.ask("Seleccione una opcion", choices=["1", "2", "3"], default="1")
    if opcion == "1":
        all_productos(conn)
    elif opcion == "2":
        all_productos_especifico(conn)
    elif opcion == "3":
        return
def all_productos(conn:Connection):
    console.print("[bold red]TODOS LOS PRODUCTOS[/bold red]")
    cursor = conn.cursor()
    cursor.execute("select id_producto, codigo_producto, titulo from productos")
    productos = cursor.fetchall()
    
    console.print("[bold red]ESTOS SON LOS PRODUCTOS[/bold red]")
    product_panel = Panel(
            Text("PRODUCTOS", style="bold green"),
            style="bright_green",
            box=box.DOUBLE
        )
    console.print(product_panel)
    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("Codigo", style="cyan", justify="center")
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Titulo", style="cyan", justify="center")
    for i in productos:
        table.add_row(str(i[0]), str(i[1]), str(i[2]))
        
    console.print(table)
    
    console.input("[bold red]Presione enter para salir[/bold red]")
def all_productos_especifico(conn:Connection):
    console.print("[bold red] PRODUCTOS [/bold red]")
    id_producto = int(Prompt.ask("[bold blue]Ingrese el id del producto a buscar[/bold blue]"))
    cursor = conn.cursor()
    consulta = "select id_producto, codigo_producto, titulo from productos where id_producto = ?"
    cursor.execute(consulta, (id_producto,))
    producto1 = cursor.fetchone()
    if not producto1:
        console.print("[bold red]Producto no encontrado[/bold red]")
        return
    panel = Panel(
        Text("DETALLE DEL PRODUCTO", style="bold green"),
        box=box.DOUBLE,
        style="bright_green"
    )
    console.print(panel)

    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Código", style="cyan", justify="center")
    table.add_column("Título", style="white", justify="center")

    table.add_row(str(producto1[0]), producto1[1], producto1[2])

    console.print(table)
    console.input("\nPresione Enter para salir")
    
    # #EMAIL
    # subject = "Consulta del producto"
    # mensaje = f"""
    # Se ha encontrado el producto.
    
    # ID: {producto1[0]}
    # Codigo: {producto1[1]}
    # Titulo: {producto1[2]}
    # """