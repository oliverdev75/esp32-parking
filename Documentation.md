## Jinja
### Que es y para que sirve?
Es un motor de plantillas 'templates' que permite combinar archivos HTML estáticos con datos proporcionados desde Python. 
### Como se usa?
1. **Configura Flask con un archivo HTML:**
Flask utiliza Jinja por defecto para manejar las plantillas. Los archivos HTML deben estar dentro de una carpeta llamada templates.
2. **Crear una plantilla HTML**
3. **Renderiza la plantilla desde Python**

```
@app.route('/RenderTemplateTest', methods=['GET', 'POST'])
def RenderTemplateTest():
    return render_template('index.html')
```
