let refresh = function() {
    let imgs = document.getElementsByTagName( 'img');

    for ( let i = 0; i < imgs.length; i++) {
        let src = imgs.item(i).getAttribute('data-src');
        src += '#t=' + Date.now();
        imgs.item(i).setAttribute('src', src);

    };
}
window.setInterval( refresh, 30000);
