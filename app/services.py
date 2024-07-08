from .models import Orden, OrdenItem, Producto

class OrderService:
    def __init__(self, orden_id):
        self.orden = Orden.objects.get(id=orden_id)

    def complete_order(self):
        if not self.orden.completada:
            self.orden.completada = True
            self.orden.save()
            self.reduce_stock()
        
    def reduce_stock(self):
        orden_items = OrdenItem.objects.filter(orden=self.orden)
        for item in orden_items:
            producto = item.producto
            producto.stock -= item.cantidad
            producto.save()
