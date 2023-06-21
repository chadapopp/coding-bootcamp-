document.querySelector("input").addEventListener("keyup", searchTable)

function searchTable(event)
{
    const query = event.target.value.toLowerCase()
    const allRows = document.querySelectorAll("table tbody tr")
    for(let i=0; i < allRows.length; i++) {
        const row = allRows[i]
        const rowColumns = row.querySelectorAll("td")
        let match = false
        for(let j=0; j < rowColumns.length;j++) {
            const td = rowColumns[j]
            if(td.textContent.toLowerCase().includes(query)) {
                match = true
                break;
            }
        }
        if(match) {
            row.classList.remove("hide")
        } else {
            row.classList.add("hide")
        }
    }
}