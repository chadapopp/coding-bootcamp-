const allLi = document.querySelectorAll(".tab-link")
for(const tabLi of allLi) {
    tabLi.addEventListener("click", handleTabClick)
}
const tabContents = document.querySelectorAll(".tab-content")
function handleTabClick(event) {
    // console.log(event.target)
    const element = event.target
    const targetId = element.getAttribute("data-target")

    // Hide all tab content
    for(const tabContent of tabContents) {
        tabContent.classList.remove("active")
    }
    // Remove class active from all li
    for(const li of allLi) {
        li.classList.remove("active")
    }
    
    document.querySelector(targetId).classList.add("active")
    element.classList.add("active")
}