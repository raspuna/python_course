
var git_user = document.getElementById("user-id")
var user_name = document.querySelector("#user-name")
var user_img = document.querySelector("#user-img")

async function getData(element){
    var data = await getCoderData(git_user.value)
    /*console.log(data)*/
    user_name.innerText = data.name + " has " + data.followers + " followers."
    user_img.innerHTML="<img src='"+data.avatar_url+"'>"

    return 0
}
async function getCoderData(user_name){
    var Response = await fetch("https://api.github.com/users/"+user_name)
    var coderData = await Response.json();
    return coderData;
}

console.log(getCoderData());
