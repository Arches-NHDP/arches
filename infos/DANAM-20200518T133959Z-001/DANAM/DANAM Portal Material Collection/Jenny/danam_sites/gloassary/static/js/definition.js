var modal = document.getElementById("definitionModal")

var span = modal.getElementsByClassName("close")[0]
var definition = modal.getElementsByClassName("definition")[0]
var en = modal.getElementsByClassName("en")[0]
var dev = modal.getElementsByClassName("dev")[0]
function displayModal(message, eng, devn) {
    modal.style.display = "block"
    modal.classList.add('fade-in')
    definition.innerHTML = message
    en.innerHTML = eng
    dev.innerHTML = devn
    
}
function hideModal(message, eng, devn) {
    modal.style.display = "none"
    modal.classList.remove('fade-in')
    definition.innerHTML = message
    en.innerHTML = eng
    dev.innerHTML = devn
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    hideModal("No data", "", "")
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    hideModal("No data", "", "")
  }
}

document.getElementById('content').addEventListener('dblclick', handleDbClick)

function handleDbClick() {
    var selectedWord = ""
    
    if (window.getSelection) {
        selectedWord = window.getSelection()
    }
    else if (document.getSelection) {
        selectedWord = document.getSelection()
    } else if (document.selection) {
        selectedWord = document.selection.createRange().text
    }
    
    selectedWord = encodeURI(selectedWord.toString().trim())
    if(selectedWord !== ''){
        fetch(`/vocab/api/vocab/${selectedWord}/`)
            .then((resp) => resp.json())
            .then(function(data) {
                // console.log(data);
                
                var def = unicodeToHtmlCode(data.message)
                var english = unicodeToHtmlCode(data.en)
                var np = unicodeToHtmlCode(data.dev)
                // console.log(def)
                // console.log(decodeUnicode(data.message))
                displayModal(def, english, np)
            })
            .catch(function(err) {
                console.log('error during fetch', err)
            })
    }

}
function highlight(text){
        // html = document.documentElement.innerHTML;
        html = document.getElementById('content').innerHTML;
       
      //  alert(html);
        //text = text.trim();
        //text="kav";
        re = new RegExp(text,'g');
      
        //re = new RegExp("/\b" + text + "b/g"); 
        //alert(re);
        
        if(re.test(html)){
            html = html.replace(re, '<span class="highlight-text">'+ " " + text+'</span>');
        }
        html = unicodeToHtmlCode(html);
        document.getElementById('content').innerHTML = html;
    }
 
function unicodeToHtmlCode (str) {
    // replace \u0000 by &#x0000; in the given string
    return str.replace(/\\[uU]([a-fA-F0-9]{4})/g, function(matchedString, group1) {
        return "&#x" + group1 + ";"
    })
}

function decodeUnicode(str) {
    return str.replace(/\[uU]([a-fA-F0-9]{4})/g, function(matchedString, group1) {
        return String.fromCharCode(parseInt(group1, 16))
    })
}
    

    fetch(`/vocab/api/vocablist/all`)
        .then((resp) => resp.json())
        .then(function(data) {
    // console.log(data);
            for (i in data.list){
                //var def = unicodeToHtmlCode(data.list[i]);
                //alert(def);
                highlight(data.list[i]);
                //highlight(def);
            }
        })
        .catch(function(err) {
        console.log('error during fetch', err)
        })
        
