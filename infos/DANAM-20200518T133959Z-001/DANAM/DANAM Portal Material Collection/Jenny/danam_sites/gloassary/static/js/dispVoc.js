var modal = document.getElementById("definitionModal")

var span = modal.getElementsByClassName("close")[0]
var definition = modal.getElementsByClassName("definition")[0]

function displayModal(message) {
	    modal.style.display = "block"
	    modal.classList.add('fade-in')
	    definition.innerHTML = message
}
function hideModal(message) {
	    modal.style.display = "none"
	    modal.classList.remove('fade-in')
	    definition.innerHTML = message
}
// When the user clicks on <span> (x), close the modal
 span.onclick = function() {
     hideModal("No data")
}

//     // When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
     hideModal("No data")
    }
}

document.getElementById('content').addEventListener('dblclick', handleDbClick)

function handleDbClick() {
  var selectedWord = ""
  alert("test");
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
        fetch(`/api/definition/${selectedWord}/`)
        .then((resp) => resp.json())
        .then(function(data) {
                                                                                                                         // console.log(data);
            var def = unicodeToHtmlCode(data.message)
                                                                                                                                     // console.log(def)
                                                                                                                                  // console.log(decodeUnicode(data.message))
                                                                                                                                 displayModal(def)
                                                                                                                              })
        .catch(function(err) {
           console.log('error during fetch', err)
         })
     }
}

function unicodeToHtmlCode (str) {
 // replace \u0000 by &#x0000; in the given string
          return str.replace(/\\[uU]([a-fA-F0-9]{4})/g, function(matchedString, group1) {
          return "&#x" + group1 + ";"
})
//                                                                                                                                                                                                                                                                     }
//
//                                                                                                                                                                                                                                                                     function decodeUnicode(str) {
//                                                                                                                                                                                                                                                                         return str.replace(/\[uU]([a-fA-F0-9]{4})/g, function(matchedString, group1) {
//                                                                                                                                                                                                                                                                                 return String.fromCharCode(parseInt(group1, 16))
//                                                                                                                                                                                                                                                                                     })
//                                                                                                                                                                                                                                                                                     }var modal = document.getElementById("definitionModal")
//
//                                                                                                                                                                                                                                                                                     var span = modal.getElementsByClassName("close")[0]
//                                                                                                                                                                                                                                                                                     var definition = modal.getElementsByClassName("definition")[0]
//
//                                                                                                                                                                                                                                                                                     function displayModal(message) {
//                                                                                                                                                                                                                                                                                         modal.style.display = "block"
//                                                                                                                                                                                                                                                                                             modal.classList.add('fade-in')
//                                                                                                                                                                                                                                                                                                 definition.innerHTML = message
//                                                                                                                                                                                                                                                                                                 }
//                                                                                                                                                                                                                                                                                                 function hideModal(message) {
//                                                                                                                                                                                                                                                                                                     modal.style.display = "none"
//                                                                                                                                                                                                                                                                                                         modal.classList.remove('fade-in')
//                                                                                                                                                                                                                                                                                                             definition.innerHTML = message
//                                                                                                                                                                                                                                                                                                             }
//                                                                                                                                                                                                                                                                                                             // When the user clicks on <span> (x), close the modal
//                                                                                                                                                                                                                                                                                                             span.onclick = function() {
//                                                                                                                                                                                                                                                                                                                 hideModal("No data")
//                                                                                                                                                                                                                                                                                                                 }
//
//                                                                                                                                                                                                                                                                                                                 // When the user clicks anywhere outside of the modal, close it
//                                                                                                                                                                                                                                                                                                                 window.onclick = function(event) {
//                                                                                                                                                                                                                                                                                                                   if (event.target == modal) {
//                                                                                                                                                                                                                                                                                                                       hideModal("No data")
//                                                                                                                                                                                                                                                                                                                         }
//                                                                                                                                                                                                                                                                                                                         }
//
//                                                                                                                                                                                                                                                                                                                         document.getElementById('content').addEventListener('dblclick', handleDbClick)
//
//                                                                                                                                                                                                                                                                                                                         function handleDbClick() {
//                                                                                                                                                                                                                                                                                                                             var selectedWord = ""
//                                                                                                                                                                                                                                                                                                                                 alert("test");
//                                                                                                                                                                                                                                                                                                                                     if (window.getSelection) {
//                                                                                                                                                                                                                                                                                                                                             selectedWord = window.getSelection()
//                                                                                                                                                                                                                                                                                                                                                 }
//                                                                                                                                                                                                                                                                                                                                                     else if (document.getSelection) {
//                                                                                                                                                                                                                                                                                                                                                             selectedWord = document.getSelection()
//                                                                                                                                                                                                                                                                                                                                                                 } else if (document.selection) {
//                                                                                                                                                                                                                                                                                                                                                                         selectedWord = document.selection.createRange().text
//                                                                                                                                                                                                                                                                                                                                                                             }
//
	//                                                                                                                                                                                                                                                                                                                                                                                 selectedWord = encodeURI(selectedWord.toString().trim())
	//                                                                                                                                                                                                                                                                                                                                                                                     if(selectedWord !== ''){
//                                                                                                                                                                                                                                                                                                                                                                                             fetch(`/api/definition/${selectedWord}/`)
//                                                                                                                                                                                                                                                                                                                                                                                                         .then((resp) => resp.json())
//                                                                                                                                                                                                                                                                                                                                                                                                                     .then(function(data) {
//                                                                                                                                                                                                                                                                                                                                                                                                                                     // console.log(data);
//                                                                                                                                                                                                                                                                                                                                                                                                                                                     var def = unicodeToHtmlCode(data.message)
	//                                                                                                                                                                                                                                                                                                                                                                                                                                                                     // console.log(def)
	//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     // console.log(decodeUnicode(data.message))
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     displayModal(def)
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 })
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             .catch(function(err) {
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             console.log('error during fetch', err)
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         })
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             }
//
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             }
//
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             function unicodeToHtmlCode (str) {
	//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 // replace \u0000 by &#x0000; in the given string
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     return str.replace(/\\[uU]([a-fA-F0-9]{4})/g, function(matchedString, group1) {
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             return "&#x" + group1 + ";"
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 })
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 }
	//
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 function decodeUnicode(str) {
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     return str.replace(/\[uU]([a-fA-F0-9]{4})/g, function(matchedString, group1) {
	//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             return String.fromCharCode(parseInt(group1, 16))
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 })
	//                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 }
