// Initialize Firebase
// Initialize Firebase
var firebaseConfig = {
  apiKey: "AIzaSyBR5ADeIWMZ0YUSPhvCMT_IISCa-cmb4EE",
  authDomain: "stock-data-fc41e.firebaseapp.com",
  projectId: "stock-data-fc41e",
  storageBucket: "stock-data-fc41e.appspot.com",
  messagingSenderId: "31054906120",
  appId: "1:31054906120:web:6a511eb07276159eb0a2bd"
};
firebase.initializeApp(firebaseConfig);

//Reference messages collection
  // Reference Messages collection
  let contactInfo = firebase.database().ref("information");




  document.querySelector(".contact-form").addEventListener("submit", submitForm);
  
  function submitForm(e) {
    e.preventDefault();
  

    let sd= document.querySelector(".sd").value;
    let ed = document.querySelector(".ed").value;
  
    console.log( sd,ed);
  
    saveContactInfo(sd,ed);
    alert("Your Message has been sent Successfully. Thank You!");
    document.querySelector(".contact-form").reset();
  }
  
  
  
  
  function saveContactInfo(sd,ed) {
    let newContactInfo = contactInfo.push();
  
    newContactInfo.set({
      sd: sd,
      ed: ed,
      
    });
  }