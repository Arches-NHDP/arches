function unicodeToHtmlCode (str) {
    // replace \u0000 by &#x0000; in the given string
    return str.replace(/\\[uU]([a-fA-F0-9]{4})/g, function(matchedString, group1) {
        return "&#x" + group1 + ";"
    })
}

function decodeUnicode(str) {
    return str.replace(/\\[uU]([a-fA-F0-9]{4})/g, function(matchedString, group1) {
        return String.fromCharCode(parseInt(group1, 16))
    })
}

function tst(){

  document.getElementById("deb").innerHTML = "test";


}
