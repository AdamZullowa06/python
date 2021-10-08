# python keyword argument list

def create_html(tag, text, **attributes) :
    html = f"<{tag}"
    for key, value in attributes.items() :
        html = html + f" {key}='{value}'"
    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "helo world", href="www.google.com", style="link")
print(html)