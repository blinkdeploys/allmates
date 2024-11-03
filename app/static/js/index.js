function toggleByName(name, show=null) {
    const doms = document.getElementsByName(name);
    for (const dom of doms) {
        if (dom) {
            if (show !== true && show !== false) { show = dom.className.includes("d-none"); }
            if (show) { dom.classList.remove('d-none'); }
            else { dom.classList.add('d-none'); }
        }
    }
}

function toggleById(id, show=false) {
    const dom = document.getElementById(id);
    if (dom) {
        if (show) {
            dom.classList.remove('d-none');
        } else {
            dom.classList.add('d-none');
        }
    }
}