window.addEventListener('load', () => {

    
    const sd = sessionStorage.getItem('sd');
    const ed = sessionStorage.getItem('ed');
    
    document.getElementById('sd').innerHTML = sd;
    document.getElementById('ed').innerHTML = ed;
    var fs=require('fs'); 
 

    fs.writeFile('data.txt', sd, function(err, result) {
        if(err) console.log('error', err);
      });
      fs.writeFile('data.txt', ed, function(err, result) {
        if(err) console.log('error', err);
      });


})