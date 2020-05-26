from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
#from glossary_form import Glossary_Form

# Create your views here.

from django.http import HttpResponse
import rdflib



def index(request):
    return render(request, "glossary/index.html")

def showVoc(request):
    return render(request, "glossary/danamvocab.html")

def showDetail(request, word):
    return render(request, "glossary/details.html")

def category(request, category_name_url):
    context = RequestContext(request)
    cat_list = get_category_list()
    category_name = decode_url(category_name_url)

    context_dict = {'cat_list': cat_list, 'category_name': category_name}

    try:
        category = Category.objects.get(name=category_name)

        # Add category to the context so that we can access the id and likes
        context_dict['category'] = category

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
    except Category.DoesNotExist:
        pass

    return render_to_response('glossary/glossarytest.html', context_dict, context)

def enterGLOSSARY(request):
	return render(request, "glossary/glossarytest.html")
    #pass


#@login_required
def like_category(request):
    #context = RequestContext(request)
    cat_id = None
    #if request.method == 'GET':
    #    cat_id = request.GET['category_id']

    likes = 0
    #if cat_id:
    category = Category.objects.get(id=int(cat_id))
    if category:
        likes = category.likes + 1
        category.likes =  likes
        category.save()

    return HttpResponse(likes)

def txtClient(request):
    txtText = request.POST.get('sometext')	
    return HttpResponse(sometext)

def harverst_term(request):
    # if this is POST request then the form is processed
    
    if request.method == 'POST':

        pop_form = Glossary_Form(request.POST)

        if pop_form.is_valid():  

            return HttpResponseRedirect('/thanks/')
    else:

        pip_form = Glossary_Form()

    return render(request, 'gloassrytest.html', {'pop_form': form})

def returnVocList(request, word):


    word = word.encode('ascii', 'backslashreplace').decode('utf-8')
    
    g = rdflib.Graph()
    g.parse("danamvocab/static/skos/nhdp-vocab.skos")

    query="""
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT ?definition ?label
        WHERE {
            ?concept skos:prefLabel ?label .
           OPTIONAL {?concept skos:definition ?definition}.
        }order by ASC(?label)
    """

    q = query.encode('UTF-8')
    qres = g.query(q)

    hasDefinition = False

    voca = []
    defn = []
    count = 0

    blFlag = False
    
    for row in qres:
        if word in row.label:
            lblVoca = row.label
            txtDefn = row.definition
            strVoc = extractVocab(lblVoca)
            strDefn = extractVocab(txtDefn)
            voca.insert(count, strVoc)
            defn.insert(count, strDefn)
            count = count + 1
            blFlag = True
        elif word == "all":
            lblVoca = row.label
            txtDefn = row.definition
            strVoc = extractVocab(lblVoca)
            strDefn = extractVocab(txtDefn)
            voca.insert(count, strVoc)
            defn.insert(count, strDefn)
            count = count + 1
            blFlag = True
        
        
    
    if blFlag:
        response =  JsonResponse(data={ 'type': 'success', 'list': voca, 'def': defn  })
        #print(response)
    else:
        response =  JsonResponse(data={'type': 'error', 'list': 'No vocaulary list exists' }, status=404)
    return response

def getWordDefinition(request, word):
   # print('----------- New request ------------')
   # print(word)
   # print(word.encode('ascii', 'backslashreplace'))
    
    # convert the word to unicode
    word = word.encode('ascii', 'backslashreplace').decode('utf-8')

   # print(word)

    g = rdflib.Graph()
    g.parse("danamvocab/static/skos/nhdp-vocab.skos")

    query="""
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX local: <http://localhost:8000/>
        SELECT ?definition ?label ?altlabel ?image ?note
        WHERE {  
            ?concept skos:prefLabel ?label .
           OPTIONAL {?concept skos:definition ?definition}.
           OPTIONAL {?concept skos:altLabel ?altlabel}.
           OPTIONAL {?concept skos:scopeNote ?note}.
           OPTIONAL {?concept local:image ?image}.
        }
    """
    
    q = query.encode('UTF-8')
    qres = g.query(q)

    hasDefinition = False
    definition = ""
    word = '"value": "' + word + '"'
    for row in qres:
        if  word in row.label:
            
            defn = row.definition
            definition = extractVocab(defn)
            #label = row.label
            lbl = extractVocab(row.label)
            #altlabel = row.altlabel
            altlbl = extractVocab(row.altlabel)
            #image = row.image
            nte = extractVocab(row.note)
            imgs = extractVocab(row.image)
            
            hasDefinition = True

    if hasDefinition:
        #response =  JsonResponse(data={ 'type': 'success', 'message': definition, 'en': lbl})
        response =  JsonResponse(data={ 'type': 'success', 'message': definition, 'en': lbl, 'dev': altlbl, 'image': imgs, 'note':nte})
    else:
        response =  JsonResponse(data={'type': 'error', 'message': 'No definition for this word', 'image': imgs }, status=404)

    # or if necessary look at https://github.com/ottoyiu/django-cors-headers 
    # response["Access-Control-Allow-Origin"] = "*"

    return response

def extractVocab(word):

    if word:
        voc = word.split('value": "', 1)
        voc = voc[1]
        voc = voc.split('"}', 1)
        voc = voc[0]

        return voc
    else:
        return ''




    