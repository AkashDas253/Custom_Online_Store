from django.shortcuts import render
from .models import OrderItem,Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):

    cart = Cart(request)
    if request.method == 'POST':

        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            
            # clear the cart
            cart.clear()

            return render(request,  'orders/order/created.html',  {'order': order})

    else:

        form = OrderCreateForm()

    return render(request, 'orders/order/create.html',  {'cart': cart, 'form': form})



from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,  'admin/orders/order/detail.html',  {'order': order})



"""from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')])
    
    return response"""

from django.conf import settings
from django.http import HttpResponse
import os
from io import BytesIO
from xhtml2pdf import pisa

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    template_path = 'orders/order/pdf.html'
    context = {'order': order}

    # Render HTML template to string
    html = render(request, template_path, context).content.decode("utf-8")

    # Create a BytesIO buffer to receive the PDF data
    buffer = BytesIO()

    # Generate PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(html, dest=buffer, encoding='utf-8', link_callback=fetch_resources)

    if not pisa_status.err:
        # If PDF generation was successful, get the PDF data from the buffer
        pdf_data = buffer.getvalue()
        buffer.close()
        
        # Create a HttpResponse object with PDF data
        response = HttpResponse(pdf_data, content_type='application/pdf')
        response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
        
        return response
    else:
        # If PDF generation fails, return an error response
        return HttpResponse('Error generating PDF', status=500)

def fetch_resources(uri, rel):
    # Function to fetch external resources such as CSS files
    # Replace 'settings.STATIC_ROOT' with the path to your CSS file
    if uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, "css/pdf.css"))
        return path
    return uri
