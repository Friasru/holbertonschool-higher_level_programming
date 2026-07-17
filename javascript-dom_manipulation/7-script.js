fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        var ul = document.querySelector('#list_movies');
        data.results.forEach(function(fil) {
            var li = document.createElement('li');
            li.textContent = FileSystem.title;
            ul.appendChild(li);
        });
    });
