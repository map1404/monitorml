var firebaseConfig = {
    apiKey: "AIzaSyDAtboqc4-E2zZ4G0Vlkccj2c9nyG0Gssw",
    authDomain: "patient-vitals.firebaseapp.com",
    projectId: "patient-vitals",
    storageBucket: "patient-vitals.appspot.com",
    messagingSenderId: "1079942926348",
    appId: "1:1079942926348:web:254b8d0b553a0788429e29"
  };

  firebase.initializeApp(firebaseConfig);
  var firestore = firebase.firestore()

  const db = firestore.collection("patientForm")

  
  let submitButton = document.getElementById('submit')

  //create event listener to allow form submission

  submitButton.addEventListener("click",(e)=>{
      // Prevent default form submission behaviour
      e.preventDefault()

      // Get form values
      let firstName = document.getElementById('fname').value
      let lastName = document.getElementById('lname').value
      let doctorName = document.getElementById('docname').value
      let bloodPressure = document.getElementById('bloodpres').value
      let oxygenSaturation = document.getElementById('oxygensat').value
      let pulseRate = document.getElementById('pulserate').value
      let temparature = document.getElementById('temp').value

      // Save Form Data to Firebase
      db.doc().set({
          fname: firstName,
          lname: lastName,
          docname: doctorName,
          bloodpres: bloodPressure,
          oxygensat: oxygenSaturation,
          pulserate: pulseRate,
          temp:temparature
      }).then(()=>{
          console.log("Data saved")
      }).catch((error) =>{
        console.log(error)
      })
      //alert after form submitted
      alert("Form is submitted successfully")
  })