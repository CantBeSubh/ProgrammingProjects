function myFunction() {
  let name = document.getElementById("name").value;
  let number = document.getElementById("numb").value;
  let dob = document.getElementById("dob").value;
  let text=CryptoJS.MD5(name+dob+number);
  document.getElementById("demo").innerHTML = `YOUR PWD IS ${text}`;
}
