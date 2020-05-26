
import json
import uuid
from django.http import Http404, HttpResponse, JsonResponse
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from django.shortcuts import render

g = Graph()
source_file = "gloassary/static/skos/danam_glossary.skos"
g.parse(source_file, format="application/rdf+xml")
skos= Namespace("http://www.w3.org/2004/02/skos/core#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
danam = Namespace("https://uni-heidelberg.de/danam/glossaries/terms/images/")
g_eng = g_nep = g_def = g_uuid = g_thumb = g_imag = g_heidicon = ""        
def list_terms(request):
    
    if request.is_ajax():
        #actual_data = []

        query = """
                PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX danam: <https://uni-heidelberg.de/danam/glossaries/terms/images/>
                SELECT ?concept ?definition ?label ?altlabel ?img ?it ?heidicon
                WHERE {  
                   ?concept rdf:type skos:Concept .
                   ?concept skos:prefLabel ?label .
                   ?concept danam:image ?img .
                   OPTIONAL {?concept skos:definition ?definition} .
                   OPTIONAL {?concept skos:altLabel ?altlabel} .
                   OPTIONAL {?concept danam:image ?img} .
                   OPTIONAL {?concept danam:imagethumbnail ?it} .
                   OPTIONAL {?concept danam:heidicon ?heidicon} .
                }
                ORDER BY ASC(?label)
            """

        q = query.encode('UTF-8')
        qres = g.query(q)
        #raw_data = {"eng": "", "np": "", "desc": ""}
        #data = []
        #for row in qres:
        #    raw_data["eng"]=row.label
        #    raw_data["np"]=row.altlabel
        #    raw_data["desc"]=row.definition
        #    data.append(raw_data)

        #print(data)
        #data = json.dumps(data)
        data = qres.serialize(format='json')
        return HttpResponse(data, content_type='application/json')

    else:
        raise Http404
def add_terms(request):

    if request.is_ajax() and request.POST:
        strText = request.POST.get('term-roman') 
        data = {'message': "%s added" % strText}
        
        trmRoman = request.POST.get('term-roman')
        trmDev = request.POST.get('term-dev')
        trmDes = request.POST.get('description')
        trmImgThumb = request.POST.get('thumb')
        trmImage = request.POST.get('image_link')
        trmHeidICON = request.POST.get('heidicon')


        strUUID = str(uuid.uuid4())
        indTerm = URIRef(skos+strUUID)


        g.add( (indTerm, RDF.type, skos.Concept))
        g.add( (indTerm, skos.prefLabel, Literal(trmRoman, lang="EN")) )
        g.add( (indTerm, skos.altLabel, Literal(trmDev, lang="NP")) )
        g.add( (indTerm, skos.definition, Literal(trmDes, lang="EN")) )
        g.add( (indTerm, danam.image, Literal(trmImage, lang="EN")) )
        g.add( (indTerm, danam.imagethumbnail, Literal(trmImgThumb, lang="EN")) )
        g.add( (indTerm, danam.heidicon, Literal(trmHeidICON, lang="EN")) )
        g.serialize(destination=source_file,  format="application/rdf+xml")

        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404

def remove_terms(request):
    
    if request.is_ajax() and request.POST:
        strTxt = request.POST.get('delete')

        msg = {'message': "%s deleted" % strTxt}
        delIndTerm = URIRef(strTxt)

        g.remove( (delIndTerm, None, None) )
        g.serialize(destination=source_file,  format="application/rdf+xml")

        return HttpResponse(json.dumps(msg), content_type='application/json')
    else:
        raise Http404 

def do_update_terms(request):
    if request.is_ajax() and request.POST:
        strTxt = request.POST.get('uuid')

        msg = {'message': "%s updated" % strTxt}
        indTerm = URIRef(strTxt)
        trmRoman = request.POST.get('term-roman')
        trmDev = request.POST.get('term-dev')
        trmDes = request.POST.get('description')
        trmImg = request.POST.get('image_link')
        trmImgThumb = request.POST.get('thumb')
        trmHeidICON = request.POST.get('heidicon')

        g.remove( (indTerm, None, None) )

        g.add( (indTerm, RDF.type, skos.Concept))
        g.add( (indTerm, skos.prefLabel, Literal(trmRoman, lang="EN")) )
        g.add( (indTerm, skos.altLabel, Literal(trmDev, lang="NP")) )
        g.add( (indTerm, skos.definition, Literal(trmDes, lang= "EN")) )
        g.add( (indTerm, danam.image, Literal(trmImg, lang="EN")) )
        g.add( (indTerm, danam.imagethumbnail, Literal(trmImgThumb, lang="EN")) )
        g.add( (indTerm, danam.heidicon, Literal(trmHeidICON, lang="EN")) )
        g.serialize(destination=source_file,  format="application/rdf+xml")

        return HttpResponse(json.dumps(msg), content_type='application/json')
    else:
        raise Http404 

def upload_terms(request):
    
    
    
    global g_uuid, g_eng, g_nep, g_def, g_imag, g_thumb, g_heidicon
    if request.is_ajax() and request.POST:
        
        
        
        g_uuid = request.POST.get('uuid')
        g_eng = request.POST.get('eng')
        g_nep = request.POST.get('nep')
        g_def = request.POST.get('def')
        g_imag = request.POST.get('imag')
        g_thumb = request.POST.get('thumb')
        g_heidicon = request.POST.get('heidicon')
        
        data = {"uuid": g_uuid, "eng": g_eng, "np": g_nep, "def": g_def, "imag": g_imag, "thumb": g_thumb, "heidicon": g_heidicon}
        
        return HttpResponse(json.dumps(data), content_type='application/json')
        
    else:
        raise Http404
        
    
def glossary_listing(request):
    return render(request, "glossary/list.html")

def test(request):
    return render(request, "glossary/tablesort.html")

def update_terms(request):
    global g_uuid, g_eng, g_nep, g_def, g_imag, g_thumb, g_heidicon
    return render(request, "glossary/editterms.html", {"uuid": g_uuid, "eng": g_eng, "np": g_nep, "def": g_def, "imag": g_imag, "thumb": g_thumb, "heidicon": g_heidicon})
def easydb_imagepicker(request):
    return render(request, "glossary/imgpicker.html")