const searchField = document.querySelector('#searchField');
const appTable = document.querySelector('.product-grid');
const paginationContainer = document.querySelector('.pagination');
const cardContainer = document.querySelector('.card-body');

const tableOutput = document.querySelector('.table-output');
tableOutput.style.display = "none";

searchField.addEventListener('keyup', (e) => {

    const searchValue = e.target.value;
    if (searchValue.length > 0) {
        cardContainer.innerHTML = "";
        paginationContainer.style.display = "none"
        console.log("searchValue", searchValue);
        fetch("search_projets", {
                body: JSON.stringify({ searchText: searchValue }),
                method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                tableOutput.style.display = "block";
                appTable.style.display = "none";

                if (data.length === 0) {
                    tableOutput.innerHTML = "No results found";

                } else {
                    data.array.forEach((projet) => {
                        cardContainer.innerHTML += ` 
                        <img src = "/media/${ projet.image }" class = "img-fluid mb-3" alt = "" /> 
                        <h6 class = "product-title" > ${ projet.titre } </h6> 
                        <p class = "product-price fs-5 mb-1" > < span > statut du projet: ${ projet.statut } < /span></p >
                            <div class = "rating mb-0" >
                            <i class = "bi bi-star-fill text-warning" > < /i> 
                            <i class = "bi bi-star-fill text-warning" > < /i> 
                        <i class = "bi bi-star-fill text-warning" > < /i> 
                        <i class = "bi bi-star-fill text-warning" > < /i> 
                        <i class = "bi bi-star-fill text-warning" > < /i>
                        </div>
                        Mots clés ${projet.mots_cles}
                        <small>74 Vue(s)</small>
                         <div class="actions d-flex align-items-center justify-content-center gap-2 mt-3">
                          <a href="{% url 'projet_detail' projet.pk %}" tag='' class="btn btn-sm btn-outline-success">Detail</a>
                        </div> 
                        `;

                    });
                }
            });


    } else {
        tableOutput.style.display = "none";
        appTable.style.display = "block";
        paginationContainer.style.display = "block";
    }
});