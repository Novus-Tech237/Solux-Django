from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context={}):
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if pdf.error:
        return HttpResponse("Invalid PDF",status_code=400, context_type = 'text/plain')
    return HttpResponse(result.getvalue(), context_type = 'application/pdf')