try:
    import cStringIO as StringIO
except ImportError:
    try:
        import StringIO as StringIO
    except ImportError:
        from io import StringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

from django.http import HttpResponse
import json as json2

def index(request, json):
    json = json2.loads(json)
    return render_to_pdf('mytemplate.html', json)
