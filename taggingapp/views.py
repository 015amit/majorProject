from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
import PyPDF2
import os


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def newfile(request):
    filename = request.POST['filename'] # assuming filename is received via POST request
    filepath = os.path.join('static', filename)
    with open(filepath, 'w') as f:
        # You can write to the file here if you want to
        pass # do nothing
        
    return HttpResponse('File created successfully')
    
import io

def openfile(request):
    pdfFileObj = request.FILES['file'] 
    name = request.FILES['file'].name
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
    n = pdfReader.numPages
    pageObj = pdfReader.getPage(0)
    x = pageObj.extractText()
    for i in range(n):
        if i != 0:
            pageObj = pdfReader.getPage(i)
            x += pageObj.extractText()

    # Create a BytesIO object to store the file data
    file_data = io.BytesIO()
    
    # Write the file data to the BytesIO object
    file_data.write(x.encode('utf-8'))

    # Reset the position of the BytesIO object to the beginning
    file_data.seek(0)

    # Create a response object with the file data as the content
    response = HttpResponse(file_data, content_type='application/pdf')
    
    # Set the filename in the Content-Disposition header
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(name)
    
    return response


def find_and_replace(request):
    text = request.POST.get('text', '')
    search_text = request.POST.get('search_text', '')
    replace_text = request.POST.get('replace_text', '')
    replace_count = 0
    
    if text and search_text and replace_text:
        text = text.replace(search_text, replace_text, -1)
        replace_count = text.count(replace_text)
    
    return JsonResponse({'text': text, 'replace_count': replace_count})