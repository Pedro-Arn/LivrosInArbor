document.getElementById("header").innerHTML = fetch("{% templates 'header.html' %}")
    .then(response => response.text())
    .then(data => document.getElementById('header').innerHTML = data);

document.getElementById("footer").innerHTML = fetch("{% static 'html/footer.html' %}")
    .then(response => response.text())
    .then(data => document.getElementById('footer').innerHTML = data);
