import httpGet from "../http_get.js"
import TableCreator from "../table_creator.js"
let ucastnici = JSON.parse(httpGet("/valtice_api/ucastnici"))
let registrovanych = JSON.parse(httpGet("/valtice_api/registrovanych"))["pocet"]

let tc = new TableCreator(document.getElementById("parent_div"), true, true, true)
tc.make_header(["Jméno", "E-mail", "Registrován", "Hlavní třída"])
ucastnici.forEach(element => {
    let jmeno_a = document.createElement("a")
    jmeno_a.href = "/valtice/ucastnik/" + element["id"]
    jmeno_a.innerText = element["full_name"]
    jmeno_a.setAttribute("class", "jmeno-a")
    let trida_a = document.createElement("a")
    trida_a.href = "/valtice/trida/" + element["hlavni_trida_1_id"]
    trida_a.innerText = element["hlavni_trida_1"]
    trida_a.setAttribute("class", "trida-a")
    let email_element
    if (element["email"] == "-") {
        email_element = document.createElement("span")
        email_element.innerText = "-"
    } else {
        let a = document.createElement("a")
        a.href="mailto:" + element["email"]
        a.innerText = element["email"]
        email_element = a
    }
    tc.make_row([jmeno_a, email_element, element["registrovan"], trida_a])
});

document.getElementById("total").innerText = ucastnici.length
document.getElementById("registrovanych").innerText = String(registrovanych) + " (" + String(Math.round(registrovanych / ucastnici.length * 100)) + "%)"