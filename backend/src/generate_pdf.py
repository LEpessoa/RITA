import jinja2
import pdfkit
from datetime import datetime


def gen_pdf():
    my_name = "Frank Andrade"
    item1 = "TV"
    item2 = "Couch"
    item3 = "Washing Machine"
    today_date = datetime.today().strftime("%d %b, %Y")

    context = {
        "my_name": my_name,
        "item1": item1,
        "item2": item2,
        "item3": item3,
        "today_date": today_date,
    }

    template_loader = jinja2.FileSystemLoader("../pdf_templates/report")
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template("index.html")
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    pdfkit.from_string(
        output_text,
        "pdf_generated.pdf",
        configuration=config,
        css="../pdf_templates/report/style.css",
    )
