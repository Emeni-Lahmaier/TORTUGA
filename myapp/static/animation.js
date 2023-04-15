function flipCard(cardContainer) {
    cardContainer.classList.toggle("card-flipped");
}

function editCard(cardContainer) {
    // Remove card-flipped class from all other card containers
    var cardContainers = document.querySelectorAll(".card-container");
    for (var i = 0; i < cardContainers.length; i++) {
        if (cardContainers[i] != cardContainer) {
            cardContainers[i].classList.remove("card-flipped");
        }
    }

    // Flip the clicked card container
    cardContainer.classList.add("card-flipped");
}
